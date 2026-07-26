# -*- coding: utf-8 -*-
"""Страницы каталога: индекс + 6 категорий."""
from _build import page, cta_band, breadcrumbs, cat_url, WA
from _data import BRAND, SPECS, GRAIN, CATALOG


def build_catalog_index():
    cards = []
    for c in CATALOG:
        flag = '<span class="catcard__flag mono">ФЛАГМАН</span>' if c.get("flagship") else ''
        cards.append("""<a href="{u}" class="catcard reveal">
<div class="catcard__media"><img src="assets/img/{img}" alt="{t} — Steppe Steel" loading="lazy"></div>
<div class="catcard__body">
<span class="catcard__code mono">{code}</span>{flag}
<h3 class="catcard__title">{t}</h3>
<p class="catcard__lead">{lead}</p>
<span class="catcard__more mono">Смотреть решения →</span>
</div>
</a>""".format(u=cat_url(c["slug"]), img=c["img"], t=c["title"], code=c["code"],
                flag=flag, lead=c["lead"]))

    body = """<section class="page-hero">
<div class="container">
<p class="eyebrow reveal">Каталог решений</p>
<h1 class="reveal">Что мы строим</h1>
<p class="section__lead reveal">Шесть направлений на одном каркасе: оцинкованный профиль до&nbsp;{steel} и&nbsp;чёрный металл. Пролёт до&nbsp;{span} без внутренних колонн, расчёт под {snow}&nbsp;снеговой район и&nbsp;морозы до&nbsp;{temp}. Любой размер — под ваш участок и&nbsp;нагрузки.</p>
</div>
</section>

<section class="section">
<div class="container">
<div class="catgrid">
{cards}
</div>
</div>
</section>

{cta}""".format(steel=SPECS["steel_max_mm"], span=SPECS["span_max_m"],
                snow=SPECS["snow_region"], temp=SPECS["temp_min"],
                cards="\n".join(cards),
                cta=cta_band("Не нашли свой формат?",
                             "Мы проектируем под задачу: габариты, нагрузки, ворота под вашу технику. Пришлите размеры — инженер посчитает за 24 часа."))

    return page("katalog.html",
                "Каталог зданий из металлоконструкций — Steppe Steel",
                "Зернохранилища, склады и ангары, ангары для техники, цеха, спортзалы, гаражи. Пролёт до 24 м без колонн, расчёт под III снеговой район Казахстана.",
                body, active="katalog.html")


