"""Seventh batch: everyday listening, weak forms, reading for gist and detail, writing tasks, grammar and vocabulary.

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
            "slug": "a1-listen-souvenir", "title": "В магазина за сувенири", "title_en": "In a gift shop", "kind": "listening",
            "minutes": 6, "xp": 15, "summary": "Петя купува подаръци за семейството си.", "theory": INTRO,
            "dialogue": dialogue(
                ("Assistant", "Hi there! Are you looking for anything special?", "Здравейте! Търсите ли нещо конкретно?"),
                ("Petya", "Yes, a present for my brother. He likes football.", "Да, подарък за брат ми. Той харесва футбол."),
                ("Assistant", "What about this T-shirt? It's twelve pounds.", "Какво ще кажете за тази тениска? Струва дванадесет паунда."),
                ("Petya", "Do you have it in large?", "Имате ли я в размер L?"),
                ("Assistant", "Yes, here you are. Anything else?", "Да, заповядайте. Нещо друго?"),
                ("Petya", "And two postcards, please.", "И две картички, моля."),
                ("Assistant", "That's thirteen pounds altogether. Would you like a bag?", "Общо тринадесет паунда. Искате ли торбичка?"),
                ("Petya", "No, thanks. I have one.", "Не, благодаря. Имам."),
            ),
            "exercises": [
                C("За кого е подаръкът?", ["За брат ѝ", "За майка ѝ", "За приятел"], 0, instruction=DQ),
                C("Какво купува Петя?", ["Тениска и две картички", "Топка и картичка", "Само картички"], 0, instruction=DQ),
                C("Какъв размер иска?", ["L", "M", "S"], 0, instruction=DQ),
                C("Колко плаща общо?", ["£13", "£12", "£30"], 0, instruction=DQ),
                L("Какво пита продавачката?", "Would you like a bag?", ["Искате ли торбичка?", "Имате ли чанта?", "Чия е чантата?"], 0),
                D("Do you have it in large?"),
                S("Two postcards, please."),
            ],
        },
    ],
    "a1-first-steps": [
        {
            "slug": "a1-this-that", "title": "This, that, these, those", "title_en": "Demonstratives",
            "kind": "grammar", "minutes": 6, "xp": 15, "summary": "Това тук и онова там: в магазина и на пазара.",
            "theory": """
<table>
<tr><th></th><th>Близо (тук)</th><th>Далеч (там)</th></tr>
<tr><td>Единствено число</td><td class="en">this</td><td class="en">that</td></tr>
<tr><td>Множествено число</td><td class="en">these</td><td class="en">those</td></tr>
</table>
<ul>
<li><span class="en">How much is this bag?</span> Колко струва тази чанта (в ръката ми)?</li>
<li><span class="en">I'd like those apples, please.</span> Онези ябълки (там).</li>
<li><span class="en">This is my friend, Ana.</span> Така представяме човек.</li>
</ul>
<div class="tip">Внимавай с произношението: <span class="en">this</span> (кратко „и“) и <span class="en">these</span> (дълго „ии“).</div>
""",
            "exercises": [
                C("___ shoes are too small. (в ръцете ми)", ["These", "This", "That"], 0),
                C("Look at ___ mountain over there!", ["that", "this", "these"], 0),
                C("Представяш приятел:", ["This is Maria.", "That are Maria.", "These is Maria."], 0),
                C("How much are ___ glasses over there?", ["those", "that", "this"], 0),
                L("Коя дума чу?", "These are my keys.", ["these", "this"], 0),
                O("Тази чанта е моя.", "This bag is mine"),
            ],
        },
    ],
    "a1-skills": [
        {
            "slug": "a1-read-email-friend", "title": "Четене: имейл от приятел", "title_en": "Reading: an email from a friend",
            "kind": "reading", "minutes": 6, "xp": 15, "summary": "Умение: да намериш кой, къде и кога.",
            "theory": """<div class="tip"><strong>Умение: основна информация.</strong> Първо прочети целия имейл бързо. После търси отговорите на въпросите кой, къде, кога.</div>""" + reading("Hi from Barcelona!", [
                "Hi Elena,",
                "I'm in Barcelona with my sister for a week. Our hotel is near the beach and it's very nice.",
                "Every morning we have breakfast in a small café. In the afternoon we visit museums or go to the beach. The food is great!",
                "We come home on Sunday. Can we meet next Tuesday? I have a present for you!",
                "Love, Kate",
            ], [("near", "близо до"), ("every morning", "всяка сутрин"), ("visit", "посещавам"), ("present", "подарък")]),
            "exercises": [
                C("С кого е Кейт?", ["Със сестра си", "С Елена", "С приятелка"], 0, instruction=RQ),
                C("Колко време е в Барселона?", ["Една седмица", "Един ден", "Един месец"], 0, instruction=RQ),
                C("Къде е хотелът?", ["Близо до плажа", "В центъра", "До летището"], 0, instruction=RQ),
                C("Кога се връща Кейт?", ["В неделя", "Във вторник", "В събота"], 0, instruction=RQ),
                C("Какво иска Кейт?", ["Да се видят следващия вторник", "Елена да дойде в Барселона", "Да купи подарък"], 0, instruction=RQ),
                F("Every ___ we have breakfast in a café.", "morning"),
            ],
        },
        {
            "slug": "a1-opposites", "title": "Противоположни прилагателни", "title_en": "Opposite adjectives",
            "kind": "vocabulary", "minutes": 6, "xp": 15, "summary": "Голям и малък, евтин и скъп: учи думите по двойки.",
            "theory": """
<p>Прилагателните се запомнят по-лесно по двойки.</p>
<table>
<tr><th>Дума</th><th>Противоположно</th><th>Значение</th></tr>
<tr><td class="en">big</td><td class="en">small</td><td>голям / малък</td></tr>
<tr><td class="en">cheap</td><td class="en">expensive</td><td>евтин / скъп</td></tr>
<tr><td class="en">old</td><td class="en">new / young</td><td>стар / нов, млад</td></tr>
<tr><td class="en">hot</td><td class="en">cold</td><td>горещ / студен</td></tr>
<tr><td class="en">easy</td><td class="en">difficult</td><td>лесен / труден</td></tr>
<tr><td class="en">full</td><td class="en">empty</td><td>пълен / празен</td></tr>
<tr><td class="en">open</td><td class="en">closed</td><td>отворен / затворен</td></tr>
<tr><td class="en">early</td><td class="en">late</td><td>рано / късно</td></tr>
</table>
<div class="tip">Прилагателното е преди съществителното и не се променя: <span class="en">a big house, two big houses</span>.</div>
""",
            "exercises": [
                C("Противоположното на cheap:", ["expensive", "small", "old"], 0),
                C("The shop is ___ on Sundays. You can't go in.", ["closed", "open", "full"], 0),
                C("He is 90. He's very ___ .", ["old", "new", "late"], 0),
                C("Кое е правилно?", ["two big houses", "two bigs houses"], 0),
                F("The bus is ___ . There are no seats. (пълен)", "full"),
                O("Тестът е лесен.", "The test is easy"),
            ],
        },
    ],
    "a1-speak-write": [
        {
            "slug": "a1-write-my-day", "title": "Пиши: моят ден", "title_en": "Writing: my daily routine",
            "kind": "writing", "minutes": 7, "xp": 15, "summary": "Кратък текст за ежедневието в Present Simple.",
            "theory": model_text("My day", [
                "I get up at seven o'clock and I have coffee and toast for breakfast.",
                "I start work at nine. I work in an office in the city centre.",
                "In the evening I usually cook dinner and watch TV. Sometimes I go to the gym.",
                "I go to bed at eleven.",
            ], [("I get up at seven o'clock", "кога (at + час)"), ("I start work at nine", "Present Simple за навици"),
                ("usually, sometimes", "колко често: преди глагола"), ("In the evening...", "редът на деня")]) + """
