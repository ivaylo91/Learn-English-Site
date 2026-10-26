"""Conversation, reading and vocabulary lessons for every level.

Reading texts are kept short and close to the level (learners need to know about 98% of the words to read
without help), with a small glossary for the rest.
"""

from html import escape

from .courses import C, F, O, T

Q = "Отговори според текста"


def reading(title, paragraphs, glossary):
    """Reading box with a listen button, followed by a glossary table."""
    text = " ".join(paragraphs)
    body = "".join(f"<p>{escape(p)}</p>" for p in paragraphs)
    rows = "".join(f'<tr><td class="en">{escape(en)}</td><td>{escape(bg)}</td></tr>' for en, bg in glossary)
    return f"""
<p>Прочети текста. Ако искаш, първо го чуй. Непознатите думи са обяснени отдолу.</p>
<div class="reading" lang="en">
<h4><span>{escape(title)}</span><button type="button" class="btn btn-secondary btn-sm" data-speak="{escape(text)}" aria-label="Чуй текста"><i class="fa-solid fa-volume-high" aria-hidden="true"></i></button></h4>
{body}
</div>
<h3>Нови думи</h3>
<table><tr><th>Английски</th><th>Български</th></tr>{rows}</table>
"""


UNITS = [
    # ---------------- A1 ----------------
    {
        "level": "A1", "title": "Общуване и четене", "slug": "a1-skills", "icon": "fa-comments", "order": 4,
        "summary": "Учтиви молби, първи текст за четене и думи за дрехи.",
        "lessons": [
            {
                "slug": "a1-polite-requests", "title": "Молби, благодарности и извинения", "title_en": "Please, thank you, sorry",
                "kind": "conversation", "minutes": 6, "xp": 15, "summary": "Малките думи, които правят разговора учтив.",
                "theory": """
<p>В английския <span class="en">please</span> и <span class="en">thank you</span> се казват много по-често, отколкото „моля“ и „благодаря“ в българския. Без тях молбата звучи грубо.</p>
<h3>Молби</h3>
<ul>
<li><span class="en">Can I have a coffee, please?</span> Може ли едно кафе?</li>
<li><span class="en">Could you help me, please?</span> Бихте ли ми помогнали? (по-учтиво)</li>
<li><span class="en">Can you repeat that, please?</span> Може ли да повторите?</li>
</ul>
<h3>Отговори</h3>
<table>
<tr><th>Ситуация</th><th>Английски</th></tr>
<tr><td>благодарност</td><td class="en">Thank you. / Thanks a lot.</td></tr>
<tr><td>отговор на благодарност</td><td class="en">You're welcome. / No problem.</td></tr>
<tr><td>извинение</td><td class="en">Sorry! / I'm so sorry.</td></tr>
<tr><td>за да привлечеш внимание</td><td class="en">Excuse me...</td></tr>
</table>
<div class="tip"><span class="en">Excuse me</span> е преди да безпокоиш някого. <span class="en">Sorry</span> е след като си направил/а нещо нередно.</div>
""",
                "exercises": [
                    C("Какво казваш, когато някой ти благодари?", ["You're welcome.", "Excuse me.", "Sorry."], 0),
                    C("Искаш да питаш непознат за пътя. Започваш с:", ["Sorry...", "Excuse me...", "Please..."], 1),
                    C("Кое е най-учтиво?", ["Give me water.", "I want water.", "Could I have some water, please?"], 2),
                    F("Can you speak more slowly, ___ ?", "please"),
                    O("Може ли да повторите, моля?", "Can you repeat that please|Could you repeat that please"),
                    T("Много благодаря!", "Thanks a lot|Thank you very much|Thank you so much|Thanks very much"),
                ],
            },
            {
                "slug": "a1-read-my-day", "title": "Четене: Денят на Ана", "title_en": "Reading: Anna's day",
                "kind": "reading", "minutes": 7, "xp": 15, "summary": "Кратък текст в Present Simple с въпроси.",
                "theory": reading("Anna's day", [
                    "Anna is from Sofia. She is twenty-eight and she works in a bank.",
                    "She gets up at seven o'clock and has coffee and toast for breakfast. She goes to work by bus.",
                    "Anna finishes work at five. In the evening she cooks dinner, reads a book or watches TV with her cat, Mimi.",
                    "At the weekend she visits her parents. They live in a small village near Plovdiv.",
                ], [("gets up", "става (от сън)"), ("toast", "препечена филийка"), ("finishes", "приключва"),
                    ("village", "село"), ("at the weekend", "през уикенда")]),
                "exercises": [
                    C("Къде работи Ана?", ["В банка", "В училище", "В магазин"], 0, instruction=Q),
                    C("Как отива на работа?", ["С автобус", "Пеша", "С кола"], 0, instruction=Q),
                    C("Кога свършва работа?", ["В 5", "В 7", "В 8"], 0, instruction=Q),
                    C("Къде живеят родителите ѝ?", ["В село близо до Пловдив", "В София", "В Пловдив"], 0, instruction=Q),
                    F("Anna ___ (have) coffee for breakfast.", "has"),
                    O("Тя гледа телевизия вечер.", "She watches TV in the evening"),
                ],
            },
            {
                "slug": "a1-colours-clothes", "title": "Цветове и дрехи", "title_en": "Colours and clothes",
                "kind": "vocabulary", "minutes": 6, "xp": 15, "summary": "Как да опишеш какво носиш.",
                "theory": """
<h3>Цветове</h3>
<p><span class="en">red</span> червен, <span class="en">blue</span> син, <span class="en">green</span> зелен, <span class="en">yellow</span> жълт, <span class="en">black</span> черен, <span class="en">white</span> бял, <span class="en">grey</span> сив, <span class="en">brown</span> кафяв, <span class="en">pink</span> розов, <span class="en">orange</span> оранжев</p>
<h3>Дрехи</h3>
<table>
<tr><th>Английски</th><th>Български</th></tr>
<tr><td class="en">a shirt / a T-shirt</td><td>риза / тениска</td></tr>
<tr><td class="en">a dress / a skirt</td><td>рокля / пола</td></tr>
<tr><td class="en">trousers / jeans</td><td>панталон / дънки</td></tr>
<tr><td class="en">a jacket / a coat</td><td>яке / палто</td></tr>
<tr><td class="en">shoes / trainers</td><td>обувки / маратонки</td></tr>
</table>
<div class="tip"><span class="en">Trousers, jeans, shorts</span> са винаги в множествено число: <span class="en">My jeans are new.</span> Цветът стои пред дрехата: <span class="en">a red dress</span>.</div>
<p>Какво носиш? <span class="en">I'm wearing a blue shirt and black jeans.</span></p>
""",
                "exercises": [
                    C("„Сив“ на английски е:", ["green", "grey", "brown"], 1),
                    C("My jeans ___ too long.", ["is", "are"], 1, "Jeans е в множествено число."),
                    C("Кое е правилно?", ["a dress red", "a red dress"], 1, "Прилагателното е пред съществителното."),
                    F("I'm ___ (wear) a white T-shirt.", "wearing"),
                    O("Тя носи черно палто.", "She is wearing a black coat|She's wearing a black coat"),
                    T("Обувките ми са кафяви.", "My shoes are brown"),
                ],
            },
        ],
    },
    # ---------------- A2 ----------------
    {
        "level": "A2", "title": "Ежедневни ситуации", "slug": "a2-skills", "icon": "fa-phone", "order": 4,
        "summary": "Телефон, лекар, картичка от пътуване и професии.",
        "lessons": [
            {
                "slug": "a2-phone-calls", "title": "Телефонен разговор", "title_en": "Phone calls",
                "kind": "conversation", "minutes": 7, "xp": 20, "summary": "Как да се представиш и да оставиш съобщение.",
                "theory": """
<table>
<tr><th>Искаш да...</th><th>Английски</th></tr>
<tr><td>се представиш</td><td class="en">Hello, this is Maria. (не I am Maria)</td></tr>
<tr><td>потърсиш някого</td><td class="en">Can I speak to Mr Brown, please?</td></tr>
<tr><td>помолиш да изчакат</td><td class="en">Hold on, please. / One moment.</td></tr>
<tr><td>оставиш съобщение</td><td class="en">Can I leave a message?</td></tr>
<tr><td>кажеш, че ще звъннеш пак</td><td class="en">I'll call back later.</td></tr>
<tr><td>не чуваш добре</td><td class="en">Sorry, the line is bad. Could you speak up?</td></tr>
</table>
<div class="tip">По телефона казваме <span class="en">This is...</span>, а не <em>I am...</em>, и питаме <span class="en">Who's calling?</span>, а не <em>Who are you?</em></div>
""",
                "exercises": [
                    C("Как се представяш по телефона?", ["I am Peter.", "This is Peter.", "Here Peter."], 1),
                    C("Hold on, please. означава:", ["Изчакайте, моля.", "Затворете, моля.", "Говорете по-високо."], 0),
                    C("Учтиво питане кой се обажда:", ["Who are you?", "Who's calling, please?", "What is your name?"], 1),
                    F("Can I leave a ___ ?", "message"),
                    O("Ще ви се обадя по-късно.", "I will call you back later|I'll call you back later"),
                    T("Може ли да говоря с Мария?", "Can I speak to Maria|Could I speak to Maria|May I speak to Maria"),
                ],
            },
            {
                "slug": "a2-at-the-doctor", "title": "При лекаря", "title_en": "At the doctor's",
                "kind": "conversation", "minutes": 7, "xp": 20, "summary": "Как да кажеш какво те боли.",
                "theory": """
<h3>Какво те боли</h3>
<ul>
<li><span class="en">I've got a headache / a stomach ache / a sore throat.</span> Боли ме глава / стомах / гърло.</li>
<li><span class="en">I've got a temperature.</span> Имам температура.</li>
<li><span class="en">My back hurts.</span> Боли ме гърбът.</li>
<li><span class="en">I feel sick.</span> Гади ми се.</li>
</ul>
<h3>Какво ще те попитат</h3>
<p><span class="en">What's the problem? How long have you had it? Are you allergic to anything?</span></p>
<h3>Какво ще чуеш накрая</h3>
<p><span class="en">Here's a prescription.</span> Ето рецепта. <span class="en">Take one tablet three times a day.</span></p>
<div class="tip">На английски не казваш „боли ме глава“ дословно. Използваш <span class="en">I've got a headache</span> или <span class="en">my head hurts</span>.</div>
""",
                "exercises": [
                    C("„Боли ме гърло“ е:", ["I've got a sore throat.", "My throat is sick.", "I have pain throat."], 0),
                    C("Prescription означава:", ["Рецепта", "Предписание за глоба", "Регистрация"], 0),
                    C("Лекарят пита How long have you had it? Какво иска да знае?", ["Откога те боли", "Колко струва", "Къде живееш"], 0),
                    F("My back ___ (hurt).", "hurts"),
                    O("Имам температура от два дни.", "I have had a temperature for two days|I've had a temperature for two days"),
                    T("Алергичен/а съм към пеницилин.", "I am allergic to penicillin|I'm allergic to penicillin"),
                ],
            },
            {
                "slug": "a2-read-postcard", "title": "Четене: Картичка от Единбург", "title_en": "Reading: a postcard from Edinburgh",
                "kind": "reading", "minutes": 7, "xp": 20, "summary": "Минало време в реален текст.",
                "theory": reading("Hi from Edinburgh!", [
                    "Dear Mum and Dad,",
                    "We arrived in Edinburgh on Tuesday. The flight was short, but our hotel was difficult to find.",
                    "Yesterday we walked up to the castle. It was cold and windy, but the view was amazing!",
                    "In the evening we tried haggis. Peter loved it, I didn't.",
                    "Tomorrow we're going to take the train to the Highlands. See you next week!",
                    "Love, Elena",
                ], [("arrived", "пристигнахме"), ("castle", "замък"), ("windy", "ветровито"),
                    ("view", "гледка"), ("tried", "опитахме"), ("haggis", "шотландско ястие")]),
                "exercises": [
                    C("Кога пристигат в Единбург?", ["Във вторник", "В неделя", "Вчера"], 0, instruction=Q),
                    C("Какво е било трудно?", ["Да намерят хотела", "Полетът", "Да видят замъка"], 0, instruction=Q),
                    C("Какво е било времето при замъка?", ["Студено и ветровито", "Топло и слънчево", "Дъждовно"], 0, instruction=Q),
                    C("Хареса ли ѝ хагисът?", ["Не", "Да", "Не го опита"], 0, instruction=Q),
                    F("We ___ (walk) up to the castle yesterday.", "walked"),
                    O("Гледката беше невероятна.", "The view was amazing"),
                ],
            },
            {
                "slug": "a2-jobs", "title": "Работа и професии", "title_en": "Jobs and work",
                "kind": "vocabulary", "minutes": 6, "xp": 20, "summary": "Професии и как да говориш за работата си.",
                "theory": """
<table>
<tr><th>Професия</th><th>Български</th></tr>
<tr><td class="en">a nurse</td><td>медицинска сестра</td></tr>
<tr><td class="en">an engineer</td><td>инженер</td></tr>
<tr><td class="en">a shop assistant</td><td>продавач/ка</td></tr>
<tr><td class="en">a lawyer</td><td>адвокат</td></tr>
<tr><td class="en">an accountant</td><td>счетоводител</td></tr>
<tr><td class="en">a builder</td><td>строител</td></tr>
<tr><td class="en">a software developer</td><td>програмист</td></tr>
</table>
<h3>Как да говориш за работата си</h3>
<ul>
<li><span class="en">What do you do?</span> Какво работиш? (не <em>What is your work?</em>)</li>
<li><span class="en">I work for a big company. I work in marketing.</span></li>
<li><span class="en">I'm self-employed.</span> Работя на свободна практика.</li>
<li><span class="en">I'm looking for a job.</span> Търся работа.</li>
</ul>
""",
                "exercises": [
                    C("Как питаш какво работи някой?", ["What do you do?", "What is your work?", "What are you working?"], 0),
                    C("Accountant е:", ["счетоводител", "актьор", "адвокат"], 0),
                    C("She's a nurse. Тя е:", ["медицинска сестра", "лекар", "учителка"], 0),
                    F("I work ___ a small IT company.", "for|at"),
                    O("Търся работа в Лондон.", "I am looking for a job in London|I'm looking for a job in London"),
                    T("Той е инженер.", "He is an engineer|He's an engineer", "Engineer започва с гласен звук, затова an."),
                ],
            },
        ],
    },
    # ---------------- B1 ----------------
    {
        "level": "B1", "title": "Мнения и текстове", "slug": "b1-skills", "icon": "fa-comment-dots", "order": 4,
        "summary": "Предложения, мнения, официален имейл и колокации с make и do.",
        "lessons": [
            {
                "slug": "b1-suggestions", "title": "Предложения и покани", "title_en": "Suggestions and invitations",
                "kind": "conversation", "minutes": 7, "xp": 20, "summary": "Let's, How about, Why don't we и как да откажеш учтиво.",
                "theory": """
<table>
<tr><th>Израз</th><th>Следва</th><th>Пример</th></tr>
<tr><td class="en">Let's</td><td>глагол</td><td class="en">Let's go to the cinema.</td></tr>
<tr><td class="en">How about / What about</td><td>-ing</td><td class="en">How about going to the cinema?</td></tr>
<tr><td class="en">Why don't we</td><td>глагол</td><td class="en">Why don't we go to the cinema?</td></tr>
<tr><td class="en">Would you like to</td><td>глагол</td><td class="en">Would you like to come to dinner?</td></tr>
</table>
<h3>Приемане и отказ</h3>
<ul>
<li><span class="en">That's a great idea! / I'd love to.</span></li>
<li><span class="en">I'm afraid I can't. I'm busy on Friday.</span> Съжалявам, не мога.</li>
<li><span class="en">Maybe another time?</span> Може би друг път?</li>
</ul>
<div class="tip">Голото <span class="en">No</span> звучи рязко. Отказът обикновено има три части: благодарност, причина, алтернатива.</div>
""",
                "exercises": [
                    C("How about ___ a walk?", ["take", "taking", "to take"], 1),
                    C("Why don't we ___ pizza tonight?", ["order", "ordering", "to order"], 0),
                    C("Най-учтивият отказ:", ["No.", "I don't want.", "I'd love to, but I'm busy. Maybe next week?"], 2),
                    F("Would you like ___ come with us?", "to"),
                    O("Хайде да отидем на плаж.", "Let's go to the beach"),
                    T("Какво ще кажеш да вечеряме навън?", "How about eating out|What about eating out|How about having dinner out|Why don't we eat out"),
                ],
            },
            {
                "slug": "b1-opinions", "title": "Мнение, съгласие и несъгласие", "title_en": "Giving opinions",
                "kind": "conversation", "minutes": 8, "xp": 20, "summary": "Как да кажеш какво мислиш и да не се съгласиш учтиво.",
                "theory": """
<h3>Мнение</h3>
<p><span class="en">I think / I believe / In my opinion / If you ask me, ...</span></p>
<h3>Съгласие</h3>
<p><span class="en">I agree. / That's true. / Exactly! / You're right.</span></p>
<h3>Несъгласие (учтиво)</h3>
<ul>
<li><span class="en">I'm not sure about that.</span></li>
<li><span class="en">I see your point, but...</span></li>
<li><span class="en">I'm afraid I don't agree.</span></li>
</ul>
<div class="tip">„Не съм съгласен“ е <span class="en">I don't agree</span> или <span class="en">I disagree</span>. А „мисля, че не“ е <span class="en">I don't think so</span>, не <em>I think no</em>.</div>
""",
                "exercises": [
                    C("Кое изречение е правилно?", ["I am agree.", "I agree.", "I am agreeing with you."], 1),
                    C("Учтиво несъгласие:", ["You're wrong.", "I see your point, but I think it's too expensive.", "No way."], 1),
                    C("„Мисля, че не“ е:", ["I think no.", "I don't think so.", "I think not so."], 1),
                    F("In my ___ , the film was too long.", "opinion"),
                    O("Не съм сигурен/на за това.", "I am not sure about that|I'm not sure about that"),
                    T("Съгласен/на съм с теб.", "I agree with you"),
                ],
            },
            {
                "slug": "b1-read-hotel-email", "title": "Четене: Имейл до хотел", "title_en": "Reading: an email to a hotel",
                "kind": "reading", "minutes": 8, "xp": 20, "summary": "Как изглежда учтив официален имейл.",
                "theory": reading("Booking enquiry", [
                    "Dear Sir or Madam,",
                    "I am writing to ask about your rooms for the weekend of 14 to 16 June. We are a family of four, with two children aged 8 and 11.",
                    "Could you tell me if you have a family room available, and whether breakfast is included in the price?",
                    "We are also planning to arrive quite late, at around 11 pm. Would that be a problem?",
                    "I look forward to hearing from you.",
                    "Kind regards, Nikolay Petrov",
                ], [("I am writing to ask about", "пиша, за да попитам за"), ("aged", "на възраст"), ("available", "свободен, наличен"),
                    ("whether", "дали"), ("included", "включен"), ("I look forward to hearing from you", "очаквам отговора ви")]),
                "exercises": [
                    C("Защо пише Николай?", ["За да попита за стая", "За да се оплаче", "За да откаже резервация"], 0, instruction=Q),
                    C("Колко души ще пътуват?", ["Четирима", "Двама", "Трима"], 0, instruction=Q),
                    C("Какво пита за закуската?", ["Дали е включена в цената", "В колко часа е", "Колко струва за деца"], 0, instruction=Q),
                    C("Какъв проблем може да има?", ["Ще пристигнат късно", "Имат куче", "Нямат кола"], 0, instruction=Q),
                    F("I look forward to ___ (hear) from you.", "hearing"),
                    O("Включена ли е закуската?", "Is breakfast included"),
                ],
            },
            {
                "slug": "b1-make-do", "title": "Make или do", "title_en": "Collocations: make and do",
                "kind": "vocabulary", "minutes": 7, "xp": 20, "summary": "И двете са „правя“, но не се разменят.",
                "theory": """
<p>Общо правило: <span class="en">make</span> е за създаване на нещо, <span class="en">do</span> е за дейност или работа. Но много изрази просто се запомнят.</p>
<table>
<tr><th>make</th><th>do</th></tr>
<tr><td class="en">make a mistake</td><td class="en">do homework</td></tr>
<tr><td class="en">make a decision</td><td class="en">do the shopping</td></tr>
<tr><td class="en">make a phone call</td><td class="en">do the dishes</td></tr>
<tr><td class="en">make money</td><td class="en">do business</td></tr>
<tr><td class="en">make friends</td><td class="en">do your best</td></tr>
<tr><td class="en">make a noise</td><td class="en">do someone a favour</td></tr>
<tr><td class="en">make an effort</td><td class="en">do exercise</td></tr>
</table>
""",
                "exercises": [
                    C("I ___ a mistake.", ["made", "did"], 0),
                    C("Can you ___ me a favour?", ["make", "do"], 1),
                    C("She ___ her homework every evening.", ["makes", "does"], 1),
                    C("We need to ___ a decision today.", ["make", "do"], 0),
                    F("Don't worry, just ___ your best.", "do"),
                    O("Той прави много пари.", "He makes a lot of money"),
                ],
            },
        ],
    },
    # ---------------- B2 ----------------
    {
        "level": "B2", "title": "Убедително общуване", "slug": "b2-skills", "icon": "fa-bullhorn", "order": 3,
        "summary": "Оплаквания, статия за четене и фалшиви приятели.",
        "lessons": [
            {
                "slug": "b2-complaints", "title": "Учтиво оплакване", "title_en": "Complaining politely",
                "kind": "conversation", "minutes": 8, "xp": 25, "summary": "Как да получиш решение, без да звучиш грубо.",
                "theory": """
<p>Ефективното оплакване на английски е спокойно и конкретно. Структура: <strong>проблем, факти, какво искаш</strong>.</p>
<table>
<tr><th>Стъпка</th><th>Израз</th></tr>
<tr><td>започни меко</td><td class="en">I'm afraid there's a problem with my room.</td></tr>
<tr><td>опиши фактите</td><td class="en">The air conditioning hasn't worked since we arrived.</td></tr>
<tr><td>кажи какво искаш</td><td class="en">Would it be possible to change rooms?</td></tr>
<tr><td>ако няма резултат</td><td class="en">I'd like to speak to the manager, please.</td></tr>
</table>
<div class="tip"><span class="en">I want a refund!</span> звучи агресивно. По-ефективно: <span class="en">I'd like a refund, please.</span> или <span class="en">Could I get a refund?</span></div>
""",
                "exercises": [
                    C("Най-добро начало на оплакване:", ["This is terrible!", "I'm afraid there's a problem with my order.", "You made a mistake."], 1),
                    C("Учтиво искане за възстановяване на парите:", ["Give me my money back.", "I'd like a refund, please.", "I want refund."], 1),
                    C("Would it be possible to ...? означава:", ["Възможно ли е да ...?", "Трябва да ...", "Забранено е да ..."], 0),
                    F("The heating hasn't ___ (work) since Monday.", "worked"),
                    O("Искам да говоря с управителя.", "I would like to speak to the manager|I'd like to speak to the manager"),
                ],
            },
            {
                "slug": "b2-read-four-day-week", "title": "Четене: Четиридневна работна седмица", "title_en": "Reading: the four-day week",
                "kind": "reading", "minutes": 9, "xp": 25, "summary": "Статия с аргументи за и против.",
                "theory": reading("Is the four-day week the future?", [
                    "In recent years, hundreds of companies have tested a four-day working week without cutting salaries.",
                    "The results have been largely positive. Many employees reported less stress and better sleep, and most companies said productivity stayed the same or even improved.",
                    "However, critics point out that the model does not suit every sector. Hospitals, schools and shops cannot simply close for an extra day, and some workers ended up squeezing five days of tasks into four.",
                    "For now, the four-day week looks less like a universal solution and more like an option that works well in the right conditions.",
                ], [("without cutting salaries", "без да намаляват заплатите"), ("largely", "до голяма степен"),
                    ("productivity", "производителност"), ("critics point out", "критиците отбелязват"),
                    ("sector", "сектор, бранш"), ("squeezing", "натъпкване, сбиване")]),
                "exercises": [
                    C("Какво са тествали компаниите?", ["Четири работни дни при същата заплата", "По-кратък работен ден", "Работа от вкъщи"], 0, instruction=Q),
                    C("Какво е станало с производителността според повечето компании?", ["Останала е същата или се е подобрила", "Спаднала е", "Не е измервана"], 0, instruction=Q),
                    C("Какъв е проблемът според критиците?", ["Не пасва на всички сектори", "Скъпо е", "Хората спят повече"], 0, instruction=Q),
                    C("Какъв е изводът на автора?", ["Работи добре при подходящи условия", "Трябва да се забрани", "Ще замени петдневната седмица навсякъде"], 0, instruction=Q),
                    F("Most companies said productivity stayed the ___ .", "same"),
                    O("Резултатите са до голяма степен положителни.", "The results have been largely positive|The results are largely positive"),
                ],
            },
            {
                "slug": "b2-false-friends", "title": "Фалшиви приятели", "title_en": "False friends for Bulgarian speakers",
                "kind": "vocabulary", "minutes": 8, "xp": 25, "summary": "Думи, които звучат познато, но значат друго.",
                "theory": """
<p>Някои английски думи приличат на български, но значението им е различно. Това са „фалшиви приятели“.</p>
<table>
<tr><th>Английска дума</th><th>Значи</th><th>„Българското“ значение е</th></tr>
<tr><td class="en">actual</td><td>действителен, истински</td><td>актуален = <span class="en">current, relevant</span></td></tr>
<tr><td class="en">eventually</td><td>в крайна сметка</td><td>евентуално = <span class="en">possibly</span></td></tr>
<tr><td class="en">accurate</td><td>точен</td><td>акуратен = <span class="en">neat, tidy</span></td></tr>
<tr><td class="en">sympathetic</td><td>съчувстващ</td><td>симпатичен = <span class="en">nice, likeable</span></td></tr>
<tr><td class="en">magazine</td><td>списание</td><td>магазин = <span class="en">shop</span></td></tr>
<tr><td class="en">fabric</td><td>плат</td><td>фабрика = <span class="en">factory</span></td></tr>
<tr><td class="en">cabinet</td><td>шкаф; правителство</td><td>кабинет = <span class="en">office, study</span></td></tr>
<tr><td class="en">angina</td><td>стенокардия</td><td>ангина = <span class="en">tonsillitis</span></td></tr>
</table>
""",
                "exercises": [
                    C("„Това е актуална тема“ е:", ["This is an actual topic.", "This is a current topic.", "This is an eventual topic."], 1),
                    C("Eventually означава:", ["в крайна сметка", "евентуално", "веднага"], 0),
                    C("„Той е много симпатичен“ (приятен човек):", ["He's very sympathetic.", "He's very nice.", "He's very accurate."], 1),
                    C("Купих списание:", ["I bought a magazine.", "I bought a shop."], 0),
                    C("Работи във фабрика:", ["She works in a fabric.", "She works in a factory."], 1),
                    T("Евентуално ще дойда утре.", "I might come tomorrow|I may come tomorrow|Possibly I'll come tomorrow|I will possibly come tomorrow|I'll possibly come tomorrow|I could come tomorrow"),
                ],
            },
        ],
    },
    # ---------------- C1 ----------------
    {
        "level": "C1", "title": "Професионална комуникация", "slug": "c1-skills", "icon": "fa-briefcase", "order": 3,
        "summary": "Дипломатичен език и аналитично четене.",
        "lessons": [
            {
                "slug": "c1-hedging", "title": "Дипломатичен език", "title_en": "Hedging and softening",
                "kind": "conversation", "minutes": 9, "xp": 30, "summary": "Как да кажеш „не“ на среща, без да обидиш никого.",
                "theory": """
<p>В професионалния английски директността често звучи рязко. Носителите на езика „омекотяват“ (<span class="en">hedging</span>).</p>
<table>
<tr><th>Директно</th><th>Дипломатично</th></tr>
<tr><td class="en">This plan is wrong.</td><td class="en">I'm not entirely convinced this plan will work.</td></tr>
<tr><td class="en">It's too expensive.</td><td class="en">It seems a little on the expensive side.</td></tr>
<tr><td class="en">You're late with the report.</td><td class="en">I was wondering if there's an update on the report.</td></tr>
<tr><td class="en">No.</td><td class="en">That might be difficult at the moment.</td></tr>
</table>
<h3>Инструменти</h3>
<ul>
<li>модални глаголи: <span class="en">might, could, would</span></li>
<li>думи за степен: <span class="en">slightly, a bit, somewhat</span></li>
<li>минало вместо сегашно: <span class="en">I was wondering, I wanted to ask</span></li>
<li>отрицание на положително: <span class="en">not ideal</span> вместо <span class="en">bad</span></li>
</ul>
""",
                "exercises": [
                    C("Дипломатично за „планът е лош“:", ["The plan is bad.", "I have some concerns about the plan.", "This plan is stupid."], 1),
                    C("I was wondering if you could... е:", ["учтива молба", "заплаха", "въпрос за миналото"], 0),
                    C("Not ideal означава:", ["доста лошо (меко казано)", "идеално", "неутрално"], 0),
                    F("It ___ be difficult to finish by Friday.", "might|could|may"),
                    O("Не съм напълно убеден.", "I am not entirely convinced|I'm not entirely convinced"),
                ],
            },
            {
                "slug": "c1-read-car-free", "title": "Четене: Градове без коли", "title_en": "Reading: car-free cities",
                "kind": "reading", "minutes": 10, "xp": 30, "summary": "Аналитичен текст с позиция и контрааргументи.",
                "theory": reading("Should city centres ban cars?", [
                    "Few urban policies provoke such heated debate as banning private cars from city centres.",
                    "Supporters argue that the benefits are hard to dispute: cleaner air, safer streets and more space for people rather than parking. Cities that have taken the plunge often report that local businesses, initially fearful of losing customers, end up thriving as foot traffic increases.",
                    "Opponents, however, warn that such bans can disproportionately affect elderly and disabled residents, as well as those living in suburbs with poor public transport.",
                    "The most successful schemes, it seems, are those introduced gradually and paired with genuine investment in alternatives, rather than imposed overnight.",
                ], [("provoke heated debate", "предизвикват разгорещен спор"), ("hard to dispute", "трудно оспорими"),
                    ("take the plunge", "решавам се на смела стъпка"), ("thriving", "процъфтяващ"),
                    ("disproportionately", "непропорционално"), ("paired with", "съчетан с")]),
                "exercises": [
                    C("Какво се случва често с местния бизнес според текста?", ["Процъфтява, защото минават повече хора", "Затваря", "Премества се извън града"], 0, instruction=Q),
                    C("Кого засягат забраните непропорционално според критиците?", ["Възрастни хора, хора с увреждания и жители на крайни квартали", "Туристите", "Таксиметровите шофьори"], 0, instruction=Q),
                    C("Кои схеми са най-успешни?", ["Въведените постепенно, с инвестиции в алтернативи", "Въведените за една нощ", "Тези без обществен транспорт"], 0, instruction=Q),
                    C("Take the plunge означава:", ["решавам се на смела стъпка", "скачам във вода", "отказвам се"], 0),
                    F("Few policies provoke such heated ___ .", "debate"),
                ],
            },
        ],
    },
    # ---------------- C2 ----------------
    {
        "level": "C2", "title": "Майсторство в езика", "slug": "c2-skills", "icon": "fa-gem", "order": 2,
        "summary": "Силни колокации и четене с ирония и подтекст.",
        "lessons": [
            {
                "slug": "c2-collocations", "title": "Силни колокации", "title_en": "Strong collocations",
                "kind": "vocabulary", "minutes": 8, "xp": 35, "summary": "Heavy rain, not strong rain: думите, които „вървят заедно“.",
                "theory": """
<p>Колокациите са думи, които естествено вървят заедно. Те издават носителя на езика повече от граматиката.</p>
<table>
<tr><th>Естествено</th><th>Звучи чуждо</th></tr>
<tr><td class="en">heavy rain / heavy traffic</td><td><em>strong rain, big traffic</em></td></tr>
<tr><td class="en">strong coffee</td><td><em>heavy coffee</em></td></tr>
<tr><td class="en">highly unlikely</td><td><em>very unprobable</em></td></tr>
<tr><td class="en">deeply regret</td><td><em>strongly regret</em></td></tr>
<tr><td class="en">bitterly cold</td><td><em>very strongly cold</em></td></tr>
<tr><td class="en">a fierce debate / fierce competition</td><td><em>a hard debate</em></td></tr>
<tr><td class="en">utterly ridiculous</td><td><em>totally very ridiculous</em></td></tr>
</table>
<div class="tip">Когато научаваш нова дума, научи я с 2-3 думи, с които обикновено се използва.</div>
""",
                "exercises": [
                    C("There was ___ rain all night.", ["strong", "heavy", "big"], 1),
                    C("It is ___ unlikely that he'll win.", ["highly", "strongly", "heavily"], 0),
                    C("I ___ regret my decision.", ["deeply", "heavily", "highly"], 0),
                    C("It was ___ cold this morning.", ["bitterly", "heavily", "strongly"], 0),
                    F("There's ___ competition in the market.", "fierce|stiff|intense"),
                    O("Тази идея е абсолютно абсурдна.", "This idea is utterly ridiculous"),
                ],
            },
            {
                "slug": "c2-read-review", "title": "Четене: Рецензия с ирония", "title_en": "Reading: an ironic review",
                "kind": "reading", "minutes": 10, "xp": 35, "summary": "Да разбереш какво авторът наистина мисли.",
                "theory": reading("Review: The Last Summer", [
                    "If you have ever wished that a film would explain every single emotion its characters feel, twice, then The Last Summer is the film for you.",
                    "At a modest three hours and twenty minutes, it leaves no stone unturned and no silence unfilled. The dialogue is relentless; the soundtrack, even more so.",
                    "To be fair, the cinematography is genuinely stunning, and the lead actress does what she can with a script that rarely trusts its audience.",
                    "Fans of subtlety may wish to look elsewhere. Everyone else should bring snacks. Lots of snacks.",
                ], [("leaves no stone unturned", "не пропуска нищо (тук иронично)"), ("modest", "скромен (тук иронично: дълъг)"),
                    ("relentless", "безмилостен, непрестанен"), ("cinematography", "операторска работа"),
                    ("subtlety", "финес, деликатност")]),
                "exercises": [
                    C("Какво мисли авторът за дължината на филма?", ["Прекалено дълъг е", "Подходящо кратък е", "Не споменава"], 0, instruction=Q),
                    C("Какво хвали авторът?", ["Операторската работа", "Сценария", "Музиката"], 0, instruction=Q),
                    C("„A modest three hours and twenty minutes“ е пример за:", ["ирония", "комплимент", "статистика"], 0, instruction=Q),
                    C("Какво внушава „Fans of subtlety may wish to look elsewhere“?", ["Филмът е прекалено директен", "Филмът е твърде фин", "Филмът е за деца"], 0, instruction=Q),
                    C("Relentless dialogue означава:", ["Диалогът никога не спира", "Диалогът е тих", "Няма диалог"], 0),
                ],
            },
        ],
    },
]

