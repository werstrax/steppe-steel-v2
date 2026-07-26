# -*- coding: utf-8 -*-
"""Главная страница."""
from _build import page, cta_band, cat_url, WA
from _data import BRAND, SPECS, GRAIN, CATALOG, PROCESS, ARTICLES, ADVANTAGES


def build_home():
    # 1. Сетка решений
    sol = "\n".join("""<a href="{u}" class="sol reveal">
<div class="sol__media"><img src="assets/img/{img}" alt="{t}" loading="lazy"></div>
<div class="sol__body"><span class="sol__code mono">{code}</span><h3>{t}</h3></div>
</a>""".format(u=cat_url(c["slug"]), img=c["img"], t=c["title"], code=c["code"])
        for c in CATALOG)

    # 2. Цифры — только правдивые технические
    facts = [
        ("3,5", " мм", "толщина оцинкованной стали — верх нашей линии профилирования"),
        ("24", " м", "пролёт без внутренних колонн: чистая площадь под технику"),
        ("140", " м", "максимальная длина зернохранилища, наращивается секциями"),
        ("45", " дн", "верхняя граница срока: контур здания под ключ за 30–45 дней"),
        ("50", "+ лет", "срок службы оцинкованного каркаса без покраски"),
        ("10", " дн", "поставка комплекта — конструкции в наличии на складе"),
    ]
    nums = "\n".join("""<div class="num reveal">
<span class="num__v mono"><span data-count="{v}" data-suffix="{s}">0{s}</span></span>
<span class="num__d">{d}</span>
</div>""".format(v=v, s=s, d=d) for v, s, d in facts)

    # 3. Профили
    prof = "\n".join("""<div class="prof reveal">
<span class="prof__mark mono">{m}</span>
<h3>{n}</h3>
<p class="prof__role">{role}</p>
<p class="prof__where"><span class="mono">ГДЕ РАБОТАЕТ</span>{where}</p>
</div>""".format(m=("Σ" if n == "Sigma" else n), n=n, role=role, where=where)
        for n, role, where in SPECS["profiles"])

    # 4. Преимущества
    adv = "\n".join("""<div class="adv reveal">
<span class="adv__n mono">{i:02d}</span>
<h3>{t}</h3>
<p>{d}</p>
</div>""".format(i=i + 1, t=t, d=d) for i, (t, d) in enumerate(ADVANTAGES))

    # 5. Оборудование
    eq = "\n".join("""<li class="eq reveal"><span class="eq__t">{t}</span><span class="eq__d">{d}</span></li>""".format(t=t, d=d)
                   for t, d in SPECS["equipment"])

    # 6. Калькулятор зерна
    opts = "\n".join('<option value="{v}">{n} — {v} т/м</option>'.format(v=v, n=n)
                     for n, v, _ in GRAIN)

    # 7. Процесс
    proc = "\n".join("""<li class="step reveal">
<span class="step__n mono">{n}</span>
<h3>{t}</h3>
<p>{d}</p>
<span class="step__dur mono">{dur}</span>
</li>""".format(n=n, t=t, d=d, dur=dur) for n, t, d, dur in PROCESS)

    # 8. Бегущая лента фото
    belt_imgs = ["ig-frame.jpg", "steppe-frame.jpg", "montage-drone.jpg", "winter-brand.jpg",
                 "grain-ext.jpg", "grain-karkas.jpg", "hangar-brand.jpg", "weld-brand.jpg"]
    belt = "".join('<div class="belt__i"><img src="assets/img/{i}" alt="" loading="lazy"></div>'.format(i=i)
                   for i in belt_imgs)

    # 9. Блог
    posts = "\n".join("""<a href="blog-{s}.html" class="post reveal">
<span class="post__tag mono">ИНЖЕНЕРНАЯ СТАТЬЯ</span>
<h3>{t}</h3>
<p>{d}</p>
<span class="post__more mono">Читать →</span>
</a>""".format(s=s, t=t, d=d) for s, t, d in ARTICLES)

    # 10. FAQ
    faqs = [
        ("Сколько стоит здание?",
         "Цена зависит от габаритов, нагрузок площадки и комплектации — назвать её «в среднем за м²» честно нельзя. Пришлите размеры или задачу: инженер посчитает и вернётся со спецификацией и коммерческим предложением в течение 24 часов."),
        ("Работаете только по Костанайской области?",
         "Нет. Завод стоит в селе Троебратское на трассе Костанай — Петропавловск, в самом селе есть ж/д станция Пресногорьковская. Отгружаем собственным автотранспортом и вагонами по всему Казахстану."),
        ("Можно монтировать зимой?",
         "Да. Фундамент на винтовых сваях без бетона — мокрых процессов нет, а каркас собирается на болтах без сварки на площадке. Расчёт ведём под морозы до −40 °C, поэтому монтаж не привязан к сезону."),
        ("Чем ЛСТК отличается от чёрного металла и что выберете вы?",
         "ЛСТК — лёгкий оцинкованный профиль до 3,5 мм, он выигрывает в весе, скорости монтажа и коррозионной стойкости. Чёрный металл нужен там, где есть крановые нагрузки и мощные узлы. Мы комбинируем оба в одном здании — каждая тонна стали работает по назначению."),
        ("Что вы даёте кроме металла?",
         "Раздел КМ с расчётом под вашу площадку, чертежи КМД с деталировкой каждой марки, комплект крепежа с ведомостью, маркировку деталей и сборочные схемы. По желанию — доставку и монтаж собственной бригадой со сдачей по акту."),
        ("Нужен ли бетонный фундамент?",
         "Для зернохранилищ и большинства ангаров — нет: работаем на винтовых сваях с металлическим ростверком. Это экономит недели на площадке и позволяет начинать в любой сезон. Нагрузки на фундамент считаем в разделе КМ."),
    ]
    faq = "\n".join("""<div class="faq__item reveal">
<button class="faq__q" aria-expanded="false"><span>{q}</span></button>
<div class="faq__a"><p>{a}</p></div>
</div>""".format(q=q, a=a) for q, a in faqs)

    body = """<!-- ═══ ПЕРВЫЙ ЭКРАН ═══ -->
<section class="hero">
<div class="hero__bg" aria-hidden="true">
<video class="hero__video" autoplay muted loop playsinline preload="metadata" poster="assets/img/hero-poster.jpg">
<source src="assets/video/hero-steppe.mp4" type="video/mp4">
</video>
<div class="hero__scrim"></div>
</div>
<div class="container hero__inner">
<p class="hero__eyebrow mono">ЗАВОД МЕТАЛЛОКОНСТРУКЦИЙ · КОСТАНАЙСКАЯ ОБЛАСТЬ · {tagline}</p>
<h1 class="hero__title">Ангары, зернохранилища и&nbsp;промышленные здания <span class="accent">под ключ</span></h1>
<p class="hero__lead">Завод полного цикла: проектируем, производим, комплектуем и&nbsp;монтируем. ЛСТК и&nbsp;чёрный металл, пролёт до&nbsp;{span} без колонн, контур здания за&nbsp;{days}&nbsp;дней.</p>
<div class="hero__actions">
<a href="katalog.html" class="btn btn--primary btn--lg">Смотреть каталог</a>
<a href="kontakty.html#zayavka" class="btn btn--ghost btn--lg">Рассчитать стоимость</a>
</div>
</div>
<div class="hero__strip">
<div class="container hero__strip-inner mono">
<span>ЛСТК + чёрный металл</span><span>Оцинковка до {steel}</span><span>Пролёт до {span}</span><span>Расчёт за 24 часа</span><span>Доставка по Казахстану</span>
</div>
</div>
</section>

<!-- ═══ РЕШЕНИЯ ═══ -->
<section class="section" id="solutions">
<div class="container">
<div class="section__head">
<p class="eyebrow reveal">Наши решения</p>
<h2 class="reveal">Шесть направлений на&nbsp;одном каркасе</h2>
<p class="section__lead reveal">От зернохранилища на&nbsp;винтовых сваях до&nbsp;цеха под крановые нагрузки. Любой размер считаем индивидуально — под ваш участок, объём и&nbsp;нагрузки.</p>
</div>
<div class="solgrid">
{sol}
</div>
</div>
</section>

<!-- ═══ ЦИФРЫ ═══ -->
<section class="section section--ink2" id="numbers">
<div class="container">
<div class="section__head">
<p class="eyebrow reveal">Завод в цифрах</p>
<h2 class="reveal">Инженерные параметры, а&nbsp;не&nbsp;обещания</h2>
<p class="section__lead reveal">Здесь только то, что зафиксировано в&nbsp;расчёте и&nbsp;спецификации. Цифры по&nbsp;объектам и&nbsp;срокам работы компании появятся здесь, когда мы&nbsp;сможем подтвердить каждую документами.</p>
</div>
<div class="numgrid">
{nums}
</div>
</div>
</section>

<!-- ═══ ПРОИЗВОДСТВО (видео) ═══ -->
<section class="section" id="factory">
<div class="container">
<div class="split">
<div class="split__text">
<p class="eyebrow reveal">Производство</p>
<h2 class="reveal">Собственная линия профилирования</h2>
<p class="section__lead reveal">Оцинкованная сталь толщиной до&nbsp;{steel} проходит через нашу линию профилирования, плазменную и&nbsp;лазерную резку, резьбонарезные и&nbsp;сварочные участки. Геометрия одинакова на&nbsp;всей партии — детали сходятся на&nbsp;монтаже без подгонки.</p>
<ul class="eqlist">
{eq}
</ul>
<a href="proizvodstvo.html" class="btn btn--ghost reveal">Как устроено производство</a>
</div>
<figure class="split__media reveal">
<video autoplay muted loop playsinline preload="metadata" poster="assets/img/prod-line.jpg" aria-label="Линия профилирования — видеовизуализация">
<source src="assets/video/line.mp4" type="video/mp4">
</video>
<figcaption class="mono">ЛИНИЯ ПРОФИЛИРОВАНИЯ · ВИЗУАЛИЗАЦИЯ</figcaption>
</figure>
</div>
</div>
</section>

<!-- ═══ ПРОФИЛИ ═══ -->
<section class="section section--light" id="profiles">
<div class="container">
<div class="section__head">
<p class="eyebrow reveal">Линейка профилей</p>
<h2 class="reveal">Три профиля — три задачи в&nbsp;каркасе</h2>
<p class="section__lead reveal">Толщина подбирается под расчётную нагрузку: чем выше снеговая нагрузка и&nbsp;пролёт, тем толще металл в&nbsp;несущих элементах. Максимум нашей линии — {steel}.</p>
</div>
<div class="profgrid">
{prof}
</div>
<p class="note reveal">Расчёт ведём под {snow}&nbsp;снеговой район севера Казахстана ({snow_load}) и&nbsp;эксплуатацию при морозах до&nbsp;{temp}. Раздел КМ выпускаем на&nbsp;каждый объект.</p>
</div>
</section>

<!-- ═══ ПРЕИМУЩЕСТВА ═══ -->
<section class="section" id="why">
<div class="container">
<div class="section__head">
<p class="eyebrow reveal">Почему Steppe Steel</p>
<h2 class="reveal">Шесть причин строить у&nbsp;нас</h2>
</div>
<div class="advgrid">
{adv}
</div>
</div>
</section>

<!-- ═══ ЗЕРНОХРАНИЛИЩА + КАЛЬКУЛЯТОР ═══ -->
<section class="section section--ink2" id="grain">
<div class="container">
<div class="section__head">
<p class="eyebrow reveal">Флагманский продукт</p>
<h2 class="reveal">Зернохранилище нового поколения</h2>
<p class="section__lead reveal">Напольное хранение навалом на&nbsp;винтовых сваях — без бетона. Наклонные стены и&nbsp;подкосная система рассчитаны на&nbsp;боковое давление зерна, длина наращивается секциями до&nbsp;{grain_len}&nbsp;м. Костанайская область собрала 6,7&nbsp;млн тонн зерна, а&nbsp;хранилища страны вмещают около половины урожая.</p>
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
<a href="katalog-zernohranilishcha.html" class="btn btn--primary btn--block">Смотреть зернохранилища</a>
<p class="calcbox__disclaimer">Оценка по вместимости на 1&nbsp;м длины. Точный расчёт с&nbsp;запасом на&nbsp;технику и&nbsp;раздельное хранение делает инженер.</p>
</div>
<figure class="calcbox__media">
<video autoplay muted loop playsinline preload="metadata" poster="assets/img/grain-ext.jpg" aria-label="Зернохранилище — видеовизуализация">
<source src="assets/video/grain2.mp4" type="video/mp4">
</video>
<figcaption class="mono">ЗЕРНОХРАНИЛИЩЕ НА ВИНТОВЫХ СВАЯХ · ВИЗУАЛИЗАЦИЯ</figcaption>
</figure>
</div>
</div>
</section>

<!-- ═══ ПРОЦЕСС ═══ -->
<section class="section section--light" id="process">
<div class="container">
<div class="section__head">
<p class="eyebrow reveal">Как мы работаем</p>
<h2 class="reveal">От заявки до&nbsp;сдачи по&nbsp;акту</h2>
<p class="section__lead reveal">Шесть шагов и&nbsp;один договор: цена и&nbsp;срок фиксируются после утверждения проекта КМ/КМД, оплата — по&nbsp;этапам.</p>
</div>
<ol class="steps">
{proc}
</ol>
</div>
</section>

<!-- ═══ ГАЛЕРЕЯ ═══ -->
<section class="section" id="gallery">
<div class="container">
<div class="section__head">
<p class="eyebrow reveal">Каркасы и проекты</p>
<h2 class="reveal">Как это выглядит</h2>
<p class="section__lead reveal">Реальные фото монтажа и&nbsp;проектные визуализации. Больше процессов и&nbsp;объектов — в&nbsp;Instagram <a href="{ig}" target="_blank" rel="noopener" class="accent">{ig_h}</a>.</p>
</div>
</div>
<div class="belt" aria-hidden="true">
<div class="belt__track">{belt}{belt}</div>
</div>
<div class="container">
<p class="note reveal">Фото каркаса — реальный объект Steppe Steel; остальные кадры — проектные визуализации.</p>
</div>
</section>

<!-- ═══ БЛОГ ═══ -->
<section class="section section--ink2" id="blog">
<div class="container">
<div class="section__head">
<p class="eyebrow reveal">Инженерный блог</p>
<h2 class="reveal">Разбираем то, о&nbsp;чём спрашивают чаще всего</h2>
</div>
<div class="postgrid">
{posts}
</div>
</div>
</section>

<!-- ═══ FAQ ═══ -->
<section class="section" id="faq">
<div class="container">
<div class="section__head">
<p class="eyebrow reveal">Вопросы и ответы</p>
<h2 class="reveal">Что спрашивают перед договором</h2>
</div>
<div class="faq">
{faq}
</div>
</div>
</section>

{cta}""".format(
        tagline=BRAND["tagline"], span=SPECS["span_max_m"], days=SPECS["build_days"],
        steel=SPECS["steel_max_mm"], sol=sol, nums=nums, eq=eq, prof=prof,
        snow=SPECS["snow_region"], snow_load=SPECS["snow_load"], temp=SPECS["temp_min"],
        adv=adv, grain_len=SPECS["grain_max_len_m"], opts=opts, proc=proc,
        belt=belt, ig=BRAND["instagram"], ig_h=BRAND["instagram_handle"],
        posts=posts, faq=faq,
        cta=cta_band("Расчёт и коммерческое предложение за 24 часа",
                     "Пришлите габариты или просто опишите задачу — инженер посчитает каркас, подготовит спецификацию и назовёт срок."))

    return page("index.html",
                "Steppe Steel — завод металлоконструкций и ЛСТК в Казахстане",
                "Завод металлоконструкций полного цикла в Костанайской области: ангары, зернохранилища, склады, цеха. ЛСТК и чёрный металл, пролёт до 24 м. Расчёт за 24 часа.",
                body, active="index.html")
