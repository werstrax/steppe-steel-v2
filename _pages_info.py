# -*- coding: utf-8 -*-
"""Внутренние страницы: производство, технология, доставка, о компании, контакты, блог."""
from _build import page, cta_band, breadcrumbs, cat_url, WA
from _data import BRAND, SPECS, GRAIN, CATALOG, PROCESS, ARTICLES, ADVANTAGES

CRUMB_HOME = ("index.html", "Главная")


def _hero(eyebrow, h1, lead, actions=True):
    act = """<div class="page-hero__actions reveal">
<a href="kontakty.html#zayavka" class="btn btn--primary">Рассчитать стоимость</a>
<a href="{wa}" class="btn btn--ghost js-wa" data-wa="engineer">Консультация инженера</a>
</div>""".format(wa=WA) if actions else ""
    return """<section class="page-hero">
<div class="container">
<p class="eyebrow reveal">{e}</p>
<h1 class="reveal">{h}</h1>
<p class="section__lead reveal">{l}</p>
{act}
</div>
</section>""".format(e=eyebrow, h=h1, l=lead, act=act)


# ═══════════ ПРОИЗВОДСТВО ═══════════
def build_production():
    eq = "\n".join("""<div class="adv reveal"><span class="adv__n mono">{i:02d}</span><h3>{t}</h3><p>{d}</p></div>""".format(
        i=i + 1, t=t, d=d) for i, (t, d) in enumerate(SPECS["equipment"]))

    body = """{cr}
{hero}

<section class="section">
<div class="container">
<figure class="showcase reveal">
<video autoplay muted loop playsinline preload="metadata" poster="assets/img/prod-line.jpg" aria-label="Линия профилирования — видеовизуализация">
<source src="assets/video/line.mp4" type="video/mp4">
</video>
<figcaption class="mono">ЛИНИЯ ПРОФИЛИРОВАНИЯ · ОЦИНКОВАННЫЙ ПРОФИЛЬ · ВИЗУАЛИЗАЦИЯ</figcaption>
</figure>
</div>
</section>

<section class="section section--ink2">
<div class="container">
<div class="section__head">
<p class="eyebrow reveal">Участки</p>
<h2 class="reveal">Что стоит за словом «завод»</h2>
<p class="section__lead reveal">Не сборочная площадка и&nbsp;не&nbsp;перепродажа профиля: раскрой, обработка, сборка узла и&nbsp;контроль — внутри одного предприятия. Оборудование работает по&nbsp;программам из&nbsp;раздела КМ, без ручной разметки «на&nbsp;глаз».</p>
</div>
<div class="advgrid">
{eq}
</div>
</div>
</section>

<section class="section">
<div class="container">
<div class="split">
<div class="split__text">
<p class="eyebrow reveal">Контроль</p>
<h2 class="reveal">Одинаковая геометрия на&nbsp;всей партии</h2>
<p class="section__lead reveal">Отверстия под болт выполняются на&nbsp;производстве по&nbsp;чертежам КМД, а&nbsp;не&nbsp;«болгаркой по&nbsp;месту». Каждая деталь маркируется — каркас собирается на&nbsp;площадке как конструктор, без подгонки. Это то, что отличает заводской комплект от&nbsp;металла, нарезанного на&nbsp;коленке.</p>
<ul class="eqlist">
<li class="eq reveal"><span class="eq__t">Раскрой по картам</span><span class="eq__d">минимальный отход металла, повторяемость деталей</span></li>
<li class="eq reveal"><span class="eq__t">Отверстия на заводе</span><span class="eq__d">элементы сходятся на монтаже без рассверливания</span></li>
<li class="eq reveal"><span class="eq__t">Маркировка деталей</span><span class="eq__d">каждая марка помечена и указана в сборочной схеме</span></li>
<li class="eq reveal"><span class="eq__t">Сварка в кондукторах</span><span class="eq__d">фермы и колонны из чёрного металла с контролем геометрии</span></li>
</ul>
</div>
<figure class="split__media reveal">
<img src="assets/img/weld-brand.jpg" alt="Сварка узла стальной фермы — визуализация" loading="lazy">
<figcaption class="mono">СВАРОЧНЫЙ УЧАСТОК · ВИЗУАЛИЗАЦИЯ</figcaption>
</figure>
</div>
</div>
</section>

<section class="section section--light">
<div class="container">
<div class="section__head">
<p class="eyebrow reveal">Материал</p>
<h2 class="reveal">Оцинкованная сталь до&nbsp;{steel}</h2>
<p class="section__lead reveal">Толщина подбирается под расчётную нагрузку. Цинковое покрытие защищает металл {zinc}&nbsp;лет без покраски и&nbsp;антикоррозийного обслуживания — каркас переживает не&nbsp;одно поколение кровли.</p>
</div>
<div class="tbl-wrap reveal">
<table class="tbl">
<thead><tr><th>Параметр</th><th>Значение</th><th>Что это значит для объекта</th></tr></thead>
<tbody>
<tr><td><strong>Толщина стали</strong></td><td class="mono accent">до {steel}</td><td>Верх нашей линии профилирования — хватает на несущие элементы больших пролётов</td></tr>
<tr><td><strong>Пролёт без колонн</strong></td><td class="mono accent">до {span}</td><td>Чистая рабочая площадь: техника и стеллажи не упираются в опоры</td></tr>
<tr><td><strong>Снеговой район</strong></td><td class="mono accent">{snow} ({snow_load})</td><td>Расчёт под север Казахстана, а не типовой пакет «средней полосы»</td></tr>
<tr><td><strong>Температура эксплуатации</strong></td><td class="mono accent">до {temp}</td><td>Материал и узлы рассчитаны на зимнюю эксплуатацию и монтаж</td></tr>
<tr><td><strong>Срок службы оцинковки</strong></td><td class="mono accent">{zinc} лет</td><td>Без покраски и обслуживания в течение всего срока</td></tr>
<tr><td><strong>Поставка комплекта</strong></td><td class="mono accent">{supply} дней</td><td>Конструкции в наличии — старт проекта без ожидания проката</td></tr>
</tbody>
</table>
</div>
</div>
</section>

{cta}""".format(
        cr=breadcrumbs([CRUMB_HOME, (None, "Производство")]),
        hero=_hero("Производство",
                   "Завод полного цикла",
                   "Профилирование оцинкованной стали, плазменная и&nbsp;лазерная резка, резьбонарезные и&nbsp;сварочные участки. Проектирование, производство, комплектация и&nbsp;отгрузка — внутри одного предприятия, без посредников и&nbsp;потери ответственности между подрядчиками."),
        eq=eq, steel=SPECS["steel_max_mm"], span=SPECS["span_max_m"], zinc=SPECS["zinc_years"],
        snow=SPECS["snow_region"], snow_load=SPECS["snow_load"], temp=SPECS["temp_min"],
        supply=SPECS["supply_days"],
        cta=cta_band("Нужен расчёт под ваш объект?",
                     "Инженер посчитает каркас под нагрузки вашей площадки и подготовит спецификацию в течение 24 часов."))

    return page("proizvodstvo.html",
                "Производство металлоконструкций — завод Steppe Steel, Казахстан",
                "Собственная линия профилирования, плазменная и лазерная резка, сварочные участки. Оцинкованная сталь до 3,5 мм, контроль геометрии на каждом этапе.",
                body, active="proizvodstvo.html")


