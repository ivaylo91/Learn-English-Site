"""Eighth batch: practical listening, pronunciation, reading skills, writing tasks, grammar and topic vocabulary.

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
            "slug": "a1-listen-bus", "title": "Билет за автобус", "title_en": "Buying a bus ticket", "kind": "listening",
            "minutes": 6, "xp": 15, "summary": "Иво пита шофьора как да стигне до центъра.", "theory": INTRO,
            "dialogue": dialogue(
                ("Ivo", "Excuse me, does this bus go to the city centre?", "Извинете, този автобус ходи ли до центъра?"),
                ("Driver", "Yes, it does.", "Да, ходи."),
                ("Ivo", "A single ticket, please. How much is it?", "Един билет в едната посока, моля. Колко струва?"),
                ("Driver", "Two pounds fifty. You can pay by card here.", "Два паунда и петдесет. Може да платите с карта тук."),
                ("Ivo", "Thanks. Can you tell me when to get off?", "Благодаря. Ще ми кажете ли кога да сляза?"),
                ("Driver", "Sure. It's the fifth stop, about fifteen minutes.", "Разбира се. Петата спирка е, около петнадесет минути."),
            ),
            "exercises": [
                C("Накъде отива Иво?", ["Към центъра", "Към летището", "Към гарата"], 0, instruction=DQ),
                C("Какъв билет купува?", ["В едната посока", "За отиване и връщане", "Дневна карта"], 0, instruction=DQ),
                C("Колко струва?", ["£2.50", "£5", "£1.50"], 0, instruction=DQ),
                C("На коя спирка слиза?", ["Петата", "Петнадесетата", "Третата"], 0, instruction=DQ),
                L("Какво означава get off?", "Can you tell me when to get off?", ["слизам", "качвам се", "плащам"], 0),
                D("Does this bus go to the city centre?"),
                S("A single ticket, please."),
            ],
        },
    ],
    "a1-pronunciation": [
        {
            "slug": "a1-pron-s-endings", "title": "Окончание -s: три звука", "title_en": "The -s ending",
            "kind": "pronunciation", "minutes": 6, "xp": 15, "summary": "Cats, dogs, buses: как звучи -s в края.",
            "theory": """
<p>Окончанието <span class="en">-s</span> (множествено число и <span class="en">he / she / it</span>) има три произношения.</p>
<table>
<tr><th>Звук</th><th>Кога</th><th>Примери</th></tr>
<tr><td>/s/ „с“</td><td>след беззвучни звукове: p, t, k, f</td><td class="en">cats, books, stops, laughs</td></tr>
<tr><td>/z/ „з“</td><td>след звучни звукове и гласни</td><td class="en">dogs, plays, bags, lives</td></tr>
<tr><td>/ɪz/ „из“ (нова сричка)</td><td>след s, z, sh, ch, x, ge</td><td class="en">buses, watches, boxes, pages</td></tr>
</table>
<div class="tip">Най-важното: при <span class="en">buses, watches, boxes</span> се добавя цяла сричка. <span class="en">Bus</span> е една сричка, <span class="en">buses</span> са две.</div>
""",
            "exercises": [
                C("Как звучи -s в dogs?", ["/z/", "/s/", "/ɪz/"], 0),
                C("Как звучи -s в books?", ["/s/", "/z/", "/ɪz/"], 0),
                C("Как звучи -es в watches?", ["/ɪz/ (нова сричка)", "/s/", "/z/"], 0),
                C("Колко срички има boxes?", ["Две", "Една", "Три"], 0),
                S("She watches films and plays games."),
                D("He likes cats and dogs."),
            ],
        },
    ],
    "a1-daily-places": [
        {
            "slug": "a1-imperatives", "title": "Повелително наклонение", "title_en": "Imperatives",
            "kind": "grammar", "minutes": 6, "xp": 15, "summary": "Open, don't touch, let's go: инструкции и табели.",
            "theory": """
