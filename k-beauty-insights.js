document.documentElement.classList.add('js');

const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

function animateCount(element) {
  if (element.dataset.animated) return;
  element.dataset.animated = 'true';
  const target = Number(element.dataset.target);
  const suffix = element.dataset.suffix || '';
  if (reducedMotion) {
    element.textContent = `${target}${suffix}`;
    return;
  }
  const start = performance.now();
  const duration = 900;
  const tick = (now) => {
    const progress = Math.min((now - start) / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    element.textContent = `${Math.round(target * eased)}${suffix}`;
    if (progress < 1) requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
}

document.querySelectorAll('main > section, main > aside').forEach((section) => section.setAttribute('data-reveal', ''));

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    entry.target.classList.add('is-visible');
    entry.target.querySelectorAll('.count-up').forEach(animateCount);
    if (entry.target.classList.contains('drivers')) entry.target.querySelector('.bars')?.classList.add('is-visible');
    observer.unobserve(entry.target);
  });
}, { threshold: 0.12 });

document.querySelectorAll('[data-reveal]').forEach((section) => observer.observe(section));
document.querySelectorAll('.count-up').forEach((number) => {
  number.textContent = `0${number.dataset.suffix || ''}`;
});

const hero = document.querySelector('.hero');
const heroObject = document.querySelector('.hero-object');

if (hero && !reducedMotion) {
  hero.addEventListener('pointermove', (event) => {
    const bounds = hero.getBoundingClientRect();
    const x = (event.clientX - bounds.left) / bounds.width - 0.5;
    const y = (event.clientY - bounds.top) / bounds.height - 0.5;
    if (heroObject) heroObject.style.transform = `rotateY(${x * 10}deg) rotateX(${-y * 8}deg) translate3d(${x * 10}px, ${y * 8}px, 0)`;
  });
  hero.addEventListener('pointerleave', () => {
    if (heroObject) heroObject.style.transform = '';
  });
}

const shaderCanvas = document.querySelector('.hero-shader');
if (shaderCanvas) {
  const gl = shaderCanvas.getContext('webgl', { alpha: true, antialias: false });
  if (gl) {
    const vertexSource = 'attribute vec2 p;void main(){gl_Position=vec4(p,0.,1.);}';
    const fragmentSource = `
      precision mediump float;
      uniform vec2 r;
      uniform float t;
      void main(){
        vec2 uv=(gl_FragCoord.xy-.5*r.xy)/min(r.x,r.y);
        float a=atan(uv.y,uv.x);
        float d=length(uv);
        float wave=sin(d*13.0-t*0.75+a*2.0)*0.5+0.5;
        float ribbons=sin((uv.x+sin(uv.y*4.0+t*.28)*.18)*8.0-t*.45)*.5+.5;
        float field=smoothstep(.12,.92,wave*.55+ribbons*.45);
        vec3 pearl=vec3(.969,.961,1.0);
        vec3 lavender=vec3(.788,.725,.937);
        vec3 navy=vec3(.082,.094,.247);
        vec3 color=mix(pearl,lavender,field*.68);
        color=mix(color,navy,smoothstep(.68,1.28,d)*.22);
        gl_FragColor=vec4(color,1.0);
      }`;
    const compile = (type, source) => {
      const shader = gl.createShader(type);
      gl.shaderSource(shader, source);
      gl.compileShader(shader);
      return shader;
    };
    const program = gl.createProgram();
    gl.attachShader(program, compile(gl.VERTEX_SHADER, vertexSource));
    gl.attachShader(program, compile(gl.FRAGMENT_SHADER, fragmentSource));
    gl.linkProgram(program);
    gl.useProgram(program);
    const vertices = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, vertices);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,-1,1,-1,-1,1,-1,1,1,-1,1,1]), gl.STATIC_DRAW);
    const position = gl.getAttribLocation(program, 'p');
    gl.enableVertexAttribArray(position);
    gl.vertexAttribPointer(position, 2, gl.FLOAT, false, 0, 0);
    const resolution = gl.getUniformLocation(program, 'r');
    const time = gl.getUniformLocation(program, 't');
    const renderShader = (now = 0) => {
      const ratio = Math.min(window.devicePixelRatio || 1, 1.5);
      const width = Math.max(1, Math.round(shaderCanvas.clientWidth * ratio));
      const height = Math.max(1, Math.round(shaderCanvas.clientHeight * ratio));
      if (shaderCanvas.width !== width || shaderCanvas.height !== height) {
        shaderCanvas.width = width;
        shaderCanvas.height = height;
        gl.viewport(0, 0, width, height);
      }
      gl.uniform2f(resolution, width, height);
      gl.uniform1f(time, now * .001);
      gl.drawArrays(gl.TRIANGLES, 0, 6);
      if (!reducedMotion) requestAnimationFrame(renderShader);
    };
    renderShader();
  }
}