# ═══════════ ТЕХНОЛОГИЯ ═══════════
def build_technology():
    prof = "\n".join("""<div class="prof reveal">
<span class="prof__mark mono">{m}</span>
<h3>{n}</h3>
<p class="prof__role">{role}</p>
<p class="prof__where"><span class="mono">ГДЕ РАБОТАЕТ</span>{where}</p>
</div>""".format(m=("Σ" if n == "Sigma" else n), n=n, role=role, where=where)
        for n, role, where in SPECS["profiles"])

    body = """{cr}
{hero}

<section class="section section--light">
<div class="container">
<div class="section__head">
<p class="eyebrow reveal">Линейка профилей</p>
<h2 class="reveal">Три профиля — три задачи</h2>
<p class="section__lead reveal">Толщина каждого подбирается под расчётную нагрузку: чем выше снеговая нагрузка и&nbsp;пролёт, тем толще металл в&nbsp;несущих элементах. Максимум линии — {steel}.</p>
</div>
<div class="profgrid">
{prof}
</div>
</div>
</section>

<section class="section">
<div class="container">
<div class="section__head">
<p class="eyebrow reveal">Два материала</p>
<h2 class="reveal">ЛСТК и&nbsp;чёрный металл: зачем комбинировать</h2>
<p class="section__lead reveal">«Что лучше?» — вопрос поставлен неправильно. У&nbsp;каждого материала своя зона, где он&nbsp;выигрывает, и&nbsp;правильный проект чаще всего использует оба.</p>
</div>
<div class="tbl-wrap reveal">
<table class="tbl">
<thead><tr><th>Критерий</th><th>ЛСТК (оцинкованный профиль)</th><th>Чёрный металл (прокат)</th></tr></thead>
<tbody>
<tr><td><strong>Вес каркаса</strong></td><td>лёгкий — меньше нагрузка на фундамент, дешевле основание и логистика</td><td>тяжелее в разы — массивные фундаменты, дороже доставка</td></tr>
<tr><td><strong>Пролёты</strong></td><td><span class="mono accent">до {span}</span> без внутренних колонн</td><td>большие пролёты и высоты за счёт сварных ферм</td></tr>
<tr><td><strong>Крановые нагрузки</strong></td><td>не рассчитан на мостовые краны</td><td>кран-балки и мостовые краны — штатный режим</td></tr>
<tr><td><strong>Скорость монтажа</strong></td><td>болтовая сборка без сварки на площадке — быстро, в том числе зимой</td><td>сварка и укрупнительная сборка — дольше и дороже на площадке</td></tr>
<tr><td><strong>Защита от коррозии</strong></td><td>оцинковка — <span class="mono accent">{zinc} лет</span> без покраски</td><td>лакокрасочное покрытие с периодическим обновлением</td></tr>
<tr><td><strong>Стоимость</strong></td><td>ниже: меньше стали, легче фундамент</td><td>выше металлоёмкость — оправдана там, где нужна несущая способность</td></tr>
</tbody>
</table>
</div>
<p class="note reveal">Подробный разбор с&nbsp;примерами — в&nbsp;статье <a href="blog-lstk-lmk.html" class="accent">«ЛСТК или чёрный металл: что выбрать»</a>.</p>
</div>
</section>

<section class="section section--ink2">
<div class="container">
<div class="split">
<div class="split__text">
<p class="eyebrow reveal">Фундамент</p>
<h2 class="reveal">Винтовые сваи вместо бетона</h2>
<p class="section__lead reveal">Свайный фундамент с&nbsp;металлическим ростверком снимает с&nbsp;площадки мокрые процессы: не&nbsp;нужно ждать набора прочности бетона, а&nbsp;монтаж не&nbsp;привязан к&nbsp;сезону и&nbsp;идёт при морозах до&nbsp;{temp}. Нагрузки на&nbsp;фундамент считаются в&nbsp;разделе КМ.</p>
<ul class="eqlist">
<li class="eq reveal"><span class="eq__t">Без бетонных работ</span><span class="eq__d">экономия недель на площадке и денег на основании</span></li>
<li class="eq reveal"><span class="eq__t">Монтаж зимой</span><span class="eq__d">нет мокрых процессов — сезон не диктует график</span></li>
<li class="eq reveal"><span class="eq__t">100% болтовые узлы</span><span class="eq__d">каркас разборный: ликвидный актив, можно перевезти</span></li>
<li class="eq reveal"><span class="eq__t">Ростверк из металла</span><span class="eq__d">связывает сваи и распределяет нагрузку по основанию</span></li>
</ul>
<a href="blog-fundament.html" class="btn btn--ghost reveal">Разбор: сваи против бетона</a>
</div>
<figure class="split__media reveal">
<img src="assets/img/grain-joint.jpg" alt="Опорный узел: винтовая свая, ростверк и подкос на болтах — визуализация" loading="lazy">
<figcaption class="mono">ОПОРНЫЙ УЗЕЛ · СВАЯ, РОСТВЕРК И ПОДКОС · ВИЗУАЛИЗАЦИЯ</figcaption>
</figure>
</div>
</div>
</section>

<section class="section section--light">
<div class="container">
<div class="section__head">
<p class="eyebrow reveal">Документация</p>
<h2 class="reveal">КМ и&nbsp;КМД — что вы получаете на&nbsp;руки</h2>
</div>
<div class="steps">
<li class="step reveal"><span class="step__n mono">КМ</span><h3>Конструкции металлические</h3><p>Расчётная схема и&nbsp;сбор нагрузок под вашу площадку, подбор сечений, конструктивные решения узлов, спецификация металла и&nbsp;нагрузки на&nbsp;фундамент.</p><span class="step__dur mono">для экспертизы, банка, субсидий</span></li>
<li class="step reveal"><span class="step__n mono">КМД</span><h3>Деталировочные чертежи</h3><p>Чертёж каждой марки и&nbsp;отправочного элемента, все отверстия под болт, маркировка деталей, сборочные схемы и&nbsp;ведомость метизов.</p><span class="step__dur mono">для производства и монтажа</span></li>
</div>
<p class="note reveal">Зачем это заказчику и&nbsp;почему без проекта цена всегда «на&nbsp;глаз» — в&nbsp;статье <a href="blog-km-kmd.html" class="accent">«Что такое КМ и&nbsp;КМД»</a>.</p>
</div>
</section>

{cta}""".format(
        cr=breadcrumbs([CRUMB_HOME, (None, "Технология")]),
        hero=_hero("Технология",
                   "Как устроен наш каркас",
                   "Оцинкованный тонкостенный профиль до&nbsp;{steel} в&nbsp;связке с&nbsp;чёрным металлом, свайный фундамент без бетона и&nbsp;100% болтовая сборка. Ниже — из&nbsp;чего это состоит и&nbsp;почему работает на&nbsp;севере Казахстана.".format(steel=SPECS["steel_max_mm"])),
        prof=prof, steel=SPECS["steel_max_mm"], span=SPECS["span_max_m"],
        zinc=SPECS["zinc_years"], temp=SPECS["temp_min"],
        cta=cta_band("Подберём конструктив под вашу задачу",
                     "Опишите объект и площадку — инженер предложит схему каркаса и посчитает металлоёмкость."))

    return page("tehnologiya.html",
                "Технология ЛСТК: профили Sigma, C, П и чёрный металл — Steppe Steel",
                "Оцинкованный профиль до 3,5 мм, комбинирование с чёрным металлом, винтовые сваи без бетона, разделы КМ и КМД. Расчёт под III снеговой район Казахстана.",
                body, active="tehnologiya.html")


