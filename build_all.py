# -*- coding: utf-8 -*-
"""Полная сборка сайта Steppe Steel v2."""
import io, os, sys

OUT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, OUT)

# 1) склеить CSS-довески, если они есть
css_path = os.path.join(OUT, "assets", "css", "style.css")
for extra in ("_art.css",):
    p = os.path.join(OUT, extra)
    if os.path.exists(p):
        base = io.open(css_path, encoding="utf-8").read()
        add = io.open(p, encoding="utf-8").read()
        if add.strip() not in base:
            io.open(css_path, "w", encoding="utf-8").write(base + add)
        os.remove(p)

import _pages_home, _pages_catalog, _pages_info, _pages_articles
from _data import BRAND, CATALOG, ARTICLES

made = []
made.append(_pages_home.build_home())
made += _pages_catalog.build_all()
made.append(_pages_info.build_production())
made.append(_pages_info.build_technology())
made.append(_pages_info.build_delivery())
made.append(_pages_info.build_about())
made.append(_pages_info.build_contacts())
made.append(_pages_info.build_blog_index())
made += _pages_articles.build_all()

# robots.txt + sitemap.xml
io.open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8").write(
    "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % BRAND["domain"])

urls = "\n".join(
    "  <url><loc>%s/%s</loc><priority>%s</priority></url>" % (
        BRAND["domain"], f, "1.0" if f == "index.html" else ("0.9" if f.startswith("katalog") else "0.7"))
    for f in made)
io.open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n' % urls)

print("Собрано страниц: %d" % len(made))
for m in made:
    print("  ", m)
print("  robots.txt, sitemap.xml")
