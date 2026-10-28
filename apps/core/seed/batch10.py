"""Tenth batch: more reading and writing at every level, practical vocabulary, and two grammar gaps (I was born,
in case).

EXTRA_LESSONS adds lessons to existing units (by unit slug).
"""

from .courses import C, D, F, L, O, S, T, W
from .courses_skills import reading
from .listening import INTRO, dialogue
from .speaking_writing import model_text

RQ = "Отговори според текста"
DQ = "Отговори според диалога"

EXTRA_LESSONS = {
    # ---------------- A1 ----------------
    "a1-first-steps": [
        {
            "slug": "a1-was-born", "title": "I was born: кога и къде си роден", "title_en": "Saying when and where you were born",
            "kind": "grammar", "minutes": 5, "xp": 15, "summary": "Роден съм през 1990 в Пловдив: с was, не с am.",
            "theory": """
<p>На английски „роден съм“ винаги е в минало време: <span class="en">I was born</span>.</p>
<table>
<tr><th>Въпрос</th><th>Отговор</th></tr>
<tr><td class="en">Where were you born?</td><td class="en">I was born in Plovdiv.</td></tr>
<tr><td class="en">When were you born?</td><td class="en">I was born in 1990. / I was born on 5 May.</td></tr>
<tr><td class="en">Where was she born?</td><td class="en">She was born in Spain.</td></tr>
</table>
<div class="tip">Предлози: <span class="en">in</span> + град, държава, година, месец; <span class="en">on</span> + дата.</div>
""",
            "exercises": [
                C("Роден съм в София:", ["I was born in Sofia.", "I am born in Sofia.", "I born in Sofia."], 0),
                C("Where ___ you born?", ["were", "was", "are"], 0),
                C("He was born ___ 1985.", ["in", "on", "at"], 0),
                C("She was born ___ 12 March.", ["on", "in", "at"], 0),
                F("My parents ___ born in Varna.", "were"),
                O("Къде си роден?", "Where were you born"),
            ],
        },
    ],
    "a1-skills": [
        {
            "slug": "a1-read-weather", "title": "Четене: прогноза за времето", "title_en": "Reading: a weather forecast",
            "kind": "reading", "minutes": 6, "xp": 15, "summary": "Умение: да намериш деня и времето, което те интересува.",
            "theory": """<div class="tip"><strong>Умение: търсене по ден.</strong> Прогнозата е подредена по дни. Намери деня, после прочети само неговия ред.</div>""" + reading("Weekend weather in Edinburgh", [
                "Friday: cloudy and cold, 8°C. Rain in the evening.",
                "Saturday: sunny in the morning, windy in the afternoon, 12°C.",
                "Sunday: rain all day, 9°C. Take an umbrella!",
                "Monday: sunny and warm, 15°C. A good day for a walk.",
            ], [("cloudy", "облачно"), ("windy", "ветровито"), ("all day", "цял ден"), ("umbrella", "чадър"),
                ("a walk", "разходка")]),
            "exercises": [
                C("Кой ден е най-топъл?", ["Понеделник", "Събота", "Петък"], 0, instruction=RQ),
                C("Кога вали цял ден?", ["В неделя", "В петък", "В събота"], 0, instruction=RQ),
                C("Какво е времето в събота следобед?", ["Ветровито", "Дъждовно", "Облачно"], 0, instruction=RQ),
                C("Колко градуса е в петък?", ["8", "12", "15"], 0, instruction=RQ),
                C("Кой ден е добър за разходка?", ["Понеделник", "Неделя", "Петък"], 0, instruction=RQ),
                F("Take an ___ on Sunday!", "umbrella"),
            ],
        },
        {
            "slug": "a1-hobbies", "title": "Хобита: play, go или do?", "title_en": "Hobbies with play, go and do",
            "kind": "vocabulary", "minutes": 6, "xp": 15, "summary": "Play football, go swimming, do yoga.",
            "theory": """
<table>
<tr><th>Глагол</th><th>Кога</th><th>Примери</th></tr>
<tr><td class="en">play</td><td>игри с топка, игри, инструменти</td><td class="en">play football, play chess, play the guitar</td></tr>
<tr><td class="en">go</td><td>дейности с -ing</td><td class="en">go swimming, go running, go shopping, go dancing</td></tr>
<tr><td class="en">do</td><td>индивидуални спортове и занимания</td><td class="en">do yoga, do karate, do exercise</td></tr>
</table>
<p>Други хобита: <span class="en">read books, watch films, cook, paint, take photos, listen to music</span>.</p>
<div class="tip">Въпрос: <span class="en">What do you do in your free time?</span> Отговор: <span class="en">I like playing tennis.</span></div>
""",
            "exercises": [
                C("I ___ tennis every Saturday.", ["play", "go", "do"], 0),
                C("Let's ___ swimming!", ["go", "play", "do"], 0),
                C("She ___ yoga in the morning.", ["does", "plays", "goes"], 0),
                C("He ___ the piano very well.", ["plays", "does", "goes"], 0),
                F("We often go ___ in the mountains. (на поход: hike)", "hiking"),
                T("Какво правиш в свободното си време?", "What do you do in your free time"),
            ],
        },
    ],
    "a1-speak-write": [
        {
            "slug": "a1-write-penpal", "title": "Пиши: първо писмо до нов приятел", "title_en": "Writing: to a new pen pal",
            "kind": "writing", "minutes": 7, "xp": 15, "summary": "Представи се: име, възраст, град, работа, хобита.",
            "theory": model_text("Hello from Bulgaria!", [
                "Hi Emma,",
                "My name is Viktor and I'm 28. I'm from Ruse, a city on the Danube in Bulgaria.",
                "I'm an engineer. In my free time I play basketball and I go cycling.",
                "What about you? What do you do in your free time?",
                "Write soon!",
                "Viktor",
            ], [("My name is... and I'm 28", "име и възраст"), ("I'm from..., a city...", "откъде си"),
                ("I'm an engineer.", "работа: a / an + професия"), ("In my free time I...", "хобита"),
                ("What about you?", "въпрос към приятеля")]),
            "exercises": [
                C("Аз съм инженер:", ["I'm an engineer.", "I'm engineer.", "I'm a engineer."], 0),
                C("Аз съм на 28:", ["I'm 28.", "I have 28.", "I'm 28 years."], 0),
                C("Добър въпрос в края:", ["What about you?", "Yours faithfully,", "Bye forever!"], 0),
                F("I'm ___ Ruse. (от)", "from"),
                W("Напиши кратко писмо до нов приятел: име, възраст, откъде си, работа, хобита и един въпрос.",
                  "Hi Leo, my name is Mila and I'm 24. I'm from Burgas, a city by the sea. I'm a teacher. In my free time I read books and I go swimming. What about you? Write soon! Mila",
                  ["Име и възраст (I'm..., не I have...)", "Откъде си", "Работа с a / an", "Хобита", "Въпрос в края"]),
            ],
        },
    ],
    # ---------------- A2 ----------------
    "a2-listening": [
        {
            "slug": "a2-listen-dentist", "title": "Записване на час при зъболекар", "title_en": "Booking a dentist appointment",
            "kind": "listening", "minutes": 7, "xp": 20, "summary": "Ден, час и какво да носиш: обаждане до клиника.", "theory": INTRO,
            "dialogue": dialogue(
                ("Receptionist", "Good morning, Smile Dental Clinic.", "Добро утро, дентална клиника „Смайл“."),
                ("Rosen", "Hello, I'd like to make an appointment, please. I've got a terrible toothache.", "Здравейте, бих искал да си запиша час, моля. Ужасно ме боли зъб."),
                ("Receptionist", "Oh dear. Are you a patient here already?", "Ох. Пациент ли сте вече при нас?"),
                ("Rosen", "No, it's my first time.", "Не, за първи път съм."),
                ("Receptionist", "OK. We have an appointment today at 4:30, or tomorrow at 9:00.", "Добре. Имаме час днес в 4:30 или утре в 9:00."),
                ("Rosen", "Today, please. The sooner the better.", "Днес, моля. Колкото по-скоро, толкова по-добре."),
                ("Receptionist", "Fine. Please come ten minutes early to fill in a form, and bring your ID.", "Добре. Елате десет минути по-рано, за да попълните формуляр, и носете лична карта."),
            ),
            "exercises": [
                C("Какъв е проблемът на Росен?", ["Боли го зъб", "Има температура", "Счупил си е ръката"], 0, instruction=DQ),
                C("Ходил ли е преди в клиниката?", ["Не, за първи път е", "Да, често", "Не се казва"], 0, instruction=DQ),
                C("Кой час избира?", ["Днес в 4:30", "Утре в 9:00", "Днес в 9:00"], 0, instruction=DQ),
                C("Защо трябва да дойде по-рано?", ["За да попълни формуляр", "За да плати", "За да изчака лекаря"], 0, instruction=DQ),
                L("Какво означава The sooner the better?", "The sooner the better.", ["Колкото по-скоро, толкова по-добре.", "По-добре по-късно.", "Скоро ще е по-добре."], 0),
                D("I'd like to make an appointment, please."),
                S("I've got a terrible toothache."),
            ],
        },
    ],
    "a2-skills": [
        {
            "slug": "a2-read-biography", "title": "Четене: кратка биография", "title_en": "Reading: a short biography",
            "kind": "reading", "minutes": 7, "xp": 20, "summary": "Умение: да следиш години и събития в живота на човек.",
            "theory": """<div class="tip"><strong>Умение: хронология.</strong> Биографиите са в Past Simple и подредени по години. Подчертай годините и какво се случва с всяка.</div>""" + reading("Vanga Kostova: the chef from the village", [
                "Vanga Kostova was born in a small village near Smolyan in 1975. As a child, she spent hours in the kitchen with her grandmother.",
                "In 1995 she moved to Sofia to study economics, but she never stopped cooking for her friends.",
                "In 2004 she left her job in a bank and opened a tiny restaurant with only six tables. People loved her traditional recipes.",
                "In 2016 she wrote a cookbook, and two years later it won a national prize. Today she has three restaurants.",
            ], [("as a child", "като дете"), ("moved", "премести се"), ("left her job", "напусна работата си"),
                ("tiny", "мъничък"), ("recipes", "рецепти"), ("won a prize", "спечели награда")]),
            "exercises": [
                C("Къде е родена Ванга?", ["В село край Смолян", "В София", "В Пловдив"], 0, instruction=RQ),
                C("Какво учи в София?", ["Икономика", "Готварство", "Право"], 0, instruction=RQ),
                C("Кога отваря първия си ресторант?", ["2004", "1995", "2016"], 0, instruction=RQ),
                C("Кога книгата ѝ печели награда?", ["2018", "2016", "2004"], 0, instruction=RQ),
                C("Колко ресторанта има днес?", ["Три", "Един", "Шест"], 0, instruction=RQ),
                F("She ___ (open) a restaurant in 2004.", "opened"),
            ],
        },
        {
            "slug": "a2-fit-suit-match", "title": "Fit, suit или match?", "title_en": "Fit, suit and match",
            "kind": "vocabulary", "minutes": 6, "xp": 20, "summary": "Става ли ми, отива ли ми: в магазина за дрехи.",
            "theory": """
<table>
<tr><th>Глагол</th><th>Значение</th><th>Пример</th></tr>
<tr><td class="en">fit</td><td>става ми (размерът е точен)</td><td class="en">These shoes don't fit. They're too small.</td></tr>
<tr><td class="en">suit</td><td>отива ми (изглеждам добре)</td><td class="en">Blue really suits you.</td></tr>
<tr><td class="en">match / go with</td><td>подхожда на (нещо друго)</td><td class="en">The bag matches your shoes.</td></tr>
<tr><td class="en">try on</td><td>пробвам</td><td class="en">Can I try this on?</td></tr>
</table>
<p>Полезни: <span class="en">the changing rooms</span> (пробните), <span class="en">a bigger / smaller size</span>, <span class="en">It's too tight / too loose</span> (тясно / широко).</p>
""",
            "exercises": [
                C("The jacket is the right size. It ___ me.", ["fits", "suits", "matches"], 0),
                C("That colour really ___ you. You look great!", ["suits", "fits", "tries"], 0),
                C("Does this belt ___ my shoes?", ["match", "fit", "suit"], 0),
                C("Може ли да го пробвам?", ["Can I try it on?", "Can I try on it?", "Can I fit it?"], 0),
                F("These jeans are too ___ . I need a bigger size. (тесни)", "tight|small"),
                T("Къде са пробните?", "Where are the changing rooms|Where are the fitting rooms"),
            ],
        },
    ],
    # ---------------- B1 ----------------
    "b1-skills": [
        {
            "slug": "b1-read-forum", "title": "Четене: мнения във форум", "title_en": "Reading: forum posts",
            "kind": "reading", "minutes": 8, "xp": 25, "summary": "Умение: да сравниш няколко мнения и да намериш кой какво мисли.",
            "theory": """<div class="tip"><strong>Умение: сравняване на мнения.</strong> Търси думите, които издават позиция: <span class="en">I'd recommend, the problem is, personally, it depends</span>. Отбележи за всеки човек: за, против или „зависи“.</div>""" + reading("Forum: Is it worth learning to drive in a big city?", [
                "Teo: Honestly, no. I live in London and I get everywhere by bike or tube. Parking alone would cost me a fortune.",
                "Hana: It depends where you work. My office is outside the city and the bus takes ninety minutes, so for me a car is essential.",
                "Marco: Learn anyway, even if you don't buy a car. You never know when you'll need it, for example on holiday or in an emergency.",
                "Joy: I learned at 35 and I wish I'd done it earlier. It's much harder when you're older and more nervous.",
            ], [("the tube", "лондонското метро"), ("a fortune", "цяло състояние"), ("essential", "необходим"),
                ("anyway", "все пак, въпреки това"), ("I wish I'd done it", "съжалявам, че не съм го направил")]),
            "exercises": [
                C("Кой е против да се учи шофиране?", ["Тео", "Марко", "Хана"], 0, instruction=RQ),
                C("Каква е позицията на Хана?", ["Зависи къде работиш", "Винаги е излишно", "Задължително е за всички"], 0, instruction=RQ),
                C("Защо Марко съветва да се учи?", ["Може да потрябва неочаквано", "Колите са евтини", "Метрото е скъпо"], 0, instruction=RQ),
                C("Какво съжалява Джой?", ["Че не се е научила по-рано", "Че е купила кола", "Че живее в Лондон"], 0, instruction=RQ),
                C("Кой дава аргумент за цената?", ["Тео", "Джой", "Марко"], 0, instruction=RQ),
                F("For me a car is ___ . (необходима)", "essential|necessary"),
            ],
        },
        {
            "slug": "b1-technology", "title": "Технологии в ежедневието", "title_en": "Everyday technology",
            "kind": "vocabulary", "minutes": 7, "xp": 25, "summary": "Charge, download, log in, back up: думите на телефона и компютъра.",
            "theory": """
<table>
<tr><th>Израз</th><th>Значение</th></tr>
<tr><td class="en">charge my phone / a charger</td><td>зареждам телефона / зарядно</td></tr>
<tr><td class="en">download / upload</td><td>свалям / качвам</td></tr>
<tr><td class="en">log in / log out</td><td>влизам / излизам (от профил)</td></tr>
<tr><td class="en">a password, reset my password</td><td>парола, сменям паролата (когато съм я забравил)</td></tr>
<tr><td class="en">back up my files</td><td>правя резервно копие</td></tr>
<tr><td class="en">update the app</td><td>обновявам приложението</td></tr>
<tr><td class="en">the battery is dead / flat</td><td>батерията е паднала</td></tr>
<tr><td class="en">no signal / bad connection</td><td>няма обхват / лоша връзка</td></tr>
</table>
<div class="tip">„Зареждам телефона“ е <span class="en">charge</span>, а не <em>load</em>. А Wi-Fi паролата е <span class="en">the Wi-Fi password</span>.</div>
""",
            "exercises": [
                C("My phone is dead. Can I ___ it here?", ["charge", "load", "fill"], 0),
                C("I forgot my password, so I need to ___ it.", ["reset", "back up", "download"], 0),
                C("You should ___ your photos in case you lose your phone.", ["back up", "log out", "charge"], 0),
                C("I can't call you. There's no ___ here.", ["signal", "battery", "password"], 0),
                F("Don't forget to log ___ when you use a public computer.", "out"),
                T("Каква е паролата за Wi-Fi?", "What's the Wi-Fi password|What is the Wi-Fi password|What's the wifi password"),
            ],
        },
    ],
    # ---------------- B2 ----------------
    "b2-skills": [
        {
            "slug": "b2-read-science", "title": "Четене: научнопопулярна статия", "title_en": "Reading: popular science",
            "kind": "reading", "minutes": 9, "xp": 30, "summary": "Умение: да различиш доказаното от възможното.",
            "theory": """<div class="tip"><strong>Умение: доказателства.</strong> Научните текстове различават <span class="en">shows / proves</span> (силно) от <span class="en">suggests / may / is linked to</span> (по-слабо). „Свързано с“ не значи „причинява“.</div>""" + reading("Is coffee good for you?", [
                "For decades, coffee was treated as a guilty pleasure. Today, a growing number of large studies suggest that moderate coffee drinkers, around three to four cups a day, may actually live slightly longer.",
                "However, researchers are careful to point out that these studies show a link, not a cause. People who drink coffee may also differ in other ways, for example in income or lifestyle.",
                "What is better established is that too much caffeine can disturb sleep and raise anxiety, especially in people who are sensitive to it.",
                "The sensible conclusion, then, is not that everyone should start drinking coffee, but that most coffee lovers have little reason to give it up.",
            ], [("a guilty pleasure", "удоволствие, за което се чувстваш виновен"), ("moderate", "умерен"),
                ("point out", "посочвам"), ("established", "доказан, утвърден"), ("disturb", "нарушава"),
                ("sensible", "разумен")]),
            "exercises": [
                C("Какво показват големите изследвания?", ["Връзка между умереното кафе и по-дълъг живот", "Че кафето удължава живота", "Че кафето е вредно"], 0, instruction=RQ),
                C("Защо учените са внимателни?", ["Връзката не е доказана причина", "Изследванията са малки", "Кафето е скъпо"], 0, instruction=RQ),
                C("Кое е по-добре доказано?", ["Твърде много кофеин нарушава съня", "Кафето лекува тревожност", "Три чаши са задължителни"], 0, instruction=RQ),
                C("Какъв е изводът?", ["Любителите на кафе нямат голяма причина да го спрат", "Всички трябва да пият кафе", "Кафето трябва да се забрани"], 0, instruction=RQ),
                C("Коя дума изразява най-голяма сигурност?", ["established", "suggest", "may"], 0),
            ],
        },
        {
            "slug": "b2-education", "title": "Образование и учене", "title_en": "Education vocabulary",
            "kind": "vocabulary", "minutes": 8, "xp": 30, "summary": "Degree, tuition fees, drop out: честа изпитна тема.",
            "theory": """
<table>
<tr><th>Израз</th><th>Значение</th></tr>
<tr><td class="en">a degree in law</td><td>диплома (висше образование) по право</td></tr>
<tr><td class="en">graduate from university</td><td>завършвам университет</td></tr>
<tr><td class="en">tuition fees</td><td>такси за обучение</td></tr>
<tr><td class="en">drop out (of)</td><td>прекъсвам, отказвам се от обучение</td></tr>
<tr><td class="en">resit / retake an exam</td><td>явявам се отново на изпит</td></tr>
<tr><td class="en">a scholarship</td><td>стипендия</td></tr>
<tr><td class="en">a lecture / a seminar</td><td>лекция / семинар</td></tr>
<tr><td class="en">lifelong learning</td><td>учене през целия живот</td></tr>
</table>
<div class="tip">Фалшив приятел: „абсолвент“ не е <span class="en">absolvent</span>, а <span class="en">graduate</span>. „Лектор“ в университет е <span class="en">lecturer</span>.</div>
""",
            "exercises": [
                C("She has a ___ in economics.", ["degree", "diploma of high", "graduate"], 0),
                C("He ___ from Sofia University in 2020.", ["graduated", "finished from", "absolved"], 0),
                C("I failed the exam, so I have to ___ it in September.", ["resit", "drop out", "graduate"], 0),
                C("She got a ___ , so she doesn't pay tuition fees.", ["scholarship", "lecture", "degree"], 0),
                F("He dropped ___ of university after one year.", "out"),
                C("Tuition fees са:", ["такси за обучение", "учебници", "стипендии"], 0),
            ],
        },
    ],
    "b2-complex-structures": [
        {
            "slug": "b2-in-case", "title": "In case, so that, in order to", "title_en": "Purpose and precaution",
            "kind": "grammar", "minutes": 7, "xp": 25, "summary": "За да... и в случай че...: два различни смисъла.",
            "theory": """
<table>
<tr><th>Израз</th><th>Значение</th><th>Пример</th></tr>
<tr><td class="en">in order to / so as to + глагол</td><td>за да (цел)</td><td class="en">I left early in order to catch the train.</td></tr>
<tr><td class="en">so that + изречение</td><td>за да (цел, с подлог и can/could/would)</td><td class="en">I left early so that I could catch the train.</td></tr>
<tr><td class="en">in case + сегашно време</td><td>в случай че (предпазна мярка)</td><td class="en">Take an umbrella in case it rains.</td></tr>
<tr><td class="en">if</td><td>ако (условие)</td><td class="en">If it rains, we'll stay home.</td></tr>
</table>
<div class="tip"><span class="en">Take an umbrella in case it rains</span> = вземи го сега, за всеки случай. <span class="en">Take an umbrella if it rains</span> = вземи го само ако вали. След <span class="en">in case</span> няма <span class="en">will</span>.</div>
""",
            "exercises": [
                C("Take some cash ___ the card machine doesn't work.", ["in case", "so that", "in order to"], 0),
                C("I spoke slowly ___ everyone could understand.", ["so that", "in case", "in order"], 0),
                C("She works at night ___ pay for her studies.", ["in order to", "so that", "in case"], 0),
                C("Write it down in case you ___ .", ["forget", "will forget", "would forget"], 0),
                F("I saved the file twice in ___ the computer crashed.", "case"),
                O("Ще ти дам номера си, в случай че имаш нужда от помощ.", "I'll give you my number in case you need help|I will give you my number in case you need help"),
            ],
        },
    ],
    "b2-speak-write": [
        {
            "slug": "b2-write-work-email", "title": "Пиши: имейл до колеги", "title_en": "Writing: an email to colleagues",
            "kind": "writing", "minutes": 9, "xp": 30, "summary": "Съобщи промяна ясно и учтиво: какво, защо, какво да направят.",
            "theory": model_text("Change to Friday's team meeting", [
                "Hi all,",
                "Just a quick update: Friday's team meeting has been moved from 10:00 to 14:00, as the client call in the morning has been rescheduled.",
                "The meeting will still be in Room 3, and we'll go through the new project timeline. Could you please send me any questions by Thursday evening, so that I can prepare answers?",
                "If the new time doesn't work for you, let me know and we'll find a solution.",
                "Thanks,",
                "Nadia",
            ], [("Just a quick update:", "ясно начало: какво се променя"),
                ("has been moved..., as...", "промяна и причина (Present Perfect, страдателен залог)"),
                ("Could you please... by Thursday?", "конкретна молба със срок"),
                ("If the new time doesn't work for you, let me know", "гъвкавост и учтивост"),
                ("Thanks,", "кратък край между колеги")]),
            "exercises": [
                C("Кое начало е най-ясно?", ["Just a quick update: the meeting has been moved to 2 pm.", "Hello, I hope you are all very well and having a nice week.", "Meeting. Change. 2 pm."], 0),
                C("Учтива молба със срок:", ["Could you please send me your questions by Thursday?", "Send questions now.", "Maybe questions?"], 0),
                C("Подходящ край между колеги:", ["Thanks,", "Yours faithfully,", "Love,"], 0),
                F("The meeting has ___ moved to Room 5.", "been"),
                W("Напиши кратък имейл до колегите: офисът ще бъде затворен в понеделник заради ремонт и всички работят от вкъщи.",
                  "Hi all, just a quick note: the office will be closed on Monday because of building repairs. Please work from home that day. All meetings will be online, and I'll send the links on Friday. Let me know if you have any problems. Thanks, Petar",
                  ["Какво се променя още в началото", "Причина", "Какво трябва да направят", "Кратък, ясен стил"]),
            ],
        },
    ],
    # ---------------- C1 ----------------
    "c1-skills": [
        {
            "slug": "c1-read-profile", "title": "Четене: портрет на човек", "title_en": "Reading: a magazine profile",
            "kind": "reading", "minutes": 10, "xp": 35, "summary": "Умение: да подредиш събития, разказани не по ред.",
            "theory": """<div class="tip"><strong>Умение: нелинеен разказ.</strong> Статиите-портрети често започват с драматичен момент и после се връщат назад. Следи сигналите за време: <span class="en">years earlier, by then, at the time, since then</span>.</div>""" + reading("The woman who mapped the river", [
                "When Irina Vasileva stepped onto the stage in Geneva to collect the award, few in the audience knew that she had once been told she would never work as a scientist.",
                "Years earlier, as a student in Ruse, she had been rejected by three research programmes. By then she had already spent every summer recording water levels on the Danube with equipment she had built herself.",
                "It was this stubborn, unpaid work that eventually caught the attention of an international team, which at the time was struggling to find reliable local data.",
                "Since then, her maps have been used to predict floods in four countries. Asked about her early rejections, she simply shrugs: 'They were probably right. I wasn't a scientist yet.'",
            ], [("collect the award", "получавам награда"), ("rejected", "отхвърлен"), ("stubborn", "упорит, инат"),
                ("caught the attention of", "привлече вниманието на"), ("struggling", "мъчеше се"),
                ("shrugs", "свива рамене")]),
            "exercises": [
                C("Кое се е случило най-рано?", ["Записва нивата на Дунав всяко лято", "Получава награда в Женева", "Картите ѝ предсказват наводнения"], 0, instruction=RQ),
                C("С какво започва статията?", ["С най-късното събитие: наградата", "С детството ѝ", "С отказите"], 0, instruction=RQ),
                C("Какво е привлякло международния екип?", ["Упоритата ѝ доброволна работа и данните", "Дипломата ѝ", "Препоръка от университета"], 0, instruction=RQ),
                C("Какво показва отговорът ѝ за отказите?", ["Скромност и самоирония", "Гняв", "Съжаление"], 0, instruction=RQ),
                C("Кой израз сочи по-ранно време?", ["By then", "Since then", "When... stepped onto the stage"], 0),
            ],
        },
        {
            "slug": "c1-academic-verbs", "title": "Глаголи за академичен текст", "title_en": "Academic reporting verbs",
            "kind": "vocabulary", "minutes": 8, "xp": 35, "summary": "Argue, imply, acknowledge, dismiss: точно какво прави авторът.",
            "theory": """
<table>
<tr><th>Глагол</th><th>Какво прави авторът</th><th>Пример</th></tr>
<tr><td class="en">argue / contend</td><td>защитава позиция</td><td class="en">She argues that cities should ban cars.</td></tr>
<tr><td class="en">claim / assert</td><td>твърди (без да е непременно доказано)</td><td class="en">He claims the method is faster.</td></tr>
<tr><td class="en">imply / suggest</td><td>намеква, внушава</td><td class="en">The data implies a link.</td></tr>
<tr><td class="en">acknowledge / concede</td><td>признава (слабост в своята позиция)</td><td class="en">She acknowledges that costs are high.</td></tr>
<tr><td class="en">dismiss / reject</td><td>отхвърля</td><td class="en">He dismisses the criticism as unfair.</td></tr>
<tr><td class="en">highlight / emphasise</td><td>подчертава</td><td class="en">The report highlights two risks.</td></tr>
</table>
<div class="tip">Изборът на глагол показва и <strong>твоята</strong> оценка: <span class="en">claims</span> звучи по-скептично от <span class="en">shows</span>.</div>
""",
            "exercises": [
                C("The author admits there are weaknesses. She ___ them.", ["acknowledges", "dismisses", "asserts"], 0),
                C("He says the critics are wrong and not worth discussing. He ___ them.", ["dismisses", "concedes", "implies"], 0),
                C("The results don't say it directly, but they ___ a connection.", ["imply", "dismiss", "acknowledge"], 0),
                C("Кой глагол звучи най-скептично?", ["claims", "shows", "demonstrates"], 0),
                F("The report ___ the need for more research. (подчертава)", "highlights|emphasises|emphasizes|stresses"),
                C("Concede означава:", ["признавам (неохотно)", "отричам", "обобщавам"], 0),
            ],
        },
    ],
    # ---------------- C2 ----------------
    "c2-skills": [
        {
            "slug": "c2-read-fallacies", "title": "Четене: логически грешки", "title_en": "Reading: spotting weak arguments",
            "kind": "reading", "minutes": 10, "xp": 40, "summary": "Умение: да откриеш къде убедителният текст „мами“.",
            "theory": """<div class="tip"><strong>Умение: критично четене.</strong> Чести логически грешки: <span class="en">false dilemma</span> (само два варианта), <span class="en">slippery slope</span> (едно води неизбежно до катастрофа), <span class="en">appeal to popularity</span> (всички го правят), <span class="en">ad hominem</span> (атака срещу човека, не срещу аргумента).</div>""" + reading("Why we must reject the new cycle lanes", [
                "Either we keep our roads for cars, or we accept that our city will grind to a halt. There is no middle ground.",
                "If we allow these lanes today, tomorrow it will be pedestrian zones, and within a decade nobody will be able to drive into the centre at all.",
                "Everyone I speak to agrees that the plan is absurd.",
                "And let us not forget that the councillor behind it does not even own a car, so she can hardly be trusted on transport.",
            ], [("grind to a halt", "спирам напълно, блокирам"), ("middle ground", "компромис, среден вариант"),
                ("absurd", "абсурден"), ("councillor", "общински съветник"), ("can hardly be trusted", "трудно може да ѝ се вярва")]),
            "exercises": [
                C("Абзац 1 (Either... or...) е пример за:", ["false dilemma", "ad hominem", "appeal to popularity"], 0, instruction=RQ),
                C("Абзац 2 (today lanes, tomorrow...) е пример за:", ["slippery slope", "false dilemma", "ad hominem"], 0, instruction=RQ),
                C("Абзац 3 (Everyone I speak to agrees) е пример за:", ["appeal to popularity", "slippery slope", "ad hominem"], 0, instruction=RQ),
                C("Абзац 4 (she does not own a car) е пример за:", ["ad hominem", "false dilemma", "appeal to popularity"], 0, instruction=RQ),
                C("Какво липсва в целия текст?", ["Конкретни доказателства за ефекта от алеите", "Емоции", "Ясна позиция"], 0, instruction=RQ),
            ],
        },
        {
            "slug": "c2-connotation", "title": "Конотация: slim, skinny или thin?", "title_en": "Connotation and near-synonyms",
            "kind": "vocabulary", "minutes": 8, "xp": 40, "summary": "Думи с едно значение, но различна оценка.",
            "theory": """
<p>Много английски думи означават почти едно и също, но носят <strong>положителна, неутрална или отрицателна</strong> оценка.</p>
<table>
<tr><th>Положително</th><th>Неутрално</th><th>Отрицателно</th></tr>
<tr><td class="en">slim</td><td class="en">thin</td><td class="en">skinny</td></tr>
<tr><td class="en">fragrance / scent</td><td class="en">smell</td><td class="en">stink / stench</td></tr>
<tr><td class="en">determined</td><td class="en">firm</td><td class="en">stubborn / pig-headed</td></tr>
<tr><td class="en">thrifty / economical</td><td class="en">careful with money</td><td class="en">stingy / mean</td></tr>
<tr><td class="en">confident</td><td class="en">self-assured</td><td class="en">arrogant</td></tr>
<tr><td class="en">inquisitive</td><td class="en">curious</td><td class="en">nosy</td></tr>
</table>
<div class="tip">В рецензии, препоръки и мотивационни писма изборът между <span class="en">determined</span> и <span class="en">stubborn</span> променя цялото внушение.</div>
""",
            "exercises": [
                C("Препоръка за кандидат: She is very ___ . (положително)", ["determined", "stubborn", "pig-headed"], 0),
                C("He keeps asking about my private life. He's so ___ .", ["nosy", "inquisitive", "curious"], 0),
                C("The perfume has a lovely ___ .", ["scent", "stink", "stench"], 0),
                C("Коя дума е най-негативна?", ["stingy", "thrifty", "economical"], 0),
                C("Neutral: She's very ___ . (не дебела, без оценка)", ["thin", "skinny", "slim"], 0),
                F("He's not confident, he's ___ : he thinks he's better than everyone. (арогантен)", "arrogant"),
            ],
        },
    ],
    "c2-speak-write": [
        {
            "slug": "c2-write-discursive", "title": "Пиши: дискурсивно есе", "title_en": "Writing: a discursive essay",
            "kind": "writing", "minutes": 10, "xp": 40, "summary": "Претегли две позиции безпристрастно и стигни до нюансирано заключение.",
            "theory": model_text("Should museums return objects to their countries of origin?", [
                "Few debates in the cultural world are as charged as the question of restitution.",
                "Advocates argue that many objects were acquired through conquest or coercion, and that their return is a matter of justice rather than generosity.",
                "Opponents counter that major museums make these works accessible to millions and preserve them to a standard some countries of origin cannot yet guarantee.",
                "Yet the two positions are less incompatible than they appear. Long-term loans, shared research and joint exhibitions suggest that ownership and access need not be a zero-sum game.",
            ], [("Few debates... are as charged as...", "силен, балансиран увод"),
                ("Advocates argue that...", "първата позиция, безпристрастно"),
                ("Opponents counter that...", "втората позиция"),
                ("Yet the two positions are less incompatible than they appear.", "нюансиран синтез вместо победител"),
                ("need not be a zero-sum game", "прецизна, академична формулировка")]) + """
<div class="tip">За разлика от есето с позиция, дискурсивното есе представя двете страни справедливо и често завършва със синтез, а не с „победител“.</div>
""",
            "exercises": [
                C("Каква е целта на дискурсивното есе?", ["Да претегли позициите безпристрастно", "Да убеди с всички средства", "Да разкаже история"], 0),
                C("Opponents counter that... служи за:", ["въвеждане на противоположната позиция", "заключение", "пример"], 0),
                C("A zero-sum game означава:", ["ситуация, в която печалбата на един е загуба за друг", "игра без правила", "безполезен спор"], 0),
                F("___ argue that the objects should be returned. (Привържениците)", "Advocates|Supporters|Proponents"),
                W("Напиши два абзаца от дискурсивно есе: Трябва ли изкуственият интелект да се използва за оценяване на изпити? Представи двете страни безпристрастно.",
                  "Advocates argue that AI marking would be faster and more consistent, freeing teachers to teach. Opponents counter that algorithms struggle with originality and may reproduce hidden biases. Yet the two views need not exclude each other: AI could flag patterns while humans give final grades.",
                  ["Двете позиции, представени честно", "Advocates argue / Opponents counter", "Синтез вместо победител", "Предпазлив, академичен стил"]),
            ],
        },
    ],
}

