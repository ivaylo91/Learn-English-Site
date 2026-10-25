"""Starter course content. Loaded by `manage.py seed_content`; safe to run repeatedly."""


def C(prompt, choices, correct, explanation="", instruction="Избери правилния отговор"):
    return {"type": "choice", "instruction": instruction, "prompt": prompt,
            "choices": choices, "correct": correct, "explanation": explanation}


def F(prompt, answers, explanation="", instruction="Попълни празното място"):
    return {"type": "fill", "instruction": instruction, "prompt": prompt, "answers": answers, "explanation": explanation}


def T(prompt, answers, explanation="", instruction="Преведи на английски"):
    return {"type": "translate", "instruction": instruction, "prompt": prompt, "answers": answers,
            "explanation": explanation}


def L(prompt, audio, choices, correct, explanation="", instruction="Слушай и избери"):
    """Listening choice: the learner hears `audio`, then answers `prompt`."""
    return {**C(prompt, choices, correct, explanation, instruction), "audio": audio}


def D(audio, answers="", explanation="", instruction="Диктовка"):
    """Dictation: the learner hears `audio` and types it. Extra accepted variants go in answers."""
    return {"type": "dictation", "instruction": instruction, "prompt": "Слушай и напиши изречението.",
            "audio": audio, "answers": "|".join(a for a in [audio, answers] if a), "explanation": explanation}


LEVELS = [
    {"code": "A1", "title": "Начинаещи", "order": 1,
     "summary": "Първите думи и изречения: поздрави, числа, глаголът to be.",
     "description": "За пълни начинаещи. Ще се научиш да се представяш, да броиш, да говориш за себе си и "
                    "ежедневието си с прости изречения."},
    {"code": "A2", "title": "Основно ниво", "order": 2,
     "summary": "Ежедневни ситуации, минало време, пазаруване и пътуване.",
     "description": "Разказваш какво се е случило, питаш за посока, поръчваш в ресторант и се справяш с "
                    "типичните ситуации при пътуване."},
    {"code": "B1", "title": "Средно ниво", "order": 3,
     "summary": "Свободни разговори по познати теми, мнения и планове.",
     "description": "Изразяваш мнение, разказваш за опит, даваш съвети и говориш за бъдещи планове."},
    {"code": "B2", "title": "Над средното", "order": 4,
     "summary": "Сложни текстове, дискусии и уверено писане.",
     "description": "Разбираш статии и филми без превод, спориш аргументирано и пишеш ясни текстове."},
    {"code": "C1", "title": "Напреднали", "order": 5,
     "summary": "Гъвкав и точен език за работа и учене.",
     "description": "Използваш английски свободно в професионална и академична среда."},
    {"code": "C2", "title": "Владеене", "order": 6,
     "summary": "Нюанси, идиоми и език почти като на роден говорител.",
     "description": "Разбираш почти всичко и се изразяваш прецизно, с богат речник и стил."},
]


