"""Sixth batch: travel listening, pronunciation, reading skills, writing tasks, grammar and words Bulgarians confuse.

EXTRA_LESSONS adds lessons to existing units (by unit slug).
"""

from .courses import C, D, F, L, O, S, T
from .courses_skills import reading
from .listening import INTRO, dialogue
from .speaking_writing import model_text

RQ = "Отговори според текста"
DQ = "Отговори според диалога"

EXTRA_LESSONS = {
    # ---------------- A1 ----------------
    "a1-listening": [
        {
            "slug": "a1-listen-taxi", "title": "В таксито", "title_en": "In a taxi", "kind": "listening",
            "minutes": 6, "xp": 15, "summary": "Мария взима такси от летището до хотела.", "theory": INTRO,
            "dialogue": dialogue(
                ("Driver", "Hello! Where to?", "Здравейте! Накъде?"),
                ("Maria", "The Grand Hotel, please. It's on King Street.", "Хотел „Гранд“, моля. На улица „Кинг“ е."),
                ("Driver", "No problem. Put your bag in the back.", "Няма проблем. Сложете чантата отзад."),
                ("Maria", "How long does it take?", "Колко време отнема?"),
                ("Driver", "About twenty minutes. The traffic is OK today.", "Около двадесет минути. Днес движението е нормално."),
                ("Maria", "How much is it?", "Колко ще струва?"),
                ("Driver", "About fifteen euros.", "Около петнадесет евро."),
                ("Maria", "Can I pay by card?", "Мога ли да платя с карта?"),
                ("Driver", "Yes, of course.", "Да, разбира се."),
            ),
            "exercises": [
                C("Къде отива Мария?", ["В хотел", "На летището", "На гарата"], 0, instruction=DQ),
                C("Колко време е пътят?", ["Около 20 минути", "Около 15 минути", "Един час"], 0, instruction=DQ),
                C("Колко ще струва приблизително?", ["15 евро", "50 евро", "20 евро"], 0, instruction=DQ),
                C("Как ще плати?", ["С карта", "В брой", "Не казва"], 0, instruction=DQ),
                L("Какво означава Where to?", "Where to?", ["Накъде?", "Къде си?", "Откъде сте?"], 0),
                D("Can I pay by card?"),
                S("The Grand Hotel, please."),
            ],
        },
    ],
    "a1-pronunciation": [
        {
            "slug": "a1-pron-numbers", "title": "Thirteen или thirty?", "title_en": "Teen and ty numbers",
            "kind": "pronunciation", "minutes": 6, "xp": 15, "summary": "Как да не объркаш 13 и 30 в магазина.",
            "theory": """
<p>Числата 13–19 и 30–90 звучат почти еднакво. Разликата е в <strong>ударението</strong> и в последния звук.</p>
<table>
<tr><th>-teen (13–19)</th><th>-ty (30–90)</th></tr>
<tr><td class="en">thir<strong>TEEN</strong> (дълго „ии“, ударение накрая)</td><td class="en"><strong>THIR</strong>ty (ударение в началото, кратко „и“)</td></tr>
<tr><td class="en">four<strong>TEEN</strong></td><td class="en"><strong>FOR</strong>ty</td></tr>
<tr><td class="en">fif<strong>TEEN</strong></td><td class="en"><strong>FIF</strong>ty</td></tr>
<tr><td class="en">eigh<strong>TEEN</strong></td><td class="en"><strong>EIGH</strong>ty</td></tr>
</table>
<div class="tip">Ако не си сигурен за цената, попитай: <span class="en">Sorry, one five or five zero?</span></div>
""",
            "exercises": [
                L("Кое число чу?", "thirteen", ["13", "30"], 0),
                L("Кое число чу?", "forty", ["14", "40"], 1),
                L("Кое число чу?", "fifteen", ["15", "50"], 0),
                L("Кое число чу?", "eighty", ["18", "80"], 1),
                C("Къде е ударението в sixty?", ["В началото: SIXty", "В края: sixTY"], 0),
                S("It costs nineteen euros."),
                D("It's seventy pounds."),
            ],
        },
    ],
    "a1-skills": [
        {
            "slug": "a1-read-signs", "title": "Четене: табели и надписи", "title_en": "Reading: signs and notices",
            "kind": "reading", "minutes": 6, "xp": 15, "summary": "Надписите, които ще видиш на летището, в метрото и в магазина.",
            "theory": """<div class="tip"><strong>Умение: разбиране на кратки надписи.</strong> Надписите са кратки и без граматика. Търси ключовата дума: <span class="en">no, only, exit, closed</span>.</div>""" + reading("Signs", [
                "Way out. No entry. Staff only. Mind the gap.",
                "Out of order. Please use the other lift.",
                "Closed for lunch, back at 2 pm.",
                "Sale: 50% off all shoes. Please queue here.",
            ], [("way out", "изход"), ("no entry", "вход забранен"), ("staff only", "само за персонала"),
                ("mind the gap", "внимавай с пролуката (между влака и перона)"), ("out of order", "не работи"),
                ("lift", "асансьор"), ("off", "намаление"), ("queue", "редя се на опашка")]),
            "exercises": [
                C("Какво означава Out of order?", ["Не работи", "Извън реда", "Поръчката е готова"], 0),
                C("Staff only означава:", ["Само за персонала", "Само за деца", "Само днес"], 0),
                C("Търсиш изхода. Коя табела?", ["Way out", "No entry", "Mind the gap"], 0),
                C("Closed for lunch, back at 2 pm. Кога отваря отново?", ["В 14:00", "В 12:00", "Утре"], 0, instruction=RQ),
                C("50% off означава:", ["Половин цена", "50 обувки", "Затворено"], 0),
                F("Please ___ here. (наредете се на опашка)", "queue"),
            ],
        },
        {
            "slug": "a1-time-dates", "title": "Часове и дати", "title_en": "Telling the time and dates",
            "kind": "vocabulary", "minutes": 7, "xp": 15, "summary": "Половин, четвърт, първи май: за влакове и резервации.",
            "theory": """
<h3>Часове</h3>
<table>
<tr><th>Час</th><th>Казваме</th></tr>
<tr><td>7:00</td><td class="en">seven o'clock</td></tr>
<tr><td>7:15</td><td class="en">quarter past seven / seven fifteen</td></tr>
<tr><td>7:30</td><td class="en">half past seven / seven thirty</td></tr>
<tr><td>7:45</td><td class="en">quarter to eight / seven forty-five</td></tr>
<tr><td>7:10</td><td class="en">ten past seven</td></tr>
<tr><td>7:50</td><td class="en">ten to eight</td></tr>
</table>
<div class="tip"><span class="en">Past</span> = след часа, <span class="en">to</span> = до следващия час. Във Великобритания често ще чуеш и <span class="en">half seven</span>: това също е 7:30.</div>
<h3>Дати</h3>
<p>Пишем <span class="en">1 May</span> или <span class="en">May 1</span>, но казваме с поредно числително: <span class="en">the first of May</span>. Предлозите: <span class="en">on Monday, on 1 May, in May, in 2026, at 7 o'clock</span>.</p>
""",
            "exercises": [
                C("Как се казва 8:30?", ["half past eight", "half past seven", "half eight past"], 0),
                C("Как се казва 9:45?", ["quarter to ten", "quarter past nine", "quarter to nine"], 0),
                C("Как четем 3 March?", ["the third of March", "the three of March", "March three"], 0),
                C("My birthday is ___ June.", ["in", "on", "at"], 0),
                C("The train leaves ___ 6:15.", ["at", "on", "in"], 0),
                L("Колко е часът?", "It's ten to five.", ["4:50", "5:10", "10:05"], 0),
                D("The museum opens at half past nine."),
            ],
        },
    ],
    "a1-my-world": [
        {
            "slug": "a1-object-pronouns", "title": "Me, him, her: местоимения след глагол", "title_en": "Object pronouns",
            "kind": "grammar", "minutes": 6, "xp": 15, "summary": "Обичам я, обади ми се, ела с нас.",
            "theory": """
<table>
<tr><th>Подлог</th><th>След глагол или предлог</th><th>Пример</th></tr>
<tr><td class="en">I</td><td class="en">me</td><td class="en">Call me.</td></tr>
<tr><td class="en">you</td><td class="en">you</td><td class="en">I love you.</td></tr>
<tr><td class="en">he</td><td class="en">him</td><td class="en">Ask him.</td></tr>
<tr><td class="en">she</td><td class="en">her</td><td class="en">I know her.</td></tr>
<tr><td class="en">it</td><td class="en">it</td><td class="en">I like it.</td></tr>
<tr><td class="en">we</td><td class="en">us</td><td class="en">Come with us.</td></tr>
<tr><td class="en">they</td><td class="en">them</td><td class="en">Look at them.</td></tr>
</table>
<div class="tip">На български местоимението често е преди глагола („Обичам я“, „Дай ми“). На английски е <strong>след</strong> глагола: <span class="en">Give me the key.</span></div>
""",
            "exercises": [
                C("Where is Tom? I can't see ___ .", ["he", "him", "his"], 1),
                C("Anna is nice. I like ___ .", ["her", "she", "hers"], 0),
                C("Can you help ___ ? (нас)", ["we", "us", "our"], 1),
                C("These shoes are great. I want ___ .", ["it", "they", "them"], 2),
                F("Please call ___ tomorrow. (мен)", "me"),
                O("Дай ми ключа.", "Give me the key"),
            ],
        },
    ],
    # ---------------- A2 ----------------
    "a2-listening": [
        {
            "slug": "a2-listen-pharmacy", "title": "В аптеката", "title_en": "At the pharmacy", "kind": "listening",
            "minutes": 7, "xp": 20, "summary": "Иван има главоболие и пита фармацевта за съвет.", "theory": INTRO,
            "dialogue": dialogue(
                ("Pharmacist", "Hello, can I help you?", "Здравейте, с какво да помогна?"),
                ("Ivan", "Yes, I have a bad headache and a sore throat.", "Да, имам силно главоболие и болно гърло."),
                ("Pharmacist", "How long have you had it?", "От колко време е?"),
                ("Ivan", "Since yesterday. I think I have a cold.", "От вчера. Мисля, че съм настинал."),
                ("Pharmacist", "Do you have a temperature?", "Имате ли температура?"),
                ("Ivan", "No, I don't think so.", "Не, не мисля."),
                ("Pharmacist", "Take these tablets twice a day, after meals. And drink lots of water.", "Пийте тези таблетки два пъти на ден, след хранене. И пийте много вода."),
                ("Ivan", "Thank you. Are they OK if I'm driving?", "Благодаря. Може ли да шофирам с тях?"),
                ("Pharmacist", "Yes, they won't make you sleepy.", "Да, няма да ви приспиват."),
            ),
            "exercises": [
                C("Какво боли Иван?", ["Главата и гърлото", "Стомахът", "Гърбът"], 0, instruction=DQ),
                C("От кога е болен?", ["От вчера", "От седмица", "От днес сутринта"], 0, instruction=DQ),
                C("Колко пъти на ден трябва да пие таблетките?", ["Два", "Три", "Веднъж"], 0, instruction=DQ),
                C("Кога да ги пие?", ["След хранене", "Преди хранене", "Преди сън"], 0, instruction=DQ),
                L("Какво означава sore throat?", "I have a sore throat.", ["болно гърло", "кашлица", "хрема"], 0),
                D("Take these tablets twice a day."),
                S("I have a bad headache."),
            ],
        },
    ],
    "a2-skills": [
        {
            "slug": "a2-read-recipe", "title": "Четене: рецепта", "title_en": "Reading: a recipe",
            "kind": "reading", "minutes": 7, "xp": 20, "summary": "Умение: да следиш стъпки и инструкции по ред.",
            "theory": """<div class="tip"><strong>Умение: четене на инструкции.</strong> Инструкциите са в повелително наклонение (<span class="en">cut, add, mix</span>). Думите <span class="en">first, then, after that, finally</span> показват реда.</div>""" + reading("Easy pancakes (for 4 people)", [
                "You need: 200 g flour, 2 eggs, 300 ml milk, a pinch of salt and a little butter.",
                "First, put the flour and salt in a large bowl. Then add the eggs and half of the milk, and mix well.",
                "After that, add the rest of the milk slowly. Leave the mixture for ten minutes.",
                "Finally, heat a little butter in a pan and cook each pancake for about one minute on each side.",
            ], [("flour", "брашно"), ("a pinch of", "щипка"), ("bowl", "купа"), ("mix", "разбърквам"),
                ("the rest of", "останалото"), ("mixture", "смес"), ("pan", "тиган"), ("side", "страна")]),
            "exercises": [
                C("Колко яйца трябват?", ["2", "4", "200"], 0, instruction=RQ),
                C("Какво слагаш първо в купата?", ["Брашното и солта", "Яйцата", "Млякото"], 0, instruction=RQ),
                C("Колко време оставяш сместа?", ["10 минути", "1 минута", "Час"], 0, instruction=RQ),
                C("Колко се пече всяка палачинка от всяка страна?", ["Около минута", "10 минути", "Пет минути"], 0, instruction=RQ),
                F("___ , heat the butter in a pan. (Накрая)", "Finally"),
                O("Добави млякото бавно.", "Add the milk slowly"),
            ],
        },
        {
            "slug": "a2-weather", "title": "Времето и сезоните", "title_en": "Weather and seasons",
            "kind": "vocabulary", "minutes": 6, "xp": 20, "summary": "Да говориш за времето: любимата тема на британците.",
            "theory": """
<table>
<tr><th>Съществително</th><th>Прилагателно</th><th>Значение</th></tr>
<tr><td class="en">sun</td><td class="en">sunny</td><td>слънчево</td></tr>
<tr><td class="en">rain</td><td class="en">rainy</td><td>дъждовно</td></tr>
<tr><td class="en">cloud</td><td class="en">cloudy</td><td>облачно</td></tr>
<tr><td class="en">wind</td><td class="en">windy</td><td>ветровито</td></tr>
<tr><td class="en">fog</td><td class="en">foggy</td><td>мъгливо</td></tr>
<tr><td class="en">snow</td><td class="en">snowy</td><td>снежно</td></tr>
</table>
<p>Температура: <span class="en">hot, warm, mild, cool, cold, freezing</span>. Сезони: <span class="en">spring, summer, autumn (US: fall), winter</span>.</p>
<div class="tip">„Вали“ е <span class="en">It's raining</span>, а не <em>It's rain</em>. Въпрос: <span class="en">What's the weather like?</span></div>
""",
            "exercises": [
                C("Как питаш какво е времето?", ["What's the weather like?", "How is the weather like?", "What weather is it?"], 0),
                C("Вали сняг:", ["It's snowing.", "It's snow.", "It snowy."], 0),
                C("Много е студено, под нулата:", ["It's freezing.", "It's mild.", "It's warm."], 0),
                C("The sky is grey today. It's ___ .", ["cloudy", "sunny", "hot"], 0),
                L("Какво е времето?", "It's windy and cold today.", ["Ветровито и студено", "Слънчево и топло", "Дъждовно"], 0),
                F("I love ___ because of the snow. (зима)", "winter"),
            ],
        },
    ],
    "a2-comparisons-quantities": [
        {
            "slug": "a2-few-little", "title": "A few, a little, few, little", "title_en": "A few and a little",
            "kind": "grammar", "minutes": 6, "xp": 20, "summary": "Малко, но достатъчно, или почти никак.",
            "theory": """
<table>
<tr><th></th><th>Броими (friends, minutes)</th><th>Неброими (money, time)</th></tr>
<tr><td>малко, но достатъчно</td><td class="en">a few</td><td class="en">a little</td></tr>
<tr><td>почти никак (негативно)</td><td class="en">few</td><td class="en">little</td></tr>
</table>
<ul>
<li><span class="en">I have a few friends in London.</span> Имам няколко приятели (хубаво е).</li>
<li><span class="en">Few people came.</span> Дойдоха малко хора (жалко).</li>
<li><span class="en">We have a little time.</span> Имаме малко време (стига ни).</li>
<li><span class="en">There's little hope.</span> Почти няма надежда.</li>
</ul>
<div class="tip">В разговорен език вместо <span class="en">few / little</span> казваме <span class="en">not many / not much</span>.</div>
""",
            "exercises": [
                C("Can I ask you ___ questions?", ["a few", "a little"], 0),
                C("I need ___ help with this bag.", ["a few", "a little"], 1),
                C("The town is boring. There's ___ to do.", ["little", "a little"], 0, "Почти нищо: little."),
                C("She has ___ friends, so she's often lonely.", ["few", "a few"], 0),
                F("Add a ___ salt.", "little"),
                O("Имаме няколко минути.", "We have a few minutes"),
            ],
        },
    ],
    "a2-speak-write": [
        {
            "slug": "a2-write-home", "title": "Пиши: опиши дома си", "title_en": "Writing: describe your home",
            "kind": "writing", "minutes": 8, "xp": 20, "summary": "Описание с there is/are, предлози и прилагателни.",
            "theory": model_text("My flat", [
                "I live in a small flat on the third floor of an old building in the centre of Plovdiv.",
                "There are two rooms: a living room and a bedroom. There's also a tiny kitchen and a bathroom.",
                "My favourite place is the balcony. There are lots of plants, and in the evening I can see the old town from there.",
                "It isn't very big, but it's bright and cosy, and I love it.",
            ], [("on the third floor", "къде точно (on + етаж)"), ("There are two rooms: ...", "какво има (there is / there are)"),
                ("My favourite place is...", "лично отношение"), ("It isn't very big, but...", "обобщение с but")]) + """
<div class="tip">Свързвай с <span class="en">and, but, also</span> и добави прилагателни: <span class="en">bright, cosy, quiet, tiny, modern</span>.</div>
""",
            "exercises": [
                C("___ two bedrooms in my flat.", ["There are", "There is", "It has"], 0),
                C("I live ___ the second floor.", ["on", "in", "at"], 0),
                C("Уютен:", ["cosy", "crowded", "cheap"], 0),
                F("There ___ a big window in the kitchen.", "is|'s"),
                O("Апартаментът ми е малък, но светъл.", "My flat is small but bright"),
                T("Любимото ми място е балконът.", "My favourite place is the balcony|My favorite place is the balcony"),
            ],
        },
    ],
    # ---------------- B1 ----------------
    "b1-listening": [
        {
            "slug": "b1-listen-voicemail", "title": "Гласово съобщение", "title_en": "A voicemail message", "kind": "listening",
            "minutes": 7, "xp": 25, "summary": "Съобщение от хотела за промяна в резервацията.", "theory": INTRO,
            "dialogue": dialogue(
                ("Receptionist", "Hello, this is a message for Ms Elena Dimitrova. It's Sarah from the Harbour Hotel in Brighton.", "Здравейте, това е съобщение за г-жа Елена Димитрова. Обажда се Сара от хотел „Харбър“ в Брайтън."),
                ("Receptionist", "I'm calling about your booking for next Friday. Unfortunately, there's a problem with the sea-view room you reserved.", "Обаждам се за резервацията ви за следващия петък. За съжаление има проблем със стаята с изглед към морето."),
                ("Receptionist", "We're repairing the windows on that floor, so we'd like to offer you a larger room at the back of the hotel instead.", "Ремонтираме прозорците на този етаж, затова бихме искали да ви предложим по-голяма стая в задната част на хотела."),
                ("Receptionist", "Of course, there's no extra charge, and breakfast will be free for both nights.", "Разбира се, без доплащане, а закуската ще е безплатна и за двете нощувки."),
                ("Receptionist", "If that's not OK, please call me back before Wednesday on 01273 555 019. Thanks, bye!", "Ако това не ви устройва, моля, обадете ми се преди сряда на 01273 555 019. Благодаря, довиждане!"),
            ),
            "exercises": [
                C("Защо се обажда Сара?", ["Има проблем с резервираната стая", "Хотелът е пълен", "Резервацията е отменена"], 0, instruction=DQ),
                C("Какво предлагат вместо стаята?", ["По-голяма стая отзад", "Друг хотел", "Отстъпка от 50%"], 0, instruction=DQ),
                C("Какво получава Елена безплатно?", ["Закуска", "Вечеря", "Паркинг"], 0, instruction=DQ),
                C("Докога трябва да се обади, ако не е съгласна?", ["Преди сряда", "До петък", "Днес"], 0, instruction=DQ),
                L("Какво означава no extra charge?", "There's no extra charge.", ["без доплащане", "без промяна", "без закуска"], 0),
                D("Please call me back before Wednesday."),
            ],
        },
    ],
    "b1-pronunciation": [
        {
            "slug": "b1-pron-intonation", "title": "Интонация на въпросите", "title_en": "Question intonation",
            "kind": "pronunciation", "minutes": 7, "xp": 25, "summary": "Кога гласът се качва и кога пада.",
            "theory": """
<table>
<tr><th>Въпрос</th><th>Интонация</th><th>Пример</th></tr>
<tr><td>Да/не въпрос</td><td>гласът се <strong>качва</strong> в края ↗</td><td class="en">Are you ready?</td></tr>
<tr><td>Въпрос с wh- дума</td><td>гласът <strong>пада</strong> в края ↘</td><td class="en">Where do you live?</td></tr>
<tr><td>Изброяване</td><td>↗ ↗ ↘ (последното пада)</td><td class="en">tea, coffee or juice?</td></tr>
<tr><td>Въпрос-опашка за потвърждение</td><td>пада ↘</td><td class="en">It's nice, isn't it?</td></tr>
</table>
<div class="tip">Ако wh- въпрос завърши с качване, звучи изненадано или все едно не си чул: <span class="en">You live WHERE? ↗</span></div>
""",
            "exercises": [
                C("Как завършва Do you like jazz?", ["Гласът се качва", "Гласът пада"], 0),
                C("Как завършва What time is it?", ["Гласът се качва", "Гласът пада"], 1),
                C("Would you like tea or coffee? (избор от две)", ["качва на tea, пада на coffee", "качва и на двете", "пада и на двете"], 0),
                S("Are you ready?"),
                S("Where do you live?"),
                S("Would you like tea or coffee?"),
                D("What time does the shop close?"),
            ],
        },
    ],
    "b1-skills": [
        {
            "slug": "b1-read-headings", "title": "Четене: заглавия на абзаци", "title_en": "Reading: matching headings",
            "kind": "reading", "minutes": 8, "xp": 25, "summary": "Умение: намиране на главната идея на всеки абзац.",
            "theory": """<div class="tip"><strong>Умение: главна идея.</strong> Главната идея обикновено е в първото или последното изречение на абзаца. Не избирай заглавие само защото съвпада една дума.</div>""" + reading("Travelling on a budget", [
                "[1] The cheapest flights are usually on Tuesdays and Wednesdays. Booking six to eight weeks in advance also helps, and it's worth checking smaller airports.",
                "[2] Hostels are no longer just for students. Many now have private rooms, and staying with locals through home-sharing sites can cost half the price of a hotel.",
                "[3] Eating in tourist areas can double your costs. Walk two streets away from the main square, or buy fresh food at local markets and have a picnic.",
                "[4] Many cities offer free walking tours, and museums often have one free day a month. A city pass can also save money if you plan to see a lot.",
            ], [("on a budget", "с ограничен бюджет"), ("in advance", "предварително"), ("it's worth", "струва си"),
                ("locals", "местни хора"), ("double", "удвоявам"), ("city pass", "градска карта за забележителности")]),
            "exercises": [
                C("Най-подходящо заглавие за [1]:", ["When to book", "Where to sleep", "Free things to do"], 0, instruction=RQ),
                C("Най-подходящо заглавие за [2]:", ["Cheaper places to stay", "Student life", "Expensive hotels"], 0, instruction=RQ),
                C("Най-подходящо заглавие за [3]:", ["Eat like a local", "The main square", "Cooking at home"], 0, instruction=RQ),
                C("Най-подходящо заглавие за [4]:", ["Sightseeing for less", "Walking is healthy", "Museums are closed"], 0, instruction=RQ),
                C("Кога са най-евтините полети според текста?", ["Вторник и сряда", "Уикенда", "Петък"], 0, instruction=RQ),
                F("It's ___ checking smaller airports. (струва си)", "worth"),
            ],
        },
        {
            "slug": "b1-travel-collocations", "title": "Колокации за пътуване", "title_en": "Travel collocations",
            "kind": "vocabulary", "minutes": 7, "xp": 25, "summary": "Catch a flight, miss the bus, check in: кой глагол с коя дума.",
            "theory": """
<table>
<tr><th>Израз</th><th>Значение</th></tr>
<tr><td class="en">catch / miss a train, bus, flight</td><td>хващам / изпускам</td></tr>
<tr><td class="en">get on / get off a bus, train, plane</td><td>качвам се / слизам</td></tr>
<tr><td class="en">get in / get out of a car, taxi</td><td>качвам се / слизам (кола)</td></tr>
<tr><td class="en">check in / check out</td><td>настанявам се / напускам (хотел)</td></tr>
<tr><td class="en">book a room, a ticket</td><td>резервирам</td></tr>
<tr><td class="en">go sightseeing</td><td>разглеждам забележителности</td></tr>
<tr><td class="en">take a trip, go on holiday</td><td>пътувам, отивам на почивка</td></tr>
<tr><td class="en">a one-way / return ticket</td><td>билет в едната посока / отиване и връщане</td></tr>
</table>
<div class="tip"><span class="en">Travel</span> е глагол или общо понятие. За конкретно пътуване казваме <span class="en">trip</span> или <span class="en">journey</span>: <span class="en">How was your trip?</span>, не <em>How was your travel?</em></div>
""",
            "exercises": [
                C("We ran but we ___ the last bus.", ["missed", "lost", "passed"], 0),
                C("Слизам от автобуса:", ["get off the bus", "get out the bus", "go down the bus"], 0),
                C("Качвам се в таксито:", ["get in the taxi", "get on the taxi"], 0),
                C("How was your ___ ?", ["trip", "travel"], 0),
                F("What time do we have to check ___ of the hotel?", "out"),
                T("Билет за отиване и връщане, моля.", "A return ticket, please|A return ticket please|A round-trip ticket, please|A round trip ticket please"),
            ],
        },
    ],
    "b1-experience-advice": [
        {
            "slug": "b1-permission", "title": "Can, may, be allowed to: разрешение", "title_en": "Permission",
            "kind": "grammar", "minutes": 7, "xp": 20, "summary": "Как да попиташ дали може и да кажеш какво е забранено.",
            "theory": """
<table>
<tr><th>Израз</th><th>Употреба</th><th>Пример</th></tr>
<tr><td class="en">Can I...?</td><td>неформално</td><td class="en">Can I sit here?</td></tr>
<tr><td class="en">Could I...?</td><td>по-учтиво</td><td class="en">Could I use your phone?</td></tr>
<tr><td class="en">May I...?</td><td>много учтиво, официално</td><td class="en">May I come in?</td></tr>
<tr><td class="en">be allowed to</td><td>правила (всички времена)</td><td class="en">You aren't allowed to smoke here. We weren't allowed to take photos.</td></tr>
<tr><td class="en">mustn't</td><td>строга забрана</td><td class="en">You mustn't park here.</td></tr>
</table>
<div class="tip">В минало време за правила: <span class="en">was / were allowed to</span>, не <em>could</em> за конкретен случай.</div>
""",
            "exercises": [
                C("Най-учтиво на интервю:", ["May I sit down?", "Can I sit?", "I sit, OK?"], 0),
                C("In the museum, we ___ take photos.", ["weren't allowed to", "didn't allowed to", "couldn't allowed"], 0),
                C("You ___ use your phone during the exam. (строго забранено)", ["mustn't", "don't have to"], 0),
                F("Are we ___ to bring food into the cinema?", "allowed"),
                O("Може ли да отворя прозореца?", "Could I open the window|Can I open the window|May I open the window"),
            ],
        },
    ],
    "b1-speak-write": [
        {
            "slug": "b1-write-enquiry", "title": "Пиши: имейл с въпроси", "title_en": "Writing: an email asking for information",
            "kind": "writing", "minutes": 9, "xp": 25, "summary": "Полуофициален имейл до училище, хотел или туристическа агенция.",
            "theory": model_text("Enquiry about English courses", [
                "Dear Sir or Madam,",
                "I saw your advertisement for summer English courses and I would like some more information.",
                "First, could you tell me how many students there are in each class? I would also like to know whether the price includes accommodation.",
                "Finally, is it possible to start the course in the middle of July?",
                "I look forward to hearing from you.",
                "Yours faithfully,",
                "Petar Georgiev",
            ], [("Dear Sir or Madam,", "когато не знаеш името"), ("I saw your advertisement for...", "защо пишеш"),
                ("could you tell me how many...", "непряк въпрос (без обърнат словоред)"),
                ("I would also like to know whether...", "втори въпрос, учтиво"),
                ("Yours faithfully,", "край, когато не знаеш името")]) + """
<div class="tip">В непрекия въпрос редът е като в твърдение: <span class="en">Could you tell me <strong>where the school is</strong>?</span>, не <em>where is the school</em>.</div>
""",
            "exercises": [
                C("Писмото започва с Dear Sir or Madam. Край:", ["Yours faithfully,", "Yours sincerely,", "Love,"], 0),
                C("Правилен непряк въпрос:", ["Could you tell me what time the course starts?", "Could you tell me what time does the course start?"], 0),
                C("I would like to know ___ breakfast is included.", ["whether", "that", "what"], 0),
                F("I look forward to ___ from you.", "hearing"),
                O("Бихте ли ми казали колко струва?", "Could you tell me how much it costs"),
            ],
        },
    ],
    # ---------------- B2 ----------------
    "b2-listening": [
        {
            "slug": "b2-listen-car-rental", "title": "Наем на кола", "title_en": "Renting a car", "kind": "listening",
            "minutes": 8, "xp": 30, "summary": "Застраховка, гориво и депозит: какво да питаш на гишето.", "theory": INTRO,
            "dialogue": dialogue(
                ("Agent", "Good morning. Do you have a reservation?", "Добро утро. Имате ли резервация?"),
                ("Nikolay", "Yes, under the name Petrov. A small car for five days.", "Да, на името Петров. Малка кола за пет дни."),
                ("Agent", "Here it is. The price includes basic insurance, but I'd recommend full cover. It's an extra twelve euros a day, and you won't pay anything if the car is damaged.", "Ето я. Цената включва основна застраховка, но бих препоръчал пълно покритие. Струва още дванадесет евро на ден и няма да плащате нищо, ако колата бъде повредена."),
                ("Nikolay", "I think I'll take the basic one. What's the deposit?", "Мисля, че ще взема основната. Какъв е депозитът?"),
                ("Agent", "Eight hundred euros, which we'll block on your credit card and release when you return the car.", "Осемстотин евро, които ще блокираме по кредитната ви карта и ще освободим, когато върнете колата."),
                ("Nikolay", "And the fuel?", "А горивото?"),
                ("Agent", "It's full to full. If you bring it back with less fuel, we charge a refuelling fee.", "Пълен към пълен. Ако я върнете с по-малко гориво, начисляваме такса за зареждане."),
                ("Nikolay", "Got it. And can my wife drive it too?", "Ясно. А може ли и съпругата ми да я кара?"),
                ("Agent", "Yes, but she'll need to show her licence, and there's a small fee for an additional driver.", "Да, но трябва да покаже шофьорската си книжка и има малка такса за допълнителен шофьор."),
            ),
            "exercises": [
                C("Каква застраховка избира Николай?", ["Основната", "Пълното покритие", "Никаква"], 0, instruction=DQ),
                C("Колко струва пълното покритие?", ["12 евро на ден", "12 евро общо", "800 евро"], 0, instruction=DQ),
                C("Какво става с депозита?", ["Блокира се по картата и се освобождава при връщане", "Плаща се в брой", "Не се връща"], 0, instruction=DQ),
                C("Какво означава full to full?", ["Взимаш и връщаш колата с пълен резервоар", "Горивото е включено", "Колата е пълна с багаж"], 0, instruction=DQ),
                C("Какво трябва съпругата да покаже?", ["Шофьорска книжка", "Паспорт", "Кредитна карта"], 0, instruction=DQ),
                L("Какво означава additional driver?", "There's a fee for an additional driver.", ["допълнителен шофьор", "по-опитен шофьор", "професионален шофьор"], 0),
                D("What's the deposit?"),
            ],
        },
    ],
    "b2-skills": [
        {
            "slug": "b2-read-attitude", "title": "Четене: отношението на автора", "title_en": "Reading: the writer's attitude",
            "kind": "reading", "minutes": 9, "xp": 30, "summary": "Умение: да разбереш какво мисли авторът, без да го казва директно.",
            "theory": """<div class="tip"><strong>Умение: отношение и тон.</strong> Търси оценъчни думи (<span class="en">sadly, surprisingly, so-called</span>), сравнения и какво авторът поставя в края, където е най-силният акцент.</div>""" + reading("The rise of the digital nomad", [
                "Digital nomads, people who work online while travelling the world, are often presented as the ultimate success story: laptop on the beach, no boss, total freedom.",
                "The reality is somewhat less glamorous. Many nomads report loneliness, unreliable internet and the exhausting task of finding a new flat every few weeks.",
                "There is also a cost that rarely makes it into the photos. In popular destinations such as Lisbon and Bali, rents have risen sharply, pushing local families out of their own neighbourhoods.",
                "None of this means remote work is a bad idea. But perhaps it is time we stopped treating it as a lifestyle advert and started asking who pays for it.",
            ], [("ultimate", "върховен, най-добрият"), ("somewhat", "донякъде"), ("glamorous", "бляскав"),
                ("unreliable", "ненадежден"), ("exhausting", "изтощителен"), ("sharply", "рязко"),
                ("pushing out", "изтласквам")]),
            "exercises": [
                C("Какво е отношението на автора към дигиталните номади?", ["Критично, но балансирано", "Изцяло възторжено", "Безразлично"], 0, instruction=RQ),
                C("Защо авторът казва somewhat less glamorous?", ["За да омаловажи иронично бляскавия образ", "За да похвали номадите", "За да опише плажа"], 0, instruction=RQ),
                C("Каква цена „рядко влиза в снимките“?", ["Покачването на наемите за местните", "Цената на лаптопа", "Билетите за самолет"], 0, instruction=RQ),
                C("Каква е основната идея на последния абзац?", ["Трябва да питаме кой плаща за този начин на живот", "Дистанционната работа е лоша", "Всички трябва да станат номади"], 0, instruction=RQ),
                F("The reality is ___ less glamorous. (донякъде)", "somewhat"),
            ],
        },
        {
            "slug": "b2-confusing-words", "title": "Думи, които българите бъркат", "title_en": "Commonly confused words",
            "kind": "vocabulary", "minutes": 8, "xp": 30, "summary": "Borrow/lend, rob/steal, say/tell, remember/remind.",
            "theory": """
<table>
<tr><th>Двойка</th><th>Разлика</th><th>Пример</th></tr>
<tr><td class="en">borrow / lend</td><td>взимам назаем / давам назаем</td><td class="en">Can I borrow your pen? Can you lend me your pen?</td></tr>
<tr><td class="en">steal / rob</td><td>крада нещо / обирам човек или място</td><td class="en">They stole my bag. They robbed a bank.</td></tr>
<tr><td class="en">say / tell</td><td>казвам (нещо) / казвам на някого</td><td class="en">She said hello. She told me the truth.</td></tr>
<tr><td class="en">remember / remind</td><td>помня / напомням</td><td class="en">Remind me to call Mum.</td></tr>
<tr><td class="en">win / earn</td><td>печеля (награда) / изкарвам (заплата)</td><td class="en">He earns €2,000 a month.</td></tr>
<tr><td class="en">lose / miss</td><td>губя / изпускам, липсва ми</td><td class="en">I missed the bus. I miss you.</td></tr>
</table>
<div class="tip"><span class="en">Tell</span> винаги иска човек след себе си: <span class="en">tell me, tell her</span>. Изключения: <span class="en">tell the truth, tell a lie, tell a story</span>.</div>
""",
            "exercises": [
                C("Could you ___ me some money?", ["lend", "borrow"], 0),
                C("Someone ___ my wallet on the metro.", ["stole", "robbed"], 0),
                C("He ___ me he was tired.", ["told", "said"], 0),
                C("Please ___ me to buy milk.", ["remind", "remember"], 0),
                C("Nurses don't ___ enough money.", ["earn", "win"], 0),
                C("I really ___ my family when I travel.", ["miss", "lose"], 0),
                F("She ___ that she would be late.", "said"),
            ],
        },
    ],
    "b2-complex-structures": [
        {
            "slug": "b2-reporting-verbs", "title": "Suggest, advise, refuse: глаголи за преразказ", "title_en": "Reporting verbs",
            "kind": "grammar", "minutes": 8, "xp": 25, "summary": "Как да преразкажеш, без да повтаряш said, said, said.",
            "theory": """
<table>
<tr><th>Модел</th><th>Глаголи</th><th>Пример</th></tr>
<tr><td>+ to + глагол</td><td class="en">agree, refuse, promise, offer, threaten</td><td class="en">He refused to pay.</td></tr>
<tr><td>+ човек + to + глагол</td><td class="en">advise, ask, tell, remind, warn, invite</td><td class="en">She advised me to rest.</td></tr>
<tr><td>+ -ing</td><td class="en">suggest, recommend, deny, admit</td><td class="en">He admitted taking the money.</td></tr>
<tr><td>+ предлог + -ing</td><td class="en">apologise for, insist on, accuse sb of</td><td class="en">They accused him of lying.</td></tr>
</table>
<div class="tip"><span class="en">Suggest</span> никога не е с човек + to: <span class="en">He suggested going</span> или <span class="en">He suggested that we go</span>, не <em>He suggested me to go</em>.</div>
""",
            "exercises": [
                C("„I'll help you,“ she said. → She ___ to help me.", ["offered", "suggested", "advised"], 0),
                C("„You should see a doctor.“ → He ___ me to see a doctor.", ["advised", "suggested", "offered"], 0),
                C("Кое е правилно?", ["She suggested taking a taxi.", "She suggested me to take a taxi."], 0),
                C("„I didn't break it!“ → He ___ breaking it.", ["denied", "refused", "admitted"], 0),
                F("He apologised ___ being late.", "for"),
                O("Тя отказа да отговори.", "She refused to answer"),
            ],
        },
    ],
    # ---------------- C1 ----------------
    "c1-listening": [
        {
            "slug": "c1-listen-complaint-call", "title": "Обаждане: изгубен багаж", "title_en": "Phone call: lost luggage",
            "kind": "listening", "minutes": 9, "xp": 35, "summary": "Учтиво, но твърдо: как да получиш обезщетение.", "theory": INTRO,
            "dialogue": dialogue(
                ("Agent", "Customer services, this is James speaking. How can I help?", "Обслужване на клиенти, Джеймс на телефона. С какво мога да помогна?"),
                ("Daria", "Hi James. My suitcase didn't arrive on flight BA 891 from Sofia three days ago, and I still haven't heard anything.", "Здравейте, Джеймс. Куфарът ми не пристигна с полет BA 891 от София преди три дни и все още нямам никаква информация."),
                ("Agent", "I'm sorry to hear that. Do you have your file reference?", "Съжалявам да го чуя. Имате ли номер на досието?"),
                ("Daria", "Yes, it's LHR 40217. I was told someone would call me within 24 hours, but no one did.", "Да, LHR 40217. Казаха ми, че ще ми се обадят до 24 часа, но никой не се обади."),
                ("Agent", "I can see the bag has been traced to Frankfurt. It should be on this evening's flight and delivered to your hotel tomorrow morning.", "Виждам, че куфарът е открит във Франкфурт. Би трябвало да е на вечерния полет и да бъде доставен в хотела ви утре сутринта."),
                ("Daria", "That's a relief. In the meantime, I've had to buy clothes and toiletries. Am I entitled to any compensation?", "Това е облекчение. Междувременно ми се наложи да купя дрехи и тоалетни принадлежности. Имам ли право на обезщетение?"),
                ("Agent", "You are. Keep all your receipts and submit them through our online claim form. Reasonable essential purchases are covered.", "Да, имате. Пазете всички касови бележки и ги подайте чрез онлайн формуляра. Разумните необходими покупки се покриват."),
                ("Daria", "Fine. Could you also make a note that I wasn't called back as promised?", "Добре. Бихте ли отбелязали и че не ми се обадиха, както беше обещано?"),
                ("Agent", "Certainly, I've added that to your file.", "Разбира се, добавих го в досието ви."),
            ),
            "exercises": [
                C("Къде е открит куфарът?", ["Във Франкфурт", "В София", "В Лондон"], 0, instruction=DQ),
                C("Кога ще го получи Дария?", ["Утре сутринта", "Тази вечер", "След три дни"], 0, instruction=DQ),
                C("Какво трябва да направи, за да получи обезщетение?", ["Да пази бележките и да подаде онлайн формуляр", "Да отиде на летището", "Да напише писмо"], 0, instruction=DQ),
                C("Защо Дария иска да се отбележи нещо в досието?", ["Не са ѝ се обадили, както са обещали", "Иска нов полет", "Куфарът е повреден"], 0, instruction=DQ),
                L("Какво означава Am I entitled to compensation?", "Am I entitled to any compensation?", ["Имам ли право на обезщетение?", "Трябва ли да платя?", "Мога ли да се оплача?"], 0),
                L("Какво означава That's a relief?", "That's a relief.", ["Това е облекчение.", "Това е проблем.", "Това е подарък."], 0),
                D("Could you make a note of that, please?"),
            ],
        },
    ],
    "c1-skills": [
        {
            "slug": "c1-linking-expressions", "title": "Свързващи изрази за напреднали", "title_en": "Advanced linking expressions",
            "kind": "vocabulary", "minutes": 8, "xp": 35, "summary": "Nevertheless, whereas, provided that: точните връзки в текста.",
            "theory": """
<table>
<tr><th>Функция</th><th>Изрази</th><th>Пример</th></tr>
<tr><td>противопоставяне</td><td class="en">nevertheless, nonetheless, even so</td><td class="en">It was expensive. Nevertheless, we bought it.</td></tr>
<tr><td>контраст между две неща</td><td class="en">whereas, while</td><td class="en">I like tea, whereas my wife prefers coffee.</td></tr>
<tr><td>условие</td><td class="en">provided that, as long as, unless</td><td class="en">You can go, provided that you're back by ten.</td></tr>
<tr><td>добавяне</td><td class="en">furthermore, moreover, in addition</td><td class="en">Moreover, the plan is cheaper.</td></tr>
<tr><td>резултат</td><td class="en">consequently, as a result, hence</td><td class="en">Sales fell. Consequently, jobs were cut.</td></tr>
<tr><td>отстъпка</td><td class="en">admittedly, granted</td><td class="en">Admittedly, it's not perfect.</td></tr>
</table>
<div class="tip"><span class="en">Nevertheless, moreover, consequently</span> започват ново изречение (след точка или точка и запетая). <span class="en">Whereas, provided that</span> свързват две части в едно изречение.</div>
""",
            "exercises": [
                C("The hotel was old. ___ , it was very comfortable.", ["Nevertheless", "Whereas", "Provided that"], 0),
                C("My brother loves the city, ___ I prefer the countryside.", ["whereas", "moreover", "consequently"], 0),
                C("You can borrow the car ___ you fill it up.", ["provided that", "nevertheless", "whereas"], 0),
                C("The roads were icy. ___ , many flights were cancelled. (резултат)", ["Consequently", "Admittedly", "Whereas"], 0),
                F("The flat is cheap. ___ , it's close to work. (освен това)", "Moreover|Furthermore|In addition|What's more"),
                C("Unless означава:", ["освен ако не", "въпреки че", "следователно"], 0),
            ],
        },
    ],
    "c1-precise-expression": [
        {
            "slug": "c1-emphatic-do", "title": "Емфатично do: I do like it", "title_en": "Emphasis with auxiliaries",
            "kind": "grammar", "minutes": 7, "xp": 30, "summary": "Как да подчертаеш, че нещо наистина е така.",
            "theory": """
<p>В утвърдително изречение можем да добавим <span class="en">do / does / did</span> (с ударение), за да подчертаем, да възразим или да изразим контраст.</p>
<table>
<tr><th>Функция</th><th>Пример</th></tr>
<tr><td>възразяване</td><td class="en">"You don't care." "I <strong>do</strong> care!"</td></tr>
<tr><td>контраст</td><td class="en">I didn't see Tom, but I <strong>did</strong> see his sister.</td></tr>
<tr><td>подчертаване</td><td class="en">She <strong>does</strong> look tired.</td></tr>
<tr><td>учтива покана</td><td class="en"><strong>Do</strong> sit down.</td></tr>
</table>
<div class="tip">При други спомагателни глаголи просто ги ударяваме: <span class="en">I <strong>AM</strong> listening!</span>, <span class="en">I <strong>HAVE</strong> finished.</span></div>
""",
            "exercises": [
                C("„You never help me.“ „That's not true, I ___ help you!“", ["do", "does", "am"], 0),
                C("He didn't call, but he ___ send a message.", ["did", "does", "was"], 0),
                C("This soup ___ smell good!", ["does", "do", "is"], 0),
                C("Do sit down. Това е:", ["учтива покана", "въпрос", "заповед с раздразнение"], 0),
                F("I know you think I forgot, but I ___ remember your birthday!", "did"),
                S("I do understand how you feel."),
            ],
        },
    ],
    "c1-speak-write": [
        {
            "slug": "c1-write-proposal", "title": "Пиши: предложение", "title_en": "Writing: a proposal",
            "kind": "writing", "minutes": 10, "xp": 35, "summary": "Как да убедиш ръководството: проблем, идея, ползи.",
            "theory": model_text("Proposal: a staff language programme", [
                "Purpose: This proposal outlines a plan to introduce free English classes for staff and explains the expected benefits.",
                "Current situation: Over 40% of our customers are now international, yet fewer than a third of front-desk staff feel confident speaking English.",
                "Proposed programme: Two one-hour classes per week during working hours, run by an external teacher, with separate groups for beginners and intermediate learners.",
                "Benefits: Staff would be able to deal with guests more efficiently, which should lead to better online reviews and fewer complaints.",
                "Conclusion: I strongly recommend a six-month pilot, after which the results could be reviewed before a decision is made about continuing.",
            ], [("This proposal outlines...", "цел (официално)"), ("Current situation:", "проблемът с факти"),
                ("Proposed programme:", "конкретно решение"), ("would be able to... which should lead to...", "ползи (предпазливо: would, should)"),
                ("I strongly recommend a pilot", "ясна препоръка, следващ стъпка")]) + """
<div class="tip"><strong>Доклад</strong> описва какво е станало. <strong>Предложение</strong> гледа напред и убеждава: <span class="en">would, could, should</span>, ясни ползи.</div>
""",
            "exercises": [
                C("Каква е основната разлика между доклад и предложение?", ["Предложението гледа напред и убеждава", "Предложението е без заглавия", "Няма разлика"], 0),
                C("Предпазливо описание на ползи:", ["This should lead to fewer complaints.", "This will definitely fix everything.", "Complaints will disappear."], 0),
                C("Подходящо начало:", ["This proposal outlines a plan to...", "Hi everyone, I have an idea!", "In my opinion, people are lazy."], 0),
                F("I strongly ___ a six-month pilot.", "recommend|suggest|propose"),
                O("Това би довело до по-добри отзиви.", "This would lead to better reviews"),
            ],
        },
    ],
    # ---------------- C2 ----------------
    "c2-listening": [
        {
            "slug": "c2-listen-english-history", "title": "Подкаст: откъде идва английският", "title_en": "Podcast: where English comes from",
            "kind": "listening", "minutes": 9, "xp": 40, "summary": "Викинги, нормани и защо английският има толкова синоними.", "theory": INTRO,
            "dialogue": dialogue(
                ("Host", "Today we're asking why English seems to have two or three words for everything. Professor Hale, where does that come from?", "Днес питаме защо английският сякаш има по две-три думи за всичко. Професор Хейл, откъде идва това?"),
                ("Hale", "Largely from history. English started as a Germanic language, but then it was invaded twice: first by the Vikings, and then, in 1066, by the French-speaking Normans.", "До голяма степен от историята. Английският започва като германски език, но после е нападнат два пъти: първо от викингите, а после, през 1066 г., от френскоговорящите нормани."),
                ("Host", "And the Normans became the ruling class.", "И норманите стават управляващата класа."),
                ("Hale", "Exactly. For about three centuries, French was the language of the court and the law, while ordinary people went on speaking English. That's why we have pairs like 'cow' and 'beef'. The animal kept its English name in the fields, but the meat on the lord's table got a French one.", "Точно така. Около три века френският е езикът на двора и закона, а обикновените хора продължават да говорят английски. Затова имаме двойки като cow и beef. Животното запазва английското си име на полето, а месото на трапезата на благородника получава френско."),
                ("Host", "So the register difference we still feel today, 'begin' versus 'commence', is essentially a class difference.", "Значи разликата в стила, която усещаме и днес, begin срещу commence, по същество е класова разлика."),
                ("Hale", "To a surprising extent, yes. The short Germanic words still sound warmer and more direct, while the Latin and French ones sound formal and distant. Good writers exploit that contrast all the time.", "В изненадваща степен, да. Кратките германски думи и днес звучат по-топло и директно, а латинските и френските звучат официално и дистанцирано. Добрите писатели използват този контраст постоянно."),
            ),
            "exercises": [
                C("Защо английският има толкова синоними според професора?", ["Заради нашествията и смесването с френски", "Защото е най-старият език", "Заради интернет"], 0, instruction=DQ),
                C("Защо имаме cow, но beef?", ["Месото на трапезата на благородниците получава френско име", "Beef е американска дума", "Cow е по-нова дума"], 0, instruction=DQ),
                C("Колко време френският е езикът на двора?", ["Около три века", "Около 30 години", "До днес"], 0, instruction=DQ),
                C("Как звучат кратките германски думи според професора?", ["По-топло и директно", "По-официално", "Остаряло"], 0, instruction=DQ),
                C("Кое е официалното съответствие на begin?", ["commence", "start", "kick off"], 0),
                L("Какво означава exploit that contrast?", "Good writers exploit that contrast all the time.", ["използват този контраст", "избягват този контраст", "критикуват този контраст"], 0),
                D("English started as a Germanic language."),
            ],
        },
    ],
    "c2-skills": [
        {
            "slug": "c2-read-literary", "title": "Четене: художествен откъс", "title_en": "Reading: a literary extract",
            "kind": "reading", "minutes": 10, "xp": 40, "summary": "Умение: образен език, атмосфера и какво е премълчано.",
            "theory": """<div class="tip"><strong>Умение: художествено четене.</strong> В литературата чувствата рядко се назовават директно. Те се показват чрез детайли, жестове и метафори. Питай се: защо авторът е избрал точно тази подробност?</div>""" + reading("The kitchen", [
                "My mother's kitchen had not changed in thirty years. The same blue clock ticked above the cooker, two minutes slow, as it always had been, because she said it gave her time to think.",
                "I put the kettle on and found her cup, the chipped one with the faded roses, still upside down on the draining board where she had left it.",
                "Outside, the neighbour's dog was barking at nothing. I stood there for a long time, listening to the clock insist that it was earlier than it was.",
            ], [("cooker", "печка"), ("chipped", "очукан"), ("faded", "избелял"), ("draining board", "отцедник до мивката"),
                ("insist", "настоявам")]),
            "exercises": [
                C("Какво най-вероятно се е случило с майката?", ["Починала е наскоро", "Заминала е на почивка", "Готви в другата стая"], 0, instruction=RQ),
                C("Защо е важна чашата, „още обърната на отцедника“?", ["Показва, че майката я е оставила и не се е върнала", "Чашата е счупена", "Разказвачът е разсеян"], 0, instruction=RQ),
                C("Какво внушава часовникът, който „настоява, че е по-рано“?", ["Желание времето да се върне назад", "Часовникът трябва да се поправи", "Разказвачът закъснява"], 0, instruction=RQ),
                C("Какъв е тонът на откъса?", ["Тих, тъжен, сдържан", "Весел и комичен", "Гневен"], 0, instruction=RQ),
                C("Кучето лае at nothing. Какво подсилва това?", ["Чувството за празнота", "Опасност", "Хумор"], 0, instruction=RQ),
            ],
        },
    ],
    "c2-speak-write": [
        {
            "slug": "c2-write-review-critical", "title": "Пиши: критична рецензия", "title_en": "Writing: a critical review",
            "kind": "writing", "minutes": 10, "xp": 40, "summary": "Балансирана, остроумна оценка на книга, филм или изложба.",
            "theory": model_text("Ambition without a map", [
                "Few debut novels arrive with as much noise as The Glass Year, and fewer still survive it intact.",
                "There is no denying the author's gift for a sentence: the opening chapter, set in a flooded Venice, is as vivid as anything published this decade.",
                "Where the novel falters is in its structure. Three timelines compete for attention, and by the midpoint it is hard to care which one wins.",
                "Still, for all its flaws, this is the work of a writer worth watching. Read it for the prose; forgive it the plot.",
            ], [("Few... and fewer still...", "остроумно, балансирано начало"),
                ("There is no denying...", "силна похвала"),
                ("Where the novel falters is...", "критика чрез изречение за акцент"),
                ("for all its flaws", "отстъпка: въпреки недостатъците"),
                ("Read it for...; forgive it...", "запомнящ се, паралелен край")]),
            "exercises": [
                C("There is no denying... служи за:", ["силна похвала", "силна критика", "въведение на сюжета"], 0),
                C("For all its flaws означава:", ["въпреки всичките си недостатъци", "заради недостатъците си", "без недостатъци"], 0),
                C("Where the novel falters is in its structure. Каква конструкция е това?", ["Изречение за акцент (cleft)", "Условно изречение", "Въпрос"], 0),
                F("There is no ___ her talent. (не може да се отрече)", "denying"),
                O("Прочети я заради езика.", "Read it for the prose|Read it for the language"),
            ],
        },
    ],
}