MISTAKES = {
    "a1-was-born": [
        ("I am born in 1990.", "I was born in 1990.", "Роден съм: was born."),
    ],
    "a1-hobbies": [
        ("I play yoga.", "I do yoga.", "Yoga, karate: do."),
        ("I go to swimming.", "I go swimming.", "Go + -ing, без to."),
    ],
    "a1-write-penpal": [
        ("I'm engineer.", "I'm an engineer.", "Професия: a / an."),
        ("I have 28 years.", "I'm 28.", "Възраст: to be."),
    ],
    "a2-fit-suit-match": [
        ("This colour fits you.", "This colour suits you.", "Отива ти: suit. Размер: fit."),
        ("Can I try on it?", "Can I try it on?", "Местоимението е между try и on."),
    ],
    "b1-technology": [
        ("I need to load my phone.", "I need to charge my phone.", "Зареждам батерия: charge."),
    ],
    "b2-education": [
        ("I finished from university.", "I graduated from university.", "Завършвам университет: graduate from."),
        ("He is an absolvent.", "He is a graduate.", "Абсолвент: graduate."),
    ],
    "b2-in-case": [
        ("Take a coat in case it will be cold.", "Take a coat in case it's cold.", "След in case: сегашно време."),
    ],
    "c1-academic-verbs": [
        ("The study proves that coffee may help.", "The study suggests that coffee may help.", "May е предпазливо: suggests, не proves."),
    ],
}