const supportsFinePointer = window.matchMedia('(any-pointer: fine)').matches;

const reactiveBubbles = hero ? [...hero.querySelectorAll('.hero-stat-wrap .object-stat, .hero-data-rail article')] : [];

if (hero && supportsFinePointer && !reducedMotion && reactiveBubbles.length) {
  const bubbleStates = reactiveBubbles.map((element, index) => ({
    element,
    depth: index === 0 ? 18 : 10 + index * 4,
    x: 0,
    y: 0,
    rotation: 0,
    targetX: 0,
    targetY: 0,
    targetRotation: 0
  }));
  let bubbleFrame;

  const renderBubbleMotion = () => {
    let moving = false;
    bubbleStates.forEach((state, index) => {
      state.x += (state.targetX - state.x) * 0.12;
      state.y += (state.targetY - state.y) * 0.12;
      state.rotation += (state.targetRotation - state.rotation) * 0.12;
      state.element.style.setProperty('--motion-x', `${state.x.toFixed(2)}px`);
      state.element.style.setProperty('--motion-y', `${state.y.toFixed(2)}px`);
      state.element.style.setProperty('--motion-r', `${state.rotation.toFixed(2)}deg`);
      moving ||= Math.abs(state.targetX - state.x) > 0.05 || Math.abs(state.targetY - state.y) > 0.05 || Math.abs(state.targetRotation - state.rotation) > 0.03;
    });
    bubbleFrame = moving ? requestAnimationFrame(renderBubbleMotion) : undefined;
  };

  const startBubbleMotion = () => {
    if (!bubbleFrame) bubbleFrame = requestAnimationFrame(renderBubbleMotion);
  };

  hero.addEventListener('pointermove', (event) => {
    const bounds = hero.getBoundingClientRect();
    const x = ((event.clientX - bounds.left) / bounds.width - 0.5) * 2;
    const y = ((event.clientY - bounds.top) / bounds.height - 0.5) * 2;
    bubbleStates.forEach((state, index) => {
      const direction = index % 2 ? -1 : 1;
      state.targetX = x * state.depth * direction;
      state.targetY = y * state.depth * 0.65;
      state.targetRotation = x * direction * (index === 0 ? 2.2 : 3.4);
    });
    startBubbleMotion();
  }, { passive: true });

  hero.addEventListener('pointerleave', () => {
    bubbleStates.forEach((state) => {
      state.targetX = 0;
      state.targetY = 0;
      state.targetRotation = 0;
    });
    startBubbleMotion();
  });
}

if (supportsFinePointer && !reducedMotion) {
  const siteCursor = document.createElement('div');
  siteCursor.className = 'site-cursor';
  siteCursor.setAttribute('aria-hidden', 'true');
  document.body.appendChild(siteCursor);
  document.body.classList.add('custom-cursor');

  let cursorX = -50;
  let cursorY = -50;
  let cursorFrame;

  const renderCursor = () => {
    siteCursor.style.transform = `translate3d(${cursorX}px, ${cursorY}px, 0) rotate(-12deg)`;
    cursorFrame = undefined;
  };

  window.addEventListener('pointermove', (event) => {
    cursorX = event.clientX;
    cursorY = event.clientY;
    siteCursor.classList.add('is-visible');
    if (!cursorFrame) cursorFrame = requestAnimationFrame(renderCursor);
  }, { passive: true });

  document.addEventListener('pointerover', (event) => {
    siteCursor.classList.toggle('is-interactive', Boolean(event.target.closest('a, button, [role="button"], input, select, textarea')));
  });
  document.addEventListener('pointerdown', () => siteCursor.classList.add('is-pressed'));
  document.addEventListener('pointerup', () => siteCursor.classList.remove('is-pressed'));
  document.documentElement.addEventListener('mouseleave', () => siteCursor.classList.remove('is-visible'));
}
