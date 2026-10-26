"""More listening and pronunciation lessons.

EXTRA_LESSONS adds lessons to existing units (by unit slug). UNITS are new pronunciation units.
Pronunciation priorities follow the Lingua Franca Core research: consonants and clusters, vowel length and
sentence (nuclear) stress matter most for being understood; word stress is also taught.
"""

from .courses import C, D, F, L
from .listening import INTRO, Q, dialogue

HEAR = "Коя дума чу?"

EXTRA_LESSONS = {
    "a1-listening": [
        {
            "slug": "a1-listen-hotel", "title": "В хотела: настаняване", "title_en": "Checking in at a hotel", "kind": "listening",
            "minutes": 6, "xp": 15, "summary": "Иван се настанява в хотел в Лондон.", "theory": INTRO,
            "dialogue": dialogue(
                ("Receptionist", "Good evening! Welcome to the Park Hotel.", "Добър вечер! Добре дошли в хотел „Парк“."),
                ("Ivan", "Hi. I have a reservation. My name is Ivan Georgiev.", "Здравейте. Имам резервация. Казвам се Иван Георгиев."),
                ("Receptionist", "Yes, a single room for three nights. Can I see your passport, please?", "Да, единична стая за три нощувки. Може ли паспорта ви?"),
                ("Ivan", "Here you are. What time is breakfast?", "Заповядайте. В колко часа е закуската?"),
                ("Receptionist", "From seven to ten, on the first floor. Your room is 214.", "От седем до десет, на първия етаж. Стаята ви е 214."),
                ("Ivan", "Thank you. Is there Wi-Fi in the room?", "Благодаря. Има ли Wi-Fi в стаята?"),
                ("Receptionist", "Yes, the password is on your key card. Enjoy your stay!", "Да, паролата е на картата ви. Приятен престой!"),
            ),
            "exercises": [
                C("За колко нощувки е резервацията?", ["Три", "Една", "Седем"], 0, instruction=Q),
                C("Какво иска рецепционистът да види?", ["Паспорта", "Кредитна карта", "Билета"], 0, instruction=Q),
                C("До колко часа е закуската?", ["До 10", "До 7", "До 11"], 0, instruction=Q),
                C("Коя е стаята на Иван?", ["214", "241", "204"], 0, instruction=Q),
                L("Какво чу?", "Enjoy your stay!", ["Приятен престой!", "Довиждане!", "Добре дошли!"], 0),
                D("I have a reservation."),
            ],
        },
    ],
    "a2-listening": [
        {
            "slug": "a2-listen-airport", "title": "Съобщения на летището", "title_en": "Airport announcements", "kind": "listening",
            "minutes": 7, "xp": 20, "summary": "Да разбереш промяна на изхода и закъснение.", "theory": INTRO,
            "dialogue": dialogue(
                ("Announcer", "Good afternoon. This is an announcement for passengers on flight BA 893 to Sofia.", "Добър ден. Съобщение за пътниците на полет BA 893 за София."),
                ("Announcer", "Due to a technical problem, this flight is delayed by forty minutes.", "Поради технически проблем полетът закъснява с четиридесет минути."),
                ("Announcer", "The new departure time is fifteen fifty. Boarding will now take place at gate 22, not gate 14.", "Новият час на излитане е 15:50. Качването ще бъде от изход 22, а не от изход 14."),
                ("Announcer", "Passengers with small children may board first. We apologise for any inconvenience.", "Пътниците с малки деца могат да се качат първи. Извиняваме се за неудобството."),
            ),
            "exercises": [
                C("За кой град е полетът?", ["София", "Солун", "Сплит"], 0, instruction=Q),
                C("С колко закъснява полетът?", ["40 минути", "14 минути", "4 часа"], 0, instruction=Q),
                C("От кой изход се качват сега?", ["22", "14", "15"], 0, instruction=Q),
                C("Кой може да се качи първи?", ["Пътници с малки деца", "Бизнес класа", "Всички едновременно"], 0, instruction=Q),
                L("Какво означава due to?", "Due to a technical problem, this flight is delayed.", ["поради", "въпреки", "след"], 0),
                D("The flight is delayed.", "The flight is delayed"),
            ],
        },
    ],
    "b1-listening": [
        {
            "slug": "b1-listen-weather", "title": "Прогноза за времето", "title_en": "A weather forecast", "kind": "listening",
            "minutes": 7, "xp": 25, "summary": "Монолог по радиото: какво ще е времето утре.", "theory": INTRO,
            "dialogue": dialogue(
                ("Presenter", "And now the weather for tomorrow.", "А сега прогнозата за утре."),
                ("Presenter", "The morning will start cloudy across most of the country, with some light rain in the west.", "Сутринта ще започне облачно в по-голямата част от страната, със слаб дъжд на запад."),
                ("Presenter", "By the afternoon the clouds should clear, and temperatures will reach twenty-three degrees in the south.", "Следобед облаците би трябвало да се разсеят, а температурите ще достигнат двадесет и три градуса на юг."),
                ("Presenter", "In the mountains, though, expect strong winds and possible thunderstorms in the evening.", "В планините обаче очаквайте силен вятър и възможни гръмотевични бури вечерта."),
                ("Presenter", "So if you're planning a hike, it's best to set off early.", "Така че ако планирате преход, най-добре тръгнете рано."),
            ),
            "exercises": [
                C("Какво ще е времето сутринта?", ["Облачно", "Слънчево", "Снежно"], 0, instruction=Q),
                C("Колко градуса ще има на юг следобед?", ["23", "13", "32"], 0, instruction=Q),
                C("Какво се очаква в планините вечерта?", ["Силен вятър и бури", "Сняг", "Мъгла"], 0, instruction=Q),
                C("Какъв е съветът към туристите?", ["Да тръгнат рано", "Да останат вкъщи", "Да вземат чадър"], 0, instruction=Q),
                L("Какво означава set off?", "It's best to set off early.", ["тръгвам", "пристигам", "спирам"], 0),
                D("The clouds should clear by the afternoon."),
            ],
        },
    ],
    "b2-listening": [
        {
            "slug": "b2-listen-flat", "title": "Наем на апартамент", "title_en": "Renting a flat", "kind": "listening",
            "minutes": 9, "xp": 30, "summary": "Разговор с хазяин: условия, депозит и уговорки.", "theory": INTRO,
            "dialogue": dialogue(
                ("Landlord", "So, what do you think of the flat?", "Е, какво мислите за апартамента?"),
                ("Mira", "It's lovely, and the location is perfect. Is the rent negotiable at all?", "Чудесен е, а местоположението е идеално. Има ли възможност за договаряне на наема?"),
                ("Landlord", "It's twelve hundred a month, bills not included. I could go down to eleven fifty if you sign for a year.", "Хиляда и двеста на месец, без сметките. Мога да сваля на хиляда сто и петдесет, ако подпишете за година."),
                ("Mira", "That sounds fair. How much is the deposit?", "Звучи справедливо. Колко е депозитът?"),
                ("Landlord", "Two months' rent, which you'll get back as long as there's no damage.", "Два месечни наема, които ще получите обратно, стига да няма щети."),
                ("Mira", "And would it be possible to have a cat?", "А възможно ли е да имам котка?"),
                ("Landlord", "I'd rather not, to be honest, but let me think about it.", "Честно казано, предпочитам не, но нека помисля."),
            ),
            "exercises": [
                C("Какъв е наемът без отстъпка?", ["1200 на месец", "1150 на месец", "1100 на месец"], 0, instruction=Q),
                C("При какво условие наемът намалява?", ["Ако подпише за година", "Ако плати в брой", "Ако няма котка"], 0, instruction=Q),
                C("Колко е депозитът?", ["Два месечни наема", "Един месечен наем", "500"], 0, instruction=Q),
                C("Какъв е отговорът за котката?", ["По-скоро не, но ще помисли", "Да, без проблем", "Категорично не"], 0, instruction=Q),
                L("Какво означава negotiable?", "Is the rent negotiable at all?", ["подлежи на договаряне", "задължителен", "платен предварително"], 0),
                D("Bills are not included.", "Bills aren't included"),
            ],
        },
    ],
    "a2-pronunciation": [
        {
            "slug": "a2-pron-ed", "title": "Окончание -ed: три начина", "title_en": "Past tense -ed endings",
            "kind": "pronunciation", "minutes": 7, "xp": 20, "summary": "Worked, played, wanted: защо -ed звучи различно.",
            "theory": """
<p>Окончанието <strong>-ed</strong> се чете по три начина. Българите често казват „-ед“ навсякъде, а това прави думите трудни за разбиране.</p>
<table>
<tr><th>Звук</th><th>След</th><th>Примери</th></tr>
<tr><td>/t/</td><td>беззвучни: p, k, s, sh, ch, f</td><td class="en">worked, stopped, washed, laughed</td></tr>
<tr><td>/d/</td><td>звучни и гласни: b, g, v, l, m, n, r, гласни</td><td class="en">played, lived, called, opened</td></tr>
<tr><td>/ɪd/ (отделна сричка)</td><td>само след t и d</td><td class="en">wanted, needed, visited, decided</td></tr>
</table>
<div class="tip"><span class="en">Worked</span> е една сричка: „уъркт“, не „уъркед“. Само след t и d добавяме сричка.</div>
""",
            "exercises": [
                C("Как завършва worked?", ["/t/", "/d/", "/ɪd/"], 0),
                C("Как завършва played?", ["/t/", "/d/", "/ɪd/"], 1),
                C("Как завършва wanted?", ["/t/", "/d/", "/ɪd/"], 2),
                C("Колко срички има stopped?", ["Една", "Две"], 0),
                L(HEAR, "visited", ["visit", "visited"], 1),
                D("We watched a film and talked for hours."),
            ],
        },
    ],
}