<div class="tip">При <span class="en">he / she</span> добави <span class="en">-s</span>: <span class="en">She gets up at seven.</span></div>
""",
            "exercises": [
                C("I ___ up at 7 every day.", ["get", "gets", "getting"], 0),
                C("My sister ___ in a bank.", ["works", "work", "working"], 0),
                C("Къде стои usually?", ["I usually cook dinner.", "I cook usually dinner.", "Usually I dinner cook."], 0),
                F("I go to bed ___ eleven.", "at"),
                O("Вечер гледам телевизия.", "In the evening I watch TV"),
                T("Понякога ходя на фитнес.", "Sometimes I go to the gym|I sometimes go to the gym"),
            ],
        },
    ],
    # ---------------- A2 ----------------
    "a2-listening": [
        {
            "slug": "a2-listen-tour", "title": "Обиколка с екскурзовод", "title_en": "A guided tour", "kind": "listening",
            "minutes": 7, "xp": 20, "summary": "Екскурзоводът обяснява програмата за деня.", "theory": INTRO,
            "dialogue": dialogue(
                ("Guide", "Good morning, everyone, and welcome to York! My name's Tom and I'm your guide today.", "Добро утро на всички и добре дошли в Йорк! Казвам се Том и днес съм вашият екскурзовод."),
                ("Guide", "First, we're going to walk along the old city walls. It takes about forty minutes.", "Първо ще се разходим по старите градски стени. Отнема около четиридесет минути."),
                ("Guide", "Then we'll visit the cathedral. Please remember, you can take photos inside, but no flash.", "После ще посетим катедралата. Моля, запомнете: може да снимате вътре, но без светкавица."),
                ("Guide", "At half past twelve we'll stop for lunch. You'll have an hour and a half free.", "В дванадесет и половина спираме за обяд. Ще имате час и половина свободно време."),
                ("Guide", "We meet again at two o'clock in front of the museum. Please don't be late, because the bus leaves at quarter past two.", "Срещаме се отново в два часа пред музея. Моля, не закъснявайте, защото автобусът тръгва в два и петнадесет."),
            ),
            "exercises": [
                C("Какво правят първо?", ["Разходка по градските стени", "Посещение на катедралата", "Обяд"], 0, instruction=DQ),
                C("Какво не е разрешено в катедралата?", ["Светкавица", "Снимки", "Разговори"], 0, instruction=DQ),
                C("Колко свободно време имат за обяд?", ["Час и половина", "Час", "40 минути"], 0, instruction=DQ),
                C("Къде се срещат в 14:00?", ["Пред музея", "Пред катедралата", "В автобуса"], 0, instruction=DQ),
                C("Кога тръгва автобусът?", ["В 14:15", "В 14:00", "В 12:30"], 0, instruction=DQ),
                D("Please don't be late."),
            ],
        },
    ],
    "a2-pronunciation": [
        {
            "slug": "a2-pron-contractions", "title": "Съкращения: I'm, don't, won't", "title_en": "Contractions",
            "kind": "pronunciation", "minutes": 6, "xp": 20, "summary": "Как говорят носителите: кратко и свързано.",
            "theory": """
<p>В разговор носителите почти винаги съкращават. Ако казваш всичко пълно (<span class="en">I am, do not</span>), звучи официално или подчертано.</p>
<table>
<tr><th>Пълно</th><th>Съкратено</th><th>Звучи като</th></tr>
<tr><td class="en">I am</td><td class="en">I'm</td><td>„айм“</td></tr>
<tr><td class="en">do not</td><td class="en">don't</td><td>„доунт“</td></tr>
<tr><td class="en">will not</td><td class="en">won't</td><td>„уоунт“ (не „уонт“ като want)</td></tr>
<tr><td class="en">I would / I had</td><td class="en">I'd</td><td>„айд“</td></tr>
<tr><td class="en">they are</td><td class="en">they're</td><td>„дер“</td></tr>
<tr><td class="en">it is</td><td class="en">it's</td><td>„итс“</td></tr>
</table>
<div class="tip"><span class="en">won't</span> и <span class="en">want</span> звучат различно: „уоунт“ срещу „уонт“. Слушай внимателно.</div>
""",
            "exercises": [
                L("Коя дума чу?", "I won't go.", ["won't", "want"], 0),
                L("Коя дума чу?", "I want to go.", ["won't", "want"], 1),
                C("I'd like a coffee. I'd = ?", ["I would", "I had", "I did"], 0),
                C("They're late. They're = ?", ["They are", "Their", "There"], 0),
                S("I'm sorry, I don't know."),
                S("It's OK, they're coming."),
                D("I don't think it's open."),
            ],
        },
    ],
    "a2-skills": [
        {
            "slug": "a2-read-timetable", "title": "Четене: разписание на влакове", "title_en": "Reading: a train timetable",
            "kind": "reading", "minutes": 7, "xp": 20, "summary": "Умение: таблици, часове и бележки под линия.",
            "theory": """<div class="tip"><strong>Умение: таблици и бележки.</strong> В разписанията важното често е в малкия текст отдолу: промени, дни, в които влакът не се движи, места за прекачване.</div>""" + reading("London to Oxford: weekday trains", [
                "Train A: departs London Paddington 08:15, arrives Oxford 09:10. Direct.",
                "Train B: departs 09:05, arrives 10:20. Change at Reading.",
                "Train C: departs 09:45, arrives 10:40. Direct. Not on Fridays.",
                "Train D: departs 10:30, arrives 11:25. Direct. Quiet coach available.",
                "Note: Off-peak tickets are valid on all trains after 09:30. Seats can be reserved online until 2 hours before departure.",
            ], [("departs", "тръгва"), ("arrives", "пристига"), ("direct", "директен"), ("change at", "прекачване в"),
                ("quiet coach", "тих вагон"), ("off-peak", "извън пиковите часове (по-евтин)"), ("valid", "валиден")]),
            "exercises": [
                C("Кой влак има прекачване?", ["B", "A", "C", "D"], 0, instruction=RQ),
                C("Пътуваш в петък и искаш директен влак след 9:30. Кой?", ["D", "C", "B", "A"], 0, instruction=RQ),
                C("Колко време пътува влак A?", ["55 минути", "1 час и 15 минути", "45 минути"], 0, instruction=RQ),
                C("Имаш off-peak билет. Можеш ли да хванеш влак A?", ["Не, тръгва преди 9:30", "Да", "Само в петък"], 0, instruction=RQ),
                C("Кой влак има тих вагон?", ["D", "A", "C", "B"], 0, instruction=RQ),
                F("The train ___ at 08:15. (тръгва)", "departs|leaves"),
            ],
        },
        {
            "slug": "a2-feelings", "title": "Чувства и емоции", "title_en": "Feelings and emotions",
            "kind": "vocabulary", "minutes": 7, "xp": 20, "summary": "Как да кажеш как се чувстваш по-точно от happy и sad.",
            "theory": """