<table>
<tr><th>Форма</th><th>Пример</th><th>Значение</th></tr>
<tr><td>основна форма</td><td class="en">Open the door.</td><td>Отвори вратата.</td></tr>
<tr><td class="en">Don't + глагол</td><td class="en">Don't touch!</td><td>Не пипай!</td></tr>
<tr><td class="en">Let's + глагол</td><td class="en">Let's go!</td><td>Хайде да тръгваме!</td></tr>
<tr><td class="en">Please + глагол</td><td class="en">Please sit down.</td><td>Моля, седнете.</td></tr>
</table>
<div class="tip">Една и съща форма за „ти“ и „вие“: <span class="en">Come in!</span> = Влез! / Влезте! За учтивост добави <span class="en">please</span>.</div>
""",
            "exercises": [
                C("Не пипай!", ["Don't touch!", "No touch!", "Not touch!"], 0),
                C("Хайде да ядем!", ["Let's eat!", "Let eat!", "Lets we eat!"], 0),
                C("Учтиво: седнете", ["Please sit down.", "You sit down.", "Sitting down."], 0),
                F("___ forget your passport! (Не)", "Don't|Do not"),
                O("Затвори прозореца, моля.", "Close the window please|Please close the window"),
                T("Хайде да тръгваме!", "Let's go|Let us go"),
            ],
        },
    ],
    "a1-skills": [
        {
            "slug": "a1-read-hostel-rules", "title": "Четене: правила в хостела", "title_en": "Reading: hostel rules",
            "kind": "reading", "minutes": 6, "xp": 15, "summary": "Умение: какво може и какво не може.",
            "theory": """<div class="tip"><strong>Умение: правила.</strong> Търси <span class="en">please, don't, no, you can, you must</span>. Те показват какво е разрешено и какво е забранено.</div>""" + reading("Welcome to Blue Hostel!", [
                "Check-in is from 2 pm. Check-out is before 11 am.",
                "Breakfast is free from 7 to 10 am in the kitchen.",
                "Please be quiet after 11 pm. Don't eat in the bedrooms.",
                "You can leave your bags at reception on your last day. Towels cost £2.",
            ], [("check-in / check-out", "настаняване / напускане"), ("quiet", "тихо"), ("bedrooms", "спални"),
                ("leave your bags", "оставяш багажа си"), ("towels", "кърпи")]),
            "exercises": [
                C("От колко часа е настаняването?", ["14:00", "11:00", "07:00"], 0, instruction=RQ),
                C("Колко струва закуската?", ["Безплатна е", "£2", "Не пише"], 0, instruction=RQ),
                C("Къде не можеш да ядеш?", ["В спалните", "В кухнята", "На рецепцията"], 0, instruction=RQ),
                C("Какво можеш да направиш в последния ден?", ["Да оставиш багажа на рецепцията", "Да останеш до 14:00", "Да вземеш кърпа безплатно"], 0, instruction=RQ),
                C("Колко струват кърпите?", ["£2", "Безплатни", "£11"], 0, instruction=RQ),
                F("Please be ___ after 11 pm. (тихи)", "quiet"),
            ],
        },
    ],
    "a1-speak-write": [
        {
            "slug": "a1-write-friend", "title": "Пиши: опиши приятел", "title_en": "Writing: describe a friend",
            "kind": "writing", "minutes": 7, "xp": 15, "summary": "Външност, характер и какво правите заедно.",
            "theory": model_text("My best friend", [
                "My best friend is Lora. She is 25 and she lives in Varna.",
                "She is tall and she has long brown hair and green eyes.",
                "She is very funny and kind. She works as a nurse.",
                "At the weekend we often go to the beach or watch films together.",
            ], [("She is 25", "възраст: to be, не have"), ("She has long brown hair", "външност: has"),
                ("She is very funny and kind", "характер: is + прилагателно"),
                ("we often go...", "какво правите заедно")]) + """
<div class="tip">Ред на прилагателните: размер, цвят, съществително: <span class="en">long brown hair</span>, не <em>brown long hair</em>.</div>
""",
            "exercises": [
                C("Тя е на 25:", ["She is 25.", "She has 25.", "She have 25 years."], 0),
                C("Тя има дълга кестенява коса:", ["She has long brown hair.", "She has brown long hair.", "She is long brown hair."], 0),
                C("Той е забавен:", ["He is funny.", "He has funny.", "He funny."], 0),
                F("She ___ green eyes.", "has"),
                O("Той е висок и мил.", "He is tall and kind|He's tall and kind"),
                T("Тя работи като медицинска сестра.", "She works as a nurse"),
            ],
        },
    ],
    # ---------------- A2 ----------------
    "a2-listening": [
        {
            "slug": "a2-listen-lost-property", "title": "Бюро за изгубени вещи", "title_en": "At lost property", "kind": "listening",
            "minutes": 7, "xp": 20, "summary": "Ана е забравила раницата си във влака.", "theory": INTRO,
            "dialogue": dialogue(
                ("Clerk", "Lost property. How can I help?", "Изгубени вещи. С какво мога да помогна?"),
                ("Ana", "I left my backpack on the train from Manchester this morning.", "Забравих раницата си във влака от Манчестър тази сутрин."),
                ("Clerk", "What time did the train arrive?", "В колко часа пристигна влакът?"),
                ("Ana", "At about ten past nine.", "Около девет и десет."),
                ("Clerk", "And what does the backpack look like?", "А как изглежда раницата?"),
                ("Ana", "It's black and quite small, with a red bottle on the side. There's a laptop and a blue notebook inside.", "Черна е и доста малка, с червена бутилка отстрани. Вътре има лаптоп и син тефтер."),
                ("Clerk", "Let me check... Yes, I think we have it. Can I see some ID, please?", "Нека проверя... Да, мисля, че е при нас. Може ли документ за самоличност?"),
                ("Ana", "Here's my passport. Oh, thank goodness!", "Ето паспорта ми. О, слава богу!"),
            ),
            "exercises": [
                C("Какво е изгубила Ана?", ["Раница", "Куфар", "Чанта за лаптоп"], 0, instruction=DQ),
                C("Откъде идва влакът?", ["От Манчестър", "От Лондон", "От Ливърпул"], 0, instruction=DQ),
                C("Как изглежда раницата?", ["Черна, малка, с червена бутилка", "Червена и голяма", "Синя, с черна бутилка"], 0, instruction=DQ),
                C("Какво има вътре?", ["Лаптоп и син тефтер", "Паспорт и портфейл", "Дрехи"], 0, instruction=DQ),
                C("Какво трябва да покаже Ана?", ["Документ за самоличност", "Билета", "Касова бележка"], 0, instruction=DQ),
                L("Какво пита служителят?", "What does it look like?", ["Как изглежда?", "Харесва ли ви?", "Какво има вътре?"], 0),
                D("I left my backpack on the train."),
            ],
        },
    ],
    "a2-how-we-do": [
        {
            "slug": "a2-possessive-pronouns", "title": "Mine, yours, hers: чие е?", "title_en": "Possessive pronouns",
            "kind": "grammar", "minutes": 6, "xp": 20, "summary": "Моят, твоят, нейният: без съществително след тях.",
            "theory": """
<table>
<tr><th>Пред съществително</th><th>Самостоятелно</th><th>Пример</th></tr>
<tr><td class="en">my</td><td class="en">mine</td><td class="en">It's my bag. It's mine.</td></tr>
<tr><td class="en">your</td><td class="en">yours</td><td class="en">Is this yours?</td></tr>
<tr><td class="en">his</td><td class="en">his</td><td class="en">The car is his.</td></tr>
<tr><td class="en">her</td><td class="en">hers</td><td class="en">The keys are hers.</td></tr>
<tr><td class="en">our</td><td class="en">ours</td><td class="en">The house is ours.</td></tr>
<tr><td class="en">their</td><td class="en">theirs</td><td class="en">That table is theirs.</td></tr>
</table>
<p>Въпрос: <span class="en">Whose is this?</span> Чие е това?</p>
<div class="tip">След <span class="en">mine, yours, hers</span> няма съществително: <span class="en">It's mine</span>, не <em>It's mine bag</em>. И без апостроф: <span class="en">yours</span>, не <em>your's</em>.</div>
""",
            "exercises": [
                C("„Whose is this phone?“ „It's ___ .“ (мой)", ["mine", "my", "me"], 0),
                C("This isn't my coat. It's ___ . (неин)", ["hers", "her", "her's"], 0),
                C("Is this pen ___ ? (твоя)", ["yours", "your", "your's"], 0),
                C("___ is this? (Чие)", ["Whose", "Who's", "Who"], 0),
                F("That car is ___ . (наша)", "ours"),
                O("Тези ключове са негови.", "These keys are his"),
            ],
        },
    ],
    "a2-skills": [
        {
            "slug": "a2-read-product-reviews", "title": "Четене: отзиви за продукт", "title_en": "Reading: product reviews",
            "kind": "reading", "minutes": 7, "xp": 20, "summary": "Умение: сравняване на мнения преди покупка.",
            "theory": """<div class="tip"><strong>Умение: сравняване.</strong> Когато четеш няколко отзива, търси какво повтарят повечето хора. Едно мнение може да е изключение; три еднакви мнения са сигнал.</div>""" + reading("TravelPro suitcase: customer reviews", [
                "★★★★★ Maya: Light and strong. I took it on five flights and it still looks new. The wheels are very quiet.",
                "★★★★☆ Tom: Great size for a weekend trip and it fits in the cabin. But the zip is a bit weak.",
                "★★☆☆☆ Lisa: The zip broke after two trips. Customer service sent a new one, but it took three weeks.",
                "★★★★☆ Raj: Good value for money. Light and easy to carry. Be careful with the zip, though.",
            ], [("light", "лек"), ("wheels", "колелца"), ("cabin", "салон на самолета (ръчен багаж)"),
                ("zip", "цип"), ("weak", "слаб"), ("value for money", "добро съотношение цена-качество"), ("though", "все пак")]),
            "exercises": [
                C("Какъв проблем споменават трима от четиримата?", ["Ципът", "Колелцата", "Цената"], 0, instruction=RQ),
                C("Какво харесват повечето хора?", ["Лек е", "Голям е", "Тежък е"], 0, instruction=RQ),
                C("Става ли куфарът за ръчен багаж?", ["Да", "Не", "Не пише"], 0, instruction=RQ),
                C("Какво се е случило с Лиза?", ["Ципът се счупил и чакала три седмици за нов", "Изгубила куфара", "Колелцата се счупили"], 0, instruction=RQ),
                C("Value for money означава:", ["добро съотношение цена-качество", "много скъп", "безплатен"], 0),
                F("The wheels are very ___ . (тихи)", "quiet"),
            ],
        },
        {
            "slug": "a2-house-chores", "title": "Домакинска работа", "title_en": "Housework",
            "kind": "vocabulary", "minutes": 6, "xp": 20, "summary": "Do the washing, make the bed: кой глагол с коя работа.",
            "theory": """
<table>
<tr><th>Израз</th><th>Значение</th></tr>
<tr><td class="en">do the washing</td><td>пера</td></tr>
<tr><td class="en">do the washing-up / do the dishes</td><td>мия чинии</td></tr>
<tr><td class="en">do the ironing</td><td>гладя</td></tr>
<tr><td class="en">do the cleaning, clean the bathroom</td><td>чистя</td></tr>
<tr><td class="en">make the bed</td><td>оправям леглото</td></tr>
<tr><td class="en">take out the rubbish (US: trash)</td><td>изнасям боклука</td></tr>
<tr><td class="en">hoover / vacuum the floor</td><td>чистя с прахосмукачка</td></tr>
<tr><td class="en">water the plants</td><td>поливам цветята</td></tr>
</table>
<div class="tip">Повечето домакински задачи са с <span class="en">do</span>. Изключение: <span class="en">make the bed</span>.</div>
""",
            "exercises": [
                C("Оправям леглото:", ["make the bed", "do the bed", "fix the bed"], 0),
                C("Мия чиниите:", ["do the washing-up", "make the washing-up", "wash up the dishes plates"], 0),
                C("Can you ___ the rubbish, please?", ["take out", "make out", "do out"], 0),
                C("I ___ the ironing on Sundays.", ["do", "make", "take"], 0),
                F("Don't forget to ___ the plants. (полееш)", "water"),
                O("Аз пера, а той мие чиниите.", "I do the washing and he does the dishes|I do the washing and he does the washing-up"),
            ],
        },
    ],
    "a2-speak-write": [
        {
            "slug": "a2-write-travel-blog", "title": "Пиши: блог за пътуване", "title_en": "Writing: a travel blog post",
            "kind": "writing", "minutes": 8, "xp": 20, "summary": "Разкажи за едно пътуване: къде, какво, какво ти хареса.",
            "theory": model_text("Three days in Rome", [
                "Last month I spent three amazing days in Rome with my best friend.",
                "On the first day we visited the Colosseum. It was huge and very crowded, but I loved it.",
                "The next day we walked around the old town and ate the best pizza of my life.",
                "The only bad thing was the heat: it was 35 degrees! Next time I want to go in spring.",
            ], [("Last month I spent...", "кога, къде, с кого"), ("On the first day... The next day...", "ред на събитията"),
                ("It was huge... but I loved it", "впечатления с прилагателни"),
                ("the best pizza of my life", "превъзходна степен за силен ефект"),
                ("Next time I want to...", "край с план")]),
            "exercises": [
                C("Кое време използваш за разказа?", ["Past Simple", "Present Continuous", "Future"], 0),
                C("Подходящо начало на блог:", ["Last summer I spent a week in Greece.", "Dear Sir or Madam,", "Yours faithfully,"], 0),
                C("the ___ pizza of my life", ["best", "better", "good"], 0),
                F("On the first day we ___ (visit) the museum.", "visited"),
                O("Следващия път искам да отида през пролетта.", "Next time I want to go in spring|Next time I want to go in the spring"),
            ],
        },
    ],
    # ---------------- B1 ----------------
    "b1-listening": [
        {
            "slug": "b1-listen-landlord", "title": "Обаждане до хазяина", "title_en": "Calling the landlord", "kind": "listening",
            "minutes": 7, "xp": 25, "summary": "Бойлерът не работи: как да обясниш проблем и да уговориш ремонт.", "theory": INTRO,
            "dialogue": dialogue(
                ("Landlord", "Hello, Mr Hughes speaking.", "Ало, Хюз на телефона."),
                ("Kalina", "Hi, it's Kalina from flat 4. I'm afraid there's a problem with the boiler. There's no hot water since yesterday evening.", "Здравейте, Калина от апартамент 4 е. Страхувам се, че има проблем с бойлера. Няма топла вода от вчера вечерта."),
                ("Landlord", "Oh dear. Have you tried turning it off and on again?", "Ох. Опитахте ли да го изключите и включите отново?"),
                ("Kalina", "Yes, twice. There's a red light flashing, and it's making a strange noise.", "Да, два пъти. Мига червена лампичка и издава странен шум."),
                ("Landlord", "Right, I'd better send a plumber. Would tomorrow morning suit you?", "Добре, по-добре да изпратя водопроводчик. Удобно ли ви е утре сутринта?"),
                ("Kalina", "I'm at work until one. Could he come in the afternoon instead?", "На работа съм до един. Може ли да дойде следобед вместо това?"),
                ("Landlord", "I'll ask him to come at three. If there's any problem, I'll text you.", "Ще го помоля да дойде в три. Ако има проблем, ще ви пиша."),
            ),
            "exercises": [
                C("Какъв е проблемът?", ["Няма топла вода", "Няма ток", "Тече вода"], 0, instruction=DQ),
                C("От кога е проблемът?", ["От вчера вечерта", "От седмица", "От тази сутрин"], 0, instruction=DQ),
                C("Какво прави бойлерът?", ["Мига червена лампичка и шуми", "Изобщо не се включва", "Пуши"], 0, instruction=DQ),
                C("Защо Калина не може сутринта?", ["На работа е до един", "Ще пътува", "Спи"], 0, instruction=DQ),
                C("Кога ще дойде водопроводчикът?", ["В 15:00", "Утре сутринта", "В 13:00"], 0, instruction=DQ),
                L("Какво означава Would tomorrow suit you?", "Would tomorrow morning suit you?", ["Удобно ли ви е утре?", "Ще облечете ли костюм утре?", "Ще бъдете ли тук утре?"], 0),
                D("There's no hot water."),
            ],
        },
    ],
    "b1-pronunciation": [
        {
            "slug": "b1-pron-r", "title": "Звукът R", "title_en": "The R sound",
            "kind": "pronunciation", "minutes": 7, "xp": 25, "summary": "Английското r не е българското „р“.",
            "theory": """
<p>Българското „р“ се произнася с потрепване на езика. Английското <span class="en">r</span> е меко: езикът се свива назад и <strong>не докосва</strong> небцето.</p>
<table>
<tr><th>Позиция</th><th>Британски</th><th>Американски</th></tr>
<tr><td>пред гласна: <span class="en">red, very</span></td><td>чува се (меко)</td><td>чува се</td></tr>
<tr><td>в края или пред съгласна: <span class="en">car, park, water</span></td><td><strong>не се чува</strong>: „ка:“, „па:к“</td><td>чува се: „кар“</td></tr>
</table>
<div class="tip">Свързващо r: в британския, когато следващата дума започва с гласна, r се връща: <span class="en">far away</span> звучи „фа:р ъуей“.</div>
""",
            "exercises": [
                C("Чува ли се r в car (британски)?", ["Не, звучи „ка:“", "Да, силно", "Да, с потрепване"], 0),
                C("Чува ли се r в red?", ["Да, меко", "Не", "Само в американския"], 0),
                C("Как се произнася английското r?", ["Езикът не докосва небцето", "С потрепване на езика", "Като „л“"], 0),
                L("Кое изречение чу?", "The car is very red.", ["The car is very red.", "The cat is very wet."], 0),
                S("Turn right at the river."),
                S("Are you ready for dinner?"),
                D("Where are the restrooms?"),
            ],
        },
    ],
    "b1-tenses-detail": [
        {
            "slug": "b1-indirect-questions", "title": "Непреки въпроси: Do you know where...?", "title_en": "Indirect questions",
            "kind": "grammar", "minutes": 7, "xp": 20, "summary": "Учтивите въпроси, с които говорят носителите.",
            "theory": """
<p>Непреките въпроси са по-учтиви. Започват с <span class="en">Could you tell me..., Do you know..., I wonder...</span>, а след тях словоредът е като в <strong>твърдение</strong>.</p>
<table>
<tr><th>Пряк въпрос</th><th>Непряк въпрос</th></tr>
<tr><td class="en">Where is the station?</td><td class="en">Could you tell me where the station is?</td></tr>
<tr><td class="en">What time does it open?</td><td class="en">Do you know what time it opens?</td></tr>
<tr><td class="en">Did he call?</td><td class="en">Do you know if / whether he called?</td></tr>
</table>
<div class="tip">Без <span class="en">do / does / did</span> след въпросителната дума, а при да/не въпроси добави <span class="en">if</span> или <span class="en">whether</span>.</div>
""",
            "exercises": [
                C("Could you tell me where ___ ?", ["the bank is", "is the bank", "does the bank"], 0),
                C("Do you know what time ___ ?", ["the train leaves", "does the train leave", "leaves the train"], 0),
                C("Do you know ___ the shop is open?", ["if", "that", "what"], 0),
                C("I wonder ___ .", ["how much it costs", "how much does it cost", "how much costs it"], 0),
                F("Can you tell me ___ this bus goes to the airport? (дали)", "if|whether"),
                O("Знаете ли къде е тоалетната?", "Do you know where the toilet is"),
            ],
        },
    ],
    "b1-skills": [
        {
            "slug": "b1-read-story", "title": "Четене: кратък разказ", "title_en": "Reading: a short story",
            "kind": "reading", "minutes": 8, "xp": 25, "summary": "Умение: да следиш събитията и чувствата на героите.",
            "theory": """<div class="tip"><strong>Умение: четене на разказ.</strong> Следи реда на събитията (<span class="en">when, then, suddenly, at last</span>) и как се променят чувствата на героя.</div>""" + reading("The wrong train", [
                "Nadia was nervous. It was her first trip abroad alone, and she had a job interview in Edinburgh at two o'clock.",
                "She found a seat, put on her headphones and closed her eyes. When she opened them an hour later, the sea was on the wrong side of the window.",
                "'Excuse me, is this the train to Edinburgh?' she asked the man opposite. He smiled sadly. 'I'm afraid it's going to Glasgow.'",
                "Nadia felt sick. But the man, it turned out, worked for the same company. He made a phone call, and the interview was moved to the next morning. She got the job.",
            ], [("abroad", "в чужбина"), ("alone", "сам/а"), ("opposite", "срещу"), ("it turned out", "оказа се"),
                ("moved", "преместен")]),
            "exercises": [
                C("Как се чувства Надя в началото?", ["Нервна", "Спокойна", "Ядосана"], 0, instruction=RQ),
                C("Как разбира, че нещо не е наред?", ["Морето е от другата страна на прозореца", "Кондукторът ѝ казва", "Вижда табела"], 0, instruction=RQ),
                C("Накъде всъщност отива влакът?", ["Към Глазгоу", "Към Единбург", "Към Лондон"], 0, instruction=RQ),
                C("Кой ѝ помага?", ["Мъж, който работи в същата фирма", "Кондукторът", "Приятелка"], 0, instruction=RQ),
                C("Как завършва историята?", ["Интервюто е преместено и тя получава работата", "Тя изпуска интервюто", "Тя се прибира у дома"], 0, instruction=RQ),
                F("It ___ out that he worked for the same company. (оказа се)", "turned"),
            ],
        },
        {
            "slug": "b1-money-banking", "title": "Пари и банки", "title_en": "Money and banking",
            "kind": "vocabulary", "minutes": 7, "xp": 25, "summary": "Теглене, сметка, такса: думите за банка и банкомат.",
            "theory": """
<table>
<tr><th>Дума</th><th>Значение</th></tr>
<tr><td class="en">bank account</td><td>банкова сметка</td></tr>
<tr><td class="en">withdraw money / take out cash</td><td>тегля пари</td></tr>
<tr><td class="en">cash machine (UK), ATM (US)</td><td>банкомат</td></tr>
<tr><td class="en">PIN, contactless</td><td>ПИН, безконтактно</td></tr>
<tr><td class="en">a fee, a charge</td><td>такса</td></tr>
<tr><td class="en">exchange rate</td><td>валутен курс</td></tr>
<tr><td class="en">save / spend / waste money</td><td>спестявам / харча / прахосвам</td></tr>
<tr><td class="en">owe, debt</td><td>дължа, дълг</td></tr>
<tr><td class="en">change</td><td>ресто; дребни</td></tr>
</table>
<div class="tip">„Ресто“ е <span class="en">change</span>: <span class="en">Keep the change.</span> Задръжте рестото.</div>
""",
            "exercises": [
                C("I need to ___ some money from the cash machine.", ["withdraw", "borrow", "earn"], 0),
                C("What's the ___ rate for euros today?", ["exchange", "change", "money"], 0),
                C("Задръжте рестото:", ["Keep the change.", "Keep the rest.", "Keep the money back."], 0),
                C("There's a £3 ___ for using this ATM.", ["fee", "price", "bill"], 0),
                F("I ___ my brother £50. (дължа)", "owe"),
                T("Може ли да платя безконтактно?", "Can I pay contactless|Can I pay by contactless|Can I pay with contactless"),
            ],
        },
    ],
    "b1-speak-write": [
        {
            "slug": "b1-write-apology", "title": "Пиши: имейл с извинение", "title_en": "Writing: an apology email",
            "kind": "writing", "minutes": 8, "xp": 25, "summary": "Извини се, обясни и предложи решение.",
            "theory": model_text("Sorry about Saturday", [
                "Hi Martin,",
                "I'm really sorry I missed your birthday party on Saturday.",
                "My car broke down on the way, and by the time it was fixed, it was nearly midnight. I should have called you, but my phone battery was dead too.",
                "I feel terrible about it. Can I take you out for dinner next week to make up for it? My treat!",
                "Speak soon,",
                "Irina",
            ], [("I'm really sorry I missed...", "извинение веднага в началото"),
                ("My car broke down...", "кратко обяснение"),
                ("I should have called you", "съжаление (should have + 3-та форма)"),
                ("Can I... to make up for it?", "предложение за поправяне"),
                ("My treat!", "аз черпя")]),
            "exercises": [
                C("Съжалявам, че не ти се обадих (трябваше да):", ["I should have called you.", "I should call you.", "I must called you."], 0),
                C("Кое е най-доброто начало?", ["I'm really sorry I missed your party.", "Hi! What's new?", "Dear Sir or Madam,"], 0),
                C("to make up for it означава:", ["за да се реванширам", "за да се сдобрим", "за да го измисля"], 0),
                F("I'm sorry ___ being late. (за)", "for|about"),
                O("Трябваше да ти кажа.", "I should have told you"),
            ],
        },
    ],
    # ---------------- B2 ----------------
    "b2-listening": [
        {
            "slug": "b2-listen-audio-guide", "title": "Аудиогид в музея", "title_en": "A museum audio guide",
            "kind": "listening", "minutes": 8, "xp": 30, "summary": "Историята на една картина: монолог с подробности.", "theory": INTRO,
            "dialogue": dialogue(
                ("Guide", "You are now standing in front of one of the gallery's most famous paintings, 'The Fighting Temeraire', by J. M. W. Turner.", "Сега стоите пред една от най-известните картини в галерията, „Бойният кораб Темерер“ на Дж. М. У. Търнър."),
                ("Guide", "Painted in 1839, it shows an old warship, which had fought at the Battle of Trafalgar, being pulled up the river to be broken up for scrap.", "Нарисувана през 1839 г., тя показва стар военен кораб, участвал в битката при Трафалгар, теглен нагоре по реката, за да бъде нарязан за скрап."),
                ("Guide", "Notice the contrast: the ghostly white sailing ship behind, and in front, the small, dark steam tug that is pulling it.", "Забележете контраста: призрачният бял ветроход отзад и отпред малкият тъмен парен влекач, който го тегли."),
                ("Guide", "Many people see it as a picture about the end of one age and the beginning of another, the industrial age.", "Мнозина я виждат като картина за края на една епоха и началото на друга, индустриалната."),
                ("Guide", "Interestingly, Turner refused to sell it. He called it his 'darling' and left it to the nation when he died.", "Интересното е, че Търнър отказал да я продаде. Наричал я „моята любимка“ и я завещал на нацията, когато починал."),
                ("Guide", "In 2005, it was voted the greatest painting in a British art gallery. To continue, please walk through to Room 35.", "През 2005 г. е избрана за най-великата картина в британска галерия. За да продължите, моля, минете в зала 35."),
            ),
            "exercises": [
                C("Какво показва картината?", ["Стар военен кораб, теглен, за да бъде нарязан", "Битката при Трафалгар", "Нов параход"], 0, instruction=DQ),
                C("Кой тегли кораба?", ["Малък парен влекач", "Друг ветроход", "Хора на брега"], 0, instruction=DQ),
                C("Как мнозина тълкуват картината?", ["Край на една епоха и начало на индустриалната", "Победа във война", "Любовна история"], 0, instruction=DQ),
                C("Какво е направил Търнър с картината?", ["Отказал да я продаде и я завещал на нацията", "Продал я скъпо", "Унищожил я"], 0, instruction=DQ),
                C("Какво се случва през 2005 г.?", ["Избрана е за най-великата картина в британска галерия", "Открадната е", "Реставрирана е"], 0, instruction=DQ),
                L("Какво означава broken up for scrap?", "It was pulled up the river to be broken up for scrap.", ["нарязан за скрап", "поправен", "продаден на търг"], 0),
                D("Please walk through to Room 35."),
            ],
        },
    ],
    "b2-complex-structures": [
        {
            "slug": "b2-verb-pattern-meaning", "title": "Stop to или stop -ing?", "title_en": "Verbs that change meaning",
            "kind": "grammar", "minutes": 8, "xp": 25, "summary": "Remember, forget, stop, try: различно значение с to и -ing.",
            "theory": """
<table>
<tr><th>Глагол</th><th>+ to</th><th>+ -ing</th></tr>
<tr><td class="en">stop</td><td><span class="en">I stopped to buy coffee.</span> Спрях, за да купя кафе.</td><td><span class="en">I stopped smoking.</span> Спрях да пуша.</td></tr>
<tr><td class="en">remember</td><td><span class="en">Remember to lock the door.</span> (задача за после)</td><td><span class="en">I remember locking it.</span> (спомен от миналото)</td></tr>
<tr><td class="en">forget</td><td><span class="en">I forgot to call her.</span> (не се обадих)</td><td><span class="en">I'll never forget meeting her.</span> (спомен)</td></tr>
<tr><td class="en">try</td><td><span class="en">I tried to open it.</span> (опитах, трудно е)</td><td><span class="en">Try restarting it.</span> (експеримент: виж дали помага)</td></tr>
<tr><td class="en">regret</td><td><span class="en">I regret to tell you...</span> (официално: съжалявам да съобщя)</td><td><span class="en">I regret saying that.</span> (съжалявам, че го казах)</td></tr>
</table>
""",
            "exercises": [
                C("We stopped ___ a photo of the view. (за да направим)", ["to take", "taking"], 0),
                C("He stopped ___ two years ago. Now he doesn't drink.", ["drinking", "to drink"], 0),
                C("Please remember ___ the lights off when you leave.", ["to turn", "turning"], 0),
                C("I clearly remember ___ the keys on the table.", ["putting", "to put"], 0),
                C("The laptop is slow. Try ___ it. (опитай дали ще помогне)", ["restarting", "to restart"], 0),
                F("I regret ___ (say) that to him.", "saying"),
            ],
        },
    ],
    "b2-skills": [
        {
            "slug": "b2-read-interview", "title": "Четене: интервю", "title_en": "Reading: an interview",
            "kind": "reading", "minutes": 9, "xp": 30, "summary": "Умение: да намираш една и съща идея, казана с други думи.",
            "theory": """<div class="tip"><strong>Умение: перифраза.</strong> Въпросите рядко използват същите думи като текста. <span class="en">I couldn't stand it</span> в текста може да е <span class="en">she hated it</span> в отговора.</div>""" + reading("'I quit my office job to become a chef'", [
                "Q: Why did you leave a well-paid job in finance? A: Honestly, I couldn't stand another day in front of a spreadsheet. Cooking was the only thing that made me lose track of time.",
                "Q: Was it hard at first? A: Brutal. I was 34, working alongside 19-year-olds who were faster than me. I earned a third of my old salary.",
                "Q: Any regrets? A: Only that I didn't do it sooner. I'm more tired than ever, but I've never been happier.",
                "Q: What would you say to someone thinking of doing the same? A: Try it first. Work weekends in a kitchen before you hand in your notice. Dreams look different at two in the morning.",
            ], [("couldn't stand", "не можех да понасям"), ("lose track of time", "забравям за времето"),
                ("brutal", "жестоко"), ("alongside", "заедно с"), ("hand in your notice", "подаваш оставка")]),
            "exercises": [
                C("Какво е мислела за старата си работа?", ["Мразела я е", "Харесвала я е", "Била е безразлична"], 0, instruction=RQ),
                C("Какво показва lose track of time за готвенето?", ["Напълно я е поглъщало", "Отнемало е твърде много време", "Закъснявала е"], 0, instruction=RQ),
                C("Как е било в началото?", ["Много трудно и с по-ниска заплата", "Лесно", "По-добре платено"], 0, instruction=RQ),
                C("За какво съжалява?", ["Че не го е направила по-рано", "Че е напуснала", "За нищо от професията"], 0, instruction=RQ),
                C("Какъв съвет дава?", ["Първо да опиташ, преди да напуснеш", "Да напуснеш веднага", "Да не правиш промени"], 0, instruction=RQ),
                F("Work in a kitchen before you hand in your ___ . (оставка)", "notice"),
            ],
        },
        {
            "slug": "b2-crime", "title": "Престъпност и закон", "title_en": "Crime and the law",
            "kind": "vocabulary", "minutes": 8, "xp": 30, "summary": "Burglary, fine, sentence: новини и изпитни теми.",
            "theory": """
<table>
<tr><th>Престъпление</th><th>Извършител</th><th>Значение</th></tr>
<tr><td class="en">theft</td><td class="en">thief</td><td>кражба / крадец</td></tr>
<tr><td class="en">burglary</td><td class="en">burglar</td><td>кражба с взлом (в дом)</td></tr>
<tr><td class="en">pickpocketing</td><td class="en">pickpocket</td><td>джебчийство</td></tr>
<tr><td class="en">robbery</td><td class="en">robber</td><td>обир (със заплаха)</td></tr>
<tr><td class="en">fraud</td><td class="en">fraudster</td><td>измама</td></tr>
</table>
<p>Законът: <span class="en">arrest</span> (арестувам), <span class="en">charge sb with</span> (повдигам обвинение), <span class="en">trial</span> (съдебен процес), <span class="en">guilty / innocent</span> (виновен / невинен), <span class="en">a fine</span> (глоба), <span class="en">a sentence</span> (присъда), <span class="en">witness</span> (свидетел).</p>
<div class="tip"><span class="en">Fine</span> е и глоба: <span class="en">I got a parking fine.</span> Получих глоба за паркиране.</div>
""",
            "exercises": [
                C("Someone broke into our house. It was a ___ .", ["burglary", "fraud", "fine"], 0),
                C("Watch your wallet on the metro. There are ___ .", ["pickpockets", "burglars", "witnesses"], 0),
                C("He was found ___ and sent to prison.", ["guilty", "innocent", "fined"], 0),
                C("I got a £60 parking ___ .", ["fine", "sentence", "charge"], 0),
                F("The police ___ two men last night. (арестуваха)", "arrested"),
                C("Fake emails that steal your bank details are a type of ___ .", ["fraud", "burglary", "robbery"], 0),
            ],
        },
    ],
    "b2-speak-write": [
        {
            "slug": "b2-write-essay", "title": "Пиши: есе с мнение", "title_en": "Writing: an opinion essay",
            "kind": "writing", "minutes": 10, "xp": 30, "summary": "Изпитно есе: две дадени идеи и твоя собствена.",
            "theory": model_text("Should tourists pay to enter popular cities?", [
                "In recent years, cities such as Venice have started charging day visitors an entry fee. Although this may seem unfair, I believe it is a reasonable idea.",
                "Firstly, the money raised can be spent on cleaning streets and repairing historic buildings, which suffer most from mass tourism.",
                "Secondly, a fee may encourage visitors to stay longer and spend more locally, rather than arriving for a few hours by cruise ship.",
                "Some argue that such fees make travel more expensive for families. However, if the charge is small and children go free, this problem can be avoided.",
                "In conclusion, entry fees, if managed carefully, can protect popular cities for future generations.",
            ], [("Although this may seem..., I believe...", "увод: тема и твоята позиция"),
                ("Firstly,... Secondly,...", "един аргумент на абзац"),
                ("Some argue that... However,...", "противоположно мнение и отговор"),
                ("In conclusion,", "кратко заключение, без нови идеи")]) + """
<div class="tip">В изпита B2 често получаваш две идеи и трябва да добавиш своя. Пиши по един абзац на идея и включи противоположното мнение.</div>
""",
            "exercises": [
                C("Къде е твоето мнение в есето?", ["В увода и в заключението", "Само в средата", "Никъде"], 0),
                C("Some argue that... However,... служи за:", ["Противоположно мнение и отговор", "Увод", "Пример"], 0),
                C("Какво не се пише в заключението?", ["Нови аргументи", "Обобщение", "Позицията ти"], 0),
                F("___ this may seem unfair, I believe it is a good idea. (Въпреки че)", "Although|Though|While"),
                O("В заключение, таксите могат да защитят градовете.", "In conclusion fees can protect cities"),
            ],
        },
    ],
    # ---------------- C1 ----------------
    "c1-listening": [
        {
            "slug": "c1-listen-bank-call", "title": "Обаждане от банката", "title_en": "A call from the bank",
            "kind": "listening", "minutes": 9, "xp": 35, "summary": "Подозрителна транзакция: как да разбереш и как да се защитиш.", "theory": INTRO,
            "dialogue": dialogue(
                ("Bank", "Good afternoon, is that Mr Stoyanov? I'm calling from the fraud team at Northway Bank.", "Добър ден, г-н Стоянов ли е? Обаждам се от отдела за измами на банка „Нортуей“."),
                ("Alex", "Yes, speaking. Before we go on, how do I know this call is genuine?", "Да, аз съм. Преди да продължим, откъде да знам, че обаждането е истинско?"),
                ("Bank", "That's a very sensible question. I won't ask for your PIN or password. If you prefer, hang up and call the number on the back of your card.", "Много разумен въпрос. Няма да ви питам за ПИН или парола. Ако предпочитате, затворете и се обадете на номера на гърба на картата."),
                ("Alex", "I'll do that, thanks.", "Така ще направя, благодаря."),
                ("Bank", "Thank you for calling back, Mr Stoyanov. We've flagged a payment of eight hundred and forty pounds to an online electronics store in the early hours of this morning. Did you authorise it?", "Благодаря, че се обадихте, г-н Стоянов. Маркирахме плащане от осемстотин и четиридесет паунда към онлайн магазин за електроника рано тази сутрин. Вие ли го разрешихте?"),
                ("Alex", "Absolutely not. I was asleep.", "Категорично не. Спях."),
                ("Bank", "In that case, I'll block the card straight away and raise a dispute. You'll be refunded within five working days, and a replacement card will arrive by post.", "В такъв случай ще блокирам картата веднага и ще започна оспорване. Ще ви бъдат възстановени парите до пет работни дни, а нова карта ще пристигне по пощата."),
                ("Alex", "And in the meantime?", "А междувременно?"),
                ("Bank", "You can still use your phone to pay; the digital card will be reissued within the hour.", "Все още можете да плащате с телефона; дигиталната карта ще бъде преиздадена до час."),
            ),
            "exercises": [
                C("Защо Алекс затваря и се обажда отново?", ["За да провери, че обаждането е истинско", "Връзката прекъсва", "Банката го моли да изчака"], 0, instruction=DQ),
                C("Какво няма да поиска банката?", ["ПИН или парола", "Името му", "Дали е разрешил плащането"], 0, instruction=DQ),
                C("Колко е подозрителното плащане?", ["£840", "£480", "£8,400"], 0, instruction=DQ),
                C("Кога ще получи парите обратно?", ["До пет работни дни", "Веднага", "След месец"], 0, instruction=DQ),
                C("Как може да плаща междувременно?", ["С телефона", "Само в брой", "Не може"], 0, instruction=DQ),
                L("Какво означава Did you authorise it?", "Did you authorise it?", ["Вие ли го разрешихте?", "Вие ли го написахте?", "Видяхте ли го?"], 0),
                L("Какво означава raise a dispute?", "I'll block the card and raise a dispute.", ["започна оспорване", "вдигна лихвата", "започна спор с вас"], 0),
            ],
        },
    ],
    "c1-complex": [
        {
            "slug": "c1-future-in-past", "title": "Was going to, was about to", "title_en": "The future in the past",
            "kind": "grammar", "minutes": 7, "xp": 30, "summary": "Щях да..., тъкмо щях да...: планове, които не са се случили.",
            "theory": """
<table>
<tr><th>Форма</th><th>Значение</th><th>Пример</th></tr>
<tr><td class="en">was / were going to</td><td>щях да (план, често неизпълнен)</td><td class="en">I was going to call you, but I forgot.</td></tr>
<tr><td class="en">was / were about to</td><td>тъкмо щях да (след миг)</td><td class="en">I was about to leave when the phone rang.</td></tr>
<tr><td class="en">would</td><td>бъдеще, гледано от миналото</td><td class="en">She knew she would miss him.</td></tr>
<tr><td class="en">was to / was to have done</td><td>съдба; официален план (неизпълнен)</td><td class="en">It was to be his last film. The minister was to have spoken, but cancelled.</td></tr>
</table>
""",
            "exercises": [
                C("I ___ tell you, but you found out first.", ["was going to", "will", "am going to"], 0),
                C("We ___ go out when it started to pour.", ["were about to", "are about to", "will be about to"], 0),
                C("He promised he ___ write every week.", ["would", "will", "was"], 0),
                C("Little did they know, it ___ their last meeting.", ["was to be", "is going to be", "would have"], 0),
                F("I was ___ to switch off my phone when it rang. (тъкмо щях)", "about"),
                O("Щях да ти кажа.", "I was going to tell you"),
            ],
        },
    ],
    "c1-skills": [
        {
            "slug": "c1-read-paraphrase", "title": "Четене: капани в отговорите", "title_en": "Reading: distractors and paraphrase",
            "kind": "reading", "minutes": 10, "xp": 35, "summary": "Умение: защо отговорът с „думата от текста“ често е грешен.",
            "theory": """<div class="tip"><strong>Умение: капани (distractors).</strong> В изпитите грешните отговори често повтарят думи от текста, но променят смисъла. Верният отговор обикновено е <strong>перифраза</strong>. Провери дали отговорът казва точно същото, а не само звучи познато.</div>""" + reading("Remote villages and the digital economy", [
                "When high-speed internet finally reached the mountain village of Leshten, few residents expected much to change. The population had been falling for decades, and the school had closed in 2009.",
                "Yet within five years, around twenty remote workers had moved in, most of them families from Sofia. Their arrival did not reverse the decline overnight, but it slowed it considerably.",
                "Not everyone welcomed the newcomers. Some older residents complained that property prices had risen beyond the reach of local young people, the very group the village most needed to keep.",
                "The mayor remains cautiously optimistic: 'Connectivity alone doesn't save a village. People stay where they feel they belong.'",
            ], [("residents", "жители"), ("reverse the decline", "обръщам упадъка"), ("considerably", "значително"),
                ("beyond the reach of", "недостъпен за"), ("cautiously optimistic", "предпазливо оптимистичен"),
                ("belong", "принадлежа")]),
            "exercises": [
                C("Какъв е ефектът от новодошлите според текста?", ["Забавили са намаляването на населението", "Обърнали са упадъка веднага", "Отворили са училището отново"], 0, instruction=RQ),
                C("Защо отговорът „Обърнали са упадъка“ е капан?", ["Текстът казва did not reverse... overnight", "Текстът не споменава упадък", "Защото е твърде дълъг"], 0, instruction=RQ),
                C("Какво е притеснението на някои по-възрастни жители?", ["Местните млади не могат да си позволят имоти", "Новодошлите са шумни", "Интернетът е бавен"], 0, instruction=RQ),
                C("Какво мисли кметът?", ["Интернетът сам по себе си не е достатъчен", "Интернетът спаси селото", "Новодошлите трябва да си тръгнат"], 0, instruction=RQ),
                C("Cautiously optimistic е перифраза на:", ["hopeful but careful", "very worried", "completely certain"], 0),
            ],
        },
        {
            "slug": "c1-communication-idioms", "title": "Идиоми за общуване", "title_en": "Idioms about communication",
            "kind": "vocabulary", "minutes": 8, "xp": 35, "summary": "Beat around the bush, get the wrong end of the stick.",
            "theory": """
<table>
<tr><th>Идиом</th><th>Значение</th></tr>
<tr><td class="en">beat around the bush</td><td>увъртам, не казвам направо</td></tr>
<tr><td class="en">get straight to the point</td><td>минавам направо на въпроса</td></tr>
<tr><td class="en">get the wrong end of the stick</td><td>разбирам погрешно</td></tr>
<tr><td class="en">be on the same page</td><td>мислим еднакво, разбрали сме се</td></tr>
<tr><td class="en">put it in a nutshell</td><td>казвам накратко</td></tr>
<tr><td class="en">talk someone round</td><td>убеждавам някого</td></tr>
<tr><td class="en">a heart-to-heart</td><td>откровен разговор</td></tr>
<tr><td class="en">it goes without saying</td><td>от само себе си се разбира</td></tr>
</table>
""",
            "exercises": [
                C("Stop ___ and tell me what happened!", ["beating around the bush", "getting the wrong end of the stick", "being on the same page"], 0),
                C("No, that's not what I meant. You've got the wrong end of the ___ .", ["stick", "bush", "page"], 0),
                C("Before we start, let's make sure we're all on the same ___ .", ["page", "point", "stick"], 0),
                C("To put it in a ___ , the project failed.", ["nutshell", "shell", "point"], 0),
                F("It goes without ___ that you're welcome to stay.", "saying"),
                C("A heart-to-heart е:", ["откровен разговор", "кардиолог", "спор"], 0),
            ],
        },
    ],
    "c1-speak-write": [
        {
            "slug": "c1-write-decline", "title": "Пиши: учтив отказ", "title_en": "Writing: declining a request",
            "kind": "writing", "minutes": 9, "xp": 35, "summary": "Кажи „не“ на колега или клиент, без да развалиш отношенията.",
            "theory": model_text("Re: Help with the conference", [
                "Hi Laura,",
                "Thank you for thinking of me for the conference team. It sounds like a fantastic event, and I'm flattered you asked.",
                "Unfortunately, I'm not in a position to take it on at the moment. With the product launch at the end of the month, I wouldn't be able to give it the time it deserves.",
                "That said, I'd be happy to review the programme once it's drafted, and you might want to ask Petar, who organised last year's event very successfully.",
                "Best of luck with it, and do keep me in mind for the next one.",
                "Best,",
                "Elena",
            ], [("Thank you for thinking of me...", "благодарност преди отказа"),
                ("I'm not in a position to take it on", "твърд, но учтив отказ"),
                ("I wouldn't be able to give it the time it deserves", "причина, представена като загриженост"),
                ("That said, I'd be happy to...", "алтернатива: показваш добра воля"),
                ("do keep me in mind for the next one", "оставяш вратата отворена")]),
            "exercises": [
                C("Най-дипломатичен отказ:", ["I'm not in a position to take it on at the moment.", "No, I don't want to.", "I can't, sorry, bye."], 0),
                C("That said, служи за:", ["Въвеждане на алтернатива след отказ", "Обобщение", "Повторение"], 0),
                C("Защо авторката предлага Петър?", ["За да помогне, въпреки отказа", "За да се оплаче от него", "Защото той е шефът"], 0),
                F("I wouldn't be able to give it the time it ___ .", "deserves"),
                O("Благодаря, че се сетихте за мен.", "Thank you for thinking of me"),
            ],
        },
    ],
    # ---------------- C2 ----------------
    "c2-listening": [
        {
            "slug": "c2-listen-forgetting", "title": "Лекция: защо забравяме езици", "title_en": "Lecture: why we forget languages",
            "kind": "listening", "minutes": 9, "xp": 40, "summary": "Изтриване, достъп и защо знанието никога не изчезва напълно.", "theory": INTRO,
            "dialogue": dialogue(
                ("Lecturer", "Anyone who has tried to speak a language they learned at school will know the feeling: the words are somewhere, but they simply won't come.", "Всеки, който се е опитвал да говори език, учен в училище, познава усещането: думите са някъде, но просто не идват."),
                ("Lecturer", "Researchers call this language attrition, and the crucial point is that it's largely a problem of access rather than storage.", "Изследователите наричат това езикова атриция, а ключовото е, че тя е до голяма степен проблем на достъпа, а не на съхранението."),
                ("Lecturer", "In other words, the knowledge hasn't been deleted. It's been buried under more recent, more frequently used material.", "С други думи, знанието не е изтрито. То е затрупано под по-скорошен, по-често използван материал."),
                ("Lecturer", "The evidence for this is the so-called savings effect. People who relearn a forgotten language do so far faster than complete beginners, often recovering years of study in a matter of weeks.", "Доказателство за това е т.нар. ефект на спестяванията. Хората, които учат отново забравен език, го правят много по-бързо от пълните начинаещи, често възстановявайки години учене за седмици."),
                ("Lecturer", "Interestingly, what you learned most thoroughly tends to survive longest. Vocabulary fades first; grammar, once mastered, is remarkably resilient.", "Интересно е, че наученото най-задълбочено оцелява най-дълго. Речникът избледнява първи; граматиката, веднъж овладяна, е забележително устойчива."),
                ("Lecturer", "So the practical moral is reassuring: nothing you've studied is truly wasted. It's merely waiting to be woken up.", "Практическата поука е успокояваща: нищо, което сте учили, не е наистина пропиляно. Просто чака да бъде събудено."),
            ),
            "exercises": [
                C("Каква е главната идея за забравянето?", ["Проблемът е в достъпа, не в съхранението", "Знанието се изтрива напълно", "Само децата забравят"], 0, instruction=DQ),
                C("Какво е ефектът на спестяванията?", ["Повторното учене е много по-бързо", "Спестяваш пари от курсове", "Помниш само думи"], 0, instruction=DQ),
                C("Какво избледнява първо?", ["Речникът", "Граматиката", "Произношението"], 0, instruction=DQ),
                C("Каква е поуката според лектора?", ["Нищо научено не е напълно пропиляно", "Трябва да учиш всеки ден, иначе губиш всичко", "По-добре е да учиш само граматика"], 0, instruction=DQ),
                L("Какво означава resilient?", "Grammar, once mastered, is remarkably resilient.", ["устойчив", "сложен", "крехък"], 0),
                L("Какво означава in a matter of weeks?", "often recovering years of study in a matter of weeks", ["само за няколко седмици", "след много седмици", "всяка седмица"], 0),
                D("Nothing you've studied is truly wasted."),
            ],
        },
    ],
    "c2-nuance-style": [
        {
            "slug": "c2-fronting", "title": "Изнасяне напред: Strange as it may seem", "title_en": "Fronting for emphasis",
            "kind": "grammar", "minutes": 8, "xp": 35, "summary": "Как стилистично да поставиш акцента в началото.",
            "theory": """
<table>
<tr><th>Структура</th><th>Пример</th><th>Значение</th></tr>
<tr><td>прилагателно/наречие + <span class="en">as</span> + подлог + глагол</td><td class="en">Strange as it may seem, I enjoyed it.</td><td>Колкото и странно да изглежда...</td></tr>
<tr><td class="en">Try as I might, ...</td><td class="en">Try as I might, I couldn't open it.</td><td>Колкото и да се опитвах...</td></tr>
<tr><td>изнесено допълнение</td><td class="en">That I can understand. His rudeness I cannot.</td><td>Това го разбирам. Грубостта му не.</td></tr>
<tr><td>изнесено място + инверсия</td><td class="en">On the hill stood an old church.</td><td>На хълма се издигаше стара църква.</td></tr>
<tr><td class="en">Such was / So + прил. + was</td><td class="en">Such was the noise that no one slept.</td><td>Толкова голям беше шумът, че...</td></tr>
</table>
<div class="tip">Тези конструкции са литературни и официални. В разговор звучат драматично, затова ги използвай с мярка.</div>
""",
            "exercises": [
                C("___ it may sound, I prefer winter.", ["Strange as", "As strange", "Strange though as"], 0),
                C("___ , I couldn't remember her name. (Колкото и да се опитвах)", ["Try as I might", "As I might try", "Might I try"], 0),
                C("At the end of the street ___ .", ["stood a tiny café", "a tiny café stood it", "did stand a tiny café"], 0),
                C("___ his anger that he couldn't speak.", ["Such was", "So was", "Such did"], 0),
                F("Tired ___ we were, we kept walking.", "as|though"),
                C("That I can forgive. Каква е функцията?", ["Акцент върху допълнението", "Въпрос", "Условие"], 0),
            ],
        },
    ],
}

