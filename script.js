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

backButton?.querySelector('span')?.replaceChildren('Back to home');

backButton?.addEventListener('click', () => {
  window.location.href = 'index.html#top';
});

const nextCaseStudyByPage = {
  'case-study-1.html': 'case-study-2.html',
  'case-study-2.html': 'case-study-4.html',
  'case-study-3.html': 'case-study-5.html',
  'case-study-4.html': 'case-study-3.html',
};

if (document.body.classList.contains('case-page')) {
  const currentCaseStudy = window.location.pathname.split('/').pop();
  const nextCaseStudy = nextCaseStudyByPage[currentCaseStudy];

  document.querySelector('.case-outcome a')?.remove();

  if (nextCaseStudy) {
    const nextCaseButton = document.createElement('a');
    nextCaseButton.className = 'case-next-button';
    nextCaseButton.href = nextCaseStudy;
    nextCaseButton.textContent = 'Next case study →';
    document.body.append(nextCaseButton);
  }
}

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
document.querySelector('.experience-block .eyebrow')?.replaceChildren('Professional Experience');

if (profileSection) {
  profileSection.insertAdjacentHTML('afterend', `
    <section class="resume-block skills-block core-skills">
      <span class="eyebrow">Core skills</span>
      <div>
        <p>Product design<br />UX/UI design<br />Information architecture<br />Workflow design</p>
        <p>Design systems & components<br />Wireframes, flows & prototypes<br />Responsive design<br />Production-ready specifications</p>
        <p>Remote usability testing<br />Cross-functional collaboration<br />Art direction<br />Game UX</p>
      </div>
    </section>
  `);
}

const selectedProjectsSection = [...document.querySelectorAll('.skills-block')].find((section) => (
  section.querySelector('.eyebrow')?.textContent.trim() === 'Selected Projects'
));

if (selectedProjectsSection) {
  selectedProjectsSection.classList.add('selected-projects');
  selectedProjectsSection.innerHTML = `
    <span class="eyebrow">Selected Projects</span>
    <div class="resume-project-list">
      <article>
        <span class="resume-project-number">01</span>
        <div><h2>Inventory Management System</h2><p>Independent | Product design | Operations</p><span>Independently designed and built a searchable inventory website in five days, turning CSV and Notion data into categories, filters, and location-aware views for moving, storage, and selling.</span></div>
      </article>
      <article>
        <span class="resume-project-number">02</span>
        <div><h2>abillion Profile Revamp</h2><p>UX/UI | Research</p><span>Sole UX designer for a launched profile revamp, defining systems, flows, prototypes, and production specifications; validated in UXArmy with four participants across eight tasks.</span></div>
      </article>
      <article>
        <span class="resume-project-number">03</span>
        <div><h2>Sompo Asia Website Revamp</h2><p>Responsive UI | Information architecture</p><span>Designed a full regional website across desktop and mobile, translating a refreshed brand and clearer information architecture into flows, states, and production-ready specifications.</span><a class="resume-project-link" href="https://www.sompo-apac.com/" target="_blank" rel="noopener noreferrer">View live website ↗</a></div>
      </article>
      <article>
        <span class="resume-project-number">04</span>
        <div><h2>Mad John</h2><p>Game UX | Art direction</p><span>Co-created an in-progress card-and-puzzle game; led game UX and art direction, using six mixed-experience playtests to introduce a hands-on tutorial and refine scoring.</span></div>
      </article>
      <article>
        <span class="resume-project-number">05</span>
        <div><h2>Toadally In Love</h2><p>Game jam | Art direction | UX</p><span>Led art direction and UX for a four-day puzzle-game build, creating a readable interaction system and visual world that ranked third overall among 73 entries.</span><a class="resume-project-link" href="https://szzzeler.itch.io/toadally-in-love" target="_blank" rel="noopener noreferrer">Play on itch.io ↗</a></div>
      </article>
    </div>
  `;
}

if (document.body.classList.contains('case-page') || document.body.classList.contains('resume-page')) {
  document.querySelector('main')?.insertAdjacentHTML('beforeend', `
    <footer class="footer portfolio-footer">
      <span>© 2026 Haylie Wong</span>
      <div>
        <a href="mailto:hayliewsw@gmail.com">Email</a>
        <a href="https://www.linkedin.com/in/hayliewsw/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
        <a href="https://szzzeler.itch.io" target="_blank" rel="noopener noreferrer">itch.io</a>
        <a href="resume.html">Resume</a>
      </div>
      <span>Made with care in Toronto</span>
    </footer>
  `);
}

document.querySelectorAll('.entry-date').forEach((date) => {
  date.innerHTML = date.textContent.trim().replace(/\s*—\s*/, ' —<br />');
});

if (document.body.classList.contains('resume-page')) {
  document.body.insertAdjacentHTML('beforeend', `
    <nav class="bottom-nav resume-bottom-nav" aria-label="Page navigation">
      <a class="bottom-nav-wordmark" href="index.html#top" aria-label="Haylie Wong home">HAYLIE <span>WONG</span></a>
      <a href="index.html#top">Home</a>
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
