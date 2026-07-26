# -*- coding: utf-8 -*-
"""Генератор статических страниц Steppe Steel v2."""
import io, os, sys
from _data import BRAND, SPECS, GRAIN, CATALOG, PROCESS, ARTICLES, ADVANTAGES

CSS_V = "1"
OUT = os.path.dirname(os.path.abspath(__file__))

WA = "https://wa.me/" + BRAND["phone_raw"]

WA_SVG = ('<svg viewBox="0 0 24 24" width="21" height="21" fill="currentColor" aria-hidden="true">'
          '<path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5.1-1.3A10 10 0 1 0 12 2Zm0 1.8a8.2 8.2 0 1 1-4.2 15.3'
          'l-.3-.2-3.8.8.8-2.9-.2-.3A8.2 8.2 0 0 1 12 3.8Zm-3.1 4c-.2 0-.5.1-.7.3-.2.3-.9.9-.9 2.1s.9 2.4 1 2.6'
          'c.1.2 1.8 2.8 4.3 3.9 2.1.9 2.6.7 3.1.7.5 0 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.2-.2-.5-.3'
          'l-1.7-.8c-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.4-3c-.1-.2 0-.4.1-.5l.5-.6'
          'c.2-.2.2-.3.3-.5.1-.2 0-.4 0-.5L10 8.2c-.2-.4-.4-.4-.6-.4h-.5Z"/></svg>')

NAV_PAGES = [
    ("katalog.html", "Каталог"),
    ("proizvodstvo.html", "Производство"),
    ("tehnologiya.html", "Технология"),
    ("dostavka-montazh.html", "Доставка и монтаж"),
    ("o-kompanii.html", "О компании"),
    ("blog.html", "Блог"),
    ("kontakty.html", "Контакты"),
]


def cat_url(slug):
    return "katalog-%s.html" % slug


def head(title, desc, canonical):
    return """<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{brand_domain}/{canonical}">
<meta property="og:type" content="website">
<meta property="og:url" content="{brand_domain}/{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{brand_domain}/assets/img/og-cover.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="ru_RU">
<link rel="icon" type="image/jpeg" href="assets/img/logo.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Golos+Text:wght@600;700;800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css?v={css_v}">
</head>
<body>
""".format(title=title, desc=desc, canonical=canonical,
           brand_domain=BRAND["domain"], css_v=CSS_V)


def header(active=""):
    menu = "\n".join(
        '<a href="{u}"><span class="nav__menu-code mono">{c}</span>{t}</a>'.format(
            u=cat_url(c["slug"]), c=c["code"], t=c["title"])
        for c in CATALOG)

    links = []
    for url, label in NAV_PAGES:
        if url == "katalog.html":
            links.append(
                '<div class="nav__drop">'
                '<button class="nav__drop-btn" aria-expanded="false">Каталог</button>'
                '<div class="nav__menu">{menu}\n'
                '<a href="katalog.html"><span class="nav__menu-code mono">→</span>Весь каталог</a>'
                '</div></div>'.format(menu=menu))
        else:
            cls = "nav__link is-active" if url == active else "nav__link"
            links.append('<a href="{u}" class="{c}">{t}</a>'.format(u=url, c=cls, t=label))

    return """<header class="header" id="header">
<div class="container header__inner">
<a href="index.html" class="logo" aria-label="{name} — завод металлоконструкций">
<img src="assets/img/logo.jpg" alt="{name} — Metal Structures · Industrial Systems" width="150" height="150">
</a>
<nav class="nav mono" id="nav" aria-label="Основная навигация">
{links}
</nav>
<div class="header__right">
<a href="tel:+{raw}" class="header__phone mono">{phone}</a>
<a href="{wa}" class="header__wa js-wa" data-wa="hello" aria-label="Написать в WhatsApp">{wa_svg}</a>
<button class="burger" id="burger" aria-label="Открыть меню" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
</div>
</div>
</header>
""".format(name=BRAND["name"], links="\n".join(links), raw=BRAND["phone_raw"],
           phone=BRAND["phone_display"], wa=WA, wa_svg=WA_SVG)


def footer():
    cats = "\n".join('<a href="{u}">{t}</a>'.format(u=cat_url(c["slug"]), t=c["title"])
                     for c in CATALOG)
    pages = "\n".join('<a href="{u}">{t}</a>'.format(u=u, t=t)
                      for u, t in NAV_PAGES if u != "katalog.html")

    return """<footer class="footer">
<div class="container">
<div class="footer__grid">
<div>
<a href="index.html" class="logo" aria-label="{name}"><img src="assets/img/logo.jpg" alt="{name}" width="150" height="150"></a>
<p class="footer__brand-text">Завод металлоконструкций полного цикла: ЛСТК и чёрный металл. {addr_short}.</p>
<div class="footer__socials">
<a href="{ig}" target="_blank" rel="noopener" aria-label="Instagram">
<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg></a>
<a href="{wa}" class="js-wa" data-wa="hello" aria-label="WhatsApp">{wa_svg}</a>
</div>
</div>
<div>
<p class="footer__title">Каталог</p>
<div class="footer__list">{cats}</div>
</div>
<div>
<p class="footer__title">Компания</p>
<div class="footer__list">{pages}</div>
</div>
<div>
<p class="footer__title">Контакты</p>
<div class="footer__list">
<a href="tel:+{raw}" class="mono">{phone}</a>
<a href="mailto:{email}">{email}</a>
<a href="{wa}" class="js-wa" data-wa="hello">WhatsApp — ответ 24/7</a>
<span>{addr}</span>
</div>
</div>
</div>
<div class="footer__bottom">
<span>© {name} · {tagline}</span>
<span>Казахстан, Костанайская область</span>
</div>
</div>
</footer>
<a href="{wa}" class="wa-float js-wa" data-wa="hello" aria-label="Написать в WhatsApp">{wa_svg}</a>
<script src="assets/js/main.js?v={css_v}"></script>
</body>
</html>
""".format(name=BRAND["name"], addr_short=BRAND["address_short"], ig=BRAND["instagram"],
           wa=WA, wa_svg=WA_SVG, cats=cats, pages=pages, raw=BRAND["phone_raw"],
           phone=BRAND["phone_display"], email=BRAND["email"], addr=BRAND["address"],
           tagline=BRAND["tagline"], css_v=CSS_V)


def page(filename, title, desc, body, active=""):
    html = head(title, desc, filename) + header(active) + \
        '<main class="page-main">\n' + body + '\n</main>\n' + footer()
    with io.open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    return filename


# ═══════════ Переиспользуемые блоки ═══════════

def cta_band(title, text, wa_key="kp"):
    return """<section class="section cta-band">
<div class="container cta-band__inner reveal">
<h2>{title}</h2>
<p>{text}</p>
<div class="cta-band__actions">
<a href="kontakty.html#zayavka" class="btn btn--primary btn--lg">Оставить заявку</a>
<a href="{wa}" class="btn btn--ghost btn--lg js-wa" data-wa="{k}">Написать в WhatsApp</a>
</div>
</div>
</section>""".format(title=title, text=text, wa=WA, k=wa_key)


def breadcrumbs(items):
    """items: [(url|None, label)]"""
    parts = []
    for url, label in items:
        if url:
            parts.append('<a href="{u}">{l}</a>'.format(u=url, l=label))
        else:
            parts.append('<span>{l}</span>'.format(l=label))
    return '<nav class="crumbs mono container" aria-label="Хлебные крошки">' + \
        '<span class="crumbs__sep">/</span>'.join(parts) + '</nav>'