MISTAKES = {
    "a1-polite-requests": [
        ("Give me a coffee.", "Can I have a coffee, please?", "Заповедната форма без please звучи грубо при молба."),
        ("Excuse me! (след като настъпиш някого)", "Sorry!", "Excuse me е преди да безпокоиш някого, sorry е след като си направил/а нещо."),
    ],
    "a1-colours-clothes": [
        ("My jeans is new.", "My jeans are new.", "Jeans, trousers, shorts са в множествено число."),
        ("a dress red", "a red dress", "Прилагателното стои пред съществителното."),
    ],
    "a2-phone-calls": [
        ("Hello, I am Maria.", "Hello, this is Maria.", "По телефона се представяме с this is."),
        ("Who are you?", "Who's calling, please?", "Who are you? звучи грубо по телефона."),
    ],
    "a2-at-the-doctor": [
        ("It hurts me the head.", "I've got a headache. / My head hurts.", "Не превеждай „боли ме главата“ дословно."),
        ("I have temperature.", "I've got a temperature.", "Използва се с член: a temperature."),
    ],
    "a2-jobs": [
        ("What is your work?", "What do you do?", "Стандартният въпрос за професията е What do you do?"),
        ("I am engineer.", "I am an engineer.", "Пред професия: a или an."),
    ],
    "b1-suggestions": [
        ("How about to go to the cinema?", "How about going to the cinema?", "След How about следва -ing."),
        ("Let's to go!", "Let's go!", "След let's глаголът е без to."),
    ],
    "b1-opinions": [
        ("I am agree with you.", "I agree with you.", "Agree е глагол, без am."),
        ("I think no.", "I don't think so.", "Устойчив израз: I don't think so."),
    ],
    "b1-make-do": [
        ("I did a mistake.", "I made a mistake.", "Make a mistake е устойчива колокация."),
        ("Can you make me a favour?", "Can you do me a favour?", "Do someone a favour."),
    ],
    "b2-complaints": [
        ("I want refund!", "I'd like a refund, please.", "I'd like звучи учтиво и е по-ефективно."),
    ],
    "b2-false-friends": [
        ("This is an actual problem.", "This is a current problem.", "Actual означава действителен, не актуален."),
        ("Eventually I will come.", "I might come.", "Eventually означава „в крайна сметка“."),
        ("He is very sympathetic.", "He is very nice.", "Sympathetic означава съчувстващ."),
    ],
    "c1-hedging": [
        ("Your idea is bad.", "I'm not sure that idea would work for us.", "Директната критика звучи рязко на английски."),
    ],
    "c2-collocations": [
        ("strong rain", "heavy rain", "Дъждът и трафикът са heavy."),
        ("strongly regret", "deeply regret", "Regret се съчетава с deeply."),
    ],
}
