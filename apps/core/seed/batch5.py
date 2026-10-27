"""Fifth batch: writing tasks from the Cambridge exam formats, reading-skill lessons, grammar and core vocabulary.

Writing follows the task types learners meet at each level (postcard, story, article, review, letter of
application, report, opinion article). Reading lessons each train one skill: scanning, matching, gapped text,
inference. Vocabulary focuses on the highest-frequency words (Oxford 3000).
"""

from .courses import C, F, O, T
from .courses_skills import reading
from .speaking_writing import model_text

RQ = "Отговори според текста"

EXTRA_LESSONS = {
    # ---------------- A1 ----------------
    "a1-speak-write": [
        {
            "slug": "a1-write-postcard", "title": "Пиши: картичка от почивка", "title_en": "Writing: a holiday postcard",
            "kind": "writing", "minutes": 7, "xp": 15, "summary": "Кратка картичка: къде си, какво правиш, какво е времето.",
            "theory": model_text("Greetings from Greece!", [
                "Dear Grandma,",
                "We're in Crete! The hotel is lovely and the sea is warm.",
                "Every day we swim and eat fresh fish. The weather is hot and sunny.",
                "See you next week. Lots of love,",
                "Mila",
            ], [("Dear Grandma,", "обръщение към близък човек"), ("We're in Crete!", "къде си"),
                ("Every day we...", "какво правите (Present Simple)"), ("The weather is...", "времето"),
                ("Lots of love,", "топъл край")]),
            "exercises": [
                C("С какво започва картичката до баба ти?", ["Dear Grandma,", "To whom it may concern,", "Hey you!"], 0),
                C("Как казваш какво правите всеки ден?", ["Every day we swim.", "Every day we swimming.", "Every day we are swim."], 0),
                F("The weather ___ hot and sunny.", "is"),
                C("Подходящ край на картичка до близък човек:", ["Lots of love,", "Yours faithfully,", "Regards, Mr Petrov"], 0),
                O("Хотелът е прекрасен.", "The hotel is lovely"),
                T("Ще се видим следващата седмица.", "See you next week"),
            ],
        },
    ],
    "a1-skills": [
        {
            "slug": "a1-read-flat-ad", "title": "Четене: обява за стая", "title_en": "Reading: a room for rent",
            "kind": "reading", "minutes": 6, "xp": 15, "summary": "Умение: търсене на конкретна информация (scanning).",
            "theory": """<div class="tip"><strong>Умение: scanning.</strong> Когато търсиш конкретна информация (цена, дата, телефон), не чети всяка дума. Плъзни поглед по текста и спри само при числата и ключовите думи.</div>""" + reading("Room for rent", [
                "Large room in a quiet flat near the city centre.",
                "£450 a month, bills included. Available from 1 March.",
                "Shared kitchen and bathroom. Free Wi-Fi. No pets, no smoking.",
                "Ten minutes' walk to the station. Call Sam on 07700 900123.",
            ], [("for rent", "под наем"), ("bills included", "сметките са включени"), ("available from", "свободна от"),
                ("shared", "общ, споделен"), ("pets", "домашни любимци")]),
            "exercises": [
                C("Колко струва стаята на месец?", ["£450", "£400", "£45"], 0, instruction=RQ),
                C("От кога е свободна?", ["1 март", "1 май", "Веднага"], 0, instruction=RQ),
                C("Разрешени ли са домашни любимци?", ["Не", "Да", "Само котки"], 0, instruction=RQ),
                C("Колко далеч е гарата?", ["10 минути пеша", "10 минути с кола", "До сградата"], 0, instruction=RQ),
                C("Какво е включено в цената?", ["Сметките", "Храната", "Паркингът"], 0, instruction=RQ),
                F("The kitchen and bathroom are ___ .", "shared"),
            ],
        },
        {
            "slug": "a1-everyday-verbs", "title": "Най-важните глаголи", "title_en": "The most common verbs",
            "kind": "vocabulary", "minutes": 7, "xp": 15, "summary": "Get, take, make, have: глаголите, които ще чуваш навсякъде.",
            "theory": """
<p>Малък брой глаголи покриват огромна част от ежедневната реч. Научи ги с изразите, в които се използват.</p>
<table>
<tr><th>Глагол</th><th>Чести изрази</th></tr>
<tr><td class="en">have</td><td><span class="en">have breakfast, have a shower, have fun</span></td></tr>
<tr><td class="en">get</td><td><span class="en">get up</span> (ставам), <span class="en">get home</span> (прибирам се), <span class="en">get a job</span></td></tr>
<tr><td class="en">take</td><td><span class="en">take a bus, take a photo, take a break</span></td></tr>
<tr><td class="en">make</td><td><span class="en">make dinner, make a call, make friends</span></td></tr>
<tr><td class="en">go</td><td><span class="en">go shopping, go to work, go home</span></td></tr>
<tr><td class="en">do</td><td><span class="en">do homework, do the dishes, do sport</span></td></tr>
</table>
<div class="tip"><span class="en">Go home</span> е без <span class="en">to</span>: не <em>go to home</em>.</div>
""",
            "exercises": [
                C("I usually ___ breakfast at 7.", ["have", "make", "do"], 0),
                C("Can you ___ a photo of us?", ["make", "take", "do"], 1),
                C("What time do you ___ up?", ["get", "go", "take"], 0),
                C("Кое е правилно?", ["I go to home.", "I go home."], 1),
                F("Let's ___ a break.", "take"),
                O("Ходим на пазар в събота.", "We go shopping on Saturday"),
            ],
        },
    ],
    # ---------------- A2 ----------------
    "a2-speak-write": [
        {
            "slug": "a2-write-story", "title": "Пиши: кратка история", "title_en": "Writing: a short story",
            "kind": "writing", "minutes": 8, "xp": 20, "summary": "Начало, проблем, край: история в минало време.",
            "theory": model_text("The lost key", [
                "Last Saturday I went to the beach with my friend Alex.",
                "We swam and played volleyball all afternoon. Then, when we wanted to go home, I couldn't find my car key!",
                "We looked everywhere. Finally, Alex found it in the sand next to our towels.",
                "We laughed a lot and drove home happy.",
            ], [("Last Saturday...", "кога и с кого: начало"), ("Then, when...", "проблемът"),
                ("Finally,...", "как се решава"), ("We laughed... and drove home", "край и чувства")]) + """
<div class="tip">Историята се пише в <strong>Past Simple</strong>. Свързващи думи: <span class="en">first, then, after that, suddenly, finally</span>.</div>
""",
            "exercises": [
                C("В какво време се пише историята?", ["Past Simple", "Present Simple", "Future"], 0),
                C("Коя дума въвежда решението на проблема?", ["Finally", "Last Saturday", "Every day"], 0),
                F("Suddenly, I ___ (see) a big dog.", "saw"),
                F("We ___ (look) everywhere for the key.", "looked"),
                O("Изведнъж започна да вали.", "Suddenly it started to rain"),
                T("Накрая всичко беше наред.", "Finally everything was OK|In the end everything was OK|Finally everything was fine|In the end everything was fine"),
            ],
        },
    ],
    "a2-skills": [
        {
            "slug": "a2-read-museum", "title": "Четене: уебсайт на музей", "title_en": "Reading: a museum website",
            "kind": "reading", "minutes": 7, "xp": 20, "summary": "Умение: намиране на часове, цени и правила.",
            "theory": """<div class="tip"><strong>Умение: scanning.</strong> Преди да четеш, прочети въпросите. После търси в текста само думите от въпроса: часове, цени, дни.</div>""" + reading("City Science Museum: Visit us", [
                "Opening hours: Tuesday to Sunday, 10 am to 6 pm. Closed on Mondays. Late opening on Thursdays until 9 pm.",
                "Tickets: Adults £12, students £8, children under 5 free. Family ticket (2 adults and 2 children): £30.",
                "Photos are allowed, but please don't use flash. Bags larger than a backpack must go in the cloakroom.",
                "The café on the ground floor serves lunch from 12 to 3 pm.",
            ], [("opening hours", "работно време"), ("late opening", "удължено работно време"), ("allowed", "разрешено"),
                ("flash", "светкавица"), ("cloakroom", "гардероб"), ("ground floor", "партер")]),
            "exercises": [
                C("Кой ден музеят е затворен?", ["Понеделник", "Неделя", "Четвъртък"], 0, instruction=RQ),
                C("До колко часа е отворен в четвъртък?", ["21:00", "18:00", "15:00"], 0, instruction=RQ),
                C("Колко струва билет за студент?", ["£8", "£12", "Безплатно"], 0, instruction=RQ),
                C("Какво не е разрешено?", ["Снимки със светкавица", "Снимки без светкавица", "Раници"], 0, instruction=RQ),
                C("Колко плаща семейство с двама възрастни и две деца на 7 и 9 години?", ["£30", "£40", "£24"], 0, instruction=RQ),
                F("Children under 5 go in ___ .", "free"),
            ],
        },
        {
            "slug": "a2-adjective-prepositions", "title": "Прилагателно + предлог", "title_en": "Adjectives and prepositions",
            "kind": "vocabulary", "minutes": 7, "xp": 20, "summary": "Good at, afraid of, interested in.",
            "theory": """
<p>Много прилагателни вървят с точно определен предлог. Той често е различен от българския, затова ги учи заедно.</p>
<table>
<tr><th>Израз</th><th>Значение</th></tr>
<tr><td class="en">good / bad at</td><td>добър / лош в (нещо)</td></tr>
<tr><td class="en">afraid of</td><td>страх ме е от</td></tr>
<tr><td class="en">interested in</td><td>интересувам се от</td></tr>
<tr><td class="en">proud of</td><td>горд с</td></tr>
<tr><td class="en">angry with (човек) / about (нещо)</td><td>ядосан на / заради</td></tr>
<tr><td class="en">different from</td><td>различен от</td></tr>
<tr><td class="en">married to</td><td>женен за / омъжена за</td></tr>
<tr><td class="en">tired of</td><td>писнало ми е от</td></tr>
</table>
<div class="tip">След предлога глаголът е с -ing: <span class="en">I'm good at cooking.</span></div>
""",
            "exercises": [
                C("She's very good ___ maths.", ["in", "at", "on"], 1),
                C("I'm afraid ___ spiders.", ["from", "of", "with"], 1),
                C("He's interested ___ history.", ["in", "for", "about"], 0),
                C("She's married ___ a doctor.", ["with", "to", "for"], 1),
                F("I'm tired ___ waiting.", "of"),
                O("Горд съм с теб.", "I am proud of you|I'm proud of you"),
            ],
        },
    ],
    "a2-how-we-do": [
        {
            "slug": "a2-reflexive-pronouns", "title": "Myself, yourself: възвратни местоимения", "title_en": "Reflexive pronouns",
            "kind": "grammar", "minutes": 6, "xp": 20, "summary": "Сам, себе си: кога английският иска -self.",
            "theory": """
<table>
<tr><th>Лице</th><th>Възвратно</th></tr>
<tr><td class="en">I</td><td class="en">myself</td></tr>
<tr><td class="en">you</td><td class="en">yourself / yourselves</td></tr>
<tr><td class="en">he / she / it</td><td class="en">himself / herself / itself</td></tr>
<tr><td class="en">we / they</td><td class="en">ourselves / themselves</td></tr>
</table>
<ul>
<li>Действието се връща към подлога: <span class="en">I cut myself.</span> Порязах се.</li>
<li>„Сам“ (без помощ): <span class="en">She made it herself.</span> / <span class="en">by myself</span> = сам, без компания.</li>
<li><span class="en">Enjoy yourself!</span> Забавлявай се!</li>
</ul>
<div class="tip">Много български глаголи със „се“ на английски са без <span class="en">-self</span>: облека се = <span class="en">get dressed</span>, мия се = <span class="en">wash</span>, чувствам се = <span class="en">feel</span>, срещаме се = <span class="en">meet</span>.</div>
""",
            "exercises": [
                C("Be careful! Don't hurt ___ .", ["you", "yourself", "yourselves"], 1),
                C("We painted the house ___ .", ["ourselves", "ourself", "us"], 0),
                C("Чувствам се добре:", ["I feel myself good.", "I feel good."], 1, "Feel е без myself."),
                C("I live by ___ .", ["me", "myself", "mine"], 1),
                F("Did you enjoy ___ at the party? (вие, много хора)", "yourselves"),
                O("Тя си направи тортата сама.", "She made the cake herself"),
            ],
        },
    ],
    # ---------------- B1 ----------------
    "b1-speak-write": [
        {
            "slug": "b1-write-article", "title": "Пиши: статия за списание", "title_en": "Writing: a magazine article",
            "kind": "writing", "minutes": 9, "xp": 25, "summary": "Заглавие, въпрос към читателя, личен опит.",
            "theory": model_text("Why I love cycling to work", [
                "Have you ever been stuck in traffic and wished you could just fly over it? A year ago, I decided to stop wishing and start cycling.",
                "At first it was hard. My legs hurt, and I arrived at work tired. But after a few weeks, something changed: I started to feel more awake and much happier.",
                "Cycling also saves me money. I don't pay for petrol or parking any more, and I don't need a gym.",
                "So why not give it a try? You might find it's the best part of your day.",
            ], [("Have you ever...?", "въпрос, който привлича читателя"), ("At first... But after a few weeks", "личен опит и промяна"),
                ("Cycling also...", "втори аргумент"), ("So why not give it a try?", "призив към читателя")]) + """
<div class="tip">Статията е неформална и жива: заглавие, директен въпрос към читателя, примери от собствен опит.</div>
""",
            "exercises": [
                C("Добро начало на статия:", ["Have you ever wanted to...?", "Dear Sir or Madam,", "I am writing to complain"], 0),
                C("Статията за списание обикновено е:", ["неформална и лична", "официална като доклад", "без заглавие"], 0),
                C("Подходящ край:", ["So why not give it a try?", "Yours faithfully,", "In conclusion, the data shows"], 0),
                F("At ___ it was hard, but after a few weeks it got easier.", "first"),
                O("Може би ще ти хареса.", "You might like it"),
                T("Защо не опиташ?", "Why not give it a try|Why don't you try|Why don't you give it a try|Why not try"),
            ],
        },
    ],
    "b1-skills": [
        {
            "slug": "b1-read-matching", "title": "Четене: кой какво търси?", "title_en": "Reading: matching people to texts",
            "kind": "reading", "minutes": 8, "xp": 25, "summary": "Умение: свързване на нуждите на хора с подходящия текст.",
            "theory": """<div class="tip"><strong>Умение: matching.</strong> Първо подчертай какво точно иска всеки човек (2-3 изисквания). После търси текст, който покрива <em>всички</em> изисквания, не само едно.</div>
<h2>Хората</h2>
<ul>
<li><strong>Ана</strong> иска курс вечер, за начинаещи, близо до центъра.</li>
<li><strong>Борис</strong> има опит и иска онлайн курс през уикенда.</li>
<li><strong>Вера</strong> търси курс с изпит в края, сутрин.</li>
</ul>""" + reading("Spanish courses", [
                "A) Spanish for Starters: no experience needed. Tuesday and Thursday evenings, 7 to 9 pm, in our city-centre school.",
                "B) Spanish Online Plus: for intermediate learners. Live lessons on Saturdays and Sundays, from your home.",
                "C) Exam Spanish: morning classes, Monday to Friday. The course ends with an official DELE exam.",
                "D) Spanish Conversation Club: evenings in a café outside the city. For advanced speakers only.",
            ], [("no experience needed", "не е нужен опит"), ("intermediate", "среднонапреднал"),
                ("live lessons", "уроци на живо"), ("ends with", "завършва с")]),
            "exercises": [
                C("Кой курс е подходящ за Ана?", ["A", "B", "C", "D"], 0, instruction=RQ),
                C("Кой курс е подходящ за Борис?", ["B", "A", "C", "D"], 0, instruction=RQ),
                C("Кой курс е подходящ за Вера?", ["C", "A", "B", "D"], 0, instruction=RQ),
                C("Защо D не е за Ана, въпреки че е вечер?", ["Не е за начинаещи и е извън града", "Твърде скъп е", "Онлайн е"], 0, instruction=RQ),
                F("No experience is ___ for course A.", "needed"),
            ],
        },
        {
            "slug": "b1-verb-prepositions", "title": "Глагол + предлог", "title_en": "Verbs and prepositions",
            "kind": "vocabulary", "minutes": 7, "xp": 25, "summary": "Depend on, listen to, wait for.",
            "theory": """
<table>
<tr><th>Израз</th><th>Значение</th><th>Внимание</th></tr>
<tr><td class="en">depend on</td><td>зависи от</td><td>не <em>depend from</em></td></tr>
<tr><td class="en">listen to</td><td>слушам</td><td>с човек или нещо: <span class="en">listen to music</span></td></tr>
<tr><td class="en">wait for</td><td>чакам</td><td><span class="en">wait for the bus</span></td></tr>
<tr><td class="en">ask for</td><td>моля за, искам</td><td><span class="en">ask for help</span></td></tr>
<tr><td class="en">look at / look for</td><td>гледам / търся</td><td></td></tr>
<tr><td class="en">pay for</td><td>плащам за</td><td></td></tr>
<tr><td class="en">belong to</td><td>принадлежи на</td><td></td></tr>
<tr><td class="en">agree with</td><td>съгласен съм с</td><td></td></tr>
</table>
<div class="tip">Някои глаголи са <strong>без</strong> предлог, макар в българския да има: <span class="en">discuss the plan</span>, <span class="en">enter the room</span>, <span class="en">answer the question</span>.</div>
""",
            "exercises": [
                C("It depends ___ the weather.", ["from", "on", "of"], 1),
                C("I'm waiting ___ my friend.", ["for", "on", "to"], 0),
                C("Who does this bag belong ___ ?", ["to", "at", "with"], 0),
                C("Кое е правилно?", ["Let's discuss about it.", "Let's discuss it."], 1),
                F("Can you listen ___ me, please?", "to"),
                O("Платих за обяда.", "I paid for lunch|I paid for the lunch"),
            ],
        },
    ],
    "b1-past-descriptions": [
        {
            "slug": "b1-past-ability", "title": "Could и was able to", "title_en": "Past ability",
            "kind": "grammar", "minutes": 7, "xp": 20, "summary": "Можех и успях: двете английски форми.",
            "theory": """
<table>
<tr><th>Форма</th><th>Употреба</th><th>Пример</th></tr>
<tr><td class="en">could</td><td>обща способност в миналото</td><td class="en">I could swim when I was five.</td></tr>
<tr><td class="en">was / were able to, managed to</td><td>успях да направя нещо конкретно (с усилие)</td><td class="en">The fire was huge, but everyone was able to escape.</td></tr>
<tr><td class="en">couldn't</td><td>и за общо, и за конкретно</td><td class="en">I couldn't find my keys.</td></tr>
</table>
<div class="tip">„Успях да хвана влака“ е <span class="en">I managed to catch the train</span> или <span class="en">I was able to catch the train</span>, а не <em>I could catch the train</em>.</div>
""",
            "exercises": [
                C("My grandfather ___ speak four languages.", ["could", "was able to"], 0, "Обща способност: could."),
                C("The test was hard, but I ___ pass it.", ["could", "managed to"], 1, "Конкретен успех: managed to / was able to."),
                C("I ___ sleep last night because of the noise.", ["couldn't", "wasn't able"], 0),
                F("We were ___ to find a hotel in the end.", "able"),
                O("Успях да намеря работа.", "I managed to find a job|I was able to find a job"),
            ],
        },
    ],
    "b1-tenses-detail": [
        {
            "slug": "b1-as-like", "title": "As или like", "title_en": "Using as and like",
            "kind": "grammar", "minutes": 6, "xp": 20, "summary": "Като учител или като учител?",
            "theory": """
<table>
<tr><th>Дума</th><th>Значение</th><th>Пример</th></tr>
<tr><td class="en">as + професия/роля</td><td>в качеството на (наистина е)</td><td class="en">She works as a teacher.</td></tr>
<tr><td class="en">like + съществително</td><td>подобно на (не е)</td><td class="en">He talks like a teacher.</td></tr>
<tr><td class="en">as + изречение</td><td>както</td><td class="en">Do it as I showed you.</td></tr>
<tr><td class="en">such as</td><td>като например</td><td class="en">fruit such as apples and pears</td></tr>
</table>
<div class="tip"><span class="en">I work as a nurse</span> = медицинска сестра съм. <span class="en">She sings like a bird</span> = пее като птица, но не е птица.</div>
""",
            "exercises": [
                C("I work ___ a waiter in the summer.", ["as", "like"], 0),
                C("You look ___ your mother.", ["as", "like"], 1),
                C("He used his coat ___ a blanket.", ["as", "like"], 0, "Палтото наистина служи като одеяло."),
                F("I love sports such ___ tennis and swimming.", "as"),
                O("Тя работи като лекар.", "She works as a doctor"),
            ],
        },
    ],
    # ---------------- B2 ----------------
    "b2-speak-write": [
        {
            "slug": "b2-write-review", "title": "Пиши: рецензия", "title_en": "Writing: a review",
            "kind": "writing", "minutes": 9, "xp": 30, "summary": "Опиши, оцени, препоръчай: рецензия за филм или ресторант.",
            "theory": model_text("A hidden gem in the old town", [
                "If you're looking for authentic Bulgarian food away from the tourist crowds, Stara Kashta is well worth a visit.",
                "The menu is short but impressive. The lamb, slowly cooked with herbs, was tender and full of flavour, while the homemade bread was simply outstanding.",
                "The only drawback was the service, which was rather slow on a busy Saturday evening.",
                "Overall, I would highly recommend it to anyone who values good food more than a fast meal.",
            ], [("well worth a visit", "силна препоръка в началото"), ("tender and full of flavour", "конкретно, живо описание"),
                ("The only drawback was...", "балансирана критика"), ("Overall, I would highly recommend it to...", "препоръка и за кого")]),
            "exercises": [
                C("Каква е структурата на рецензията?", ["Представяне, описание, критика, препоръка", "Само похвали", "Само факти"], 0),
                C("Учтива критика:", ["The only drawback was the slow service.", "The service was terrible, never go!", "Bad service."], 0),
                C("Силна препоръка:", ["It's well worth a visit.", "It's OK I guess.", "Maybe go."], 0),
                F("I would highly ___ it to families.", "recommend"),
                O("Като цяло ресторантът си заслужава.", "Overall the restaurant is worth it|Overall the restaurant is well worth a visit"),
            ],
        },
        {
            "slug": "b2-write-application", "title": "Пиши: мотивационно писмо", "title_en": "Writing: a letter of application",
            "kind": "writing", "minutes": 10, "xp": 30, "summary": "Кандидатстване за работа или стаж.",
            "theory": model_text("Application: Summer Tour Guide", [
                "Dear Ms Taylor,",
                "I am writing to apply for the position of summer tour guide, which was advertised on your website.",
                "I am a third-year history student at Sofia University and I have worked as a volunteer guide at the National Museum for two years. I speak fluent English and German.",
                "I believe I would be well suited to this role, as I enjoy working with people and I am confident speaking in front of groups.",
                "I would welcome the opportunity to discuss my application further. I look forward to hearing from you.",
                "Yours sincerely,",
                "Georgi Ivanov",
            ], [("I am writing to apply for the position of...", "за коя позиция и откъде знаеш"),
                ("I have worked as... for two years", "опит (Present Perfect)"),
                ("I believe I would be well suited to this role, as...", "защо си подходящ"),
                ("I would welcome the opportunity to...", "учтив завършек"),
                ("Yours sincerely,", "край, когато знаеш името")]),
            "exercises": [
                C("Писмото започва Dear Ms Taylor. Край:", ["Yours sincerely,", "Yours faithfully,", "Love,"], 0),
                C("Опит, който продължава и сега:", ["I have worked as a guide for two years.", "I work as a guide since two years.", "I am working as a guide for two years."], 0),
                F("I am writing to ___ for the position of receptionist.", "apply"),
                C("Кое изречение е най-подходящо?", ["I would be well suited to this role.", "I'm perfect, hire me.", "I need money."], 0),
                O("Говоря свободно английски и немски.", "I speak fluent English and German"),
            ],
        },
    ],
    "b2-skills": [
        {
            "slug": "b2-read-gapped", "title": "Четене: пропуснати изречения", "title_en": "Reading: gapped text",
            "kind": "reading", "minutes": 9, "xp": 30, "summary": "Умение: да разбираш как се свързват изреченията.",
            "theory": """<div class="tip"><strong>Умение: gapped text.</strong> Прочети изречението преди и след празното място. Търси връзки: местоимения (<span class="en">this, they, it</span>), противопоставяне (<span class="en">however</span>), продължение (<span class="en">also</span>).</div>""" + reading("Learning to sleep again", [
                "When Maria started working night shifts at the hospital, she thought she would get used to it quickly. [1]",
                "Her body clock simply refused to adapt. She would come home at eight in the morning, exhausted, but lie awake for hours. [2]",
                "Then a colleague suggested a few simple changes: blackout curtains, earplugs and, above all, the same bedtime every day, even on days off. [3]",
                "Within a month, Maria was sleeping six solid hours. She still misses the sun, but she no longer dreads her shifts.",
            ], [("night shifts", "нощни смени"), ("body clock", "биологичен часовник"), ("adapt", "приспособявам се"),
                ("blackout curtains", "плътни завеси"), ("dreads", "изпитва ужас от")]),
            "exercises": [
                C("Кое изречение пасва на [1]?", ["She was wrong.", "This made her very happy.", "The hospital was new."], 0, "Следващото изречение показва, че не е свикнала."),
                C("Кое изречение пасва на [2]?", ["By the afternoon, she felt worse than when she went to bed.", "She loved her new routine.", "Her colleagues were all asleep."], 0),
                C("Кое изречение пасва на [3]?", ["It sounded too simple to work, but she tried it anyway.", "She refused to listen.", "She moved to another country."], 0),
                C("Какво помага най-много според текста?", ["Едно и също време за лягане всеки ден", "Повече кафе", "Сън през деня с отворени завеси"], 0, instruction=RQ),
                F("She no longer ___ her shifts. (изпитва ужас от)", "dreads"),
            ],
        },
    ],
    "b2-linking-future": [
        {
            "slug": "b2-certainty", "title": "Bound to, likely, might: колко сигурно е", "title_en": "The future: degrees of certainty",
            "kind": "grammar", "minutes": 8, "xp": 25, "summary": "Как да покажеш колко си сигурен за бъдещето.",
            "theory": """
<table>
<tr><th>Сигурност</th><th>Изрази</th><th>Пример</th></tr>
<tr><td>почти 100%</td><td class="en">be bound to, be sure to, will definitely</td><td class="en">It's bound to rain this weekend.</td></tr>
<tr><td>вероятно</td><td class="en">be likely to, will probably</td><td class="en">Prices are likely to rise.</td></tr>
<tr><td>възможно</td><td class="en">may, might, could</td><td class="en">We might be late.</td></tr>
<tr><td>малко вероятно</td><td class="en">be unlikely to, probably won't</td><td class="en">He's unlikely to win.</td></tr>
</table>
<div class="tip">Реда на думите: <span class="en">will probably</span>, но <span class="en">probably won't</span>.</div>
""",
            "exercises": [
                C("He always forgets. He's ___ to forget again.", ["bound", "unlikely", "might"], 0),
                C("The shops are ___ to be busy on Christmas Eve.", ["likely", "unlikely"], 0),
                C("Кое е правилно?", ["She will probably come.", "She probably will come.", "She will come probably not."], 0),
                C("Кое е правилно?", ["I probably won't go.", "I won't probably go."], 0),
                F("It's very ___ that they will cancel the match. (малко вероятно)", "unlikely"),
                O("Вероятно ще закъснеем.", "We will probably be late|We'll probably be late"),
            ],
        },
    ],
    # ---------------- C1 ----------------
    "c1-speak-write": [
        {
            "slug": "c1-write-report", "title": "Пиши: доклад", "title_en": "Writing: a report",
            "kind": "writing", "minutes": 10, "xp": 35, "summary": "Заглавия, факти, препоръки: официален доклад.",
            "theory": model_text("Report: Staff canteen survey", [
                "Introduction: The aim of this report is to present the results of a survey of 80 employees about the staff canteen and to make recommendations.",
                "Food quality: The majority of respondents (65%) were satisfied with the food. However, many felt that the choice of vegetarian dishes was limited.",
                "Prices and opening hours: Prices were generally considered reasonable. A significant number of staff complained that the canteen closes too early for those on late shifts.",
                "Recommendations: It is recommended that the canteen introduce at least two vegetarian options daily and extend its opening hours until 8 pm.",
            ], [("The aim of this report is to...", "цел на доклада"),
                ("The majority of respondents...", "резултати, безлично"),
                ("A significant number of staff complained that...", "проблем, представен обективно"),
                ("It is recommended that...", "препоръки (подчинително наклонение)"),
                ("Заглавия на раздели", "докладът е с подзаглавия, за разлика от есето")]),
            "exercises": [
                C("Каква е основната разлика между доклад и есе?", ["Докладът има подзаглавия и препоръки", "Есето има подзаглавия", "Няма разлика"], 0),
                C("Безличен израз за резултати:", ["The majority of respondents were satisfied.", "Most people I asked liked it a lot.", "Everyone loved it!"], 0),
                C("It is recommended that the canteen ___ longer.", ["opens", "open", "opened"], 1, "След recommend that: основна форма."),
                F("The ___ of this report is to evaluate the new system.", "aim|purpose"),
                O("Препоръчва се да се удължи работното време.", "It is recommended that opening hours be extended|It is recommended that the opening hours be extended"),
            ],
        },
    ],
    "c1-skills": [
        {
            "slug": "c1-read-inference", "title": "Четене: подтекст и извод", "title_en": "Reading: inference",
            "kind": "reading", "minutes": 10, "xp": 35, "summary": "Умение: да разбираш какво не е казано директно.",
            "theory": """<div class="tip"><strong>Умение: inference.</strong> Авторите рядко казват всичко директно. Обърни внимание на избора на думи (<span class="en">claimed</span> вместо <span class="en">said</span>), на това какво е подчертано и какво е премълчано.</div>""" + reading("The new manager", [
                "When Daniel took over the department, he promised a fresh start. Within a month, he had replaced the coffee machine, renamed every meeting, and introduced a weekly 'innovation hour'.",
                "Sales, admittedly, remained exactly where they had been. But the office had never looked busier.",
                "At the annual review, Daniel claimed credit for a 'cultural transformation'. His team, for their part, mostly remembered the new coffee.",
            ], [("took over", "пое (ръководството)"), ("admittedly", "наистина, трябва да се признае"),
                ("claimed credit for", "приписа си заслугата за"), ("for their part", "от своя страна")]),
            "exercises": [
                C("Какво внушава авторът за промените на Даниел?", ["Повече външни, отколкото реални", "Довели са до голям успех", "Не е имало промени"], 0, instruction=RQ),
                C("Какво подсказва „the office had never looked busier“?", ["Изглеждало е активно, но без резултат", "Продажбите са се удвоили", "Офисът е бил препълнен с клиенти"], 0, instruction=RQ),
                C("Защо е използвано claimed, а не said?", ["За да покаже съмнение в твърдението", "За да покаже, че е вярно", "Защото е по-кратко"], 0, instruction=RQ),
                C("Какво мисли екипът според последното изречение?", ["Не е впечатлен от „трансформацията“", "Много е благодарен", "Иска още срещи"], 0, instruction=RQ),
                C("Admittedly въвежда:", ["неудобен факт, който трябва да се признае", "силен аргумент", "заключение"], 0),
            ],
        },
    ],
    # ---------------- C2 ----------------
    "c2-speak-write": [
        {
            "slug": "c2-write-opinion", "title": "Пиши: статия с позиция", "title_en": "Writing: an opinion article",
            "kind": "writing", "minutes": 10, "xp": 40, "summary": "Убедителен текст с отстъпка и ясна позиция.",
            "theory": model_text("In defence of boredom", [
                "We have engineered boredom out of modern life. Every queue, every commute, every pause is now filled by a screen.",
                "It is tempting to see this as progress. After all, who misses staring at a wall? Yet the evidence suggests that boredom is not wasted time but the space in which ideas take shape.",
                "Granted, not every idle moment produces a masterpiece. But a mind that is never left alone with itself loses the habit of wandering, and with it, much of its capacity for originality.",
                "Perhaps, then, the most radical thing we can do is nothing at all.",
            ], [("We have engineered boredom out of modern life.", "силно, провокативно начало"),
                ("It is tempting to... Yet...", "противопоставяне на общото мнение"),
                ("Granted, ... But...", "отстъпка, после контрааргумент"),
                ("Perhaps, then, ...", "запомнящ се край")]),
            "exercises": [
                C("Granted, ... But ... служи за:", ["отстъпка и контрааргумент", "въведение", "статистика"], 0),
                C("Кое начало е най-силно за статия с позиция?", ["We have engineered boredom out of modern life.", "In this article I will write about boredom.", "Boredom is a word."], 0),
                C("It is tempting to see this as progress. Yet... Какво прави авторът?", ["Представя общото мнение, за да го оспори", "Съгласява се напълно", "Сменя темата"], 0),
                F("___ , not every idle moment is useful. But... (Признавам, че)", "Granted|Admittedly"),
                O("Може би най-радикалното нещо е да не правим нищо.", "Perhaps the most radical thing is to do nothing"),
            ],
        },
    ],
    "c2-skills": [
        {
            "slug": "c2-read-academic", "title": "Четене: академичен откъс", "title_en": "Reading: an academic extract",
            "kind": "reading", "minutes": 10, "xp": 40, "summary": "Умение: да следиш аргумент и предпазливия език на науката.",
            "theory": """<div class="tip"><strong>Умение: академично четене.</strong> Научните текстове са предпазливи (<span class="en">suggests, may, appears to</span>). Разграничавай какво е доказано от това, което авторът само предполага.</div>""" + reading("Bilingualism and the ageing brain", [
                "A number of studies have suggested that lifelong bilingualism may delay the onset of dementia by several years.",
                "The proposed mechanism is that constantly switching between languages exercises the brain's control systems, building a form of cognitive reserve.",
                "However, the findings are far from conclusive. Several large studies have failed to replicate the effect, and critics note that bilingual participants often differ from monolingual ones in education and income.",
                "It would therefore be premature to recommend language learning primarily as a medical intervention, although its other benefits are hardly in doubt.",
            ], [("onset", "начало (на болест)"), ("cognitive reserve", "когнитивен резерв"),
                ("far from conclusive", "далеч от окончателни"), ("failed to replicate", "не успяха да повторят"),
                ("premature", "преждевременно")]),
            "exercises": [
                C("Какво твърди текстът за двуезичието и деменцията?", ["Може да я забави, но доказателствата не са окончателни", "Доказано я предотвратява", "Няма връзка"], 0, instruction=RQ),
                C("Какъв е проблемът според критиците?", ["Двуезичните участници се различават и по образование и доходи", "Изследванията са твърде скъпи", "Няма двуезични хора"], 0, instruction=RQ),
                C("Какъв е изводът на автора?", ["Преждевременно е ученето на езици да се препоръчва като лечение", "Всички трябва да учат езици, за да не боледуват", "Ученето на езици е вредно"], 0, instruction=RQ),
                C("Far from conclusive означава:", ["далеч от окончателни", "много убедителни", "окончателно опровергани"], 0),
                C("Коя дума показва предпазливост?", ["may", "proves", "always"], 0),
            ],
        },
    ],
}

