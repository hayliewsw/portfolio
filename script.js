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

const renamedCaseStudies = {
  'aurora-travel.html': 'case-study-1.html',
  'signal-studio.html': 'case-study-2.html',
  'luma.html': 'case-study-3.html',
};

document.querySelectorAll('a[href]').forEach((link) => {
  const updatedHref = renamedCaseStudies[link.getAttribute('href')];
  if (updatedHref) link.setAttribute('href', updatedHref);
});

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

const profileSection = document.querySelector('.resume-summary');

document.querySelector('.resume-hero .eyebrow')?.remove();

if (profileSection) {
  profileSection.insertAdjacentHTML('afterend', `
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

const selectedProjectsSection = [...document.querySelectorAll('.skills-block')].find((section) => (
  section.querySelector('.eyebrow')?.textContent.trim() === 'Selected project'
));

if (selectedProjectsSection) {
  selectedProjectsSection.classList.add('selected-projects');
  selectedProjectsSection.querySelector('.eyebrow').textContent = 'Selected Projects';
}

if (document.body.classList.contains('resume-page')) {
  document.body.insertAdjacentHTML('beforeend', `
    <nav class="bottom-nav resume-bottom-nav" aria-label="Page navigation">
      <a class="bottom-nav-wordmark" href="index.html#top" aria-label="Haylie Wong home">HAYLIE <span>WONG</span></a>
      <a href="index.html#top">About me</a>
      <a href="index.html#work">Projects</a>
      <a href="index.html#about">About</a>
      <a href="index.html#contact">Contact</a>
      <a class="bottom-nav-resume active" href="resume.html" aria-current="page">Resume ↗</a>
    </nav>
  `);
}

const sectionNavigation = document.querySelector('.bottom-nav');

if (sectionNavigation) {
  const navigationLinks = [...sectionNavigation.querySelectorAll('[data-nav-section]')];
  const sections = navigationLinks.map((link) => document.getElementById(link.dataset.navSection));
  const setActiveNavigation = (sectionId) => {
    navigationLinks.forEach((link) => {
      const isActive = link.dataset.navSection === sectionId;
      link.classList.toggle('active', isActive);
      link.toggleAttribute('aria-current', isActive);
    });
  };

  const navigationObserver = new IntersectionObserver((entries) => {
    const visibleSection = entries
      .filter((entry) => entry.isIntersecting)
      .sort((first, second) => second.intersectionRatio - first.intersectionRatio)[0];

    if (visibleSection) setActiveNavigation(visibleSection.target.id);
  }, { threshold: [0.25, 0.5, 0.75] });

  sections.filter(Boolean).forEach((section) => navigationObserver.observe(section));
  setActiveNavigation('top');
}