# ═══════════ ДОСТАВКА И МОНТАЖ ═══════════
def build_delivery():
    proc = "\n".join("""<li class="step reveal">
<span class="step__n mono">{n}</span><h3>{t}</h3><p>{d}</p><span class="step__dur mono">{dur}</span>
</li>""".format(n=n, t=t, d=d, dur=dur) for n, t, d, dur in PROCESS)

    body = """{cr}
{hero}

<section class="section section--light">
<div class="container">
<div class="section__head">
<p class="eyebrow reveal">Этапы</p>
<h2 class="reveal">От заявки до&nbsp;сдачи по&nbsp;акту</h2>
<p class="section__lead reveal">Цена и&nbsp;срок фиксируются в&nbsp;договоре после утверждения КМ/КМД. Оплата — по&nbsp;этапам, без «доплатите ещё столько же в&nbsp;середине стройки».</p>
</div>
<ol class="steps">
{proc}
</ol>
</div>
</section>

<section class="section">
<div class="container">
<div class="split">
<div class="split__text">
<p class="eyebrow reveal">Логистика</p>
<h2 class="reveal">Два канала отгрузки прямо с&nbsp;площадки</h2>
<p class="section__lead reveal">Завод стоит на&nbsp;трассе Костанай&nbsp;— Петропавловск, а&nbsp;ж/д станция Пресногорьковская находится в&nbsp;самом селе Троебратское. Машина с&nbsp;комплектом уходит на&nbsp;магистраль без перегрузок и&nbsp;«плеча» до&nbsp;терминала.</p>
<ul class="eqlist">
<li class="eq reveal"><span class="eq__t">Автотранспорт</span><span class="eq__d">собственные машины, отгрузка комплектом с площадки завода</span></li>
<li class="eq reveal"><span class="eq__t">Железная дорога</span><span class="eq__d">станция Пресногорьковская — в самом селе, без промежуточного плеча</span></li>
<li class="eq reveal"><span class="eq__t">По всему Казахстану</span><span class="eq__d">Костанайская, Северо-Казахстанская, Акмолинская области и дальше</span></li>
<li class="eq reveal"><span class="eq__t">Комплектная поставка</span><span class="eq__d">элементы каркаса, крепёж и схемы сборки — одной отгрузкой</span></li>
</ul>
</div>
<figure class="split__media reveal">
<img src="assets/img/montage-drone.jpg" alt="Монтаж каркаса в степи — визуализация" loading="lazy">
<figcaption class="mono">МОНТАЖ КАРКАСА · ВИЗУАЛИЗАЦИЯ</figcaption>
</figure>
</div>
</div>
</section>

<section class="section section--ink2">
<div class="container">
<div class="split">
<figure class="split__media reveal">
<img src="assets/img/winter-brand.jpg" alt="Зимний монтаж каркаса — визуализация" loading="lazy">
<figcaption class="mono">МОНТАЖ ЗИМОЙ · ВИЗУАЛИЗАЦИЯ</figcaption>
</figure>
<div class="split__text">
<p class="eyebrow reveal">Монтаж</p>
<h2 class="reveal">Своя бригада и&nbsp;работа зимой</h2>
<p class="section__lead reveal">Монтаж ведёт наша бригада со&nbsp;сдачей по&nbsp;акту. Каркас собирается на&nbsp;болтах, сварки на&nbsp;площадке нет, фундамент свайный — поэтому работы не&nbsp;останавливаются в&nbsp;мороз и&nbsp;не&nbsp;ждут схватывания бетона.</p>
<ul class="eqlist">
<li class="eq reveal"><span class="eq__t">Болтовая сборка</span><span class="eq__d">все отверстия выполнены на заводе по КМД</span></li>
<li class="eq reveal"><span class="eq__t">Без мокрых процессов</span><span class="eq__d">свайный фундамент — зимний монтаж штатный режим</span></li>
<li class="eq reveal"><span class="eq__t">Сдача по акту</span><span class="eq__d">фиксируем объём и качество выполненных работ</span></li>
<li class="eq reveal"><span class="eq__t">Шеф-монтаж</span><span class="eq__d">если собираете своими силами — сопровождаем сборку</span></li>
</ul>
</div>
</div>
</div>
</section>

{cta}""".format(
        cr=breadcrumbs([CRUMB_HOME, (None, "Доставка и монтаж")]),
        hero=_hero("Доставка и монтаж",
                   "Довозим и&nbsp;собираем сами",
                   "Отгрузка автотранспортом и&nbsp;вагонами по&nbsp;всему Казахстану, монтаж собственной бригадой со&nbsp;сдачей по&nbsp;акту. Контур здания — за&nbsp;{days}&nbsp;дней от&nbsp;договора.".format(days=SPECS["build_days"])),
        proc=proc,
        cta=cta_band("Посчитаем срок под вашу площадку",
                     "Назовите регион и объект — скажем реальный срок производства, доставки и монтажа."))

    return page("dostavka-montazh.html",
                "Доставка и монтаж металлоконструкций по Казахстану — Steppe Steel",
                "Отгрузка автотранспортом и ж/д со станции Пресногорьковская, монтаж собственной бригадой. Болтовая сборка без сварки, работы идут и зимой.",
                body, active="dostavka-montazh.html")


