/**
 * AirMenu Credit — auto-inject "Developed By Air Menu Co." footer + console credit.
 * Drop-in snippet: include this script on any page to get the credit automatically.
 *
 * Usage in any project (single line, near </body>):
 *   <script src="https://cdn.jsdelivr.net/gh/QuickAirMenu/AirMenu_AgentsOS@main/airmenu-credit/airmenu-credit.min.js"></script>
 *
 * Options (all optional):
 *   data-airmenu-link  -> override contact URL (default: https://airmenu.net/contact)
 *   data-airmenu-target -> selector/container to append footer credit into
 *   data-airmenu-no-console -> set "1" to skip the console message
 *
 * The script injects its own scoped CSS so it works in any site without styling conflicts.
 */
(function () {
  'use strict';

  var script = document.currentScript || (function () {
    var s = document.querySelector('script[data-airmenu-credit]');
    return s;
  })();

  var cfg = {};
  if (script) {
    cfg.url = script.getAttribute('data-airmenu-link') || 'https://airmenu.net/contact';
    cfg.target = script.getAttribute('data-airmenu-target') || null;
    cfg.noConsole = script.getAttribute('data-airmenu-no-console') === '1';
  } else {
    cfg.url = 'https://airmenu.net/contact';
  }

  if (!cfg.noConsole) {
    console.log(
      '%c💼 Air Menu Co. %c✨ Developed By Air Menu Co.',
      'font-size:15px;font-weight:700;background:linear-gradient(90deg,#274685,#3db3c5);-webkit-background-clip:text;-webkit-text-fill-color:transparent;',
      'font-size:12px;color:#7A7770;'
    );
    console.log(
      '%cPioneering digital solutions — digital identity, brand identity & systems to elevate your digital presence.',
      'font-size:12px;color:#3db3c5;'
    );
    console.log('%c🔗 ' + cfg.url, 'font-size:12px;color:#274685;');
  }

  function injectStyle() {
    if (document.getElementById('airmenu-credit-style')) return;
    var css = [
      '.airmenu-credit{direction:ltr;unicode-bidi:isolate;display:inline-flex;align-items:center;gap:.35rem;font-size:.75rem;letter-spacing:.04em;color:rgba(255,255,255,.35);margin:.5rem 0 0}',
      '.airmenu-credit a{font-weight:600;font-size:.78rem;text-decoration:none;background:linear-gradient(to left,#274685,#3db3c5);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;transition:opacity .3s}',
      '.airmenu-credit a:hover{opacity:.8}'
    ].join('\n');
    var style = document.createElement('style');
    style.id = 'airmenu-credit-style';
    style.textContent = css;
    document.head.appendChild(style);
  }

  function injectFooter() {
    var host = cfg.target ? document.querySelector(cfg.target) : document.querySelector('footer');
    if (!host) return;

    var p = document.createElement('p');
    p.className = 'airmenu-credit';
    p.appendChild(document.createTextNode('Developed By '));

    var a = document.createElement('a');
    a.href = cfg.url;
    a.target = '_blank';
    a.rel = 'noopener noreferrer';
    a.textContent = 'Air Menu Co.';
    p.appendChild(a);

    if (cfg.target) {
      host.appendChild(p);
    } else {
      // append after the last child of footer (e.g. after copyright line)
      host.appendChild(p);
    }
  }

  function whenReady(fn) {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', fn);
    } else {
      fn();
    }
  }

  whenReady(function () {
    injectStyle();
    injectFooter();
  });
})();