UNITS = [
    # ---------------- A1 ----------------
    {
        "level": "A1", "title": "Първи стъпки", "slug": "a1-first-steps", "icon": "fa-hand", "order": 1,
        "summary": "Поздрави, глаголът to be и числата.",
        "lessons": [
            {
                "slug": "a1-greetings", "title": "Поздрави и запознанство", "title_en": "Greetings and introductions",
                "kind": "conversation", "minutes": 5, "xp": 10,
                "summary": "Как да поздравиш, да се представиш и да попиташ как е някой.",
                "theory": """
<p>Първото, което ще ти трябва навсякъде: да поздравиш и да кажеш кой си.</p>
<h3>Поздрави</h3>
<table>
<tr><th>Английски</th><th>Български</th><th>Кога</th></tr>
<tr><td class="en">Hello / Hi</td><td>Здравей / Здрасти</td><td>по всяко време; <span class="en">Hi</span> е по-неофициално</td></tr>
<tr><td class="en">Good morning</td><td>Добро утро</td><td>до обяд</td></tr>
<tr><td class="en">Good afternoon</td><td>Добър ден</td><td>от обяд до около 18 ч.</td></tr>
<tr><td class="en">Good evening</td><td>Добър вечер</td><td>вечер, при среща</td></tr>
<tr><td class="en">Goodbye / Bye</td><td>Довиждане / Чао</td><td>при раздяла</td></tr>
</table>
<div class="tip"><strong>Внимание:</strong> <span class="en">Good night</span> не е поздрав при среща. Казва се само при раздяла вечер или преди лягане (Лека нощ).</div>
<h3>Представяне</h3>
<ul>
<li><span class="en">My name is Maria.</span> Казвам се Мария.</li>
<li><span class="en">I'm Maria.</span> Аз съм Мария.</li>
<li><span class="en">Nice to meet you.</span> Приятно ми е.</li>
<li><span class="en">Where are you from?</span> Откъде си? <span class="en">I'm from Bulgaria.</span> От България съм.</li>
</ul>
<h3>Как си?</h3>
<p><span class="en">How are you?</span> Отговорът обикновено е кратък: <span class="en">I'm fine, thanks. And you?</span> (Добре съм, благодаря. А ти?)</p>
""",
                "exercises": [
                    C("Как ще поздравиш някого в 9 сутринта?", ["Good morning", "Good night", "Good evening"], 0,
                      "Good morning се използва до обяд."),
                    C("Кое НЕ е поздрав при среща?", ["Hello", "Good night", "Good afternoon"], 1,
                      "Good night казваме само при раздяла вечер."),
                    F("My ___ is Peter.", "name", "My name is ... означава „Казвам се ...“."),
                    C("„Приятно ми е“ на английски е:", ["Nice to meet you", "See you later", "How are you?"], 0),
                    F("I'm ___ Bulgaria.", "from", "Откъде си: I'm from + държава."),
                    T("Добре съм, благодаря.", "I'm fine thanks|I am fine thanks|I'm fine thank you|I am fine thank you|I'm good thanks|I am good thanks",
                      "Може и I'm good, thanks."),
                ],
            },
            {
                "slug": "a1-verb-to-be", "title": "Глаголът to be", "title_en": "The verb to be",
                "kind": "grammar", "minutes": 7, "xp": 15,
                "summary": "Аз съм, ти си, той е: най-важният глагол в английския.",
                "theory": """
<p>Глаголът <span class="en">to be</span> означава „съм“. За разлика от българския, в английския <strong>подлогът винаги се казва</strong>: не може само „<em>am a student</em>“, а <span class="en">I am a student</span>.</p>
<h3>Форми</h3>
<table>
<tr><th>Пълна форма</th><th>Кратка форма</th><th>Български</th></tr>
<tr><td class="en">I am</td><td class="en">I'm</td><td>аз съм</td></tr>
<tr><td class="en">you are</td><td class="en">you're</td><td>ти си / вие сте</td></tr>
<tr><td class="en">he / she / it is</td><td class="en">he's / she's / it's</td><td>той / тя / то е</td></tr>
<tr><td class="en">we are</td><td class="en">we're</td><td>ние сме</td></tr>
<tr><td class="en">they are</td><td class="en">they're</td><td>те са</td></tr>
</table>
<div class="tip"><span class="en">You</span> е едновременно „ти“ и „вие“. В английския няма учтива форма с отделна дума.</div>
<h3>Отрицание</h3>
<p>Добавяме <span class="en">not</span> след глагола: <span class="en">I am not tired.</span> <span class="en">She isn't at home.</span> <span class="en">They aren't students.</span></p>
<h3>Въпрос</h3>
<p>Глаголът отива пред подлога: <span class="en">Are you ready?</span> <span class="en">Is he a doctor?</span> Кратък отговор: <span class="en">Yes, I am.</span> / <span class="en">No, he isn't.</span></p>
""",
                "exercises": [
                    C("I ___ a teacher.", ["am", "is", "are"], 0, "С I използваме am."),
                    C("She ___ from Sofia.", ["am", "is", "are"], 1, "С he, she и it използваме is."),
                    C("They ___ my friends.", ["is", "am", "are"], 2, "С we, you и they използваме are."),
                    F("We ___ at home.", "are|'re", "We are, кратко we're."),
                    C("Кое е правилното отрицание?", ["He not is tired.", "He isn't tired.", "He aren't tired."], 1,
                      "Not идва след is: he is not = he isn't."),
                    C("Кой въпрос е правилен?", ["You are a student?", "Are you a student?", "Is you a student?"], 1,
                      "Във въпроса глаголът е пред подлога."),
                    T("Аз съм от България.", "I am from Bulgaria|I'm from Bulgaria"),
                    T("Тя е лекар.", "She is a doctor|She's a doctor",
                      "Пред професия в единствено число слагаме a или an."),
                ],
            },
            {
                "slug": "a1-numbers", "title": "Числата от 1 до 20", "title_en": "Numbers 1 to 20",
                "kind": "vocabulary", "minutes": 5, "xp": 10,
                "summary": "Брои, казвай възрастта си и телефонни номера.",
                "theory": """
<table>
<tr><th>1-10</th><th>11-20</th></tr>
<tr><td><span class="en">one, two, three, four, five</span></td><td><span class="en">eleven, twelve, thirteen, fourteen, fifteen</span></td></tr>
<tr><td><span class="en">six, seven, eight, nine, ten</span></td><td><span class="en">sixteen, seventeen, eighteen, nineteen, twenty</span></td></tr>
</table>
<div class="tip">От 13 до 19 числата завършват на <strong>-teen</strong> и ударението е в края: thir<strong>TEEN</strong>. Десетиците (30, 40...) завършват на <strong>-ty</strong> с ударение в началото: <strong>THIR</strong>ty. Така се различават 13 и 30.</div>
<h3>Възраст</h3>
<p><span class="en">How old are you?</span> На колко години си? <span class="en">I'm twenty.</span> На двайсет съм.</p>
<p>Обърни внимание: казваме <span class="en">I am 20</span>, с глагола <em>to be</em>, а не „имам 20 години“.</p>
""",
                "exercises": [
                    C("Как е 12 на английски?", ["twenty", "twelve", "eleven"], 1),
                    C("Кое число е fifteen?", ["50", "15", "5"], 1, "Fif-teen завършва на -teen, значи е между 13 и 19."),
                    F("Seven + three = ___", "ten|10"),
                    C("How old are you?", ["I have twenty years.", "I'm twenty.", "I'm twenty years."], 1,
                      "Възрастта се казва с to be: I'm twenty (years old)."),
                    F("Eight, nine, ___, eleven", "ten"),
                    T("На осемнайсет години съм.", "I am eighteen|I'm eighteen|I am eighteen years old|I'm eighteen years old|I'm 18|I am 18"),
                ],
            },
        ],
    },
    {
        "level": "A1", "title": "Аз и светът около мен", "slug": "a1-my-world", "icon": "fa-house-user", "order": 2,
        "summary": "Членове, множествено число и ежедневие в сегашно време.",
        "lessons": [
            {
                "slug": "a1-articles", "title": "Членове a, an и the", "title_en": "Articles: a, an, the",
                "kind": "grammar", "minutes": 7, "xp": 15,
                "summary": "Кога казваме a, кога an и кога the.",
                "theory": """
<p>В българския членът е в края на думата (кола<strong>та</strong>). В английския е отделна дума пред съществителното.</p>
<h3>A и an: неопределен член</h3>
<p>Означава „един“, „някакъв“. Използва се само за едно нещо, което се брои.</p>
<ul>
<li><span class="en">a</span> пред съгласен <strong>звук</strong>: <span class="en">a car, a book, a university</span></li>
<li><span class="en">an</span> пред гласен <strong>звук</strong>: <span class="en">an apple, an hour, an umbrella</span></li>
</ul>
<div class="tip">Важи звукът, а не буквата. <span class="en">Hour</span> започва с „ау“, затова е <span class="en">an hour</span>. <span class="en">University</span> започва с „ю“, затова е <span class="en">a university</span>.</div>
<h3>The: определен член</h3>
<p>Като нашето „-та, -то, -ът“. Използваме го, когато е ясно за кое нещо говорим: <span class="en">I have a dog. The dog is black.</span> (Имам куче. Кучето е черно.)</p>
<p>Също за единствени неща: <span class="en">the sun, the sea, the capital</span>.</p>
""",
                "exercises": [
                    C("I have ___ apple.", ["a", "an", "the"], 1, "Apple започва с гласен звук."),
                    C("She is ___ engineer.", ["a", "an"], 1, "Engineer започва с гласен звук."),
                    C("It takes ___ hour.", ["a", "an"], 1, "H в hour не се чете, думата започва с „ау“."),
                    C("He studies at ___ university.", ["a", "an"], 0, "University започва със звук „ю“, който е съгласен."),
                    F("I see a cat. ___ cat is white.", "the", "Вече знаем за коя котка говорим, затова the."),
                    C("Look at ___ sun!", ["a", "the"], 1, "Слънцето е само едно."),
                    T("Имам една кола.", "I have a car|I've got a car|I have got a car"),
                ],
            },
            {
                "slug": "a1-plural-nouns", "title": "Множествено число", "title_en": "Plural nouns",
                "kind": "grammar", "minutes": 6, "xp": 10,
                "summary": "Една книга, две книги: правила и изключения.",
                "theory": """
<h3>Основно правило: + s</h3>
<p><span class="en">book, books</span>, <span class="en">car, cars</span>, <span class="en">friend, friends</span></p>
<h3>Особени случаи</h3>
<table>
<tr><th>Окончание</th><th>Правило</th><th>Пример</th></tr>
<tr><td>-s, -sh, -ch, -x</td><td>+ es</td><td class="en">bus, buses; box, boxes</td></tr>
<tr><td>съгласна + y</td><td>y става ies</td><td class="en">city, cities</td></tr>
<tr><td>гласна + y</td><td>+ s</td><td class="en">day, days</td></tr>
<tr><td>-f, -fe</td><td>често ves</td><td class="en">knife, knives</td></tr>
</table>
<h3>Неправилни</h3>
<p><span class="en">man, men</span>; <span class="en">woman, women</span>; <span class="en">child, children</span>; <span class="en">person, people</span>; <span class="en">foot, feet</span>; <span class="en">tooth, teeth</span>.</p>
<div class="tip">В множествено число не слагаме a/an: <span class="en">I have two cats</span>, а не <em>two a cats</em>.</div>
""",
                "exercises": [
                    F("one bus, two ___", "buses"),
                    F("one city, three ___", "cities"),
                    C("Множественото число на child е:", ["childs", "children", "childrens"], 1),
                    C("Множественото число на day е:", ["days", "daies", "dayes"], 0, "Гласна + y: просто добавяме s."),
                    F("one man, five ___", "men"),
                    T("Имам две сестри.", "I have two sisters|I've got two sisters|I have got two sisters"),
                ],
            },
            {
                "slug": "a1-present-simple", "title": "Present Simple: ежедневие", "title_en": "Present Simple",
                "kind": "grammar", "minutes": 8, "xp": 15,
                "summary": "Говорим за навици, работа и неща, които са верни винаги.",
                "theory": """
<p>Present Simple е за неща, които се случват <strong>редовно</strong> или са <strong>винаги</strong> верни: <span class="en">I work in an office.</span> <span class="en">Water boils at 100 degrees.</span></p>
<h3>Утвърдително</h3>
<p>Глаголът е в основна форма, но с <strong>he, she, it</strong> добавяме <strong>-s</strong>:</p>
<ul>
<li><span class="en">I / you / we / they work</span></li>
<li><span class="en">he / she / it works</span></li>
</ul>
<div class="tip">Това -s е най-честата грешка. Запомни: <span class="en">She live<strong>s</strong> in Varna.</span> <span class="en">My brother play<strong>s</strong> football.</span></div>
<h3>Отрицание и въпрос с do / does</h3>
<table>
<tr><th></th><th>I, you, we, they</th><th>he, she, it</th></tr>
<tr><td>Отрицание</td><td class="en">I don't like coffee.</td><td class="en">She doesn't like coffee.</td></tr>
<tr><td>Въпрос</td><td class="en">Do you like coffee?</td><td class="en">Does she like coffee?</td></tr>
</table>
<p>Когато има <span class="en">does</span>, главният глагол губи -s: <span class="en">Does he work?</span>, а не <em>Does he works?</em></p>
<h3>Думи за честота</h3>
<p><span class="en">always</span> (винаги), <span class="en">usually</span> (обикновено), <span class="en">often</span> (често), <span class="en">sometimes</span> (понякога), <span class="en">never</span> (никога). Стоят пред глагола: <span class="en">I usually drink tea.</span></p>
""",
                "exercises": [
                    C("She ___ in London.", ["live", "lives", "living"], 1, "С she добавяме -s."),
                    C("I ___ coffee every morning.", ["drink", "drinks"], 0),
                    F("He ___ (work) in a bank.", "works"),
                    C("Кое отрицание е правилно?", ["He don't like fish.", "He doesn't like fish.", "He doesn't likes fish."], 1,
                      "С he използваме doesn't, а глаголът е без -s."),
                    C("___ you speak English?", ["Do", "Does", "Are"], 0),
                    C("Does your sister ___ meat?", ["eat", "eats", "eating"], 0, "След does глаголът е в основна форма."),
                    F("We never ___ (watch) TV in the morning.", "watch"),
                    T("Той не пие кафе.", "He doesn't drink coffee|He does not drink coffee"),
                ],
            },
        ],
    },
    # ---------------- A2 ----------------
    {
        "level": "A2", "title": "Минали събития", "slug": "a2-past-events", "icon": "fa-clock-rotate-left", "order": 1,
        "summary": "Разказваме какво е станало вчера, миналата седмица, миналата година.",
        "lessons": [
            {
                "slug": "a2-was-were", "title": "Минало време на to be: was и were", "title_en": "Past of to be",
                "kind": "grammar", "minutes": 6, "xp": 15,
                "summary": "Бях, беше, бяхме: как се казва на английски.",
                "theory": """
<table>
<tr><th>Подлог</th><th>Минало време</th><th>Пример</th></tr>
<tr><td class="en">I / he / she / it</td><td class="en">was</td><td class="en">I was tired yesterday.</td></tr>
<tr><td class="en">you / we / they</td><td class="en">were</td><td class="en">They were at the beach.</td></tr>
</table>
<p>Отрицание: <span class="en">wasn't / weren't</span>. Въпрос: <span class="en">Were you at home? Was it expensive?</span></p>
<div class="tip">Полезни изрази за минало: <span class="en">yesterday</span> (вчера), <span class="en">last night</span> (снощи), <span class="en">last week</span> (миналата седмица), <span class="en">two days ago</span> (преди два дни).</div>
""",
                "exercises": [
                    C("I ___ at home last night.", ["was", "were"], 0),
                    C("They ___ in Greece last summer.", ["was", "were"], 1),
                    F("The film ___ very good.", "was"),
                    C("___ you at work yesterday?", ["Was", "Were"], 1),
                    F("We ___ (not) late. We were on time.", "weren't|were not"),
                    T("Вчера беше студено.", "It was cold yesterday|Yesterday it was cold|Yesterday was cold",
                      "За времето използваме it: it was cold."),
                ],
            },
            {
                "slug": "a2-past-simple-regular", "title": "Past Simple: правилни глаголи", "title_en": "Past Simple: regular verbs",
                "kind": "grammar", "minutes": 7, "xp": 15,
                "summary": "Окончанието -ed и въпроси с did.",
                "theory": """
<p>За завършени действия в миналото добавяме <strong>-ed</strong>: <span class="en">work, worked</span>; <span class="en">play, played</span>; <span class="en">visit, visited</span>.</p>
<h3>Правопис</h3>
<ul>
<li>завършва на -e: само <strong>-d</strong>: <span class="en">live, lived</span></li>
<li>съгласна + y: <strong>-ied</strong>: <span class="en">study, studied</span></li>
<li>кратка сричка: удвояваме: <span class="en">stop, stopped</span></li>
</ul>
<h3>Отрицание и въпрос с did</h3>
<p>Формата е еднаква за всички лица: <span class="en">I didn't work.</span> <span class="en">She didn't call.</span> <span class="en">Did you watch the match?</span></p>
<div class="tip">След <span class="en">did</span> и <span class="en">didn't</span> глаголът е в основна форма: <span class="en">Did you visit?</span>, а не <em>Did you visited?</em></div>
""",
                "exercises": [
                    F("Yesterday I ___ (watch) a film.", "watched"),
                    F("She ___ (study) English last year.", "studied"),
                    F("We ___ (stop) at a café.", "stopped"),
                    C("Кое е правилно?", ["Did you called him?", "Did you call him?", "Do you called him?"], 1),
                    C("He ___ like the food.", ["didn't", "doesn't liked", "not"], 0),
                    T("Посетихме Лондон миналата година.", "We visited London last year|Last year we visited London"),
                ],
            },
            {
                "slug": "a2-irregular-verbs", "title": "Най-честите неправилни глаголи", "title_en": "Common irregular verbs",
                "kind": "vocabulary", "minutes": 8, "xp": 15,
                "summary": "Go, went; see, saw: глаголите, които трябва да запомниш.",
                "theory": """
<p>Около 150 глагола не следват правилото с -ed. Ето най-нужните за начало:</p>
<table>
<tr><th>Основна форма</th><th>Минало</th><th>Значение</th></tr>
<tr><td class="en">go</td><td class="en">went</td><td>отивам</td></tr>
<tr><td class="en">have</td><td class="en">had</td><td>имам</td></tr>
<tr><td class="en">see</td><td class="en">saw</td><td>виждам</td></tr>
<tr><td class="en">eat</td><td class="en">ate</td><td>ям</td></tr>
<tr><td class="en">buy</td><td class="en">bought</td><td>купувам</td></tr>
<tr><td class="en">take</td><td class="en">took</td><td>вземам</td></tr>
<tr><td class="en">make</td><td class="en">made</td><td>правя</td></tr>
<tr><td class="en">come</td><td class="en">came</td><td>идвам</td></tr>
<tr><td class="en">get</td><td class="en">got</td><td>получавам, ставам</td></tr>
<tr><td class="en">find</td><td class="en">found</td><td>намирам</td></tr>
</table>
<div class="tip">В отрицание и въпрос пак използваме did + основна форма: <span class="en">I didn't go.</span> <span class="en">Did you see it?</span></div>
""",
                "exercises": [
                    F("Last summer we ___ (go) to Italy.", "went"),
                    F("I ___ (buy) a new phone yesterday.", "bought"),
                    C("Минало време на see е:", ["seed", "saw", "seen"], 1, "Seen е причастие, ще го учим по-късно."),
                    F("She ___ (eat) pizza for dinner.", "ate"),
                    C("Did you ___ the bus?", ["took", "take", "taked"], 1),
                    T("Намерих ключовете си.", "I found my keys"),
                ],
            },
        ],
    },
    {
        "level": "A2", "title": "На път", "slug": "a2-on-the-road", "icon": "fa-suitcase-rolling", "order": 2,
        "summary": "Разговори, които ще проведеш при всяко пътуване.",
        "lessons": [
            {
                "slug": "a2-asking-directions", "title": "Как да попиташ за посока", "title_en": "Asking for directions",
                "kind": "conversation", "minutes": 6, "xp": 15,
                "summary": "Учтиви въпроси и как да разбереш отговора.",
                "theory": """
<h3>Учтиво започване</h3>
<p><span class="en">Excuse me, ...</span> (Извинете, ...) е най-добрият начин да заговориш непознат.</p>
<ul>
<li><span class="en">Excuse me, where is the train station?</span> Извинете, къде е гарата?</li>
<li><span class="en">How do I get to the museum?</span> Как да стигна до музея?</li>
<li><span class="en">Is it far from here?</span> Далече ли е оттук?</li>
<li><span class="en">Is there a pharmacy near here?</span> Има ли аптека наблизо?</li>
</ul>
<h3>Какво ще чуеш</h3>
<table>
<tr><th>Английски</th><th>Български</th></tr>
<tr><td class="en">Go straight on.</td><td>Вървете направо.</td></tr>
<tr><td class="en">Turn left / right.</td><td>Завийте наляво / надясно.</td></tr>
<tr><td class="en">It's on your left.</td><td>Отляво ви е.</td></tr>
<tr><td class="en">It's next to the bank.</td><td>До банката е.</td></tr>
<tr><td class="en">It's opposite the park.</td><td>Срещу парка е.</td></tr>
<tr><td class="en">It's a five-minute walk.</td><td>На пет минути пеша е.</td></tr>
</table>
<div class="tip">Ако не разбереш: <span class="en">Sorry, could you say that again, please?</span> или <span class="en">Could you speak more slowly, please?</span></div>
""",
                "exercises": [
                    C("Как учтиво да заговориш непознат?", ["Hey you!", "Excuse me, ...", "Listen!"], 1),
                    C("„Завийте надясно“ е:", ["Turn right.", "Go right on.", "It's on the right."], 0),
                    F("How do I ___ to the airport?", "get"),
                    C("It's opposite the park. Къде е?", ["До парка", "Срещу парка", "Зад парка"], 1),
                    F("Is it ___ from here? No, it's very close.", "far"),
                    T("Извинете, къде е гарата?", "Excuse me where is the station|Excuse me where is the train station|Excuse me where's the station|Excuse me where's the train station"),
                ],
            },
            {
                "slug": "a2-at-the-restaurant", "title": "В ресторанта", "title_en": "At the restaurant",
                "kind": "conversation", "minutes": 6, "xp": 15,
                "summary": "Резервация, поръчка и сметка.",
                "theory": """
<h3>Учтиво поръчване</h3>
<p>Вместо <em>I want</em> (звучи грубо), казвай <span class="en">I'd like ...</span> (Бих искал/искала ...) или <span class="en">Can I have ...?</span></p>
<ul>
<li><span class="en">A table for two, please.</span> Маса за двама, моля.</li>
<li><span class="en">Can I see the menu, please?</span> Може ли менюто?</li>
<li><span class="en">I'd like the chicken salad.</span> Ще взема салатата с пиле.</li>
<li><span class="en">Could we have some water, please?</span> Може ли малко вода?</li>
<li><span class="en">Can we have the bill, please?</span> Може ли сметката? (в САЩ: <span class="en">the check</span>)</li>
</ul>
<h3>Какво ще те попитат</h3>
<p><span class="en">Are you ready to order?</span> Готови ли сте да поръчате? <span class="en">Anything to drink?</span> Нещо за пиене? <span class="en">Is everything OK?</span> Всичко наред ли е?</p>
<div class="tip">Бакшиш е <span class="en">tip</span>. В Обединеното кралство и САЩ често е 10-20%. Понякога вече е включен в сметката като <span class="en">service charge</span>.</div>
""",
                "exercises": [
                    C("Най-учтивият начин да поръчаш е:", ["I want a coffee.", "Give me a coffee.", "I'd like a coffee, please."], 2),
                    F("A table ___ two, please.", "for"),
                    C("Във Великобритания сметката е:", ["the bill", "the account", "the note"], 0),
                    F("Can I ___ the menu, please?", "see|have"),
                    C("Are you ready to order? означава:", ["Платихте ли?", "Готови ли сте да поръчате?", "Имате ли резервация?"], 1),
                    T("Може ли сметката, моля?", "Can we have the bill please|Can I have the bill please|Could we have the bill please|Could I have the bill please|The bill please|Can I get the bill please|Can we get the bill please"),
                ],
            },
        ],
    },
    # ---------------- B1 ----------------
    {
        "level": "B1", "title": "Опит и съвети", "slug": "b1-experience-advice", "icon": "fa-lightbulb", "order": 1,
        "summary": "Present Perfect и модалните глаголи за съвет и задължение.",
        "lessons": [
            {
                "slug": "b1-present-perfect", "title": "Present Perfect: имал ли си опит?", "title_en": "Present Perfect",
                "kind": "grammar", "minutes": 9, "xp": 20,
                "summary": "Have you ever...? Разликата с Past Simple.",
                "theory": """
<p>Present Perfect свързва миналото с настоящето. Образува се с <span class="en">have / has + минало причастие</span>: <span class="en">I have visited Paris.</span> <span class="en">She has finished.</span></p>
<h3>Кога се използва</h3>
<ul>
<li><strong>Житейски опит</strong>, без да казваме кога: <span class="en">Have you ever been to Japan?</span> <span class="en">I've never tried sushi.</span></li>
<li><strong>Резултат сега</strong>: <span class="en">I've lost my keys.</span> (и сега не мога да вляза)</li>
<li><strong>От минало до сега</strong> с <span class="en">for</span> и <span class="en">since</span>: <span class="en">I've lived here for five years / since 2020.</span></li>
</ul>
<h3>Present Perfect или Past Simple?</h3>
<table>
<tr><th>Present Perfect</th><th>Past Simple</th></tr>
<tr><td>няма конкретно време</td><td>има конкретно минало време</td></tr>
<tr><td class="en">I've been to London.</td><td class="en">I went to London in 2019.</td></tr>
</table>
<div class="tip">С <span class="en">yesterday, last year, in 2019, ago</span> никога не използваме Present Perfect.</div>
""",
                "exercises": [
                    C("___ you ever been to Spain?", ["Did", "Have", "Has"], 1),
                    C("She ___ her homework. Now she can relax.", ["has finished", "finished yesterday", "have finished"], 0),
                    C("I ___ to Rome in 2018.", ["have been", "went", "have gone"], 1, "Има конкретно минало време (2018), затова Past Simple."),
                    F("I've lived here ___ 2015.", "since", "Since + начална точка, for + период."),
                    F("We've known each other ___ ten years.", "for"),
                    C("Кое изречение е грешно?", ["I've seen that film.", "I've seen that film yesterday.", "I saw that film yesterday."], 1),
                    T("Той никога не е бил в Америка.", "He has never been to America|He's never been to America|He has never been to the USA|He's never been to the USA|He has never been to the US|He's never been to the US",
                      "Ever/never + been to за място, където си ходил."),
                ],
            },
            {
                "slug": "b1-modals-advice", "title": "Should, must и have to", "title_en": "Modals: advice and obligation",
                "kind": "grammar", "minutes": 8, "xp": 20,
                "summary": "Как да дадеш съвет и да кажеш какво е задължително.",
                "theory": """
<table>
<tr><th>Глагол</th><th>Значение</th><th>Пример</th></tr>
<tr><td class="en">should</td><td>съвет (трябва, би трябвало)</td><td class="en">You should see a doctor.</td></tr>
<tr><td class="en">must</td><td>силно задължение, често лично мнение или правило</td><td class="en">You must wear a seatbelt.</td></tr>
<tr><td class="en">have to</td><td>задължение отвън (правила, обстоятелства)</td><td class="en">I have to work on Saturday.</td></tr>
</table>
<h3>Внимание с отрицанията</h3>
<ul>
<li><span class="en">You mustn't smoke here.</span> Забранено е.</li>
<li><span class="en">You don't have to come.</span> Не е нужно да идваш (но можеш).</li>
</ul>
<div class="tip">След <span class="en">should</span> и <span class="en">must</span> глаголът е без <span class="en">to</span> и без -s: <span class="en">She should go</span>, а не <em>She should to go</em> или <em>She shoulds go</em>.</div>
""",
                "exercises": [
                    C("You look tired. You ___ go to bed early.", ["should", "mustn't", "don't have to"], 0),
                    C("Tomorrow is Sunday. I ___ get up early.", ["mustn't", "don't have to", "should"], 1,
                      "Не е нужно, но не е забранено."),
                    C("You ___ use your phone during the exam. It's forbidden.", ["don't have to", "mustn't", "shouldn't to"], 1),
                    C("She ___ wear a uniform at work.", ["has to", "have to", "must to"], 0, "С she: has to."),
                    F("You should ___ (try) this cake. It's delicious!", "try"),
                    T("Трябва да говориш с него.", "You should talk to him|You should speak to him|You should talk with him|You must talk to him|You have to talk to him|You must speak to him|You have to speak to him"),
                ],
            },
        ],
    },
]