MISTAKES = {
    "a1-write-postcard": [
        ("Every day we swimming.", "Every day we swim.", "За навици: Present Simple."),
    ],
    "a1-everyday-verbs": [
        ("I go to home.", "I go home.", "Home след go е без to."),
        ("make a photo", "take a photo", "Снимка се take, не make."),
    ],
    "a2-write-story": [
        ("Yesterday I go to the beach.", "Yesterday I went to the beach.", "Историята е в минало време."),
    ],
    "a2-adjective-prepositions": [
        ("good in maths", "good at maths", "Good at, не good in."),
        ("married with", "married to", "Married to някого."),
    ],
    "a2-reflexive-pronouns": [
        ("I feel myself good.", "I feel good.", "Feel е без myself."),
        ("We met ourselves at the café.", "We met at the café.", "Meet е без -selves."),
    ],
    "b1-write-article": [
        ("Dear readers, I am writing to inform you...", "Have you ever wondered...?", "Статията не е писмо: започни с въпрос или интересен факт."),
    ],
    "b1-verb-prepositions": [
        ("It depends from you.", "It depends on you.", "Depend on."),
        ("Let's discuss about it.", "Let's discuss it.", "Discuss е без about."),
    ],
    "b1-past-ability": [
        ("I could catch the last train.", "I managed to catch the last train.", "За конкретен успех: managed to / was able to."),
    ],
    "b1-as-like": [
        ("She works like a teacher.", "She works as a teacher.", "As = в качеството на (наистина е учител)."),
    ],
    "b2-write-application": [
        ("I am working as a guide since two years.", "I have worked as a guide for two years.", "От минало до сега: Present Perfect + for."),
    ],
    "b2-certainty": [
        ("I will probably not come.", "I probably won't come.", "Probably стои преди won't."),
    ],
    "c1-write-report": [
        ("It is recommended that the canteen opens later.", "It is recommended that the canteen open later.", "След recommend that: основна форма на глагола."),
    ],
}