MISTAKES = {
    "a1-object-pronouns": [
        ("I like she.", "I like her.", "След глагол: her, не she."),
        ("Me give the key.", "Give me the key.", "Местоимението е след глагола."),
    ],
    "a1-time-dates": [
        ("in Monday", "on Monday", "Дни и дати: on."),
        ("the three of March", "the third of March", "Дата: поредно числително."),
    ],
    "a2-weather": [
        ("It's rain.", "It's raining.", "Вали: It's raining."),
        ("How is the weather like?", "What's the weather like?", "What... like? или How is the weather?"),
    ],
    "a2-few-little": [
        ("a few money", "a little money", "Money е неброимо: a little."),
    ],
    "b1-travel-collocations": [
        ("How was your travel?", "How was your trip?", "Конкретно пътуване: trip."),
        ("get out the bus", "get off the bus", "Автобус, влак, самолет: get off."),
    ],
    "b1-permission": [
        ("We didn't allowed to take photos.", "We weren't allowed to take photos.", "Be allowed to: was / were allowed."),
    ],
    "b1-write-enquiry": [
        ("Could you tell me where is the school?", "Could you tell me where the school is?", "Непряк въпрос: словоред като в твърдение."),
    ],
    "b2-confusing-words": [
        ("Can you borrow me your car?", "Can you lend me your car?", "Lend = давам назаем."),
        ("He said me the truth.", "He told me the truth.", "Tell + човек."),
        ("They robbed my phone.", "They stole my phone.", "Steal нещо, rob човек или място."),
    ],
    "b2-reporting-verbs": [
        ("She suggested me to go.", "She suggested going. / She suggested that I go.", "Suggest не е с човек + to."),
    ],
    "c1-linking-expressions": [
        ("Whereas it was expensive, we bought it.", "Although it was expensive, we bought it.", "Whereas сравнява две неща; за отстъпка: although."),
    ],
}