MISTAKES = {
    "a1-imperatives": [
        ("No touch!", "Don't touch!", "Забрана: Don't + глагол."),
        ("Lets go!", "Let's go!", "Let's = let us (с апостроф)."),
    ],
    "a1-write-friend": [
        ("She has 25 years.", "She is 25.", "Възраст: to be."),
        ("brown long hair", "long brown hair", "Размер преди цвят."),
    ],
    "a2-possessive-pronouns": [
        ("It's mine bag.", "It's my bag. / It's mine.", "Mine е без съществително."),
        ("Is this your's?", "Is this yours?", "Без апостроф."),
    ],
    "a2-house-chores": [
        ("do the bed", "make the bed", "Леглото се make."),
    ],
    "b1-indirect-questions": [
        ("Do you know where is the station?", "Do you know where the station is?", "Непряк въпрос: словоред като в твърдение."),
        ("Can you tell me what time does it open?", "Can you tell me what time it opens?", "Без does."),
    ],
    "b1-money-banking": [
        ("Keep the rest.", "Keep the change.", "Ресто: change."),
    ],
    "b1-write-apology": [
        ("I should called you.", "I should have called you.", "Should have + 3-та форма."),
    ],
    "b2-verb-pattern-meaning": [
        ("I stopped to smoke last year.", "I stopped smoking last year.", "Отказах цигарите: stop + -ing."),
        ("Remember locking the door when you leave.", "Remember to lock the door when you leave.", "Задача за после: remember to."),
    ],
    "b2-crime": [
        ("A burglar stole my wallet on the bus.", "A pickpocket stole my wallet on the bus.", "Burglar влиза в дом; на улицата е pickpocket."),
    ],
    "c1-future-in-past": [
        ("I was going to call you, but I will forget.", "I was going to call you, but I forgot.", "Планът е в миналото: forgot."),
    ],
}
