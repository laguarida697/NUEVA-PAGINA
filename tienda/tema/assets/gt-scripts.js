(function () {
  function initReveal() {
    var els = document.querySelectorAll('.gt-reveal');
    if (!els.length) return;
    if (!('IntersectionObserver' in window)) { els.forEach(function (e) { e.classList.add('gt-visible'); }); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('gt-visible'); io.unobserve(en.target); } });
    }, { threshold: 0.12 });
    els.forEach(function (e) { io.observe(e); });
  }
  function initCuenta() {
    document.querySelectorAll('[data-gt-fecha]').forEach(function (box) {
      var fin = new Date(box.getAttribute('data-gt-fecha') + 'T23:59:59-05:00').getTime();
      var d = box.querySelector('[data-u="d"]'), h = box.querySelector('[data-u="h"]'), m = box.querySelector('[data-u="m"]'), s = box.querySelector('[data-u="s"]');
      function pad(n) { return n < 10 ? '0' + n : '' + n; }
      function tick() {
        var t = Math.max(0, fin - Date.now());
        d.textContent = Math.floor(t / 864e5);
        h.textContent = pad(Math.floor(t % 864e5 / 36e5));
        m.textContent = pad(Math.floor(t % 36e5 / 6e4));
        s.textContent = pad(Math.floor(t % 6e4 / 1e3));
      }
      tick(); setInterval(tick, 1000);
    });
  }
  function init() { initReveal(); initCuenta(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
  document.addEventListener('shopify:section:load', init);
})();
