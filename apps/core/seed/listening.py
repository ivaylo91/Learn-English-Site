"""Listening lessons: a dialogue (Speaker | English | Bulgarian) plus comprehension, listen-and-choose and dictation."""

from .courses import C, D, L

Q = "Отговори според диалога"


def listening_unit(level, slug, order, lessons):
    return {"level": level, "title": "Слушай и разбирай", "slug": slug, "icon": "fa-headphones", "order": order,
            "summary": "Диалози, въпроси за разбиране и диктовки.", "lessons": lessons}


def dialogue(*lines):
    return "\n".join(" | ".join(line) for line in lines)


INTRO = """<p>Първо слушай диалога <strong>без текст</strong>. Опитай да хванеш основното: кой говори, къде са и какво искат.
После пусни отново и провери с транскрипцията. Накрая направи упражненията.</p>"""

UNITS = [
    listening_unit("A1", "a1-listening", 9, [
        {
            "slug": "a1-listen-cafe", "title": "В кафенето", "title_en": "At the café", "kind": "listening",
            "minutes": 6, "xp": 15, "summary": "Мария поръчва кафе и кроасан.", "theory": INTRO,
            "dialogue": dialogue(
                ("Barista", "Hi! What can I get you?", "Здравейте! Какво да ви предложа?"),
                ("Maria", "Hi. Can I have a cappuccino, please?", "Здравейте. Може ли едно капучино?"),
                ("Barista", "Sure. Small or large?", "Разбира се. Малко или голямо?"),
                ("Maria", "Small, please.", "Малко, моля."),
                ("Barista", "Anything else?", "Нещо друго?"),
                ("Maria", "Yes, a croissant, please. How much is that?", "Да, един кроасан. Колко става?"),
                ("Barista", "That's five pounds twenty.", "Пет паунда и двайсет."),
                ("Maria", "Here you are.", "Заповядайте."),
                ("Barista", "Thank you. Have a nice day!", "Благодаря. Приятен ден!"),
            ),
            "exercises": [
                C("Какво поръчва Мария за пиене?", ["Капучино", "Чай", "Лате"], 0, instruction=Q),
                C("Какъв размер иска?", ["Малко", "Голямо", "Средно"], 0, instruction=Q),
                C("Колко плаща?", ["£5.20", "£2.50", "£15.20"], 0, instruction=Q),
                L("Какво чу?", "Anything else?", ["Нещо друго?", "Нещо за ядене?", "Друго кафе?"], 0),
                D("Small, please.", "Small please"),
                D("Have a nice day!"),
            ],
        },
        {
            "slug": "a1-listen-meeting", "title": "Запознанство", "title_en": "Meeting someone new", "kind": "listening",
            "minutes": 6, "xp": 15, "summary": "Том и Елена се запознават.", "theory": INTRO,
            "dialogue": dialogue(
                ("Tom", "Hi, I'm Tom. What's your name?", "Здравей, аз съм Том. Как се казваш?"),
                ("Elena", "Hi, Tom. I'm Elena.", "Здравей, Том. Аз съм Елена."),
                ("Tom", "Nice to meet you, Elena. Where are you from?", "Приятно ми е, Елена. Откъде си?"),
                ("Elena", "I'm from Bulgaria, from Plovdiv. And you?", "От България съм, от Пловдив. А ти?"),
                ("Tom", "I'm from Manchester. Are you here on holiday?", "Аз съм от Манчестър. На почивка ли си тук?"),
                ("Elena", "No, I'm here for work. I'm a nurse.", "Не, тук съм по работа. Медицинска сестра съм."),
                ("Tom", "Oh, great! I'm a teacher.", "О, чудесно! Аз съм учител."),
            ),
            "exercises": [
                C("От кой град е Елена?", ["Пловдив", "София", "Манчестър"], 0, instruction=Q),
                C("Защо е там Елена?", ["По работа", "На почивка", "Да учи"], 0, instruction=Q),
                C("Каква е професията на Том?", ["Учител", "Медицинска сестра", "Лекар"], 0, instruction=Q),
                L("Какво означава въпросът?", "Where are you from?", ["Откъде си?", "Къде живееш?", "Как се казваш?"], 0),
                D("Nice to meet you."),
                D("I'm from Bulgaria.", "I am from Bulgaria"),
            ],
        },
    ]),
    listening_unit("A2", "a2-listening", 9, [
        {
            "slug": "a2-listen-station", "title": "На гарата", "title_en": "At the train station", "kind": "listening",
            "minutes": 7, "xp": 20, "summary": "Пътник купува билет до Брайтън.", "theory": INTRO,
            "dialogue": dialogue(
                ("Passenger", "Good morning. A return ticket to Brighton, please.", "Добро утро. Билет за отиване и връщане до Брайтън, моля."),
                ("Clerk", "Are you coming back today?", "Днес ли се връщате?"),
                ("Passenger", "Yes, this evening.", "Да, довечера."),
                ("Clerk", "That's twenty-four pounds fifty.", "Двайсет и четири паунда и петдесет."),
                ("Passenger", "Can I pay by card?", "Мога ли да платя с карта?"),
                ("Clerk", "Of course. The next train leaves at ten fifteen from platform four.", "Разбира се. Следващият влак тръгва в десет и петнайсет от перон четири."),
                ("Passenger", "How long does it take?", "Колко време пътува?"),
                ("Clerk", "About an hour.", "Около час."),
                ("Passenger", "Thanks a lot.", "Много благодаря."),
            ),
            "exercises": [
                C("Какъв билет купува пътникът?", ["За отиване и връщане", "Еднопосочен", "Месечна карта"], 0, instruction=Q),
                C("Колко струва билетът?", ["£24.50", "£14.50", "£24.15"], 0, instruction=Q),
                C("От кой перон тръгва влакът?", ["Перон 4", "Перон 10", "Перон 15"], 0, instruction=Q),
                C("Колко време е пътуването?", ["Около час", "Около 15 минути", "Два часа"], 0, instruction=Q),
                L("В колко часа тръгва влакът?", "The next train leaves at ten fifteen.", ["10:15", "10:50", "9:15"], 0),
                D("Can I pay by card?"),
            ],
        },
        {
            "slug": "a2-listen-shopping", "title": "Пазаруване на дрехи", "title_en": "Shopping for clothes", "kind": "listening",
            "minutes": 7, "xp": 20, "summary": "Клиент търси яке в магазин.", "theory": INTRO,
            "dialogue": dialogue(
                ("Assistant", "Hello, can I help you?", "Здравейте, мога ли да помогна?"),
                ("Customer", "Yes, I'm looking for a jacket.", "Да, търся яке."),
                ("Assistant", "What size are you?", "Какъв размер носите?"),
                ("Customer", "Medium, I think.", "M, мисля."),
                ("Assistant", "How about this blue one?", "Какво ще кажете за това синьото?"),
                ("Customer", "It's nice. Can I try it on?", "Хубаво е. Може ли да го пробвам?"),
                ("Assistant", "Sure, the fitting rooms are over there.", "Разбира се, пробните са ей там."),
                ("Customer", "It's a bit small. Do you have it in large?", "Тесничко е. Имате ли го в L?"),
                ("Assistant", "Yes, here you are.", "Да, заповядайте."),
                ("Customer", "Perfect. I'll take it.", "Идеално. Ще го взема."),
            ),
            "exercises": [
                C("Какво търси клиентът?", ["Яке", "Риза", "Обувки"], 0, instruction=Q),
                C("Какъв цвят е якето?", ["Синьо", "Черно", "Червено"], 0, instruction=Q),
                C("Какъв е проблемът с първото яке?", ["Тесничко е", "Скъпо е", "Не харесва цвета"], 0, instruction=Q),
                C("Какъв размер купува накрая?", ["L", "M", "S"], 0, instruction=Q),
                L("Какво означава това?", "I'll take it.", ["Ще го взема.", "Ще го върна.", "Ще го пробвам."], 0),
                D("Can I try it on?"),
            ],
        },
    ]),
    listening_unit("B1", "b1-listening", 9, [
        {
            "slug": "b1-listen-weekend", "title": "Планове за уикенда", "title_en": "Weekend plans", "kind": "listening",
            "minutes": 8, "xp": 25, "summary": "Сам и Нина говорят какво ще правят.", "theory": INTRO,
            "dialogue": dialogue(
                ("Sam", "Have you got any plans for the weekend?", "Имаш ли планове за уикенда?"),
                ("Nina", "I'm going to visit my parents on Saturday. They live near the sea.", "В събота ще ходя при родителите си. Живеят близо до морето."),
                ("Sam", "That sounds lovely. Are you going by train?", "Звучи чудесно. С влак ли ще пътуваш?"),
                ("Nina", "No, I'm driving. It's cheaper, and I can stop wherever I want. What about you?", "Не, с кола. По-евтино е и мога да спра, където поискам. А ти?"),
                ("Sam", "I haven't decided yet. If the weather is good, I'll go hiking in the mountains.", "Още не съм решил. Ако времето е хубаво, ще ходя на планина."),
                ("Nina", "And if it rains?", "А ако вали?"),
                ("Sam", "Then I'll probably stay at home and finally finish that book.", "Тогава вероятно ще си остана вкъщи и най-накрая ще довърша онази книга."),
            ),
            "exercises": [
                C("Къде ще ходи Нина в събота?", ["При родителите си", "На планина", "На работа"], 0, instruction=Q),
                C("Как ще пътува?", ["С кола", "С влак", "Със самолет"], 0, instruction=Q),
                C("Защо избира този начин?", ["По-евтино е и може да спира където иска", "Влаковете не работят", "Няма билети"], 0, instruction=Q),
                C("Какво ще прави Сам, ако вали?", ["Ще довърши една книга вкъщи", "Ще ходи на кино", "Ще работи"], 0, instruction=Q),
                L("Какво ще направи Сам при хубаво време?", "If the weather is good, I'll go hiking in the mountains.",
                  ["Ще ходи на планина", "Ще отиде на море", "Ще остане вкъщи"], 0),
                D("I haven't decided yet.", "I have not decided yet"),
            ],
        },
    ]),
    listening_unit("B2", "b2-listening", 9, [
        {
            "slug": "b2-listen-interview", "title": "Интервю за работа", "title_en": "A job interview", "kind": "listening",
            "minutes": 9, "xp": 30, "summary": "Даниел кандидатства за позиция в маркетинга.", "theory": INTRO,
            "dialogue": dialogue(
                ("Interviewer", "Thanks for coming in, Daniel. Could you tell us a bit about yourself?", "Благодарим, че дойдохте, Даниел. Бихте ли ни разказали малко за себе си?"),
                ("Daniel", "Of course. I've been working in digital marketing for six years, mostly for travel companies.", "Разбира се. От шест години работя в дигиталния маркетинг, главно за туристически компании."),
                ("Interviewer", "Why are you interested in this position?", "Защо се интересувате от тази позиция?"),
                ("Daniel", "I'm looking for a role with more responsibility, and your focus on sustainable tourism really appeals to me.", "Търся роля с повече отговорност, а фокусът ви върху устойчивия туризъм наистина ме привлича."),
                ("Interviewer", "What would you say is your biggest weakness?", "Коя бихте казали, че е най-голямата ви слабост?"),
                ("Daniel", "I used to find it hard to delegate, but I've learned to trust my team, and our results have improved.", "Преди ми беше трудно да делегирам, но се научих да се доверявам на екипа си и резултатите ни се подобриха."),
                ("Interviewer", "That's good to hear. Do you have any questions for us?", "Радвам се да го чуя. Имате ли въпроси към нас?"),
                ("Daniel", "Yes. What would a typical day look like in this role?", "Да. Как би изглеждал един типичен ден на тази позиция?"),
            ),
            "exercises": [
                C("От колко години Даниел работи в маркетинга?", ["6 години", "16 години", "2 години"], 0, instruction=Q),
                C("За какви компании е работил главно?", ["Туристически", "Банки", "Болници"], 0, instruction=Q),
                C("Защо иска тази позиция?", ["Повече отговорност и интерес към устойчивия туризъм", "По-висока заплата", "Работа от вкъщи"], 0, instruction=Q),
                C("Каква слабост споменава?", ["Трудно му е било да делегира", "Често закъснява", "Не говори чужди езици"], 0, instruction=Q),
                L("Какво означава used to в това изречение?", "I used to find it hard to delegate.",
                  ["Преди беше така, вече не е", "Все още е така", "Скоро ще стане така"], 0),
                D("What would a typical day look like?"),
            ],
        },
    ]),
    listening_unit("C1", "c1-listening", 9, [
        {
            "slug": "c1-listen-remote-work", "title": "Подкаст: работа от вкъщи", "title_en": "Podcast: the future of remote work",
            "kind": "listening", "minutes": 10, "xp": 35, "summary": "Водещ и експерт обсъждат хибридната работа.", "theory": INTRO,
            "dialogue": dialogue(
                ("Host", "Welcome back to the show. Today we're asking whether remote work is here to stay.", "Добре дошли отново в предаването. Днес питаме дали дистанционната работа е тук, за да остане."),
                ("Dr Patel", "It's here to stay, but not in the form we saw during the pandemic. Most companies are settling on a hybrid model.", "Тук е, за да остане, но не във формата, която видяхме по време на пандемията. Повечето компании се спират на хибриден модел."),
                ("Host", "What's driving that shift?", "Какво стои зад тази промяна?"),
                ("Dr Patel", "Partly productivity data, which is surprisingly mixed, and partly the fact that younger employees miss the informal learning that happens in an office.", "Отчасти данните за продуктивността, които са изненадващо противоречиви, и отчасти това, че по-младите служители усещат липсата на неформалното учене в офиса."),
                ("Host", "So it's not simply about managers wanting control?", "Значи не става дума просто за мениджъри, които искат контрол?"),
                ("Dr Patel", "That's certainly a factor, but it would be an oversimplification to reduce it to that.", "Това определено е фактор, но би било прекалено опростяване всичко да се сведе до него."),
            ),
            "exercises": [
                C("Каква е основната теза на д-р Пател?", ["Хибридният модел става норма", "Всички се връщат в офиса", "Дистанционната работа изчезва"], 0, instruction=Q),
                C("Какви са данните за продуктивността според нея?", ["Противоречиви", "Категорично положителни", "Липсват"], 0, instruction=Q),
                C("Какво липсва на по-младите служители?", ["Неформалното учене в офиса", "По-високите заплати", "Пътуването до работа"], 0, instruction=Q),
                C("Какво означава oversimplification?", ["Прекалено опростяване", "Преувеличение", "Грешка в изчисленията"], 0, instruction=Q),
                L("Какво означава settling on тук?", "Most companies are settling on a hybrid model.",
                  ["Избират, спират се на", "Отказват се от", "Критикуват"], 0),
                D("Remote work is here to stay."),
            ],
        },
    ]),
    listening_unit("C2", "c2-listening", 9, [
        {
            "slug": "c2-listen-ai-debate", "title": "Дебат: изкуственият интелект в образованието",
            "title_en": "Debate: AI in education", "kind": "listening", "minutes": 10, "xp": 40,
            "summary": "Двама експерти спорят, но откриват общ език.", "theory": INTRO,
            "dialogue": dialogue(
                ("Moderator", "Let's turn to AI in classrooms. Professor Hale, you've been rather sceptical.", "Да се обърнем към изкуствения интелект в класните стаи. Професор Хейл, вие сте доста скептичен."),
                ("Professor Hale", "Sceptical, yes, but not dismissive. My concern is that we're outsourcing the very struggle that produces understanding.", "Скептичен да, но не и пренебрежителен. Притеснението ми е, че прехвърляме навън точно усилието, което води до разбиране."),
                ("Ms Rivera", "With respect, that argument was made about calculators, and before that about writing itself.", "С цялото ми уважение, същият аргумент беше изтъкван за калкулаторите, а преди това и за самото писане."),
                ("Professor Hale", "And in each case it was partly right. The question is what we're willing to trade away, and whether we're doing so deliberately.", "И всеки път е бил отчасти верен. Въпросът е от какво сме готови да се откажем и дали го правим съзнателно."),
                ("Ms Rivera", "Then we agree on more than it seems. The tool isn't the issue; unexamined adoption is.", "Тогава сме съгласни за повече, отколкото изглежда. Проблемът не е инструментът, а необмисленото му въвеждане."),
            ),
            "exercises": [
                C("Каква е позицията на професор Хейл?", ["Скептичен, но не отхвърля напълно", "Напълно против", "Ентусиазиран"], 0, instruction=Q),
                C("С какво сравнява Ривера опасенията?", ["С калкулаторите и писането", "С интернет и телевизията", "С учебниците"], 0, instruction=Q),
                C("Какво значи outsourcing the very struggle that produces understanding?", ["Прехвърляме на машината усилието, от което идва разбирането", "Плащаме на външни учители", "Учим по-бързо с помощ"], 0, instruction=Q),
                C("До какъв извод стигат накрая?", ["Проблемът е необмисленото въвеждане", "Инструментът е вреден", "Не са съгласни за нищо"], 0, instruction=Q),
                L("Какво казва професорът?", "Sceptical, yes, but not dismissive.",
                  ["Съмнява се, но не отхвърля идеята", "Напълно отхвърля идеята", "Подкрепя идеята"], 0),
                D("The tool isn't the issue.", "The tool is not the issue"),
            ],
        },
    ]),
]
