// Reveal cards and figures as they scroll in. No external calls, no tracking.
(function () {
  var els = document.querySelectorAll('.card, .list a, .callout, figure, .stats');
  els.forEach(function (e) { e.classList.add('reveal'); });
  if (!('IntersectionObserver' in window)) { els.forEach(function (e) { e.classList.add('in'); }); return; }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
  }, { rootMargin: '0px 0px -8% 0px' });
  els.forEach(function (e) { io.observe(e); });
})();
// Safety net: never leave content hidden (printing, odd viewports, screenshots).
setTimeout(function () { document.querySelectorAll('.reveal').forEach(function (e) { e.classList.add('in'); }); }, 1500);
// Count-up for big numbers when they scroll into view.
(function () {
  var nodes = document.querySelectorAll('.stats b, .sleeve .num');
  var fmt = function (s, v) {
    var m = s.match(/^([^0-9]*)([0-9][0-9,]*\.?[0-9]*)(.*)$/); if (!m) return s;
    var dec = (m[2].split('.')[1] || '').length;
    return m[1] + v.toLocaleString('en-GB', { minimumFractionDigits: dec, maximumFractionDigits: dec }) + m[3];
  };
  nodes.forEach(function (n) {
    var s = n.textContent.trim(); var m = s.match(/([0-9][0-9,]*\.?[0-9]*)/); if (!m) return;
    var target = parseFloat(m[1].replace(/,/g, '')); if (isNaN(target)) return;
    n.dataset.final = s; n.textContent = fmt(s, 0);
    var run = function () { var t0 = null; var step = function (ts) { if (!t0) t0 = ts; var p = Math.min(1, (ts - t0) / 900); var e = 1 - Math.pow(1 - p, 3); n.textContent = fmt(s, target * e); if (p < 1) requestAnimationFrame(step); else n.textContent = s; }; requestAnimationFrame(step); };
    if ('IntersectionObserver' in window) { var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { run(); io.unobserve(n); } }); }); io.observe(n); } else run();
  });
})();
// Recent gigs strip (assets/js/gigs.js). Hidden when the list is empty.
(function () {
  var el = document.getElementById('gigs'); if (!el || !window.RECENT_GIGS || !window.RECENT_GIGS.length) return;
  var txt = window.RECENT_GIGS.join('  ·  ') + '  ·  ';
  el.querySelectorAll('.marquee__track span').forEach(function (s) { s.textContent = txt; });
  el.classList.add('on');
})();