# ═══════════ О КОМПАНИИ ═══════════
def build_about():
    adv = "\n".join("""<div class="adv reveal"><span class="adv__n mono">{i:02d}</span><h3>{t}</h3><p>{d}</p></div>""".format(
        i=i + 1, t=t, d=d) for i, (t, d) in enumerate(ADVANTAGES))

    body = """{cr}
{hero}

<section class="section">
<div class="container">
<figure class="showcase reveal">
<img src="assets/img/ig-frame.jpg" alt="Оцинкованный каркас Steppe Steel на монтаже" loading="lazy">
<figcaption class="mono">НАШ КАРКАС · ОЦИНКОВАННАЯ ЛСТК · РЕАЛЬНЫЙ ОБЪЕКТ</figcaption>
</figure>
</div>
</section>

<section class="section section--ink2">
<div class="container">
<div class="section__head">
<p class="eyebrow reveal">Подход</p>
<h2 class="reveal">Шесть причин строить у&nbsp;нас</h2>
</div>
<div class="advgrid">
{adv}
</div>
</div>
</section>

<section class="section section--light">
<div class="container">
<div class="split">
<div class="split__text">
<p class="eyebrow reveal">География</p>
<h2 class="reveal">Почему завод стоит именно здесь</h2>
<p class="section__lead reveal">Село Троебратское — Узункольский район Костанайской области, север Казахстана, центр зернового пояса. Костанайская область собрала 6,7&nbsp;млн тонн зерна, а&nbsp;хранилища страны вмещают около половины урожая — поэтому зернохранилища мы&nbsp;считаем флагманским продуктом.</p>
<ul class="eqlist">
<li class="eq reveal"><span class="eq__t">Трасса</span><span class="eq__d">Костанай — Петропавловск: прямой выход на магистраль в обе стороны</span></li>
<li class="eq reveal"><span class="eq__t">Железная дорога</span><span class="eq__d">станция Пресногорьковская — в самом селе</span></li>
<li class="eq reveal"><span class="eq__t">Рядом зерновой пояс</span><span class="eq__d">Костанайская, Северо-Казахстанская и Акмолинская области</span></li>
<li class="eq reveal"><span class="eq__t">Короткое плечо</span><span class="eq__d">мы уже в вашем регионе, пока другие везут каркас за 2 000 км</span></li>
</ul>
</div>
<figure class="split__media reveal">
<img src="assets/img/steppe-frame.jpg" alt="Каркас ангара в степи — визуализация" loading="lazy">
<figcaption class="mono">КАРКАС В СТЕПИ · ВИЗУАЛИЗАЦИЯ</figcaption>
</figure>
</div>
</div>
</section>

<section class="section">
<div class="container">
<div class="section__head">
<p class="eyebrow reveal">Честно о нас</p>
<h2 class="reveal">Чего вы здесь не&nbsp;найдёте</h2>
<p class="section__lead reveal">На сайтах конкурентов принято писать «17&nbsp;лет на&nbsp;рынке», «500&nbsp;объектов» и&nbsp;показывать отзывы. Мы&nbsp;не&nbsp;публикуем цифры и&nbsp;отзывы, которые не&nbsp;можем подтвердить документами. Вместо этого показываем то, что проверяется: технические параметры, состав производства, документацию и&nbsp;реальные фото с&nbsp;монтажа в&nbsp;нашем Instagram <a href="{ig}" target="_blank" rel="noopener" class="accent">{ig_h}</a>.</p>
</div>
<div class="advgrid">
<div class="adv reveal"><span class="adv__n mono">→</span><h3>Что показываем</h3><p>Толщину стали, пролёты, снеговой район расчёта, состав комплекта, документацию КМ/КМД, фото с&nbsp;монтажа и&nbsp;проектные визуализации с&nbsp;честной подписью.</p></div>
<div class="adv reveal"><span class="adv__n mono">→</span><h3>Что скажем по запросу</h3><p>Реквизиты и&nbsp;карточку предприятия для договора, спецификацию металла по&nbsp;вашему объекту, референсы — по&nbsp;мере готовности заказчиков их&nbsp;раскрывать.</p></div>
<div class="adv reveal"><span class="adv__n mono">→</span><h3>Как проверить нас</h3><p>Задайте инженеру технический вопрос в&nbsp;WhatsApp. Разговор по&nbsp;существу о&nbsp;нагрузках, узлах и&nbsp;сечениях проверяет подрядчика лучше любого баннера с&nbsp;цифрами.</p></div>
</div>
</div>
</section>

{cta}""".format(
        cr=breadcrumbs([CRUMB_HOME, (None, "О компании")]),
        hero=_hero("О компании",
                   "Steppe Steel — завод металлоконструкций",
                   "Полный цикл в&nbsp;одних руках: проектирование&nbsp;→ производство&nbsp;→ комплектация&nbsp;→ отгрузка и&nbsp;монтаж. Работаем с&nbsp;ЛСТК и&nbsp;чёрным металлом, комбинируем технологии под объекты любой сложности. {tagline} — не&nbsp;слоган, а&nbsp;способ работы: расчёт, раздел КМ и&nbsp;контроль на&nbsp;каждом этапе.".format(tagline=BRAND["tagline"])),
        adv=adv, ig=BRAND["instagram"], ig_h=BRAND["instagram_handle"],
        cta=cta_band("Поговорим предметно?",
                     "Инженер ответит на технические вопросы и посчитает ваш объект — без давления и обзвонов."))

    return page("o-kompanii.html",
                "О компании Steppe Steel — завод металлоконструкций в Казахстане",
                "Завод полного цикла в Костанайской области: ЛСТК и чёрный металл, проектирование, производство, доставка и монтаж по всему Казахстану.",
                body, active="o-kompanii.html")


