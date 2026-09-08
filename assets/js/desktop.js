// Desktop window manager. Plain JS, no external calls.
(function () {
  var desk = document.getElementById('desk'); if (!desk) return;
  var wins = Array.prototype.slice.call(document.querySelectorAll('.win'));
  var tasks = document.getElementById('tasks');
  var z = 10;
  var mobile = function () { return window.matchMedia('(max-width: 760px)').matches; };

  function focus(w) { wins.forEach(function (x) { x.classList.remove('focus'); }); w.classList.add('focus'); w.style.zIndex = ++z; syncTasks(); }
  function open(id) { var w = document.getElementById(id); if (!w) return; w.classList.remove('min'); w.hidden = false; focus(w); if (!mobile()) w.scrollIntoView && null; }
  function minimise(w) { w.classList.add('min'); syncTasks(); }
  function close(w) { w.hidden = true; w.classList.remove('min'); syncTasks(); }

  function syncTasks() {
    tasks.innerHTML = '';
    wins.forEach(function (w) {
      if (w.hidden) return;
      var b = document.createElement('button'); b.className = 'task' + (w.classList.contains('focus') && !w.classList.contains('min') ? ' active' : '');
      b.textContent = w.dataset.title; b.onclick = function () { if (w.classList.contains('min') || !w.classList.contains('focus')) open(w.id); else minimise(w); };
      tasks.appendChild(b);
    });
  }

  // Initial layout: cascade windows that are not hidden.
  var cascade = 0;
  wins.forEach(function (w, i) {
    w.dataset.title = w.querySelector('.tbar .ti').textContent.trim();
    if (!mobile() && !w.style.left) { w.style.left = (140 + (i % 4) * 60) + 'px'; w.style.top = (30 + (i % 4) * 44) + 'px'; }
    w.addEventListener('mousedown', function () { focus(w); });
    var tb = w.querySelector('.tbar');
    tb.querySelector('.x').onclick = function (e) { e.stopPropagation(); close(w); };
    var mn = tb.querySelector('.mn'); if (mn) mn.onclick = function (e) { e.stopPropagation(); minimise(w); };
    // Drag
    var drag = null;
    tb.addEventListener('mousedown', function (e) { if (e.target.tagName === 'BUTTON' || mobile()) return; drag = { x: e.clientX - w.offsetLeft, y: e.clientY - w.offsetTop }; e.preventDefault(); });
    window.addEventListener('mousemove', function (e) { if (!drag) return; w.style.left = Math.max(0, e.clientX - drag.x) + 'px'; w.style.top = Math.max(0, e.clientY - drag.y) + 'px'; });
    window.addEventListener('mouseup', function () { drag = null; });
    tb.addEventListener('dblclick', function () { w.classList.toggle('max'); if (w.classList.contains('max')) { w.dataset.pos = w.style.left + '|' + w.style.top + '|' + w.style.width; w.style.left = '0'; w.style.top = '0'; w.style.width = '100%'; w.style.height = 'calc(100vh - 34px)'; } else { var p = (w.dataset.pos || '||').split('|'); w.style.left = p[0]; w.style.top = p[1]; w.style.width = p[2]; w.style.height = ''; } });
  });

  // Icons open windows
  document.querySelectorAll('[data-open]').forEach(function (el) {
    el.addEventListener('click', function () { open(el.dataset.open); closeStart(); });
    el.addEventListener('keydown', function (e) { if (e.key === 'Enter') open(el.dataset.open); });
  });

  // Start menu
  var sm = document.getElementById('startmenu'), sb = document.getElementById('startbtn');
  function closeStart() { sm.classList.remove('open'); }
  sb.onclick = function (e) { e.stopPropagation(); sm.classList.toggle('open'); };
  document.addEventListener('click', function (e) { if (!sm.contains(e.target)) closeStart(); });

  // Clock
  var clock = document.getElementById('clock');
  function tick() { var d = new Date(); clock.textContent = d.toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit' }); }
  tick(); setInterval(tick, 15000);

  // Now playing: cycle project titles
  var np = document.getElementById('np'); var npi = 0;
  if (np) { var names = wins.filter(function (w) { return w.classList.contains('proj'); }).map(function (w) { return w.dataset.title; }); setInterval(function () { npi = (npi + 1) % names.length; np.textContent = names[npi]; }, 4000); }

  // Splash
  var sp = document.getElementById('splash');
  if (sp) { var seen = false; try { seen = sessionStorage.getItem('splash'); } catch (e) {} if (seen) sp.classList.add('off'); else { setTimeout(function () { sp.classList.add('off'); try { sessionStorage.setItem('splash', '1'); } catch (e) {} }, 1500); } }

  syncTasks();
  var first = wins.find(function (w) { return !w.hidden; }); if (first) focus(first);
})();