<table>
<tr><th>Дума</th><th>Значение</th><th>Пример</th></tr>
<tr><td class="en">excited</td><td>развълнуван (радостно)</td><td class="en">I'm excited about the trip.</td></tr>
<tr><td class="en">nervous</td><td>притеснен, нервен</td><td class="en">I'm nervous about the exam.</td></tr>
<tr><td class="en">worried</td><td>тревожен</td><td class="en">She's worried about her dad.</td></tr>
<tr><td class="en">upset</td><td>разстроен</td><td class="en">He was upset when he lost.</td></tr>
<tr><td class="en">embarrassed</td><td>смутен, засрамен</td><td class="en">I was so embarrassed!</td></tr>
<tr><td class="en">relaxed</td><td>отпуснат, спокоен</td><td class="en">I feel relaxed on holiday.</td></tr>
<tr><td class="en">disappointed</td><td>разочарован</td><td class="en">We were disappointed with the hotel.</td></tr>
<tr><td class="en">homesick</td><td>тъгувам за дома</td><td class="en">I sometimes feel homesick.</td></tr>
</table>
<div class="tip"><span class="en">Embarrassed</span> не е „бременна“! Бременна е <span class="en">pregnant</span>.</div>
""",
            "exercises": [
                C("I have a job interview tomorrow. I'm ___ .", ["nervous", "relaxed", "homesick"], 0),
                C("The concert was cancelled. We were ___ .", ["disappointed", "excited", "relaxed"], 0),
                C("I fell over in front of everyone. I was so ___ !", ["embarrassed", "pregnant", "worried"], 0),
                C("I miss my family and my country. I'm ___ .", ["homesick", "upset", "nervous"], 0),
                F("I'm really ___ about my holiday next week! (развълнуван)", "excited"),
                O("Тя се тревожи за майка си.", "She is worried about her mother|She's worried about her mother|She is worried about her mum"),
            ],
        },
    ],
    "a2-past-events": [
        {
            "slug": "a2-subject-questions", "title": "Who called you? или Who did you call?", "title_en": "Subject and object questions",
            "kind": "grammar", "minutes": 7, "xp": 20, "summary": "Кога въпросът е без do / did.",
            "theory": """
<table>
<tr><th>Питаме за</th><th>Въпрос</th><th>Отговор</th></tr>
<tr><td>подлога (кой извърши действието)</td><td class="en">Who called you?</td><td class="en"><strong>Maria</strong> called me.</td></tr>
<tr><td>допълнението (на кого / какво)</td><td class="en">Who did you call?</td><td class="en">I called <strong>Maria</strong>.</td></tr>
<tr><td>подлога</td><td class="en">What happened?</td><td class="en">Nothing happened.</td></tr>
<tr><td>допълнението</td><td class="en">What did you see?</td><td class="en">I saw a film.</td></tr>
</table>
<div class="tip">Когато <span class="en">who / what</span> е подлог, няма <span class="en">do / does / did</span>: <span class="en">What happened?</span>, не <em>What did happen?</em></div>
""",
            "exercises": [
                C("___ ? (Какво се случи?)", ["What happened", "What did happen", "What did happened"], 0),
                C("___ the window? Tom broke it.", ["Who broke", "Who did break", "Who did broke"], 0),
                C("___ at the party? I met Anna.", ["Who did you meet", "Who met you", "Who you met"], 0),
                C("___ in this house? My grandparents live here.", ["Who lives", "Who does live", "Who do live"], 0),
                F("Who ___ you this present? My brother gave it to me.", "gave"),
                O("Кого видя вчера?", "Who did you see yesterday"),
            ],
        },
    ],
    "a2-speak-write": [
        {
            "slug": "a2-write-thank-you", "title": "Пиши: благодарствено писмо", "title_en": "Writing: a thank-you note",
            "kind": "writing", "minutes": 7, "xp": 20, "summary": "Благодари за подарък, гостуване или помощ.",
            "theory": model_text("Thank you!", [
                "Dear Mr and Mrs Brown,",
                "Thank you so much for having me last weekend. I really enjoyed staying with you.",
                "The dinner on Saturday was delicious, and it was great to see the lake. Thanks also for the lovely book.",
                "I hope you can visit me in Sofia one day.",
                "Best wishes,",
                "Nina",
            ], [("Thank you so much for having me", "благодарност за гостуване (for + -ing)"),
                ("I really enjoyed...", "какво ти е харесало"), ("Thanks also for...", "втора благодарност"),
                ("I hope you can visit me...", "покана за бъдещето"), ("Best wishes,", "топъл, но учтив край")]) + """
<div class="tip">След <span class="en">thank you for</span> идва съществително или -ing: <span class="en">Thank you for the present. Thank you for helping me.</span></div>
""",
            "exercises": [
                C("Thank you for ___ me.", ["helping", "help", "to help"], 0),
                C("Подходящ край до семейството на приятел:", ["Best wishes,", "Yours faithfully,", "Regards, Mr Ivanov"], 0),
                C("Благодарност за гостуване:", ["Thank you for having me.", "Thank you for taking me.", "Thank you for keeping me."], 0),
                F("I really ___ the dinner. (харесах)", "enjoyed|liked|loved"),
                O("Надявам се да ме посетите.", "I hope you can visit me|I hope you visit me"),
            ],
        },
    ],
    # ---------------- B1 ----------------
    "b1-listening": [
        {
            "slug": "b1-listen-gym", "title": "Записване във фитнес", "title_en": "Joining a gym", "kind": "listening",
            "minutes": 7, "xp": 25, "summary": "Видове членство, цени и условия.", "theory": INTRO,
            "dialogue": dialogue(
                ("Staff", "Hi, are you interested in joining?", "Здравейте, интересувате ли се от членство?"),
                ("Viktor", "Yes. What kind of memberships do you have?", "Да. Какви видове членство имате?"),
                ("Staff", "There are two. The standard one is thirty pounds a month and you can come any time. The off-peak one is twenty, but only before four in the afternoon.", "Има два вида. Стандартното е тридесет паунда на месец и може да идвате по всяко време. Извънпиковото е двадесет, но само преди четири следобед."),
                ("Viktor", "I work until five, so I'd need the standard one. Are classes included?", "Работя до пет, така че ще ми трябва стандартното. Включени ли са групови занимания?"),
                ("Staff", "Yes, all classes are included, but you need to book them on our app at least a day before.", "Да, всички занимания са включени, но трябва да ги запазите в приложението ни поне ден по-рано."),
                ("Viktor", "Is there a minimum contract?", "Има ли минимален договор?"),
                ("Staff", "Three months. After that, you can cancel with one month's notice.", "Три месеца. След това можете да прекратите с едномесечно предизвестие."),
                ("Viktor", "OK. And can I try it first?", "Добре. А мога ли първо да пробвам?"),
                ("Staff", "Sure, your first visit is free. Just bring some ID.", "Разбира се, първото посещение е безплатно. Носете само документ за самоличност."),
            ),
            "exercises": [
                C("Защо Виктор избира стандартното членство?", ["Работи до пет", "По-евтино е", "Включва басейн"], 0, instruction=DQ),
                C("Колко струва стандартното членство?", ["£30 на месец", "£20 на месец", "£30 на седмица"], 0, instruction=DQ),
                C("Как се запазват заниманията?", ["В приложението, поне ден по-рано", "На рецепцията", "Не е нужно"], 0, instruction=DQ),
                C("Какъв е минималният договор?", ["Три месеца", "Един месец", "Година"], 0, instruction=DQ),
                C("Какво трябва да носи за пробното посещение?", ["Документ за самоличност", "Снимка", "£20"], 0, instruction=DQ),
                L("Какво означава one month's notice?", "You can cancel with one month's notice.", ["едномесечно предизвестие", "един безплатен месец", "месечна такса"], 0),
                D("Is there a minimum contract?"),
            ],
        },
    ],
    "b1-plans-possibilities": [
        {
            "slug": "b1-so-neither", "title": "So do I, neither do I", "title_en": "Agreeing with so and neither",
            "kind": "grammar", "minutes": 6, "xp": 20, "summary": "„И аз“ и „и аз не“: кратки реакции в разговор.",
            "theory": """