# ═══════════ КОНТАКТЫ ═══════════
def build_contacts():
    types = "\n".join('<option value="{t}">{t}</option>'.format(t=c["title"]) for c in CATALOG)

    body = """{cr}
<section class="page-hero">
<div class="container">
<p class="eyebrow reveal">Контакты</p>
<h1 class="reveal">Свяжитесь с&nbsp;инженером</h1>
<p class="section__lead reveal">Самый быстрый способ — написать в&nbsp;WhatsApp: отвечаем круглосуточно, отвечает инженер, а&nbsp;не&nbsp;колл-центр. Звонить не&nbsp;обязательно.</p>
</div>
</section>

<section class="section">
<div class="container">
<div class="advgrid">
<div class="adv reveal"><span class="adv__n mono">WHATSAPP · 24/7</span><h3><a href="{wa}" class="js-wa accent" data-wa="hello">Написать в WhatsApp</a></h3><p>Основной канал. Пишите в&nbsp;любое время — отвечаем круглосуточно, обычно в&nbsp;течение часа.</p></div>
<div class="adv reveal"><span class="adv__n mono">ТЕЛЕФОН</span><h3><a href="tel:+{raw}" class="mono accent">{phone}</a></h3><p>Если удобнее голосом. На&nbsp;том&nbsp;же номере работает WhatsApp.</p></div>
<div class="adv reveal"><span class="adv__n mono">EMAIL</span><h3><a href="mailto:{email}" class="accent">{email}</a></h3><p>Для технических заданий, эскизов и&nbsp;чертежей.</p></div>
<div class="adv reveal"><span class="adv__n mono">INSTAGRAM</span><h3><a href="{ig}" target="_blank" rel="noopener" class="accent">{ig_h}</a></h3><p>Производство и&nbsp;монтаж, свежие объекты и&nbsp;процессы.</p></div>
<div class="adv reveal"><span class="adv__n mono">АДРЕС</span><h3>Завод</h3><p>{addr}</p></div>
<div class="adv reveal"><span class="adv__n mono">РАСЧЁТ</span><h3>24 часа</h3><p>Столько занимает подготовка расчёта, спецификации и&nbsp;коммерческого предложения.</p></div>
</div>
</div>
</section>

<section class="section section--ink2" id="zayavka">
<div class="container">
<div class="section__head">
<p class="eyebrow reveal">Заявка</p>
<h2 class="reveal">Оставьте задачу — посчитаем</h2>
<p class="section__lead reveal">Заполните что знаете: даже «нужен ангар под технику примерно 20×40 в&nbsp;Акмолинской области» — уже достаточно для первого расчёта. Форма откроет WhatsApp с&nbsp;готовым сообщением.</p>
</div>
<div class="calcbox reveal">
<form class="calcbox__form" id="lead-form">
<label class="field"><span>Тип здания</span>
<select name="type">
<option value="">Не выбрано</option>
{types}
<option value="Другое">Другое</option>
</select>
</label>
<label class="field"><span>Примерные размеры</span>
<input type="text" name="size" placeholder="например, 24×60 м или 3 000 т зерна">
</label>
<label class="field"><span>Регион или участок</span>
<input type="text" name="region" placeholder="область, район">
</label>
<label class="field"><span>Как к вам обращаться</span>
<input type="text" name="name" placeholder="имя">
</label>
<label class="field"><span>Телефон для связи</span>
<input type="tel" name="phone" placeholder="+7 ___ ___ __ __">
</label>
<label class="field"><span>Комментарий</span>
<textarea name="note" placeholder="что важно учесть: техника, ворота, утепление, сроки"></textarea>
</label>
<button type="submit" class="btn btn--primary btn--block">Отправить в WhatsApp</button>
<p class="calcbox__disclaimer">Нажимая кнопку, вы открываете WhatsApp с&nbsp;заполненным сообщением — отправка происходит только после вашего подтверждения в&nbsp;мессенджере.</p>
<div id="lead-done" hidden>
<p class="note">WhatsApp открыт в&nbsp;новой вкладке — нажмите «Отправить» в&nbsp;мессенджере. Не&nbsp;сработало? <a id="lead-mail" href="mailto:{email}" class="accent">Отправить на&nbsp;email</a>.</p>
</div>
</form>
<div class="calcbox__side">
<p class="calcbox__side-title mono">КАК ПОЙДЁТ ДАЛЬШЕ</p>
<div class="minifeat"><span class="minifeat__k mono">Шаг 1</span>Инженер уточнит нагрузки площадки и назначение здания</div>
<div class="minifeat"><span class="minifeat__k mono">Шаг 2</span>Готовим расчёт, спецификацию металла и коммерческое предложение — 24 часа</div>
<div class="minifeat"><span class="minifeat__k mono">Шаг 3</span>Согласуем конструктив, фиксируем цену и срок в договоре</div>
<div class="minifeat"><span class="minifeat__k mono">Шаг 4</span>Выпускаем КМ/КМД и запускаем производство</div>
</div>
</div>
</div>
</section>

<section class="section">
<div class="container">
<div class="split">
<div class="split__text">
<p class="eyebrow reveal">Как добраться</p>
<h2 class="reveal">Где находится завод</h2>
<p class="section__lead reveal">Троебратское стоит на&nbsp;трассе Костанай&nbsp;— Петропавловск, в&nbsp;центре зернового пояса севера Казахстана. В&nbsp;селе работает ж/д станция Пресногорьковская — отсюда удобно отгружать конструкции по&nbsp;всей стране.</p>
<ul class="eqlist">
<li class="eq reveal"><span class="eq__t">~245 км</span><span class="eq__d">от Костаная по трассе на Петропавловск</span></li>
<li class="eq reveal"><span class="eq__t">Узункольский р-н</span><span class="eq__d">север Костанайской области, граница с Северо-Казахстанской</span></li>
<li class="eq reveal"><span class="eq__t">ж/д станция</span><span class="eq__d">Пресногорьковская — находится в самом селе</span></li>
<li class="eq reveal"><span class="eq__t">Реквизиты</span><span class="eq__d">карточку предприятия для договора вышлем по запросу</span></li>
</ul>
</div>
<figure class="split__media reveal">
<video autoplay muted loop playsinline preload="metadata" poster="assets/img/hangar-brand.jpg" aria-label="Промышленное здание в степи — видеовизуализация">
<source src="assets/video/hangar.mp4" type="video/mp4">
</video>
<figcaption class="mono">ПРОМЫШЛЕННОЕ ЗДАНИЕ В СТЕПИ · ВИЗУАЛИЗАЦИЯ</figcaption>
</figure>
</div>
</div>
</section>""".format(
        cr=breadcrumbs([CRUMB_HOME, (None, "Контакты")]),
        wa=WA, raw=BRAND["phone_raw"], phone=BRAND["phone_display"], email=BRAND["email"],
        ig=BRAND["instagram"], ig_h=BRAND["instagram_handle"], addr=BRAND["address"],
        types=types)

    return page("kontakty.html",
                "Контакты Steppe Steel — завод металлоконструкций, Костанайская обл.",
                "Телефон и WhatsApp +7 776 603 17 66, email steppe.steel@gmail.com. Завод в с. Троебратское, Костанайская область. WhatsApp — круглосуточно.",
                body, active="kontakty.html")


