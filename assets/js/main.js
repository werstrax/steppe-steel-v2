/* ═══════════════════════════════════════════════
   STEPPE STEEL v2 — main.js
   ═══════════════════════════════════════════════ */
(function () {
  'use strict';

  var CONFIG = {
    WA_PHONE: '77766031766',
    EMAIL: 'steppe.steel@gmail.com'
  };

  var WA_TEXT = {
    hello: 'Здравствуйте! Пишу с сайта Steppe Steel.',
    kp: 'Здравствуйте! Хочу получить коммерческое предложение.',
    engineer: 'Здравствуйте! Нужна консультация инженера по проекту.',
    calc: 'Здравствуйте! Хочу рассчитать стоимость здания.'
  };

  function waUrl(text) {
    return 'https://wa.me/' + CONFIG.WA_PHONE + '?text=' + encodeURIComponent(text);
  }

  /* ───── Шапка: бургер + каталог ───── */
  function initNav() {
    var burger = document.getElementById('burger');
    var nav = document.getElementById('nav');
    var header = document.querySelector('.header');

    if (burger && nav) {
      burger.addEventListener('click', function () {
        var open = nav.classList.toggle('is-open');
        burger.classList.toggle('is-open', open);
        burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
      // закрыть меню по клику на ссылку
      nav.addEventListener('click', function (e) {
        if (e.target.closest('a')) {
          nav.classList.remove('is-open');
          burger.classList.remove('is-open');
          burger.setAttribute('aria-expanded', 'false');
        }
      });
    }

    // выпадающий каталог
    var drops = document.querySelectorAll('.nav__drop');
    Array.prototype.forEach.call(drops, function (drop) {
      var btn = drop.querySelector('.nav__drop-btn');
      if (!btn) return;
      btn.addEventListener('click', function (e) {
        e.stopPropagation();
        var wasOpen = drop.classList.contains('is-open');
        Array.prototype.forEach.call(drops, function (d) { d.classList.remove('is-open'); });
        drop.classList.toggle('is-open', !wasOpen);
        btn.setAttribute('aria-expanded', !wasOpen ? 'true' : 'false');
      });
    });
    document.addEventListener('click', function (e) {
      if (!e.target.closest('.nav__drop')) {
        Array.prototype.forEach.call(drops, function (d) { d.classList.remove('is-open'); });
      }
    });

    // затемнение шапки при скролле
    if (header) {
      var onScroll = function () {
        header.style.background = window.scrollY > 40 ? 'rgba(11,12,13,.96)' : '';
      };
      window.addEventListener('scroll', onScroll, { passive: true });
      onScroll();
    }
  }

  /* ───── Ссылки WhatsApp ───── */
  function initWa() {
    var links = document.querySelectorAll('.js-wa');
    Array.prototype.forEach.call(links, function (a) {
      var key = a.getAttribute('data-wa') || 'hello';
      a.setAttribute('href', waUrl(WA_TEXT[key] || WA_TEXT.hello));
      a.setAttribute('target', '_blank');
      a.setAttribute('rel', 'noopener');
    });
  }

  /* ───── Появление блоков ───── */
  function initReveal() {
    var els = document.querySelectorAll('.reveal');
    if (!els.length) return;
    var show = function (el) { el.classList.add('is-in'); };

    if (!('IntersectionObserver' in window)) {
      Array.prototype.forEach.call(els, show);
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { show(en.target); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: .06 });
    Array.prototype.forEach.call(els, function (el) { io.observe(el); });

    // страховка: если что-то пошло не так — показать всё
    setTimeout(function () { Array.prototype.forEach.call(els, show); }, 3000);
  }

  /* ───── Калькулятор зернохранилища ───── */
  function initGrainCalc() {
    var crop = document.getElementById('grain-crop');
    var tons = document.getElementById('grain-tons');
    var out = document.getElementById('grain-out');
    var outSec = document.getElementById('grain-sections');
    if (!crop || !tons || !out) return;

    function recalc() {
      var perM = parseFloat(crop.value) || 67;
      var t = parseFloat(tons.value) || 0;
      if (t <= 0) { out.textContent = '— м'; if (outSec) outSec.textContent = '—'; return; }
      var len = Math.round(t / perM);
      if (len < 1) len = 1;
      var capped = Math.min(len, 140);
      out.textContent = '≈ ' + capped + ' м';
      if (outSec) {
        if (len > 140) {
          outSec.textContent = 'нужно ' + Math.ceil(len / 140) + ' здания по 140 м';
        } else {
          outSec.textContent = 'одно здание, наращивается секциями';
        }
      }
    }
    crop.addEventListener('change', recalc);
    tons.addEventListener('input', recalc);
    recalc();
  }

  /* ───── Калькулятор площади здания ───── */
  function initAreaCalc() {
    var w = document.getElementById('area-w');
    var l = document.getElementById('area-l');
    var out = document.getElementById('area-out');
    if (!w || !l || !out) return;

    function recalc() {
      var a = parseFloat(w.value) || 0;
      var b = parseFloat(l.value) || 0;
      out.textContent = a > 0 && b > 0 ? (a * b).toLocaleString('ru-RU') + ' м²' : '— м²';
    }
    w.addEventListener('input', recalc);
    l.addEventListener('input', recalc);
    recalc();
  }

  /* ───── Форма заявки → WhatsApp ───── */
  function initForm() {
    var form = document.getElementById('lead-form');
    if (!form) return;

    var done = document.getElementById('lead-done');
    var mailLink = document.getElementById('lead-mail');

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var fd = new FormData(form);
      var rows = [];
      var labels = {
        type: 'Тип здания',
        size: 'Размеры',
        region: 'Регион / участок',
        name: 'Имя',
        phone: 'Телефон',
        note: 'Комментарий'
      };
      Object.keys(labels).forEach(function (k) {
        var v = (fd.get(k) || '').toString().trim();
        if (v) rows.push(labels[k] + ': ' + v);
      });
      if (!rows.length) return;

      var msg = 'Заявка с сайта Steppe Steel\n' + rows.join('\n');
      window.open(waUrl(msg), '_blank', 'noopener');

      if (done) done.hidden = false;
      if (mailLink) {
        mailLink.href = 'mailto:' + CONFIG.EMAIL +
          '?subject=' + encodeURIComponent('Заявка с сайта Steppe Steel') +
          '&body=' + encodeURIComponent(rows.join('\n'));
      }
    });
  }

  /* ───── FAQ-аккордеон ───── */
  function initFaq() {
    var items = document.querySelectorAll('.faq__item');
    Array.prototype.forEach.call(items, function (item) {
      var btn = item.querySelector('.faq__q');
      if (!btn) return;
      btn.addEventListener('click', function () {
        var open = item.classList.toggle('is-open');
        btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
    });
  }

  /* ───── Счётчики цифр ───── */
  function initCounters() {
    var els = document.querySelectorAll('[data-count]');
    if (!els.length || !('IntersectionObserver' in window)) return;

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        io.unobserve(el);
        var target = parseFloat(el.getAttribute('data-count'));
        if (isNaN(target)) return;
        var suffix = el.getAttribute('data-suffix') || '';
        var dur = 1100, t0 = null;
        function step(ts) {
          if (!t0) t0 = ts;
          var p = Math.min((ts - t0) / dur, 1);
          var eased = 1 - Math.pow(1 - p, 3);
          el.textContent = Math.round(target * eased) + suffix;
          if (p < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
      });
    }, { threshold: .4 });
    Array.prototype.forEach.call(els, function (el) { io.observe(el); });
  }

  /* ───── Инициализация ───── */
  function init() {
    initNav();
    initWa();
    initReveal();
    initGrainCalc();
    initAreaCalc();
    initForm();
    initFaq();
    initCounters();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