<table>
<tr><th>Казват</th><th>И аз (също)</th><th>Аз не</th></tr>
<tr><td class="en">I like coffee.</td><td class="en">So do I.</td><td class="en">I don't.</td></tr>
<tr><td class="en">I don't like tea.</td><td class="en">Neither do I. / Me neither.</td><td class="en">I do.</td></tr>
<tr><td class="en">I'm tired.</td><td class="en">So am I.</td><td class="en">I'm not.</td></tr>
<tr><td class="en">I can't swim.</td><td class="en">Neither can I.</td><td class="en">I can.</td></tr>
<tr><td class="en">I went to Paris.</td><td class="en">So did I.</td><td class="en">I didn't.</td></tr>
</table>
<div class="tip">Спомагателният глагол е същият като в изречението: <span class="en">am → So am I</span>, <span class="en">can't → Neither can I</span>, сегашно време → <span class="en">do</span>, минало → <span class="en">did</span>.</div>
""",
            "exercises": [
                C("„I love travelling.“ „___“", ["So do I.", "So am I.", "Neither do I."], 0),
                C("„I'm hungry.“ „___“", ["So am I.", "So do I.", "Neither am I."], 0),
                C("„I didn't sleep well.“ „___“", ["Neither did I.", "So did I.", "Neither do I."], 0),
                C("„I can't drive.“ „___“", ["Neither can I.", "So can I.", "Neither do I."], 0),
                F("„I've been to London.“ „So ___ I.“", "have"),
                S("Neither do I."),
            ],
        },
    ],
    "b1-skills": [
        {
            "slug": "b1-read-news", "title": "Четене: кратка новина", "title_en": "Reading: a news story",
            "kind": "reading", "minutes": 8, "xp": 25, "summary": "Умение: кой, какво, къде, кога, защо.",
            "theory": """<div class="tip"><strong>Умение: четене на новини.</strong> Първото изречение (лийдът) обикновено отговаря на кой, какво, къде и кога. Следващите абзаци дават подробности и мнения.</div>""" + reading("Tourist returns lost wallet with €2,000", [
                "A British tourist has been praised after returning a wallet containing more than €2,000 that he found on a beach in Sozopol on Tuesday.",
                "Mark Ellis, 34, from Leeds, noticed the wallet in the sand while he was walking his dog early in the morning. Inside, he found cash, credit cards and an ID card.",
                "He took it straight to the local police station, where officers contacted the owner, a 68-year-old fisherman who had lost it the evening before.",
                "'I couldn't believe it,' said the owner. 'That money was for my grandson's university fees.' Mr Ellis refused to accept a reward.",
            ], [("praised", "похвален"), ("containing", "съдържащ"), ("noticed", "забеляза"), ("straight", "направо"),
                ("fees", "такси"), ("refused", "отказа"), ("reward", "награда")]),
            "exercises": [
                C("Къде е намерен портфейлът?", ["На плаж в Созопол", "В полицията", "В хотел в Лийдс"], 0, instruction=RQ),
                C("Какво е правел Марк, когато го е намерил?", ["Разхождал е кучето си", "Плувал е", "Ловил е риба"], 0, instruction=RQ),
                C("Кой е собственикът?", ["68-годишен рибар", "Студент", "Полицай"], 0, instruction=RQ),
                C("За какво са били парите?", ["За университетските такси на внука", "За нова лодка", "За почивка"], 0, instruction=RQ),
                C("Какво прави Марк накрая?", ["Отказва награда", "Взима награда", "Отива на плажа"], 0, instruction=RQ),
                F("He took the wallet ___ to the police station. (направо)", "straight"),
            ],
        },
        {
            "slug": "b1-environment", "title": "Околна среда", "title_en": "The environment",
            "kind": "vocabulary", "minutes": 7, "xp": 25, "summary": "Recycling, pollution, waste: думите за често срещана изпитна тема.",
            "theory": """
<table>
<tr><th>Дума</th><th>Значение</th></tr>
<tr><td class="en">pollution</td><td>замърсяване</td></tr>
<tr><td class="en">climate change</td><td>климатични промени</td></tr>
<tr><td class="en">recycle / recycling</td><td>рециклирам / рециклиране</td></tr>
<tr><td class="en">waste</td><td>отпадъци; прахосвам</td></tr>
<tr><td class="en">plastic bottles, packaging</td><td>пластмасови бутилки, опаковки</td></tr>
<tr><td class="en">renewable energy</td><td>възобновяема енергия</td></tr>
<tr><td class="en">reduce, reuse</td><td>намалявам, използвам повторно</td></tr>
<tr><td class="en">public transport</td><td>градски транспорт</td></tr>
<tr><td class="en">endangered species</td><td>застрашени видове</td></tr>
</table>
<div class="tip"><span class="en">Waste</span> е и глагол: <span class="en">Don't waste water.</span> Не хаби вода.</div>
""",
            "exercises": [
                C("Air ___ is a big problem in big cities.", ["pollution", "recycling", "energy"], 0),
                C("Solar and wind power are ___ energy.", ["renewable", "endangered", "public"], 0),
                C("Don't ___ food. Buy only what you need.", ["waste", "recycle", "reduce"], 0),
                C("Pandas are an ___ species.", ["endangered", "renewable", "public"], 0),
                F("I always ___ glass and paper. (рециклирам)", "recycle"),
                T("Ползвам градски транспорт.", "I use public transport|I take public transport|I use public transportation"),
            ],
        },
    ],
    "b1-speak-write": [
        {
            "slug": "b1-write-for-against", "title": "Пиши: есе „за и против“", "title_en": "Writing: a for-and-against essay",
            "kind": "writing", "minutes": 9, "xp": 25, "summary": "Предимства, недостатъци и твое заключение.",
            "theory": model_text("Is it better to live in a city or in the countryside?", [
                "Nowadays more and more people move to big cities, but is city life really better?",
                "On the one hand, cities offer more jobs, better public transport and lots of things to do in the evenings.",
                "On the other hand, life in the city is expensive and stressful. The air is often polluted, and it can be hard to find a quiet place.",
                "In my opinion, the countryside is better for families, while cities are better for young people who want to build a career.",
            ], [("Nowadays... but is... really better?", "въвеждане на темата с въпрос"),
                ("On the one hand,", "аргументи за"), ("On the other hand,", "аргументи против"),
                ("In my opinion,", "твоето мнение в края")]) + """