def build_category(c):
    # таблица объектов категории
    rows = "\n".join(
        """<tr>
<td><strong>{n}</strong></td>
<td class="mono">{size}</td>
<td class="mono accent">{cap}</td>
<td>{note}</td>
<td><a href="kontakty.html#zayavka" class="tbl-cta mono">Рассчитать&nbsp;→</a></td>
</tr>""".format(n=n, size=size, cap=cap, note=note)
        for n, size, cap, note in c["items"])

    # медиа-блок: видео если есть, иначе фото
    if c.get("video"):
        media = """<figure class="showcase reveal">
<video autoplay muted loop playsinline preload="metadata" poster="assets/img/{img}" aria-label="{t} — видеовизуализация">
<source src="assets/video/{v}" type="video/mp4">
</video>
<figcaption class="mono">{t} · ВИЗУАЛИЗАЦИЯ</figcaption>
</figure>""".format(img=c["img"], v=c["video"], t=c["title"].upper())
    else:
        media = """<figure class="showcase reveal">
<img src="assets/img/{img}" alt="{t} — визуализация Steppe Steel" loading="lazy">
<figcaption class="mono">{tu} · ВИЗУАЛИЗАЦИЯ</figcaption>
</figure>""".format(img=c["img"], t=c["title"], tu=c["title"].upper())

    # спец-блок для зернохранилищ: калькулятор
    extra = ""
    if c["slug"] == "zernohranilishcha":
        opts = "\n".join('<option value="{v}">{n} — {v} т/м</option>'.format(v=v, n=n)
                         for n, v, _ in GRAIN)
        feats = "\n".join(
            '<div class="minifeat"><span class="minifeat__k mono">{v} т/м</span>{n} — {d}</div>'.format(
                v=v, n=n, d=d) for n, v, d in GRAIN)
        extra = """<section class="section section--ink2">
<div class="container">
<div class="section__head">
<p class="eyebrow reveal">Калькулятор</p>
<h2 class="reveal">Сколько метров нужно под ваш намолот</h2>
<p class="section__lead reveal">Сечение здания типовое, поэтому весь расчёт сводится к&nbsp;одному вопросу: сколько тонн ложится на&nbsp;метр длины. Выберите культуру и&nbsp;объём — получите длину.</p>
</div>
<div class="calcbox reveal">
<div class="calcbox__form">
<label class="field"><span>Культура</span>
<select id="grain-crop">{opts}</select>
</label>
<label class="field"><span>Объём хранения, тонн</span>
<input type="number" id="grain-tons" min="100" max="60000" step="100" value="3000" inputmode="numeric">
</label>
<div class="calcbox__out">
<span class="calcbox__out-label mono">Длина здания</span>
<span class="calcbox__out-value mono" id="grain-out">≈ 45 м</span>
<span class="calcbox__out-note mono" id="grain-sections">одно здание, наращивается секциями</span>
</div>
<a href="kontakty.html#zayavka" class="btn btn--primary btn--block">Получить точный расчёт</a>
<p class="calcbox__disclaimer">Оценка по вместимости на 1&nbsp;м длины. Точный расчёт с&nbsp;учётом техники и&nbsp;раздельного хранения делает инженер.</p>
</div>
<div class="calcbox__side">
<p class="calcbox__side-title mono">ВМЕСТИМОСТЬ НА 1 М ДЛИНЫ</p>
{feats}
</div>
</div>
</div>
</section>""".format(opts=opts, feats=feats)

    body = """{crumbs}
<section class="page-hero page-hero--cat">
<div class="container">
<span class="page-hero__code mono">{code}</span>
<h1 class="reveal">{title}</h1>
<p class="section__lead reveal">{lead}</p>
<div class="page-hero__actions reveal">
<a href="kontakty.html#zayavka" class="btn btn--primary">Рассчитать стоимость</a>
<a href="{wa}" class="btn btn--ghost js-wa" data-wa="engineer">Консультация инженера</a>
</div>
</div>
</section>

<section class="section">
<div class="container">
{media}
</div>
</section>

<section class="section section--light">
<div class="container">
<div class="section__head">
<p class="eyebrow reveal">Типовые конфигурации</p>
<h2 class="reveal">Размеры и вместимость</h2>
<p class="section__lead reveal">Ниже — базовые конфигурации, от&nbsp;которых удобно отталкиваться. Любой размер считаем индивидуально: цена зависит от&nbsp;габаритов, нагрузок и&nbsp;комплектации, поэтому её называет инженер после расчёта.</p>
</div>
<div class="tbl-wrap reveal">
<table class="tbl">
<thead><tr><th>Конфигурация</th><th>Габариты</th><th>Вместимость / площадь</th><th>Особенности</th><th></th></tr></thead>
<tbody>
{rows}
</tbody>
</table>
</div>
</div>
</section>

{extra}

<section class="section">
<div class="container">
<div class="section__head">
<p class="eyebrow reveal">Что входит в комплект</p>
<h2 class="reveal">Заводской комплект под сборку</h2>
</div>
<div class="kit">
<div class="kit__item reveal"><span class="kit__n mono">01</span><h3>Раздел КМ</h3><p>Расчёт каркаса под снег, ветер и&nbsp;мороз вашей площадки. Спецификация металла — основа честной сметы.</p></div>
<div class="kit__item reveal"><span class="kit__n mono">02</span><h3>Чертежи КМД</h3><p>Деталировка каждой марки с&nbsp;отверстиями под болт. Каркас собирается как конструктор, без подгонки.</p></div>
<div class="kit__item reveal"><span class="kit__n mono">03</span><h3>Элементы каркаса</h3><p>Профили Sigma, C и&nbsp;П до&nbsp;{steel}, фермы, колонны и&nbsp;опорные узлы из&nbsp;чёрного металла.</p></div>
<div class="kit__item reveal"><span class="kit__n mono">04</span><h3>Крепёж и метизы</h3><p>Полный комплект болтовых соединений с&nbsp;ведомостью — 100% болтовая сборка без сварки на&nbsp;площадке.</p></div>
<div class="kit__item reveal"><span class="kit__n mono">05</span><h3>Маркировка и схемы</h3><p>Каждая деталь помечена, к&nbsp;комплекту идут сборочные схемы для монтажной бригады.</p></div>
<div class="kit__item reveal"><span class="kit__n mono">06</span><h3>Доставка и монтаж</h3><p>Отгрузка автотранспортом или ж/д, монтаж собственной бригадой со&nbsp;сдачей по&nbsp;акту.</p></div>
</div>
</div>
</section>

{cta}""".format(crumbs=breadcrumbs([("index.html", "Главная"), ("katalog.html", "Каталог"), (None, c["title"])]),
                code=c["code"], title=c["title"], lead=c["lead"], wa=WA,
                media=media, rows=rows, extra=extra, steel=SPECS["steel_max_mm"],
                cta=cta_band("Посчитаем ваш объект за 24 часа",
                             "Пришлите габариты или просто задачу — инженер подготовит расчёт, спецификацию и коммерческое предложение."))

    return page(cat_url(c["slug"]),
                "%s из металлоконструкций — Steppe Steel, Казахстан" % c["title"],
                (c["lead"][:150] + "").replace('\xa0', ' '),
                body, active="katalog.html")


def build_all():
    made = [build_catalog_index()]
    for c in CATALOG:
        made.append(build_category(c))
    return made
