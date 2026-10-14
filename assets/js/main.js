(function () {
  // ---- theme toggle (persisted)
  var root = document.documentElement;
  var toggle = document.getElementById('theme-toggle');
  toggle.addEventListener('click', function () {
    var next = root.dataset.theme === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next;
    try { localStorage.setItem('theme', next); } catch (_) {}
  });

  // ---- mobile menu
  var burger = document.getElementById('burger');
  var links = document.getElementById('nav-links');
  burger.addEventListener('click', function () { links.classList.toggle('open'); });
  links.addEventListener('click', function (e) { if (e.target.tagName === 'A') links.classList.remove('open'); });

  // ---- typing headline
  var roles = window.ROLES || [];
  var el = document.getElementById('typed');
  var ri = 0, ci = 0, deleting = false;
  function tick() {
    var word = roles[ri] || '';
    el.textContent = deleting ? word.slice(0, ci--) : word.slice(0, ci++);
    var delay = deleting ? 28 : 55;
    if (!deleting && ci > word.length) { deleting = true; delay = 1600; }
    else if (deleting && ci < 0) { deleting = false; ci = 0; ri = (ri + 1) % roles.length; delay = 350; }
    setTimeout(tick, delay);
  }
  if (roles.length) tick();

  // ---- reveal on scroll
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
  }, { threshold: 0.12 });
  document.querySelectorAll('.reveal').forEach(function (n, i) {
    n.style.transitionDelay = Math.min(i % 6, 5) * 60 + 'ms';
    io.observe(n);
  });

  // ---- active nav link
  var sections = ['about', 'experience', 'projects', 'skills', 'contact'].map(function (id) { return document.getElementById(id); });
  var navAs = links.querySelectorAll('a');
  var so = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (!en.isIntersecting) return;
      navAs.forEach(function (a) { a.classList.toggle('active', a.getAttribute('href') === '#' + en.target.id); });
    });
  }, { rootMargin: '-40% 0px -55% 0px' });
  sections.forEach(function (s) { if (s) so.observe(s); });

  // ---- copy email
  var copy = document.getElementById('copy-email');
  var label = document.getElementById('copy-label');
  copy.addEventListener('click', function () {
    var email = 'vantasivateja@gmail.com';
    var done = function () { label.textContent = 'copied ✓'; setTimeout(function () { label.textContent = 'click to copy'; }, 1800); };
    if (navigator.clipboard) navigator.clipboard.writeText(email).then(done, done); else done();
  });

  document.getElementById('year').textContent = new Date().getFullYear();
})();