<div class="tip">Добави още свързващи думи: <span class="en">Firstly, In addition, However, To sum up</span>.</div>
""",
            "exercises": [
                C("Кой израз въвежда аргументите против?", ["On the other hand,", "On the one hand,", "In addition,"], 0),
                C("Къде обикновено е мнението ти в есето „за и против“?", ["В заключението", "В първото изречение", "Никъде"], 0),
                C("Аргумент против живота в града:", ["The air is often polluted.", "There are more jobs.", "There's a lot to do."], 0),
                F("To ___ up, both places have advantages.", "sum"),
                O("От една страна, градовете предлагат повече работа.", "On the one hand cities offer more jobs"),
            ],
        },
    ],
    # ---------------- B2 ----------------
    "b2-listening": [
        {
            "slug": "b2-listen-habits", "title": "Подкаст: как се създават навици", "title_en": "Podcast: how habits form",
            "kind": "listening", "minutes": 8, "xp": 30, "summary": "Защо силната воля не е достатъчна.", "theory": INTRO,
            "dialogue": dialogue(
                ("Host", "So, why do most New Year's resolutions fail by February?", "И така, защо повечето новогодишни обещания се провалят до февруари?"),
                ("Guest", "Because people rely on willpower, and willpower is a bit like a battery. By the end of a long day, it's flat.", "Защото хората разчитат на силата на волята, а тя е малко като батерия. В края на дълъг ден е изтощена."),
                ("Host", "So what works instead?", "Тогава какво работи?"),
                ("Guest", "Making the habit automatic. The trick is to attach it to something you already do. For example, 'after I brush my teeth, I'll do two minutes of stretching.'", "Да направиш навика автоматичен. Номерът е да го закачиш за нещо, което вече правиш. Например: „След като си измия зъбите, ще се разтягам две минути.“"),
                ("Host", "Only two minutes?", "Само две минути?"),
                ("Guest", "Absolutely. Start ridiculously small. The aim at first isn't fitness, it's simply turning up. Once the habit is established, you can build on it.", "Абсолютно. Започнете нелепо малко. Целта в началото не е форма, а просто да се появявате. Щом навикът се затвърди, можете да надграждате."),
                ("Host", "And if you miss a day?", "А ако пропуснете ден?"),
                ("Guest", "Missing once doesn't matter much. The real danger is missing twice in a row, because that's when a new pattern starts.", "Едно пропускане няма голямо значение. Истинската опасност е да пропуснете два пъти поред, защото тогава започва нов модел."),
            ),
            "exercises": [
                C("Защо обещанията се провалят според госта?", ["Хората разчитат на волята, която се изчерпва", "Целите са твърде малки", "Февруари е труден месец"], 0, instruction=DQ),
                C("Какъв е номерът за нов навик?", ["Да го свържеш с нещо, което вече правиш", "Да правиш много наведнъж", "Да чакаш мотивация"], 0, instruction=DQ),
                C("Каква е целта в началото?", ["Просто да го правиш редовно", "Да станеш във форма", "Да отслабнеш"], 0, instruction=DQ),
                C("Кое е истинската опасност?", ["Да пропуснеш два пъти поред", "Да пропуснеш веднъж", "Да започнеш твърде рано"], 0, instruction=DQ),
                L("Какво означава it's flat?", "By the end of the day, it's flat.", ["изтощена е", "равна е", "скучна е"], 0),
                L("Какво означава in a row?", "Missing twice in a row.", ["поред", "в редица", "в групата"], 0),
                D("Start ridiculously small."),
            ],
        },
    ],
    "b2-pronunciation": [
        {
            "slug": "b2-pron-weak-forms", "title": "Слаби форми: to, for, can, was", "title_en": "Weak forms",
            "kind": "pronunciation", "minutes": 7, "xp": 30, "summary": "Защо носителите „гълтат“ малките думи и как да ги чуваш.",
            "theory": """
<p>Служебните думи без ударение се произнасят с неясния звук „ъ“ (schwa). Затова е трудно да ги чуеш.</p>
<table>
<tr><th>Дума</th><th>Силна форма</th><th>Слаба форма</th><th>Пример</th></tr>
<tr><td class="en">to</td><td>„ту“</td><td>„тъ“</td><td class="en">I want to go.</td></tr>
<tr><td class="en">for</td><td>„фор“</td><td>„фъ“</td><td class="en">It's for you.</td></tr>
<tr><td class="en">can</td><td>„кен“</td><td>„кън“</td><td class="en">I can swim.</td></tr>
<tr><td class="en">was</td><td>„уоз“</td><td>„уъз“</td><td class="en">She was late.</td></tr>
<tr><td class="en">and</td><td>„енд“</td><td>„ън“</td><td class="en">fish and chips</td></tr>
<tr><td class="en">of</td><td>„ов“</td><td>„ъв“</td><td class="en">a cup of tea</td></tr>
</table>
<div class="tip">Важно: <span class="en">I <strong>can't</strong> swim</span> е с ударение и ясно „кант“, а <span class="en">I can swim</span> е със слабо „кън“. Ударението ти казва кое е.</div>
""",
            "exercises": [
                L("Чу ли can или can't?", "I can come tomorrow.", ["can", "can't"], 0),
                L("Чу ли can или can't?", "I can't come tomorrow.", ["can", "can't"], 1),
                C("Как звучи to в I want to go?", ["Слабо „тъ“", "Силно „ту“", "Не се чува изобщо"], 0),
                C("Кога използваме силната форма?", ["Когато думата е подчертана или в края на изречението", "Винаги", "Никога"], 0),
                S("A cup of tea, please."),
                S("I was waiting for you."),
                D("What are you looking for?"),
            ],
        },
    ],
    "b2-skills": [
        {
            "slug": "b2-read-fact-opinion", "title": "Четене: факт или мнение", "title_en": "Reading: fact or opinion",
            "kind": "reading", "minutes": 9, "xp": 30, "summary": "Умение: да различаваш доказано от мнението на автора.",
            "theory": """<div class="tip"><strong>Умение: факт или мнение.</strong> Фактите могат да се проверят (числа, дати, събития). Мненията издават оценъчни думи: <span class="en">should, best, clearly, unfortunately, I believe</span>.</div>""" + reading("Should schools ban mobile phones?", [
                "In 2023, several European countries, including the Netherlands, introduced rules restricting phones in classrooms.",
                "Teachers in these schools report that pupils talk to each other more during breaks.",
                "Clearly, this is the best decision any government has made about education in years.",
                "A smartphone in a pocket is simply too tempting for a teenager, and we should stop pretending otherwise.",
                "However, some parents worry that they cannot reach their children in an emergency.",
            ], [("restricting", "ограничаващи"), ("pupils", "ученици"), ("report", "съобщават"),
                ("tempting", "изкушаващ"), ("pretend", "преструвам се"), ("reach", "свързвам се с")]),
            "exercises": [
                C("Изречение 1 (In 2023, several countries...) е:", ["Факт", "Мнение"], 0, instruction=RQ),
                C("Изречение 3 (Clearly, this is the best decision...) е:", ["Мнение", "Факт"], 0, instruction=RQ),
                C("Коя дума издава мнение в изречение 4?", ["should", "pocket", "teenager"], 0, instruction=RQ),
                C("Изречение 2 (Teachers report that...) е:", ["Факт: казва какво съобщават учителите", "Мнение на автора"], 0, instruction=RQ),
                C("Каква е позицията на автора?", ["Подкрепя забраната", "Против забраната", "Неутрален"], 0, instruction=RQ),
            ],
        },
        {
            "slug": "b2-relationship-phrasals", "title": "Фразови глаголи за отношения", "title_en": "Phrasal verbs for relationships",
            "kind": "vocabulary", "minutes": 8, "xp": 30, "summary": "Get on with, fall out, make up, look up to.",
            "theory": """
