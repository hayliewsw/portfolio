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

if (hero && heroObject && !reducedMotion) {
  hero.addEventListener('pointermove', (event) => {
    const bounds = hero.getBoundingClientRect();
    const x = (event.clientX - bounds.left) / bounds.width - 0.5;
    const y = (event.clientY - bounds.top) / bounds.height - 0.5;
    heroObject.style.transform = `rotateY(${x * 10}deg) rotateX(${-y * 8}deg) translate3d(${x * 10}px, ${y * 8}px, 0)`;
  });
  hero.addEventListener('pointerleave', () => {
    heroObject.style.transform = '';
  });
}

const supportsFinePointer = window.matchMedia('(any-pointer: fine)').matches;

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
