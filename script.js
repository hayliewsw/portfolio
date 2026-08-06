const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('.main-nav');

menuButton?.addEventListener('click', () => {
  const isOpen = navigation.classList.toggle('open');
  menuButton.classList.toggle('active', isOpen);
  menuButton.setAttribute('aria-expanded', String(isOpen));
});

document.querySelectorAll('.main-nav a').forEach((link) => link.addEventListener('click', () => {
  navigation.classList.remove('open');
  menuButton.classList.remove('active');
  menuButton.setAttribute('aria-expanded', 'false');
}));

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) entry.target.classList.add('visible');
  });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal').forEach((element) => observer.observe(element));

const backButton = document.querySelector('[data-back-button]');

backButton?.addEventListener('click', () => {
  if (window.history.length > 1 && document.referrer) {
    window.history.back();
    return;
  }

  window.location.href = 'index.html#work';
});

const progressBar = document.querySelector('.page-progress span');

const updatePageProgress = () => {
  if (!progressBar) return;

  const scrollableHeight = document.documentElement.scrollHeight - window.innerHeight;
  const progress = scrollableHeight > 0 ? (window.scrollY / scrollableHeight) * 100 : 0;
  progressBar.style.width = `${Math.min(100, Math.max(0, progress))}%`;
};

window.addEventListener('scroll', updatePageProgress, { passive: true });
window.addEventListener('resize', updatePageProgress);
updatePageProgress();

const ambientSections = document.querySelectorAll('.ambient-background');
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

const driftFractalNoise = () => {
  ambientSections.forEach((section) => {
    section.style.setProperty('--caustic-one-x', `${Math.round(Math.random() * 100)}%`);
    section.style.setProperty('--caustic-one-y', `${Math.round(Math.random() * 100)}%`);
    section.style.setProperty('--caustic-two-x', `${Math.round(Math.random() * 100)}%`);
    section.style.setProperty('--caustic-two-y', `${Math.round(Math.random() * 100)}%`);
  });
};

if (!reduceMotion && ambientSections.length) {
  driftFractalNoise();
  window.setInterval(driftFractalNoise, 12000);
}

const educationSection = [...document.querySelectorAll('.skills-block')].find((section) => (
  section.querySelector('.eyebrow')?.textContent.trim() === 'Education'
));

if (educationSection) {
  educationSection.classList.add('education-block');
  educationSection.innerHTML = `
    <span class="eyebrow">Education</span>
    <div class="resume-entries">
      <article>
        <div class="entry-date">2022 — 2023</div>
        <div><h2>Design Management (Post-graduate Certificate) <span>George Brown College · Toronto, Canada</span></h2><p>Dean’s List: Fall 2022 and Winter 2023.</p></div>
      </article>
      <article>
        <div class="entry-date">2016 — 2017</div>
        <div><h2>Bachelor of Communication (Professional Communications) <span>RMIT University · Singapore & Australia</span></h2></div>
      </article>
    </div>
  `;
}

const selectedProjectSection = [...document.querySelectorAll('.skills-block')].find((section) => (
  section.querySelector('.eyebrow')?.textContent.trim() === 'Selected project'
));

if (selectedProjectSection) {
  selectedProjectSection.insertAdjacentHTML('beforebegin', `
    <section class="resume-block skills-block core-skills">
      <span class="eyebrow">Core skills</span>
      <div>
        <p>Product design<br />UX/UI design<br />Information architecture</p>
        <p>Workflow design<br />UX research<br />Visual design</p>
        <p>Cross-team collaboration<br />Art direction<br />Game UX</p>
      </div>
    </section>
  `);
}
