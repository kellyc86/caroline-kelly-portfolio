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