<table>
<tr><th>Фразов глагол</th><th>Значение</th><th>Пример</th></tr>
<tr><td class="en">get on (well) with</td><td>разбирам се с</td><td class="en">I get on well with my boss.</td></tr>
<tr><td class="en">fall out (with)</td><td>скарвам се (с)</td><td class="en">They fell out over money.</td></tr>
<tr><td class="en">make up</td><td>сдобрявам се</td><td class="en">They argued but made up the next day.</td></tr>
<tr><td class="en">look up to</td><td>уважавам, възхищавам се на</td><td class="en">I've always looked up to my grandmother.</td></tr>
<tr><td class="en">let down</td><td>разочаровам, подвеждам</td><td class="en">Don't let me down.</td></tr>
<tr><td class="en">split up / break up</td><td>разделям се</td><td class="en">They split up after five years.</td></tr>
<tr><td class="en">put up with</td><td>търпя</td><td class="en">I can't put up with the noise.</td></tr>
<tr><td class="en">bring up</td><td>отглеждам (дете)</td><td class="en">She was brought up by her aunt.</td></tr>
</table>
""",
            "exercises": [
                C("My sister and I ___ when we were kids, but now we're close.", ["fell out a lot", "looked up to", "brought up"], 0),
                C("He promised to help, but he ___ me ___ .", ["let / down", "made / up", "put / up"], 0),
                C("I really ___ my teacher. She's amazing.", ["look up to", "put up with", "fall out"], 0),
                C("They had a big argument but ___ an hour later.", ["made up", "split up", "brought up"], 0),
                F("Do you get ___ well with your neighbours?", "on"),
                F("I was brought ___ in a small village.", "up"),
            ],
        },
    ],
    "b2-speak-write": [
        {
            "slug": "b2-write-advice-email", "title": "Пиши: имейл със съвет", "title_en": "Writing: an email giving advice",
            "kind": "writing", "minutes": 9, "xp": 30, "summary": "Отговори на приятел, който иска съвет: топло, ясно, полезно.",
            "theory": model_text("Re: Moving to Bulgaria?", [
                "Hi Sam,",
                "Great to hear from you! I can't believe you're thinking of moving to Sofia. That's brilliant news.",
                "If I were you, I'd rent a flat in the centre for the first few months, so you can get to know the city before deciding where to live. It might also be worth learning the Cyrillic alphabet before you come; it'll make everything much easier.",
                "As for work, have you thought about contacting some of the international companies? Many of them are looking for native English speakers.",
                "Let me know when you're coming and I'll show you around!",
                "All the best,",
                "Dimitar",
            ], [("Great to hear from you!", "топло, неформално начало"),
                ("If I were you, I'd...", "съвет (втори условни)"),
                ("It might be worth + -ing", "мек съвет"),
                ("As for work,", "смяна на темата"),
                ("have you thought about + -ing?", "съвет като въпрос"),
                ("Let me know... I'll show you around!", "приятелски край")]),
            "exercises": [
                C("Кое е правилно?", ["If I were you, I'd rent a flat.", "If I was you, I will rent a flat.", "If I am you, I'd rent a flat."], 0),
                C("It might be worth ___ the alphabet.", ["learning", "to learn", "learn"], 0),
                C("Have you thought about ___ them?", ["contacting", "to contact", "contact"], 0),
                C("Кой израз сменя темата?", ["As for work,", "All the best,", "If I were you,"], 0),
                F("Let me know and I'll show you ___ ! (ще те разведа)", "around|round"),
                O("Ако бях на твое място, бих останал.", "If I were you I would stay|If I were you I'd stay"),
            ],
        },
    ],
    "b2-complex-structures": [
        {
            "slug": "b2-articles-advanced", "title": "Членове: кога без the", "title_en": "Articles: advanced use",
            "kind": "grammar", "minutes": 8, "xp": 25, "summary": "Life, the life, the UK, Lake Ohrid: правилата, които объркват.",
            "theory": """
<table>
<tr><th>Без член</th><th>С the</th></tr>
<tr><td>общо: <span class="en">Life is short. I love music.</span></td><td>конкретно: <span class="en">the life of Mozart, the music in this film</span></td></tr>
<tr><td>повечето държави: <span class="en">Bulgaria, France</span></td><td>с „множество“ или държава: <span class="en">the UK, the USA, the Netherlands</span></td></tr>
<tr><td>езера, планински върхове: <span class="en">Lake Ohrid, Mount Musala</span></td><td>реки, морета, планински вериги: <span class="en">the Danube, the Black Sea, the Alps</span></td></tr>
<tr><td>институции като цел: <span class="en">go to school, in hospital, in prison</span></td><td>сградата: <span class="en">I went to the school to meet the teacher.</span></td></tr>
<tr><td>хранене: <span class="en">have lunch</span></td><td>конкретно: <span class="en">The lunch was delicious.</span></td></tr>
</table>
<div class="tip">Най-честата грешка на българите е <span class="en">the</span> пред общи понятия: <em>The life is beautiful.</em> На английски: <span class="en">Life is beautiful.</span></div>
""",
            "exercises": [
                C("___ is hard sometimes.", ["Life", "The life"], 0),
                C("We swam in ___ Black Sea.", ["the", "—"], 0),
                C("I've never been to ___ Netherlands.", ["the", "—"], 0),
                C("She climbed ___ Mount Everest.", ["—", "the"], 0),
                C("He's in ___ hospital with a broken leg. (като пациент)", ["—", "the"], 0),
                C("The Danube flows into ___ .", ["the Black Sea", "Black Sea"], 0),
            ],
        },
    ],
    # ---------------- C1 ----------------
    "c1-listening": [
        {
            "slug": "c1-listen-heatwave", "title": "Радио: градовете и жегата", "title_en": "Radio: cities and heatwaves",
            "kind": "listening", "minutes": 9, "xp": 35, "summary": "Урбанист обяснява как градовете се подготвят за горещини.", "theory": INTRO,
            "dialogue": dialogue(
                ("Presenter", "Summers are getting hotter, and cities feel it most. Dr Ruiz, why are cities so much hotter than the surrounding countryside?", "Летата стават все по-горещи и градовете го усещат най-силно. Д-р Руис, защо градовете са толкова по-горещи от околността?"),
                ("Ruiz", "It's what we call the urban heat island effect. Concrete and asphalt absorb heat during the day and release it at night, so the city never really cools down.", "Това е т.нар. ефект на градския топлинен остров. Бетонът и асфалтът поглъщат топлина през деня и я отделят през нощта, така че градът никога не изстива истински."),
                ("Presenter", "And the night-time temperature is what really matters for health?", "И нощната температура е това, което наистина има значение за здравето?"),
                ("Ruiz", "Precisely. If the body can't recover overnight, the risk for elderly people rises sharply. That's often overlooked.", "Точно така. Ако тялото не може да се възстанови през нощта, рискът за възрастните хора рязко се покачва. Това често се пренебрегва."),
                ("Presenter", "What can cities realistically do?", "Какво могат реалистично да направят градовете?"),
                ("Ruiz", "Trees are the obvious answer, but they take decades to mature. In the short term, cities like Athens and Seville are painting roofs white and creating 'cool rooms' in libraries, where people can spend the hottest hours.", "Дърветата са очевидният отговор, но им трябват десетилетия, за да пораснат. В краткосрочен план градове като Атина и Севиля боядисват покривите в бяло и създават „хладни стаи“ в библиотеките, където хората могат да прекарат най-горещите часове."),
                ("Presenter", "Is that enough?", "Достатъчно ли е това?"),
                ("Ruiz", "On its own, no. But combined with early-warning systems and checking on vulnerable neighbours, it saves lives.", "Само по себе си не. Но в комбинация със системи за ранно предупреждение и грижа за уязвимите съседи спасява животи."),
            ),
            "exercises": [
                C("Какво причинява ефекта на топлинния остров?", ["Бетонът и асфалтът поглъщат и отделят топлина", "Липсата на вятър", "Колите"], 0, instruction=DQ),
                C("Защо нощната температура е важна?", ["Тялото не може да се възстанови", "Хората не могат да спят", "Повече ток се харчи"], 0, instruction=DQ),
                C("Защо дърветата не са бързо решение?", ["Растат десетилетия", "Скъпи са", "Не помагат"], 0, instruction=DQ),
                C("Какво правят Атина и Севиля?", ["Белят покриви и правят хладни стаи", "Садят гори", "Забраняват колите"], 0, instruction=DQ),
                C("Какво е мнението на д-р Руис за тези мерки?", ["Сами не стигат, но в комбинация спасяват животи", "Напълно достатъчни са", "Безполезни са"], 0, instruction=DQ),
                L("Какво означава overlooked?", "That's often overlooked.", ["пренебрегнато", "наблюдавано", "преувеличено"], 0),
                D("Trees take decades to mature."),
            ],
        },
    ],
    "c1-skills": [
        {
            "slug": "c1-read-paragraph-order", "title": "Четене: подреди абзаците", "title_en": "Reading: text structure",
            "kind": "reading", "minutes": 10, "xp": 35, "summary": "Умение: да следиш логиката и връзките в текста.",
            "theory": """<div class="tip"><strong>Умение: структура на текста.</strong> Абзаците се свързват чрез местоимения (<span class="en">this, such, these</span>), повторени думи и свързващи изрази. Абзац, който започва с <span class="en">This</span> или <span class="en">However</span>, не може да е първи.</div>""" + reading("The four-minute mile", [
                "[A] For decades, running a mile in under four minutes was considered physically impossible. Some doctors even warned that the attempt could be fatal.",
                "[B] Then, on 6 May 1954, a medical student called Roger Bannister ran it in 3 minutes 59.4 seconds.",
                "[C] What happened next is even more remarkable. Within just two months, another runner broke Bannister's record, and dozens followed in the years after.",
                "[D] This suggests that the barrier had never been purely physical. Once people believed it could be done, it became possible for many.",
            ], [("considered", "смятан за"), ("fatal", "фатален"), ("remarkable", "забележителен"),
                ("barrier", "бариера"), ("purely", "чисто, единствено")]),
            "exercises": [
                C("Защо [D] не може да е първи абзац?", ["Започва с This, което се отнася до нещо по-рано", "Твърде е кратък", "Има дата"], 0, instruction=RQ),
                C("Коя дума в [C] показва, че има предишно събитие?", ["next", "remarkable", "dozens"], 0, instruction=RQ),
                C("Каква е функцията на [A]?", ["Представя общото убеждение преди събитието", "Заключение", "Пример"], 0, instruction=RQ),
                C("Каква е главната идея на текста?", ["Границата е била повече психологическа, отколкото физическа", "Банистър е бил лекар", "Бягането е опасно"], 0, instruction=RQ),
                C("Какво означава remarkable?", ["забележителен", "забравен", "обикновен"], 0),
            ],
        },
    ],
    "c1-speak-write": [
        {
            "slug": "c1-write-profile", "title": "Пиши: професионален профил", "title_en": "Writing: a professional profile",
            "kind": "writing", "minutes": 9, "xp": 35, "summary": "Кратко представяне за CV или LinkedIn: точно, активно, без клишета.",
            "theory": model_text("Professional summary", [
                "Marketing manager with eight years' experience in the travel industry, specialising in digital campaigns for international audiences.",
                "Led a team of five that increased online bookings by 35% in two years, while reducing advertising costs.",
                "Fluent in English and German, with a strong background in data analysis and content strategy.",
                "Currently looking for a role where I can combine creativity with measurable results.",
            ], [("Marketing manager with eight years' experience...", "кой си: без I в началото"),
                ("Led a team... that increased... by 35%", "силен глагол + конкретен резултат с число"),
                ("Fluent in..., with a strong background in...", "умения, кратко"),
                ("Currently looking for a role where...", "какво търсиш")]) + """