UNITS = [
    {
        "level": "B1", "title": "Произношение", "slug": "b1-pronunciation", "icon": "fa-microphone-lines", "order": 8,
        "summary": "Ударение в думата и в изречението.",
        "lessons": [
            {
                "slug": "b1-pron-word-stress", "title": "Ударение в думата", "title_en": "Word stress",
                "kind": "pronunciation", "minutes": 7, "xp": 20, "summary": "PHOtograph, phoTOgraphy: ударението се мести.",
                "theory": """
<p>Всяка английска дума с повече от една сричка има <strong>една ударена</strong> сричка: по-дълга, по-силна и по-висока. Неударените често стават кратко „ъ“.</p>
<table>
<tr><th>Модел</th><th>Примери</th></tr>
<tr><td>повечето съществителни с 2 срички: ударение отпред</td><td class="en">TAble, WAter, DOCtor, PREsent (подарък)</td></tr>
<tr><td>повечето глаголи с 2 срички: ударение отзад</td><td class="en">deCIDE, beGIN, preSENT (представям)</td></tr>
<tr><td>-tion, -sion, -ic: ударение преди окончанието</td><td class="en">inforMAtion, deCIsion, eCONomic</td></tr>
</table>
<p>Внимавай с думи, които приличат на български, но ударението е другаде: <span class="en">HOtel</span> е hoTEL, <span class="en">deVELop, comPUter, CHOcolate, VEgetable</span>.</p>
""",
                "exercises": [
                    C("Къде е ударението в photography?", ["PHO-to-gra-phy", "pho-TO-gra-phy", "pho-to-GRA-phy"], 1),
                    C("Къде е ударението в hotel?", ["HO-tel", "ho-TEL"], 1),
                    C("Present като съществително (подарък):", ["PRE-sent", "pre-SENT"], 0),
                    C("Къде е ударението в information?", ["IN-for-ma-tion", "in-for-MA-tion", "in-FOR-ma-tion"], 1),
                    L("Коя форма чу?", "I want to present my project.", ["preSENT (глагол)", "PREsent (съществително)"], 0),
                    D("I need some information about the hotel."),
                ],
            },
            {
                "slug": "b1-pron-sentence-stress", "title": "Ударение в изречението", "title_en": "Sentence stress",
                "kind": "pronunciation", "minutes": 7, "xp": 20, "summary": "Кои думи казваме силно и защо това променя смисъла.",
                "theory": """
<p>В английското изречение ударени са <strong>думите със съдържание</strong> (съществителни, глаголи, прилагателни, наречия). Служебните думи (<span class="en">a, the, to, of, and, can</span>) са бързи и слаби.</p>
<p><span class="en">I WANT to GO to the SHOP.</span></p>
<h3>Ударението променя смисъла</h3>
<table>
<tr><th>Изречение</th><th>Смисъл</th></tr>
<tr><td class="en">I didn't take your BOOK.</td><td>взех нещо друго</td></tr>
<tr><td class="en">I didn't take YOUR book.</td><td>взех нечия друга книга</td></tr>
<tr><td class="en">I DIDN'T take your book.</td><td>не съм я взел/а изобщо</td></tr>
</table>
<div class="tip">Изследванията за разбираемост показват, че главното ударение в изречението е сред най-важните неща за това да те разберат.</div>
""",
                "exercises": [
                    C("Кои думи обикновено са ударени?", ["Съществителни, глаголи, прилагателни", "Предлози и членове", "Всички еднакво"], 0),
                    C("I didn't take YOUR book. означава:", ["Взех книгата на някой друг", "Взех нещо друго", "Не съм взел нищо"], 0),
                    C("Коя дума е ударена в: I'm going to the BEACH?", ["beach", "to", "the"], 0),
                    C("Как звучи can в: I can SWIM?", ["Кратко и слабо: „кън“", "Силно: „кен“"], 0),
                    D("Can you send me the report today?"),
                ],
            },
        ],
    },
    {
        "level": "B2", "title": "Произношение", "slug": "b2-pronunciation", "icon": "fa-microphone-lines", "order": 8,
        "summary": "Групи съгласни и свързана реч.",
        "lessons": [
            {
                "slug": "b2-pron-clusters", "title": "Групи съгласни и свързана реч", "title_en": "Consonant clusters and linking",
                "kind": "pronunciation", "minutes": 8, "xp": 25, "summary": "Months, clothes, texts и как думите се сливат.",
                "theory": """
<h3>Групи съгласни</h3>
<p>Думи като <span class="en">months, clothes, texts, sixths, asked</span> имат по няколко съгласни подред. Не добавяй гласна между тях („мънтъс“) и не изпускай съгласни: това е сред най-важните неща за разбираемостта.</p>
<ul>
<li><span class="en">months</span> /mʌnθs/</li>
<li><span class="en">asked</span> /ɑːskt/</li>
<li><span class="en">texts</span> /teksts/</li>
</ul>
<h3>Свързана реч</h3>
<p>В бърза реч съгласната в края на една дума се „залепва“ за гласната в началото на следващата:</p>
<ul>
<li><span class="en">an apple</span> звучи като „ъ-нэпъл“</li>
<li><span class="en">turn it off</span> звучи като „тър-ни-тоф“</li>
<li><span class="en">What do you want?</span> често звучи „уотчъ уонт?“</li>
</ul>
<div class="tip">Не е нужно ти да говориш така, но трябва да го разпознаваш, за да разбираш носители на езика.</div>
""",
                "exercises": [
                    L(HEAR, "months", ["month", "months"], 1),
                    L(HEAR, "asked", ["ask", "asked"], 1),
                    L("Какво чу?", "Turn it off, please.", ["Turn it off, please.", "Turn on, please.", "Tell him off, please."], 0),
                    C("Колко срички има clothes?", ["Една", "Две"], 0),
                    F("I ___ (ask) him a question yesterday.", "asked"),
                    D("She texts me every few months."),
                ],
            },
        ],
    },
]
