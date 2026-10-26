"""Fourth batch: more reading, listening, conversation, vocabulary and pronunciation lessons.

EXTRA_LESSONS adds lessons to existing units (by unit slug).
"""

from .courses import C, D, F, L, O, T
from .courses_skills import reading
from .listening import INTRO, dialogue

RQ = "Отговори според текста"
DQ = "Отговори според диалога"
HEAR = "Коя дума чу?"

EXTRA_LESSONS = {
    # ---------------- A1 ----------------
    "a1-skills": [
        {
            "slug": "a1-read-menu", "title": "Четене: Менюто в кафенето", "title_en": "Reading: a café menu",
            "kind": "reading", "minutes": 6, "xp": 15, "summary": "Разбери менюто и цените.",
            "theory": reading("Sunny Café: Menu", [
                "Breakfast (8 am to 11 am): Toast with butter and jam, £3.50. Eggs and bacon, £6.00. Fruit salad, £4.20.",
                "Lunch (12 pm to 3 pm): Tomato soup with bread, £5.00. Chicken sandwich, £6.50. Vegetarian pasta, £8.00.",
                "Drinks: Coffee, £2.50. Tea, £2.00. Fresh orange juice, £3.00.",
                "Free Wi-Fi. We accept cards. Please pay at the counter.",
            ], [("butter", "масло"), ("jam", "конфитюр"), ("bacon", "бекон"), ("vegetarian", "вегетариански"),
                ("we accept cards", "приемаме карти"), ("counter", "щанд, каса")]),
            "exercises": [
                C("До колко часа е закуската?", ["До 11", "До 12", "До 3"], 0, instruction=RQ),
                C("Колко струва супата?", ["£5.00", "£6.50", "£3.00"], 0, instruction=RQ),
                C("Кое ястие е без месо?", ["Vegetarian pasta", "Chicken sandwich", "Eggs and bacon"], 0, instruction=RQ),
                C("Къде се плаща?", ["На касата", "На масата", "Онлайн"], 0, instruction=RQ),
                F("Coffee is £2.50 and tea ___ £2.00.", "is"),
                O("Може ли един портокалов сок?", "Can I have an orange juice|Can I have a fresh orange juice"),
            ],
        },
        {
            "slug": "a1-describing-people", "title": "Описване на хора", "title_en": "Describing people",
            "kind": "vocabulary", "minutes": 6, "xp": 15, "summary": "Висок, нисък, руса коса, сини очи.",
            "theory": """
<h3>Външен вид</h3>
<table>
<tr><th>Английски</th><th>Български</th></tr>
<tr><td class="en">tall / short</td><td>висок / нисък</td></tr>
<tr><td class="en">young / old</td><td>млад / възрастен</td></tr>
<tr><td class="en">slim / overweight</td><td>слаб / с наднормено тегло</td></tr>
<tr><td class="en">long / short / curly / straight hair</td><td>дълга / къса / къдрава / права коса</td></tr>
<tr><td class="en">blonde / dark / grey hair</td><td>руса / тъмна / сива коса</td></tr>
<tr><td class="en">blue / brown / green eyes</td><td>сини / кафяви / зелени очи</td></tr>
</table>
<h3>Характер</h3>
<p><span class="en">friendly</span> дружелюбен, <span class="en">kind</span> мил, <span class="en">funny</span> забавен, <span class="en">shy</span> срамежлив, <span class="en">lazy</span> мързелив, <span class="en">clever</span> умен</p>
<div class="tip">Косата е неброима: <span class="en">She has long hair</span>, не <em>long hairs</em>. Редът е: размер, после цвят: <span class="en">long dark hair</span>.</div>
""",
            "exercises": [
                C("Тя има дълга руса коса:", ["She has long blonde hair.", "She has blonde long hairs.", "She has a long hair blonde."], 0),
                C("Shy означава:", ["срамежлив", "забавен", "висок"], 0),
                C("He is very ___ . He always makes us laugh.", ["funny", "shy", "lazy"], 0),
                F("My brother is ___ (висок) and slim.", "tall"),
                O("Той има кафяви очи.", "He has brown eyes|He has got brown eyes|He's got brown eyes"),
                T("Тя е мила и дружелюбна.", "She is kind and friendly|She's kind and friendly"),
            ],
        },
    ],
    "a1-listening": [
        {
            "slug": "a1-listen-market", "title": "На пазара", "title_en": "At the market", "kind": "listening",
            "minutes": 6, "xp": 15, "summary": "Лора купува плодове и зеленчуци.", "theory": INTRO,
            "dialogue": dialogue(
                ("Seller", "Good morning! What would you like?", "Добро утро! Какво желаете?"),
                ("Laura", "A kilo of tomatoes, please. How much are they?", "Един килограм домати, моля. Колко струват?"),
                ("Seller", "Two pounds a kilo.", "Два паунда килограма."),
                ("Laura", "OK. And six apples, please.", "Добре. И шест ябълки, моля."),
                ("Seller", "The red ones or the green ones?", "Червените или зелените?"),
                ("Laura", "The green ones. That's all, thanks.", "Зелените. Това е всичко, благодаря."),
                ("Seller", "That's three pounds forty altogether.", "Общо три паунда и четиридесет."),
            ),
            "exercises": [
                C("Колко домати купува Лора?", ["Един килограм", "Два килограма", "Шест"], 0, instruction=DQ),
                C("Колко струват доматите?", ["£2 за килограм", "£3.40 за килограм", "£6"], 0, instruction=DQ),
                C("Какви ябълки избира?", ["Зелени", "Червени", "Жълти"], 0, instruction=DQ),
                C("Колко плаща общо?", ["£3.40", "£2.00", "£4.30"], 0, instruction=DQ),
                L("Какво означава altogether?", "That's three pounds forty altogether.", ["общо", "сама", "заедно с мен"], 0),
                D("That's all, thanks."),
            ],
        },
    ],
    "a1-pronunciation": [
        {
            "slug": "a1-pron-alphabet", "title": "Азбуката и спелуване", "title_en": "The alphabet and spelling",
            "kind": "pronunciation", "minutes": 7, "xp": 15, "summary": "Как да кажеш името си буква по буква.",
            "theory": """
<p>На хотел, летище или по телефона често ще те питат: <span class="en">How do you spell that?</span> Трябва да можеш да кажеш името си буква по буква.</p>
<h3>Буквите, които българите бъркат</h3>
<table>
<tr><th>Буква</th><th>Звучи като</th><th>Не я бъркай с</th></tr>
<tr><td class="en">A</td><td>„ей“</td><td class="en">E („ии“)</td></tr>
<tr><td class="en">E</td><td>„ии“</td><td class="en">I („ай“)</td></tr>
<tr><td class="en">I</td><td>„ай“</td><td class="en">E</td></tr>
<tr><td class="en">G</td><td>„джии“</td><td class="en">J („джей“)</td></tr>
<tr><td class="en">J</td><td>„джей“</td><td class="en">G</td></tr>
<tr><td class="en">Y</td><td>„уай“</td><td class="en">I</td></tr>
<tr><td class="en">W</td><td>„дабъл ю“</td><td class="en">V („вии“)</td></tr>
<tr><td class="en">H</td><td>„ейч“</td><td>не „хаш“</td></tr>
</table>
<div class="tip">Две еднакви букви се казват с <span class="en">double</span>: Анна е <span class="en">A, double N, A</span>.</div>
""",
            "exercises": [
                L("Коя буква чу?", "G", ["G", "J"], 0),
                L("Коя буква чу?", "E", ["E", "I", "A"], 0),
                L("Коя буква чу?", "Y", ["I", "Y", "E"], 1),
                C("Как спелуваш Anna?", ["A, double N, A", "A, N, A", "A, two N, A"], 0),
                D("How do you spell that?"),
            ],
        },
    ],
    # ---------------- A2 ----------------
    "a2-skills": [
        {
            "slug": "a2-read-hotel-review", "title": "Четене: Отзив за хотел", "title_en": "Reading: a hotel review",
            "kind": "reading", "minutes": 7, "xp": 20, "summary": "Какво е добро и какво не в един хотел.",
            "theory": reading("Great location, but noisy", [
                "We stayed at the Harbour Hotel for four nights in August.",
                "The location is perfect: the beach is only two minutes away and there are lots of restaurants nearby. The staff were friendly and the breakfast was excellent.",
                "However, our room was above a bar, and it was very noisy until two in the morning. The Wi-Fi also didn't work in the room.",
                "Would I go back? Yes, but next time I'll ask for a quiet room at the back.",
            ], [("location", "местоположение"), ("nearby", "наблизо"), ("staff", "персонал"),
                ("noisy", "шумен"), ("above", "над"), ("at the back", "отзад, към двора")]),
            "exercises": [
                C("Колко нощувки са останали?", ["Четири", "Две", "Една седмица"], 0, instruction=RQ),
                C("Какво хвали авторът?", ["Местоположението, персонала и закуската", "Тишината", "Wi-Fi"], 0, instruction=RQ),
                C("Защо е било шумно?", ["Стаята е над бар", "Строителство", "Летище наблизо"], 0, instruction=RQ),
                C("Би ли се върнал/а авторът?", ["Да, но в тиха стая", "Не", "Не е ясно"], 0, instruction=RQ),
                F("The beach is only two minutes ___ .", "away"),
                O("Персоналът беше много любезен.", "The staff were very friendly|The staff was very friendly"),
            ],
        },
        {
            "slug": "a2-returns", "title": "Пазаруване и връщане на стока", "title_en": "Shopping and returns",
            "kind": "conversation", "minutes": 7, "xp": 20, "summary": "Как да върнеш или замениш нещо в магазина.",
            "theory": """
<table>
<tr><th>Искаш да...</th><th>Английски</th></tr>
<tr><td>върнеш нещо</td><td class="en">I'd like to return this, please.</td></tr>
<tr><td>кажеш проблема</td><td class="en">It doesn't fit. / It's broken. / It's the wrong size.</td></tr>
<tr><td>замениш</td><td class="en">Can I exchange it for a smaller size?</td></tr>
<tr><td>поискаш парите</td><td class="en">Can I get a refund?</td></tr>
<tr><td>покажеш бележката</td><td class="en">Here's the receipt.</td></tr>
</table>
<p>Какво може да чуеш: <span class="en">Do you have the receipt? We can give you a store credit. Sale items can't be returned.</span></p>
<div class="tip"><span class="en">It doesn't fit</span> е за размер (не ти става). <span class="en">It doesn't suit me</span> е за стил (не ти отива).</div>
""",
            "exercises": [
                C("Не ми става (размерът):", ["It doesn't fit.", "It doesn't suit me.", "It doesn't match."], 0),
                C("Receipt означава:", ["касова бележка", "рецепта", "разписание"], 0),
                C("Искаш парите си обратно:", ["Can I get a refund?", "Can I get a return?", "Give money back."], 0),
                F("Can I ___ it for a bigger size?", "exchange|change"),
                O("Бих искал/а да върна това.", "I would like to return this|I'd like to return this"),
            ],
        },
    ],
    "a2-listening": [
        {
            "slug": "a2-listen-booking", "title": "Резервация по телефона", "title_en": "Booking a table by phone",
            "kind": "listening", "minutes": 7, "xp": 20, "summary": "Петър запазва маса за рожден ден.", "theory": INTRO,
            "dialogue": dialogue(
                ("Waiter", "Good afternoon, Bella Italia. How can I help?", "Добър ден, „Бела Италия“. С какво мога да помогна?"),
                ("Peter", "Hi, I'd like to book a table for Saturday evening.", "Здравейте, бих искал да запазя маса за събота вечер."),
                ("Waiter", "Of course. For how many people?", "Разбира се. За колко души?"),
                ("Peter", "For six. It's my wife's birthday.", "За шестима. Рожден ден е на съпругата ми."),
                ("Waiter", "What time would you like? We have tables at seven or at half past eight.", "За колко часа? Имаме маси в седем или в осем и половина."),
                ("Peter", "Half past eight, please. Could we have a table by the window?", "В осем и половина, моля. Може ли маса до прозореца?"),
                ("Waiter", "I'll do my best. Can I have your name and number?", "Ще направя каквото мога. Може ли име и телефон?"),
            ),
            "exercises": [
                C("За кой ден е резервацията?", ["Събота", "Неделя", "Петък"], 0, instruction=DQ),
                C("За колко души?", ["Шест", "Четири", "Осем"], 0, instruction=DQ),
                C("Какъв е поводът?", ["Рожден ден", "Годишнина", "Бизнес среща"], 0, instruction=DQ),
                C("В колко часа ще бъдат?", ["В 8:30", "В 7:00", "В 7:30"], 0, instruction=DQ),
                L("Какво означава I'll do my best?", "I'll do my best.", ["Ще направя каквото мога.", "Обещавам.", "Не е възможно."], 0),
                D("I'd like to book a table for Saturday.", "I would like to book a table for Saturday"),
            ],
        },
    ],
    "a2-pronunciation": [
        {
            "slug": "a2-pron-silent-letters", "title": "Неми букви", "title_en": "Silent letters",
            "kind": "pronunciation", "minutes": 6, "xp": 20, "summary": "Knife, Wednesday, island: букви, които не се четат.",
            "theory": """
<p>В английския много букви се пишат, но не се произнасят. Българите често ги четат, защото в българския се чете всичко.</p>
<table>
<tr><th>Неми</th><th>Примери</th></tr>
<tr><td>k пред n</td><td class="en">knife, know, knee</td></tr>
<tr><td>w пред r</td><td class="en">write, wrong, wrist</td></tr>
<tr><td>b след m</td><td class="en">climb, bomb, thumb</td></tr>
<tr><td>l</td><td class="en">walk, talk, half, could, should</td></tr>
<tr><td>gh</td><td class="en">night, daughter, thought</td></tr>
<tr><td>друго</td><td class="en">Wednesday („уенздей“), island („айлънд“), listen, castle, hour</td></tr>
</table>
""",
            "exercises": [
                C("Коя буква е няма в knife?", ["k", "n", "f"], 0),
                C("Как звучи Wednesday?", ["„уенздей“", "„уеднесдей“", "„веднесдей“"], 0),
                C("Коя буква е няма в walk?", ["l", "w", "k"], 0),
                L(HEAR, "island", ["island", "Iceland"], 0),
                D("I know the right answer."),
            ],
        },
    ],
    # ---------------- B1 ----------------
    "b1-skills": [
        {
            "slug": "b1-read-blog", "title": "Четене: Една година в Лондон", "title_en": "Reading: a year in London",
            "kind": "reading", "minutes": 8, "xp": 20, "summary": "Блог на българка, която живее в чужбина.",
            "theory": reading("My first year in London", [
                "A year ago I packed two suitcases and moved from Varna to London. I had a job offer, a tiny room in a shared flat and absolutely no idea what to expect.",
                "The first months were harder than I thought. Everything was expensive, the weather was grey, and I missed my family and the sea.",
                "But slowly things got better. I joined a running club, made friends from all over the world, and my English improved more in a year than in ten years at school.",
                "If you're thinking of moving abroad, my advice is simple: say yes to every invitation, even when you're tired. That's how you build a new life.",
            ], [("packed", "опаковах, събрах (багаж)"), ("shared flat", "апартамент на съквартиранти"),
                ("expect", "очаквам"), ("missed", "липсваше ми"), ("joined", "присъединих се"), ("abroad", "в чужбина")]),
            "exercises": [
                C("Откъде се мести авторката?", ["От Варна", "От София", "От Бургас"], 0, instruction=RQ),
                C("Какво ѝ е липсвало?", ["Семейството и морето", "Работата", "Колата"], 0, instruction=RQ),
                C("Какво ѝ е помогнало?", ["Клуб по бягане и нови приятели", "Нова работа", "Курс по английски"], 0, instruction=RQ),
                C("Какъв е съветът ѝ?", ["Казвай „да“ на всяка покана", "Не се мести", "Пести пари"], 0, instruction=RQ),
                F("The first months were ___ (hard) than I thought.", "harder"),
                O("Английският ми се подобри много.", "My English improved a lot"),
            ],
        },
        {
            "slug": "b1-storytelling", "title": "Как да разкажеш история", "title_en": "Telling a story",
            "kind": "conversation", "minutes": 8, "xp": 20, "summary": "Начало, развитие и край: свързващи думи за разказ.",
            "theory": """
<table>
<tr><th>Част</th><th>Изрази</th></tr>
<tr><td>начало</td><td class="en">You won't believe what happened... / A few years ago... / It all started when...</td></tr>
<tr><td>последователност</td><td class="en">First, ... Then, ... After that, ... Meanwhile, ...</td></tr>
<tr><td>изненада</td><td class="en">Suddenly, ... / All of a sudden, ... / To my surprise, ...</td></tr>
<tr><td>край</td><td class="en">In the end, ... / Eventually, ... / Luckily, ...</td></tr>
<tr><td>реакция на слушателя</td><td class="en">Really? / No way! / What happened next? / Oh no!</td></tr>
</table>
<div class="tip">Фонът се разказва в Past Continuous (<span class="en">It was raining and we were walking home</span>), а събитията в Past Simple (<span class="en">when suddenly a dog ran out</span>).</div>
""",
            "exercises": [
                C("Подходящо начало на история:", ["You won't believe what happened yesterday!", "In conclusion, ...", "Firstly, I disagree."], 0),
                C("„Изведнъж“ е:", ["Suddenly", "Finally", "Meanwhile"], 0),
                C("„Накрая“ (след дълго време) е:", ["Eventually", "Actually", "Recently"], 0),
                C("We ___ along the beach when it started to rain.", ["walked", "were walking", "have walked"], 1),
                F("In the ___ , everything was fine.", "end"),
                O("И после какво стана?", "What happened next|And what happened next"),
            ],
        },
        {
            "slug": "b1-everyday-phrasal-verbs", "title": "Фразови глаголи за всеки ден", "title_en": "Everyday phrasal verbs",
            "kind": "vocabulary", "minutes": 8, "xp": 20, "summary": "Get up, look for, give up и още.",
            "theory": """
<table>
<tr><th>Фразов глагол</th><th>Значение</th><th>Пример</th></tr>
<tr><td class="en">get up</td><td>ставам (от леглото)</td><td class="en">I get up at seven.</td></tr>
<tr><td class="en">look for</td><td>търся</td><td class="en">I'm looking for my keys.</td></tr>
<tr><td class="en">look after</td><td>грижа се за</td><td class="en">She looks after her grandmother.</td></tr>
<tr><td class="en">turn on / turn off</td><td>включвам / изключвам</td><td class="en">Turn off the lights, please.</td></tr>
<tr><td class="en">give up</td><td>отказвам се</td><td class="en">He gave up smoking.</td></tr>
<tr><td class="en">find out</td><td>разбирам, научавам</td><td class="en">I found out the truth.</td></tr>
<tr><td class="en">put on / take off</td><td>обличам / събличам</td><td class="en">Put on your coat.</td></tr>
<tr><td class="en">get on with</td><td>разбирам се с някого</td><td class="en">I get on well with my boss.</td></tr>
</table>
<div class="tip">С местоимение то стои по средата: <span class="en">Turn it off</span>, не <em>Turn off it</em>.</div>
""",
            "exercises": [
                C("Търся работа:", ["I'm looking for a job.", "I'm looking after a job.", "I'm looking a job."], 0),
                C("He ___ smoking last year.", ["gave up", "gave off", "got up"], 0),
                C("Кое е правилно?", ["Turn off it.", "Turn it off."], 1),
                C("I get ___ well with my sister.", ["on", "up", "off"], 0),
                F("Can you ___ after the kids tonight?", "look"),
                O("Облечи си якето.", "Put on your jacket|Put your jacket on"),
            ],
        },
    ],
    "b1-listening": [
        {
            "slug": "b1-listen-project", "title": "Разговор с колега", "title_en": "A chat with a colleague",
            "kind": "listening", "minutes": 7, "xp": 25, "summary": "Закъснял проект и решение.", "theory": INTRO,
            "dialogue": dialogue(
                ("Kate", "Have you got a minute? It's about the website project.", "Имаш ли минутка? За проекта за сайта е."),
                ("Boris", "Sure. Is everything OK?", "Разбира се. Всичко наред ли е?"),
                ("Kate", "Not really. The designer is ill, so we won't finish by Friday.", "Не съвсем. Дизайнерката е болна, така че няма да приключим до петък."),
                ("Boris", "Hmm. Could we ask the client for a few extra days?", "Хм. Може ли да помолим клиента за няколко допълнителни дни?"),
                ("Kate", "I've already emailed them. They said Wednesday is the latest.", "Вече им писах. Казаха, че сряда е най-късно."),
                ("Boris", "OK, then I'll help with the design myself. Let's meet tomorrow at nine.", "Добре, тогава аз ще помогна с дизайна. Да се видим утре в девет."),
            ),
            "exercises": [
                C("Защо проектът закъснява?", ["Дизайнерката е болна", "Клиентът промени изискванията", "Няма бюджет"], 0, instruction=DQ),
                C("Какъв е новият краен срок?", ["Сряда", "Петък", "Понеделник"], 0, instruction=DQ),
                C("Какво ще направи Борис?", ["Ще помогне с дизайна", "Ще наеме нов дизайнер", "Ще говори с клиента"], 0, instruction=DQ),
                C("Кога ще се срещнат?", ["Утре в 9", "Днес в 9", "В сряда"], 0, instruction=DQ),
                L("Какво означава the latest тук?", "They said Wednesday is the latest.", ["най-късно", "най-новото", "последните новини"], 0),
                D("Have you got a minute?"),
            ],
        },
    ],
    # ---------------- B2 ----------------
    "b2-skills": [
        {
            "slug": "b2-read-social-media", "title": "Четене: Телефонът и сънят", "title_en": "Reading: screens and sleep",
            "kind": "reading", "minutes": 9, "xp": 25, "summary": "Научнопопулярна статия с данни и съвети.",
            "theory": reading("Why your phone is keeping you awake", [
                "Most of us check our phones in bed, but a growing body of research suggests this habit comes at a cost.",
                "Screens emit blue light, which can delay the release of melatonin, the hormone that tells our body it is time to sleep. Yet light is only part of the problem: endless scrolling keeps the brain alert, and a stressful message late at night can make it hard to switch off.",
                "Experts recommend a simple routine: put the phone away at least an hour before bed, keep it out of the bedroom, and use an old-fashioned alarm clock instead.",
                "It sounds easy, but as anyone who has tried it knows, breaking the habit is the hard part.",
            ], [("a growing body of research", "все повече изследвания"), ("comes at a cost", "има своята цена"),
                ("emit", "излъчват"), ("delay the release", "забавят отделянето"), ("alert", "бдителен, буден"),
                ("switch off", "изключвам се, отпускам се")]),
            "exercises": [
                C("Какво прави синята светлина според текста?", ["Забавя отделянето на мелатонин", "Уврежда очите", "Ускорява съня"], 0, instruction=RQ),
                C("Каква е другата част от проблема?", ["Безкрайното скролване държи мозъка буден", "Шумът от телефона", "Цената на телефона"], 0, instruction=RQ),
                C("Какво препоръчват експертите?", ["Телефонът да е вън от спалнята", "Да спим с включен телефон", "Да използваме нощен режим"], 0, instruction=RQ),
                C("„Comes at a cost“ значи:", ["има своята цена (негативни последици)", "струва пари", "е безплатно"], 0),
                F("Put the phone away at ___ an hour before bed.", "least"),
                O("Трудната част е да се откажеш от навика.", "Breaking the habit is the hard part|The hard part is breaking the habit"),
            ],
        },
        {
            "slug": "b2-negotiating", "title": "Преговори и компромис", "title_en": "Negotiating",
            "kind": "conversation", "minutes": 8, "xp": 25, "summary": "Как да предложиш, да отстъпиш и да постигнеш съгласие.",
            "theory": """
<table>
<tr><th>Цел</th><th>Изрази</th></tr>
<tr><td>предложение</td><td class="en">What if we...? / How would you feel about...? / We could offer...</td></tr>
<tr><td>условие</td><td class="en">We can agree to that, provided that... / As long as...</td></tr>
<tr><td>отстъпка</td><td class="en">I'm willing to... if you... / Let's meet halfway.</td></tr>
<tr><td>учтив отказ</td><td class="en">I'm afraid that's not something we can do.</td></tr>
<tr><td>съгласие</td><td class="en">That sounds reasonable. / I think we have a deal.</td></tr>
</table>
<div class="tip"><span class="en">Let's meet halfway</span> е „да се срещнем по средата“, т.е. всеки да отстъпи малко.</div>
""",
            "exercises": [
                C("Let's meet halfway. означава:", ["Да отстъпим и двамата", "Да се срещнем на половината път", "Да отложим срещата"], 0),
                C("Учтив отказ:", ["No way.", "I'm afraid that's not something we can do.", "Forget it."], 1),
                C("We can agree, ___ the price stays the same.", ["provided that", "despite", "unless that"], 0),
                F("I think we have a ___ !", "deal"),
                O("Готови сме да намалим цената, ако поръчате повече.", "We are willing to reduce the price if you order more|We're willing to reduce the price if you order more"),
            ],
        },
        {
            "slug": "b2-word-formation", "title": "Словообразуване", "title_en": "Word formation",
            "kind": "vocabulary", "minutes": 8, "xp": 25, "summary": "Представки и наставки: happy, unhappy, happiness.",
            "theory": """
<h3>Представки за отрицание</h3>
<p><span class="en">un-</span> (unhappy, unusual), <span class="en">in- / im- / il- / ir-</span> (incorrect, impossible, illegal, irregular), <span class="en">dis-</span> (disagree, dishonest), <span class="en">mis-</span> = грешно (misunderstand)</p>
<h3>Наставки</h3>
<table>
<tr><th>Наставка</th><th>Прави</th><th>Примери</th></tr>
<tr><td class="en">-ness, -ity, -ment, -tion</td><td>съществително</td><td class="en">kindness, ability, payment, education</td></tr>
<tr><td class="en">-ful, -less, -ous, -able</td><td>прилагателно</td><td class="en">useful, careless, dangerous, comfortable</td></tr>
<tr><td class="en">-ize / -ise, -en</td><td>глагол</td><td class="en">organise, widen, strengthen</td></tr>
<tr><td class="en">-ly</td><td>наречие</td><td class="en">carefully, honestly</td></tr>
</table>
""",
            "exercises": [
                C("Обратното на possible:", ["unpossible", "impossible", "dispossible"], 1),
                C("Обратното на honest:", ["dishonest", "unhonest", "inhonest"], 0),
                C("Съществително от kind:", ["kindful", "kindness", "kindity"], 1),
                F("This chair is very comfort___ .", "able"),
                F("Don't be so care___ ! You broke it.", "less"),
                O("Мисля, че ме разбра погрешно.", "I think you misunderstood me"),
            ],
        },
    ],
    # ---------------- C1 ----------------
    "c1-skills": [
        {
            "slug": "c1-read-tourism", "title": "Четене: Свръхтуризмът", "title_en": "Reading: overtourism",
            "kind": "reading", "minutes": 10, "xp": 30, "summary": "Мнение с аргументи и нюанси.",
            "theory": reading("Loved to death", [
                "For decades, cities competed to attract as many visitors as possible. Now a growing number of them are doing the opposite.",
                "Venice charges day-trippers an entry fee; Amsterdam has banned new hotels in its centre; Barcelona has capped the number of tourist flats. The reasoning is the same everywhere: residents are being priced out of their own neighbourhoods, while local shops are replaced by souvenir stands.",
                "Critics argue that such measures are elitist, turning travel into a luxury for the few. Yet doing nothing has its own cost. A city that exists only for visitors eventually loses the very character that made it worth visiting.",
                "The challenge, then, is not to stop tourism but to manage it: spreading visitors across seasons and lesser-known places, rather than funnelling them all into the same few streets.",
            ], [("loved to death", "обичан до смърт (съсипан от популярност)"), ("day-trippers", "еднодневни посетители"),
                ("capped", "ограничи (с таван)"), ("priced out", "изтласкани заради цените"),
                ("elitist", "елитарен"), ("funnelling", "насочване като през фуния")]),
            "exercises": [
                C("Какво прави Венеция според текста?", ["Таксува еднодневните посетители", "Забранява нови хотели", "Ограничава апартаментите за туристи"], 0, instruction=RQ),
                C("Какво е общото основание за мерките?", ["Жителите са изтласкани от цените", "Шумът", "Престъпността"], 0, instruction=RQ),
                C("Какъв е аргументът на критиците?", ["Мерките правят пътуването лукс за малцина", "Мерките са твърде слаби", "Туристите харчат малко"], 0, instruction=RQ),
                C("Какво предлага авторът?", ["Туризмът да се управлява и разпределя", "Туризмът да се спре", "Повече хотели"], 0, instruction=RQ),
                C("Priced out означава:", ["изтласкан заради високите цени", "намалени цени", "оценен"], 0),
            ],
        },
        {
            "slug": "c1-presentations", "title": "Фрази за презентация", "title_en": "Presentation language",
            "kind": "conversation", "minutes": 9, "xp": 30, "summary": "Как да структурираш презентация на английски.",
            "theory": """
<table>
<tr><th>Част</th><th>Изрази</th></tr>
<tr><td>начало</td><td class="en">Thanks for having me. Today I'd like to walk you through...</td></tr>
<tr><td>структура</td><td class="en">I've divided my talk into three parts. First, ... Then, ... Finally, ...</td></tr>
<tr><td>преход</td><td class="en">That brings me to my next point. / Moving on to...</td></tr>
<tr><td>визуален материал</td><td class="en">As you can see from this chart, ... / What this graph shows is...</td></tr>
<tr><td>акцент</td><td class="en">The key takeaway here is... / I'd like to stress that...</td></tr>
<tr><td>край и въпроси</td><td class="en">To sum up, ... / I'm happy to take any questions.</td></tr>
<tr><td>труден въпрос</td><td class="en">That's a great question. I don't have the figures with me, but I'll get back to you.</td></tr>
</table>
""",
            "exercises": [
                C("Добро начало:", ["Today I'd like to walk you through our results.", "So, hello, whatever.", "I will now speak."], 0),
                C("Преход към следваща тема:", ["That brings me to my next point.", "Stop.", "And other things."], 0),
                C("Ако нямаш отговор на въпрос:", ["I don't know.", "I'll check and get back to you.", "Next question."], 1),
                F("To ___ up, our sales grew by 12%.", "sum"),
                O("Основният извод тук е прост.", "The key takeaway here is simple"),
            ],
        },
        {
            "slug": "c1-money-idioms", "title": "Идиоми за пари и работа", "title_en": "Idioms about money and work",
            "kind": "vocabulary", "minutes": 8, "xp": 30, "summary": "Make ends meet, cost an arm and a leg.",
            "theory": """
<table>
<tr><th>Идиом</th><th>Значение</th></tr>
<tr><td class="en">cost an arm and a leg</td><td>струва много скъпо</td></tr>
<tr><td class="en">make ends meet</td><td>свързвам двата края</td></tr>
<tr><td class="en">tighten your belt</td><td>затягам колана, ограничавам разходите</td></tr>
<tr><td class="en">the bottom line</td><td>най-важното, крайният резултат</td></tr>
<tr><td class="en">a ballpark figure</td><td>приблизителна цифра</td></tr>
<tr><td class="en">back to square one</td><td>отначало, обратно в началото</td></tr>
<tr><td class="en">think outside the box</td><td>мисля нестандартно</td></tr>
<tr><td class="en">be in the red / in the black</td><td>на загуба / на печалба</td></tr>
</table>
""",
            "exercises": [
                C("The repairs cost an arm and a leg. означава:", ["Ремонтът беше много скъп", "Ремонтът беше опасен", "Ремонтът беше бърз"], 0),
                C("Can you give me a ballpark figure?", ["Приблизителна цифра", "Точна сума", "Отстъпка"], 0),
                C("The deal fell through, so we're back to ___ one.", ["square", "start", "point"], 0),
                C("The company is in the red. означава:", ["на загуба е", "на печалба е", "сменя логото си"], 0),
                F("It's hard to make ends ___ on this salary.", "meet"),
            ],
        },
    ],
    "c1-listening": [
        {
            "slug": "c1-listen-memory", "title": "Лекция: как работи паметта", "title_en": "Lecture: how memory works",
            "kind": "listening", "minutes": 9, "xp": 35, "summary": "Откъс от университетска лекция.", "theory": INTRO,
            "dialogue": dialogue(
                ("Lecturer", "Today I want to challenge a common assumption: that memory works like a video recorder.", "Днес искам да оспоря едно често срещано схващане: че паметта работи като видеорекордер."),
                ("Lecturer", "In reality, every time we recall an event, we reconstruct it, and in doing so we may alter it slightly.", "В действителност всеки път, когато си припомним събитие, ние го реконструираме и така може леко да го променим."),
                ("Lecturer", "This is why eyewitness accounts, however confident, are surprisingly unreliable.", "Ето защо показанията на очевидци, колкото и уверени да са, са изненадващо ненадеждни."),
                ("Lecturer", "The good news for learners is that the act of retrieving information strengthens it. Testing yourself is far more effective than rereading.", "Добрата новина за учещите е, че самото припомняне укрепва информацията. Да се тестваш е много по-ефективно от препрочитането."),
            ),
            "exercises": [
                C("Кое схващане оспорва лекторът?", ["Че паметта е като видеозапис", "Че паметта е генетична", "Че забравяме бързо"], 0, instruction=DQ),
                C("Какво се случва, когато си припомняме?", ["Реконструираме и може да променим спомена", "Спомените се изтриват", "Нищо не се променя"], 0, instruction=DQ),
                C("Какво казва за очевидците?", ["Изненадващо ненадеждни са", "Винаги са точни", "Помнят повече детайли"], 0, instruction=DQ),
                C("Какъв е съветът към учещите?", ["Да се тестват, а не да препрочитат", "Да препрочитат", "Да учат нощем"], 0, instruction=DQ),
                L("Какво означава alter тук?", "We may alter it slightly.", ["променим", "забравим", "запишем"], 0),
                D("Testing yourself is more effective than rereading."),
            ],
        },
    ],
    # ---------------- C2 ----------------
    "c2-listening": [
        {
            "slug": "c2-listen-writer", "title": "Интервю с писателка", "title_en": "An interview with a novelist",
            "kind": "listening", "minutes": 10, "xp": 40, "summary": "Нюанси, ирония и подтекст в разговор.", "theory": INTRO,
            "dialogue": dialogue(
                ("Interviewer", "Your new novel has been described as bleak. Would you agree?", "Новият ви роман е описан като мрачен. Съгласявате ли се?"),
                ("Novelist", "Bleak is a word critics reach for when a book doesn't end with a wedding. I'd call it honest.", "„Мрачен“ е дума, към която критиците посягат, когато една книга не завършва със сватба. Аз бих я нарекла честна."),
                ("Interviewer", "There's very little hope in it, though.", "В нея обаче има много малко надежда."),
                ("Novelist", "There's a great deal of hope; it's just not the comfortable kind. The characters don't get what they want, but they come to understand what they need.", "Има много надежда, просто не от удобния вид. Героите не получават това, което искат, но разбират от какво имат нужда."),
                ("Interviewer", "Was that a deliberate choice from the outset?", "Това съзнателен избор ли беше от самото начало?"),
                ("Novelist", "Nothing in a first draft is deliberate. The choices come later, mostly in deciding what to throw away.", "Нищо в първата чернова не е съзнателно. Изборите идват по-късно, главно в решаването какво да изхвърлиш."),
            ),
            "exercises": [
                C("Как писателката определя книгата си?", ["Честна", "Мрачна", "Забавна"], 0, instruction=DQ),
                C("Какво внушава репликата за сватбата?", ["Критиците наричат мрачна всяка книга без щастлив край", "Книгата завършва със сватба", "Тя не харесва сватби"], 0, instruction=DQ),
                C("Каква надежда има в книгата?", ["Неудобна: героите разбират от какво имат нужда", "Никаква", "Щастлив край"], 0, instruction=DQ),
                C("Кога идват съзнателните избори според нея?", ["При редакцията, когато решава какво да изхвърли", "В първата чернова", "Преди да започне"], 0, instruction=DQ),
                L("Какво означава from the outset?", "Was that a deliberate choice from the outset?", ["от самото начало", "отвън", "накрая"], 0),
                D("Nothing in a first draft is deliberate."),
            ],
        },
    ],
}

MISTAKES = {
    "a1-describing-people": [
        ("She has long hairs.", "She has long hair.", "Коса е неброимо: hair."),
        ("She has blonde long hair.", "She has long blonde hair.", "Редът е: размер, после цвят."),
    ],
    "a2-returns": [
        ("It doesn't suit. (за размер)", "It doesn't fit.", "Fit е за размер, suit за стил."),
        ("Can I take my money back?", "Can I get a refund?", "Стандартният израз е refund."),
    ],
    "b1-storytelling": [
        ("Eventually I will call you.", "I might call you.", "Eventually означава „накрая“, не „евентуално“."),
    ],
    "b1-everyday-phrasal-verbs": [
        ("Turn off it, please.", "Turn it off, please.", "Местоимението стои между глагола и частицата."),
        ("I'm looking my keys.", "I'm looking for my keys.", "„Търся“ е look for."),
    ],
    "b2-negotiating": [
        ("We agree, if only the price is the same.", "We agree, provided that the price stays the same.", "Условие: provided that / as long as."),
    ],
    "b2-word-formation": [
        ("unpossible", "impossible", "Пред p и m: im-."),
        ("unhonest", "dishonest", "Honest приема dis-."),
    ],
}