<div class="tip">Избягвай празни клишета (<span class="en">hard-working, team player, passionate</span>). Покажи ги с факти: <span class="en">led, launched, reduced, increased</span> + число.</div>
""",
            "exercises": [
                C("Кое изречение е най-силно за профил?", ["Increased online sales by 35% in two years.", "I am very hard-working.", "I am a team player and passionate."], 0),
                C("Подходящ силен глагол:", ["launched", "did", "was responsible for doing"], 0),
                C("eight years' ___ (опит)", ["experience", "experiences", "experiment"], 0),
                F("Fluent ___ English and German.", "in"),
                O("Ръководих екип от петима.", "I led a team of five|Led a team of five"),
            ],
        },
    ],
    # ---------------- C2 ----------------
    "c2-listening": [
        {
            "slug": "c2-listen-understatement", "title": "Британското подценяване", "title_en": "British understatement",
            "kind": "listening", "minutes": 9, "xp": 40, "summary": "Когато „not bad“ означава „страхотно“, а „interesting“ означава „ужасно“.", "theory": INTRO + """
<div class="tip">Британците често казват по-малко, отколкото мислят. Слушай тона и контекста, не само думите.</div>
""",
            "dialogue": dialogue(
                ("Emma", "How was the job interview, then?", "Е, как мина интервюто?"),
                ("Oliver", "Not bad, actually. They offered me the job on the spot.", "Не беше зле всъщност. Предложиха ми работата на място."),
                ("Emma", "Not bad? That's amazing! And how was the drive there? I heard about the storm.", "Не беше зле? Това е невероятно! А как мина пътят дотам? Чух за бурята."),
                ("Oliver", "Well, it was a bit of a challenge. A tree came down right in front of the car.", "Ами, беше малко предизвикателство. Едно дърво падна точно пред колата."),
                ("Emma", "A bit of a challenge! And what did you think of their offices?", "Малко предизвикателство! А какво мислиш за офисите им?"),
                ("Oliver", "Interesting. Very... brave choice of colours.", "Интересни. Много... смел избор на цветове."),
                ("Emma", "So, awful, then.", "Значи ужасни."),
                ("Oliver", "I couldn't possibly comment. But I might bring sunglasses on my first day.", "Не бих могъл да коментирам. Но може би ще си взема слънчеви очила първия ден."),
            ),
            "exercises": [
                C("Какво означава Not bad в този контекст?", ["Отлично мина", "Средно мина", "Зле мина"], 0, instruction=DQ),
                C("Какво всъщност е било пътуването?", ["Опасно и стресиращо", "Леко и приятно", "Скучно"], 0, instruction=DQ),
                C("Какво мисли Оливър за офисите?", ["Харесват му малко, цветовете са ужасни", "Много са му харесали", "Не ги е видял"], 0, instruction=DQ),
                C("I couldn't possibly comment означава:", ["Иронично потвърждение, без да го казва", "Наистина не знае", "Забранено му е"], 0, instruction=DQ),
                C("Защо Оливър ще носи слънчеви очила?", ["Шега: цветовете са твърде ярки", "Офисът е на открито", "Има проблем с очите"], 0, instruction=DQ),
                L("Какво означава on the spot?", "They offered me the job on the spot.", ["веднага, на място", "на петното", "по-късно"], 0),
                D("It was a bit of a challenge."),
            ],
        },
    ],
    "c2-skills": [
        {
            "slug": "c2-binomials", "title": "Двойни изрази: by and large", "title_en": "Binomials",
            "kind": "vocabulary", "minutes": 8, "xp": 40, "summary": "Неизменни двойки думи, които правят речта естествена.",
            "theory": """