# ═══════════ БЛОГ ═══════════
def build_blog_index():
    posts = "\n".join("""<a href="blog-{s}.html" class="post reveal">
<span class="post__tag mono">ИНЖЕНЕРНАЯ СТАТЬЯ</span>
<h3>{t}</h3><p>{d}</p>
<span class="post__more mono">Читать →</span>
</a>""".format(s=s, t=t, d=d) for s, t, d in ARTICLES)

    body = """{cr}
{hero}
<section class="section">
<div class="container">
<div class="postgrid">
{posts}
</div>
</div>
</section>
{cta}""".format(
        cr=breadcrumbs([CRUMB_HOME, (None, "Блог")]),
        hero=_hero("Блог", "Инженерный блог",
                   "Разбираем то, о&nbsp;чём заказчики спрашивают чаще всего: как считать зернохранилище, зачем нужны КМ и&nbsp;КМД, почему сваи выигрывают у&nbsp;бетона и&nbsp;когда нужен чёрный металл.", actions=False),
        posts=posts,
        cta=cta_band("Остались вопросы по вашему объекту?",
                     "Инженер ответит предметно — по нагрузкам, сечениям и срокам."))

    return page("blog.html",
                "Блог Steppe Steel — инженерные статьи о металлоконструкциях и ЛСТК",
                "Как рассчитать зернохранилище, что такое КМ и КМД, сваи против бетона, ЛСТК или чёрный металл — разбираем на реальных цифрах.",
                body, active="blog.html")