<p>Двойните изрази имат <strong>фиксиран ред</strong>. Не казваме <em>large and by</em> или <em>later or sooner</em>.</p>
<table>
<tr><th>Израз</th><th>Значение</th></tr>
<tr><td class="en">by and large</td><td>като цяло</td></tr>
<tr><td class="en">sooner or later</td><td>рано или късно</td></tr>
<tr><td class="en">odds and ends</td><td>дреболии, разни неща</td></tr>
<tr><td class="en">pros and cons</td><td>плюсове и минуси</td></tr>
<tr><td class="en">peace and quiet</td><td>тишина и спокойствие</td></tr>
<tr><td class="en">sick and tired (of)</td><td>писнало ми е (от)</td></tr>
<tr><td class="en">safe and sound</td><td>жив и здрав</td></tr>
<tr><td class="en">touch and go</td><td>несигурно, на косъм</td></tr>
<tr><td class="en">first and foremost</td><td>преди всичко</td></tr>
<tr><td class="en">trial and error</td><td>проба и грешка</td></tr>
</table>
""",
            "exercises": [
                C("They got home ___ after the storm.", ["safe and sound", "sound and safe", "touch and go"], 0),
                C("I'm ___ of waiting for him!", ["sick and tired", "tired and sick", "odds and ends"], 0),
                C("It was ___ whether we'd catch the flight.", ["touch and go", "by and large", "trial and error"], 0),
                C("___ , the project was a success. (като цяло)", ["By and large", "Large and by", "Sooner or later"], 0),
                F("We learned to cook by trial and ___ .", "error"),
                F("I just want some peace and ___ .", "quiet"),
            ],
        },
    ],
    "c2-nuance-style": [
        {
            "slug": "c2-ellipsis", "title": "Изпускане и заместване: so, not, do so", "title_en": "Ellipsis and substitution",
            "kind": "grammar", "minutes": 8, "xp": 35, "summary": "Как да не повтаряш думи и да звучиш естествено.",
            "theory": """
<table>
<tr><th>Похват</th><th>Пример</th></tr>
<tr><td><span class="en">so / not</span> вместо цяло изречение</td><td class="en">"Will it rain?" "I hope not. / I think so. / I'm afraid so."</td></tr>
<tr><td><span class="en">do so</span> (официално)</td><td class="en">Passengers may leave the train if they wish to do so.</td></tr>
<tr><td><span class="en">one / ones</span> вместо съществително</td><td class="en">I'll have the red one.</td></tr>
<tr><td>изпускане след спомагателен глагол</td><td class="en">"Have you finished?" "I have." / I'd help if I could.</td></tr>
<tr><td>изпускане на to-инфинитив</td><td class="en">"Come with us!" "I'd love to."</td></tr>
</table>
<div class="tip"><span class="en">I don't think so</span> е по-естествено от <span class="en">I think not</span>, което звучи старомодно или много официално.</div>
""",
            "exercises": [
                C("„Is the museum open today?“ „I'm afraid ___ .“ (не е)", ["not", "no", "don't"], 0),
                C("„Will you come?“ „I'd love ___ .“", ["to", "it", "so"], 0),
                C("„Is he coming?“ „I think ___ .“", ["so", "it", "yes"], 0),
                C("Those shoes are nice, but I prefer the black ___ .", ["ones", "one", "them"], 0),
                C("Guests may use the pool if they wish to ___ .", ["do so", "make so", "do it so"], 0),
                F("„Have you ever been to Japan?“ „No, but I'd like ___ .“", "to"),
            ],
        },
    ],
    "c2-speak-write": [
        {
            "slug": "c2-write-letter-editor", "title": "Пиши: писмо до редактора", "title_en": "Writing: a letter to the editor",
            "kind": "writing", "minutes": 10, "xp": 40, "summary": "Отговор на статия: учтиво несъгласие с аргументи.",
            "theory": model_text("Re: 'Tourists are ruining our coast' (12 June)", [
                "Sir,",
                "Your correspondent's article on tourism along the Black Sea coast made for uncomfortable, if somewhat one-sided, reading.",
                "While I share her concern about overdevelopment, it seems unfair to lay the blame at the door of visitors. It was, after all, local councils that approved the hotels now crowding our beaches.",
                "Tourism supports thousands of families in towns that would otherwise have little economic future. The question is not whether we welcome visitors, but how we manage their numbers.",
                "A modest tourist tax, invested in protecting the coastline, would surely serve both residents and guests better than resentment.",
                "Yours faithfully,",
                "K. Petrova, Varna",
            ], [("made for uncomfortable, if somewhat one-sided, reading", "учтива критика с отстъпка (if)"),
                ("While I share her concern..., it seems unfair to...", "съгласие, после несъгласие"),
                ("lay the blame at the door of", "идиом: обвинявам"),
                ("The question is not whether..., but how...", "преформулиране на дебата"),
                ("would surely serve... better than...", "конкретно предложение")]),
            "exercises": [
                C("Какво прави авторът в While I share her concern..., it seems unfair...?", ["Признава част от аргумента, после възразява", "Напълно се съгласява", "Сменя темата"], 0),
                C("Lay the blame at the door of означава:", ["обвинявам", "благодаря на", "посещавам"], 0),
                C("The question is not whether..., but how... служи за:", ["Преформулиране на дебата", "Въпрос към читателя", "Заключение без мнение"], 0),
                C("if somewhat one-sided. Какво означава if тук?", ["макар и", "ако", "дали"], 0),
                F("The question is not ___ we welcome visitors, but how we manage them.", "whether"),
            ],
        },
    ],
}

MISTAKES = {
    "a1-this-that": [
        ("This shoes are nice.", "These shoes are nice.", "Множествено число: these / those."),
    ],
    "a1-opposites": [
        ("two bigs houses", "two big houses", "Прилагателното не взима -s."),
    ],
    "a1-write-my-day": [
        ("She get up at seven.", "She gets up at seven.", "He / she / it: -s."),
    ],
    "a2-feelings": [
        ("I'm embarrassed. (за бременна)", "I'm pregnant.", "Embarrassed = смутен."),
        ("I'm boring.", "I'm bored.", "Как се чувстваш: -ed."),
    ],
    "a2-subject-questions": [
        ("What did happen?", "What happened?", "What е подлог: без did."),
        ("Who did call you?", "Who called you?", "Who е подлог: без did."),
    ],
    "a2-write-thank-you": [
        ("Thank you for help me.", "Thank you for helping me.", "След for: -ing."),
    ],
    "b1-so-neither": [
        ("„I'm tired.“ „So do I.“", "„I'm tired.“ „So am I.“", "Повтори същия спомагателен глагол."),
        ("„I don't like it.“ „Me too.“", "„I don't like it.“ „Me neither.“", "При отрицание: neither."),
    ],
    "b2-articles-advanced": [
        ("The life is beautiful.", "Life is beautiful.", "Общо понятие: без the."),
        ("in Black Sea", "in the Black Sea", "Морета и реки: the."),
    ],
    "b2-write-advice-email": [
        ("If I was you, I will...", "If I were you, I'd...", "Съвет: If I were you + would."),
    ],
    "c1-write-profile": [
        ("I am very hard-working and passionate.", "Increased sales by 35% in two years.", "Покажи с факти, не с клишета."),
    ],
    "c2-ellipsis": [
        ("I think yes.", "I think so.", "Думата е so."),
        ("I'm afraid no.", "I'm afraid not.", "Отрицание: not."),
    ],
}
