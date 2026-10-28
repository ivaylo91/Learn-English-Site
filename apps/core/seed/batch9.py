"""Ninth batch, built on research into errors typical of Bulgarian speakers (Present Simple vs Continuous, Present
Perfect, word order, the /h/ sound, -ing said as -ink) and the travel situations learners need most (hotel problems,
reporting a theft, flight delays).

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
    "a1-listening": [
        {
            "slug": "a1-listen-directions", "title": "Как да стигна до...?", "title_en": "Asking the way", "kind": "listening",
            "minutes": 6, "xp": 15, "summary": "Ели пита минувач как да стигне до музея.", "theory": INTRO,
            "dialogue": dialogue(
                ("Eli", "Excuse me, where is the museum, please?", "Извинете, къде е музеят, моля?"),
                ("Man", "Go straight on and take the second street on the left.", "Вървете направо и завийте по втората улица наляво."),
                ("Eli", "The second on the left. OK.", "Втората наляво. Добре."),
                ("Man", "Then walk past the church. The museum is opposite the park.", "После минете покрай църквата. Музеят е срещу парка."),
                ("Eli", "Is it far?", "Далече ли е?"),
                ("Man", "No, it's about five minutes on foot.", "Не, на около пет минути пеша е."),
                ("Eli", "Thank you very much!", "Много ви благодаря!"),
            ),
            "exercises": [
                C("Какво търси Ели?", ["Музея", "Парка", "Църквата"], 0, instruction=DQ),
                C("По коя улица да завие?", ["Втората наляво", "Първата надясно", "Втората надясно"], 0, instruction=DQ),
                C("Къде е музеят?", ["Срещу парка", "До църквата", "В парка"], 0, instruction=DQ),
                C("Колко е далеч?", ["5 минути пеша", "15 минути пеша", "5 минути с кола"], 0, instruction=DQ),
                L("Какво означава opposite?", "The museum is opposite the park.", ["срещу", "до", "зад"], 0),
                D("Go straight on."),
                S("Excuse me, where is the museum, please?"),
            ],
        },
    ],
    "a1-pronunciation": [
        {
            "slug": "a1-pron-h", "title": "Звукът H: само дъх", "title_en": "The H sound",
            "kind": "pronunciation", "minutes": 6, "xp": 15, "summary": "Английското h не е българското „х“.",
            "theory": """
<p>Българското „х“ се произнася с търкане в гърлото. Английското <span class="en">h</span> е само <strong>издишване</strong>, като когато духаш на стъкло, за да го запотиш. Без никакво стържене.</p>
<table>
<tr><th>Думи с h</th><th>Без h</th></tr>
<tr><td class="en">hat</td><td class="en">at</td></tr>
<tr><td class="en">heat</td><td class="en">eat</td></tr>
<tr><td class="en">hear</td><td class="en">ear</td></tr>
<tr><td class="en">hold</td><td class="en">old</td></tr>
</table>
<div class="tip">Неми h: <span class="en">hour, honest, honour</span> започват с гласна. Затова: <span class="en">an hour</span>, не <em>a hour</em>.</div>
""",
            "exercises": [
                L("Коя дума чу?", "hat", ["hat", "at"], 0),
                L("Коя дума чу?", "eat", ["heat", "eat"], 1),
                C("Как се произнася английското h?", ["Само издишване, без стържене", "Като българското „х“", "Не се произнася никога"], 0),
                C("Кое е правилно?", ["an hour", "a hour"], 0, "В hour h е нямо."),
                S("How are you? I'm happy here."),
                S("He has a house in Holland."),
                D("I'll be home in an hour."),
            ],
        },
    ],
    "a1-daily-places": [
        {
            "slug": "a1-place-prepositions", "title": "Под, зад, между: предлози за място", "title_en": "Prepositions of place",
            "kind": "grammar", "minutes": 6, "xp": 15, "summary": "Къде е ключът? Под масата, до чантата, зад вратата.",
            "theory": """
<table>
<tr><th>Предлог</th><th>Значение</th><th>Пример</th></tr>
<tr><td class="en">under</td><td>под</td><td class="en">The cat is under the table.</td></tr>
<tr><td class="en">behind</td><td>зад</td><td class="en">The bag is behind the door.</td></tr>
<tr><td class="en">in front of</td><td>пред</td><td class="en">I'm in front of the hotel.</td></tr>
<tr><td class="en">next to</td><td>до</td><td class="en">The bank is next to the café.</td></tr>
<tr><td class="en">between</td><td>между</td><td class="en">The shop is between the bank and the park.</td></tr>
<tr><td class="en">opposite</td><td>срещу</td><td class="en">The museum is opposite the station.</td></tr>
<tr><td class="en">above / on</td><td>над / върху</td><td class="en">The lamp is above the bed. The phone is on the bed.</td></tr>
</table>
<div class="tip"><span class="en">In front of</span> има три думи. Не казваме <em>in front the hotel</em>.</div>
""",
            "exercises": [
                C("Ключовете са под книгата:", ["The keys are under the book.", "The keys are behind the book.", "The keys are on the book."], 0),
                C("I'll wait ___ the cinema. (пред)", ["in front of", "in front", "before of"], 0),
                C("The café is ___ the bank and the hotel.", ["between", "next", "opposite of"], 0),
                C("The station is ___ the museum. (срещу)", ["opposite", "opposite of", "front"], 0),
                F("My bag is ___ the door. (зад)", "behind"),
                O("Аптеката е до банката.", "The pharmacy is next to the bank"),
            ],
        },
    ],
    "a1-skills": [
        {
            "slug": "a1-read-messages", "title": "Четене: съобщения в телефона", "title_en": "Reading: text messages",
            "kind": "reading", "minutes": 6, "xp": 15, "summary": "Умение: кратки неформални съобщения и съкращения.",
            "theory": """<div class="tip"><strong>Умение: неформални съобщения.</strong> В чатовете хората пишат кратко: <span class="en">thx</span> (thanks), <span class="en">pls</span> (please), <span class="en">b4</span> (before), <span class="en">2moro</span> (tomorrow). Търси кой, кога и какво.</div>""" + reading("Messages", [
                "Maya (10:15): Hi! Are you free 2moro? Lunch at 1?",
                "You (10:20): Yes! Where?",
                "Maya (10:22): The Italian place near the station. I'll book a table.",
                "Maya (12:40): Sorry, I'm late! 10 mins. Pls order me a pizza. Thx!",
            ], [("2moro", "утре"), ("free", "свободен"), ("book a table", "запазвам маса"), ("late", "закъснявам"),
                ("pls / thx", "моля / благодаря")]),
            "exercises": [
                C("Кога е обядът?", ["Утре в 13:00", "Днес в 10:00", "Утре в 12:40"], 0, instruction=RQ),
                C("Къде е ресторантът?", ["Близо до гарата", "В хотела", "До парка"], 0, instruction=RQ),
                C("Кой запазва маса?", ["Мая", "Ти", "Никой"], 0, instruction=RQ),
                C("С колко закъснява Мая?", ["10 минути", "40 минути", "1 час"], 0, instruction=RQ),
                C("Какво иска Мая да ѝ поръчаш?", ["Пица", "Салата", "Паста"], 0, instruction=RQ),
                C("Thx означава:", ["thanks", "this", "the X"], 0),
            ],
        },
        {
            "slug": "a1-containers", "title": "Бутилка, килограм, парче", "title_en": "Containers and quantities",
            "kind": "vocabulary", "minutes": 6, "xp": 15, "summary": "A bottle of water, a kilo of apples: пазаруване по количество.",
            "theory": """
<table>
<tr><th>Израз</th><th>Значение</th></tr>
<tr><td class="en">a bottle of water</td><td>бутилка вода</td></tr>
<tr><td class="en">a can of cola</td><td>кутийка кола</td></tr>
<tr><td class="en">a cup of coffee / a glass of wine</td><td>чаша кафе / чаша вино</td></tr>
<tr><td class="en">a kilo of tomatoes</td><td>килограм домати</td></tr>
<tr><td class="en">a loaf of bread</td><td>хляб (самун)</td></tr>
<tr><td class="en">a piece of cake</td><td>парче торта</td></tr>
<tr><td class="en">a packet of biscuits</td><td>пакет бисквити</td></tr>
<tr><td class="en">a carton of milk</td><td>кутия мляко</td></tr>
</table>
<div class="tip">Винаги с <span class="en">of</span>: <span class="en">a bottle of water</span>, не <em>a bottle water</em>.</div>
""",
            "exercises": [
                C("Можете ли да ми дадете един хляб?", ["a loaf of bread", "a bread", "one breads"], 0),
                C("I'd like a ___ of milk.", ["carton", "loaf", "piece"], 0),
                C("A ___ of cake, please.", ["piece", "bottle", "kilo"], 0),
                C("Кое е правилно?", ["a bottle of water", "a bottle water", "a water bottle of"], 0),
                F("Two ___ of coffee, please. (чаши)", "cups"),
                T("Килограм ябълки, моля.", "A kilo of apples please|A kilo of apples, please"),
            ],
        },
    ],
    # ---------------- A2 ----------------
    "a2-listening": [
        {
            "slug": "a2-listen-hotel-problem", "title": "Проблем в хотелската стая", "title_en": "A problem with the room", "kind": "listening",
            "minutes": 7, "xp": 20, "summary": "Климатикът не работи: как да се оплачеш на рецепцията.", "theory": INTRO,
            "dialogue": dialogue(
                ("Receptionist", "Good evening. How can I help?", "Добър вечер. С какво мога да помогна?"),
                ("Georgi", "Hi, I'm in room 312. I'm afraid the air conditioning isn't working, and it's really hot.", "Здравейте, в стая 312 съм. Страхувам се, че климатикът не работи, а е много горещо."),
                ("Receptionist", "I'm so sorry about that. I'll send someone up to look at it right away.", "Много съжалявам. Веднага ще изпратя някой да го погледне."),
                ("Georgi", "Thanks. Also, there aren't any towels in the bathroom.", "Благодаря. Освен това в банята няма кърпи."),
                ("Receptionist", "I'll ask housekeeping to bring some. If we can't fix the air conditioning, we can move you to another room.", "Ще помоля камериерките да донесат. Ако не успеем да поправим климатика, можем да ви преместим в друга стая."),
                ("Georgi", "That would be great. Thank you.", "Това би било чудесно. Благодаря."),
            ),
            "exercises": [
                C("В коя стая е Георги?", ["312", "213", "320"], 0, instruction=DQ),
                C("Какъв е първият проблем?", ["Климатикът не работи", "Няма топла вода", "Шумно е"], 0, instruction=DQ),
                C("Какво още липсва?", ["Кърпи", "Сапун", "Възглавници"], 0, instruction=DQ),
                C("Какво предлагат, ако не поправят климатика?", ["Друга стая", "Отстъпка", "Вентилатор"], 0, instruction=DQ),
                L("Какво означава right away?", "I'll send someone up right away.", ["веднага", "надясно", "по-късно"], 0),
                D("The air conditioning isn't working."),
                S("I'm afraid there aren't any towels."),
            ],
        },
    ],
    "a2-pronunciation": [
        {
            "slug": "a2-pron-ng", "title": "Окончание -ing: не „-инк“", "title_en": "The NG sound",
            "kind": "pronunciation", "minutes": 6, "xp": 20, "summary": "Thing и think, sing и sink: носовият звук ng.",
            "theory": """
<p>Звукът <span class="en">ng</span> (/ŋ/) е <strong>носов</strong>: задната част на езика затваря, въздухът излиза през носа. В края на думата <strong>няма</strong> „к“ или „г“.</p>
<table>
<tr><th>ng (носово)</th><th>nk (с „к“)</th></tr>
<tr><td class="en">thing</td><td class="en">think</td></tr>
<tr><td class="en">sing</td><td class="en">sink</td></tr>
<tr><td class="en">wing</td><td class="en">wink</td></tr>
<tr><td class="en">rang</td><td class="en">rank</td></tr>
</table>
<div class="tip">Българите често казват <em>„тинкинк“</em> вместо <span class="en">thinking</span>. Задръж звука в носа и не добавяй „к“ накрая: <span class="en">think-ing</span>.</div>
""",
            "exercises": [
                L("Коя дума чу?", "thing", ["thing", "think"], 0),
                L("Коя дума чу?", "sink", ["sing", "sink"], 1),
                C("Има ли „к“ в края на going?", ["Не, само носов звук", "Да, „гоуинк“"], 0),
                S("I'm thinking about going shopping."),
                S("She's singing in the morning."),
                D("What are you doing this evening?"),
            ],
        },
    ],
    "a2-how-we-do": [
        {
            "slug": "a2-simple-vs-continuous", "title": "I work или I'm working?", "title_en": "Present Simple vs Continuous",
            "kind": "grammar", "minutes": 8, "xp": 20, "summary": "Най-честата грешка на българите: в българския има едно сегашно време.",
            "theory": """
<p>В българския „работя“ значи и „работя по принцип“, и „работя в момента“. В английския това са <strong>две различни времена</strong>.</p>
<table>
<tr><th>Present Simple</th><th>Present Continuous</th></tr>
<tr><td>навици, факти, винаги: <span class="en">I work in a bank.</span></td><td>сега, в момента: <span class="en">I'm working now.</span></td></tr>
<tr><td>сигнали: <span class="en">always, usually, every day</span></td><td>сигнали: <span class="en">now, at the moment, today, this week</span></td></tr>
<tr><td class="en">She lives in Sofia.</td><td>временно: <span class="en">She's living with friends this month.</span></td></tr>
<tr><td class="en">Do you speak English?</td><td class="en">What are you doing?</td></tr>
</table>
<div class="tip">Глаголи като <span class="en">like, want, know, need, understand</span> обикновено са само в Present Simple: <span class="en">I know</span>, не <em>I'm knowing</em>.</div>
""",
            "exercises": [
                C("Look! It ___ .", ["'s raining", "rains"], 0),
                C("It ___ a lot in London.", ["rains", "is raining"], 0),
                C("I ___ what you mean.", ["understand", "am understanding"], 0),
                C("Shh! The baby ___ .", ["is sleeping", "sleeps"], 0),
                C("She usually ___ by bus, but today she ___ .", ["goes / is walking", "is going / walks", "goes / walks"], 0),
                F("What ___ you doing right now?", "are"),
                O("Тази седмица работя от вкъщи.", "I am working from home this week|I'm working from home this week"),
            ],
        },
    ],
    "a2-skills": [
        {
            "slug": "a2-read-event-poster", "title": "Четене: афиш за събитие", "title_en": "Reading: an event poster",
            "kind": "reading", "minutes": 6, "xp": 20, "summary": "Умение: дата, място, цена и условия от афиш.",
            "theory": """<div class="tip"><strong>Умение: афиши и обяви.</strong> Информацията е разпръсната. Търси ключовите блокове: кога, къде, цена, за кого, как да се запишеш.</div>""" + reading("Summer Food Festival", [
                "Saturday 14 and Sunday 15 June, 11 am to 10 pm, Riverside Park.",
                "Over 40 food stalls from around the world, live music every evening from 7 pm, and cooking classes for children (age 6 to 12).",
                "Tickets: £5 online, £7 on the day. Children under 12 go free. Cooking classes must be booked in advance.",
                "No dogs, except guide dogs. Free bus from the city centre every 20 minutes.",
            ], [("stalls", "сергии"), ("live music", "музика на живо"), ("on the day", "на място, в деня"),
                ("in advance", "предварително"), ("guide dogs", "кучета водачи")]),
            "exercises": [
                C("Колко струва билетът, ако го купиш онлайн?", ["£5", "£7", "Безплатен е"], 0, instruction=RQ),
                C("От колко часа е музиката на живо?", ["От 19:00", "От 11:00", "От 22:00"], 0, instruction=RQ),
                C("Детето ти е на 8 години. Колко плаща за вход?", ["Нищо", "£5", "£7"], 0, instruction=RQ),
                C("Какво трябва да се запази предварително?", ["Готварските класове", "Билетите", "Автобуса"], 0, instruction=RQ),
                C("Може ли да вземеш кучето си?", ["Не, само кучета водачи", "Да", "Само малки кучета"], 0, instruction=RQ),
                F("There is a free bus every ___ minutes.", "20|twenty"),
            ],
        },
        {
            "slug": "a2-time-expressions", "title": "Ago, for, since, during", "title_en": "Time expressions",
            "kind": "vocabulary", "minutes": 7, "xp": 20, "summary": "„Преди“ и „от“: думите, които българите бъркат.",
            "theory": """
<table>
<tr><th>Дума</th><th>Значение</th><th>Пример</th></tr>
<tr><td class="en">ago</td><td>преди (след периода)</td><td class="en">I came two years ago.</td></tr>
<tr><td class="en">for</td><td>от (колко време)</td><td class="en">I've lived here for two years.</td></tr>
<tr><td class="en">since</td><td>от (кога, начална точка)</td><td class="en">I've lived here since 2024.</td></tr>
<tr><td class="en">during</td><td>по време на</td><td class="en">during the film</td></tr>
<tr><td class="en">before / after</td><td>преди / след</td><td class="en">before dinner, after work</td></tr>
<tr><td class="en">until / by</td><td>до (продължава) / до (най-късно)</td><td class="en">I'll wait until six. Finish it by six.</td></tr>
</table>
<div class="tip">„Преди две години“ е <span class="en">two years ago</span>: <span class="en">ago</span> стои <strong>след</strong> периода. Не <em>before two years</em>.</div>
""",
            "exercises": [
                C("Преди три дни:", ["three days ago", "before three days", "ago three days"], 0),
                C("I've known her ___ ten years.", ["for", "since", "ago"], 0),
                C("I've known her ___ 2015.", ["since", "for", "from"], 0),
                C("Don't use your phone ___ the lesson.", ["during", "for", "while"], 0),
                C("Please send it ___ Friday. (най-късно)", ["by", "until", "for"], 0),
                F("We met five years ___ .", "ago"),
            ],
        },
    ],
    "a2-speak-write": [
        {
            "slug": "a2-write-hotel-request", "title": "Пиши: имейл до хотела", "title_en": "Writing: an email to a hotel",
            "kind": "writing", "minutes": 8, "xp": 20, "summary": "Помоли за нещо преди пристигането: ранно настаняване, тиха стая.",
            "theory": model_text("Booking 4471: two requests", [
                "Dear Sir or Madam,",
                "I have a booking for two nights from 12 August (booking number 4471).",
                "My flight arrives early in the morning. Is it possible to check in before 2 pm? Also, could we have a quiet room, please?",
                "Thank you for your help.",
                "Best regards,",
                "Dimitar Kolev",
            ], [("I have a booking for...", "кой си: дати и номер"),
                ("Is it possible to...?", "учтива молба"), ("could we have..., please?", "втора молба"),
                ("Thank you for your help.", "благодарност предварително"), ("Best regards,", "неутрален край")]),
            "exercises": [
                C("Учтива молба:", ["Is it possible to check in early?", "I want check in early.", "Give me early check-in."], 0),
                C("Кое трябва да включиш в имейла?", ["Дати и номер на резервацията", "Цялата си биография", "Нищо конкретно"], 0),
                C("Подходящ край:", ["Best regards,", "Love,", "Bye!!!"], 0),
                F("Could we ___ a room with a view, please?", "have"),
                W("Напиши кратък имейл до хотел: пристигаш късно вечерта и питаш дали рецепцията работи след полунощ.",
                  "Dear Sir or Madam, I have a booking for three nights from 5 May. My train arrives late, so I will be at the hotel after midnight. Is the reception open at that time? Thank you for your help. Best regards, Ana Ivanova",
                  ["Обръщение и край", "Дати на резервацията", "Учтив въпрос (Is it possible / Is the reception open...?)", "Благодарност"]),
            ],
        },
    ],
    # ---------------- B1 ----------------
    "b1-listening": [
        {
            "slug": "b1-listen-police", "title": "В полицията: открадната чанта", "title_en": "Reporting a theft",
            "kind": "listening", "minutes": 8, "xp": 25, "summary": "Как да опишеш какво е станало и какво е откраднато.", "theory": INTRO,
            "dialogue": dialogue(
                ("Officer", "Good afternoon. What seems to be the problem?", "Добър ден. Какъв е проблемът?"),
                ("Svetla", "Someone stole my bag about an hour ago. I was sitting outside a café on the main square.", "Някой открадна чантата ми преди около час. Седях пред едно кафене на главния площад."),
                ("Officer", "I'm sorry to hear that. Did you see the person?", "Съжалявам да го чуя. Видяхте ли човека?"),
                ("Svetla", "Not really. A man asked me for directions, and when I turned round, the bag had gone from the chair next to me.", "Не съвсем. Един мъж ме попита за посока и когато се обърнах, чантата я нямаше на стола до мен."),
                ("Officer", "That's a common trick, I'm afraid. What was in the bag?", "Това е често срещан номер, за съжаление. Какво имаше в чантата?"),
                ("Svetla", "My wallet, with two cards and about eighty euros, and my sunglasses. Luckily, I had my passport in the hotel safe.", "Портфейлът ми с две карти и около осемдесет евро, и слънчевите ми очила. За щастие паспортът ми беше в сейфа на хотела."),
                ("Officer", "Good. Have you cancelled the cards?", "Добре. Блокирахте ли картите?"),
                ("Svetla", "Yes, straight away. I need a police report for my insurance.", "Да, веднага. Трябва ми полицейски протокол за застраховката."),
                ("Officer", "Of course. Fill in this form, and I'll give you a copy with a reference number.", "Разбира се. Попълнете този формуляр и ще ви дам копие с номер."),
            ),
            "exercises": [
                C("Кога е откраднана чантата?", ["Преди около час", "Вчера", "Тази сутрин"], 0, instruction=DQ),
                C("Как е станала кражбата?", ["Мъж я разсейва с въпрос за посока", "Някой е бутнал Светла", "Оставила я е в таксито"], 0, instruction=DQ),
                C("Какво не е било в чантата?", ["Паспортът", "Портфейлът", "Слънчевите очила"], 0, instruction=DQ),
                C("Защо ѝ трябва протокол?", ["За застраховката", "За посолството", "За банката"], 0, instruction=DQ),
                L("Какво означава a common trick?", "That's a common trick, I'm afraid.", ["често срещан номер", "обикновен фокус", "лесна задача"], 0),
                D("Someone stole my bag an hour ago."),
                S("I need a police report for my insurance."),
            ],
        },
    ],
    "b1-experience-advice": [
        {
            "slug": "b1-perfect-vs-past", "title": "I've been или I went?", "title_en": "Present Perfect vs Past Simple",
            "kind": "grammar", "minutes": 8, "xp": 25, "summary": "Кога е важно КОГА: най-трудният избор за българите.",
            "theory": """
<table>
<tr><th>Present Perfect</th><th>Past Simple</th></tr>
<tr><td>опит, без да казваме кога: <span class="en">I've been to Paris.</span></td><td>конкретно кога: <span class="en">I went to Paris in 2022.</span></td></tr>
<tr><td>резултат сега: <span class="en">I've lost my keys.</span> (нямам ги)</td><td>приключила история: <span class="en">I lost my keys yesterday.</span></td></tr>
<tr><td>период до сега: <span class="en">this week, ever, never, yet, since, for</span></td><td>завършено време: <span class="en">yesterday, last year, ago, in 2020, when...</span></td></tr>
</table>
<div class="tip">Ако в изречението има <span class="en">yesterday, ago, last...</span> или въпросът е <span class="en">When...?</span>, използвай Past Simple: <span class="en">When did you arrive?</span>, не <em>When have you arrived?</em></div>
""",
            "exercises": [
                C("I ___ to Italy three times.", ["have been", "went"], 0),
                C("I ___ to Italy last summer.", ["went", "have been"], 0),
                C("When ___ you ___ here?", ["did / arrive", "have / arrived"], 0),
                C("Oh no! I ___ my phone. Have you seen it?", ["'ve lost", "lost"], 0, "Резултатът е сега: телефонът липсва."),
                C("She ___ in Berlin for five years, but now she lives in Sofia.", ["lived", "has lived"], 0, "Периодът е приключил."),
                F("I ___ (not / see) him since Monday.", "haven't seen|have not seen"),
                O("Ходил ли си някога в Лондон?", "Have you ever been to London"),
            ],
        },
    ],
    "b1-tenses-detail": [
        {
            "slug": "b1-word-order", "title": "Словоред: I like English very much", "title_en": "Word order",
            "kind": "grammar", "minutes": 7, "xp": 20, "summary": "Подлог, глагол, допълнение: и къде отиват наречията.",
            "theory": """
<p>В българския словоредът е свободен. В английския <strong>подлог + глагол + допълнение</strong> почти никога не се разделят.</p>
<table>
<tr><th>Правило</th><th>Правилно</th><th>Грешно</th></tr>
<tr><td>нищо между глагола и допълнението</td><td class="en">I like English very much.</td><td><em>I like very much English.</em></td></tr>
<tr><td>колко често: преди основния глагол, след to be</td><td class="en">I often go there. She is always late.</td><td><em>I go often there.</em></td></tr>
<tr><td>място преди време</td><td class="en">I met her at the station yesterday.</td><td><em>I met her yesterday at the station.</em> (възможно, но по-рядко)</td></tr>
<tr><td>прилагателно преди съществително</td><td class="en">a beautiful old house</td><td><em>a house beautiful old</em></td></tr>
</table>
""",
            "exercises": [
                C("Кое е правилно?", ["I like this city very much.", "I like very much this city."], 0),
                C("Кое е правилно?", ["She speaks English well.", "She speaks well English."], 0),
                C("Кое е правилно?", ["We usually have dinner at eight.", "We have usually dinner at eight.", "Usually we dinner have at eight."], 0),
                C("Кое е правилно?", ["He is never late.", "He never is late."], 0),
                O("Много обичам музиката.", "I love music very much|I really love music"),
                O("Тя винаги пие кафе сутрин.", "She always drinks coffee in the morning"),
            ],
        },
    ],
    "b1-skills": [
        {
            "slug": "b1-read-baggage", "title": "Четене: правила за багажа", "title_en": "Reading: airline baggage rules",
            "kind": "reading", "minutes": 8, "xp": 25, "summary": "Умение: условия, изключения и малкия шрифт.",
            "theory": """<div class="tip"><strong>Умение: правила и условия.</strong> Обърни внимание на думите, които ограничават: <span class="en">only, unless, except, must not, up to, per</span>. Те променят смисъла на цялото изречение.</div>""" + reading("SkyLine baggage policy", [
                "Every passenger may bring one small bag (up to 40 x 30 x 20 cm) that fits under the seat. This is included in all fares.",
                "A larger cabin bag (up to 10 kg) is only included in Plus and Flex fares. With a Basic fare, it costs €25 if added online, or €45 at the airport.",
                "Liquids in hand luggage must be in containers of 100 ml or less, in one clear plastic bag.",
                "Checked bags must not weigh more than 23 kg. Each extra kilo costs €12. Sports equipment must be booked at least 24 hours before departure.",
            ], [("fits under the seat", "събира се под седалката"), ("fare", "тарифа"), ("liquids", "течности"),
                ("containers", "опаковки"), ("checked bags", "чекиран багаж"), ("weigh", "тежи")]),
            "exercises": [
                C("Имаш Basic билет и искаш голяма ръчна чанта. Колко е най-евтино?", ["€25 онлайн", "€45", "Безплатно"], 0, instruction=RQ),
                C("Кой багаж е включен във всички тарифи?", ["Малка чанта под седалката", "10 kg ръчен багаж", "23 kg чекиран"], 0, instruction=RQ),
                C("Куфарът ти тежи 25 kg. Колко доплащаш?", ["€24", "€12", "€25"], 0, instruction=RQ),
                C("Имаш шампоан 150 ml. Можеш ли да го вземеш в ръчния багаж?", ["Не", "Да", "Само в Flex"], 0, instruction=RQ),
                C("Кога трябва да запазиш спортна екипировка?", ["Поне 24 часа преди полета", "На летището", "Не е нужно"], 0, instruction=RQ),
                F("Checked bags must not ___ more than 23 kg.", "weigh"),
            ],
        },
        {
            "slug": "b1-personality", "title": "Характер: reliable, bossy, generous", "title_en": "Personality adjectives",
            "kind": "vocabulary", "minutes": 7, "xp": 25, "summary": "Как да опишеш какъв е човекът, не само как изглежда.",
            "theory": """
<table>
<tr><th>Положително</th><th>Значение</th><th>Отрицателно</th><th>Значение</th></tr>
<tr><td class="en">reliable</td><td>надежден</td><td class="en">lazy</td><td>мързелив</td></tr>
<tr><td class="en">generous</td><td>щедър</td><td class="en">mean (UK)</td><td>стиснат</td></tr>
<tr><td class="en">outgoing</td><td>общителен</td><td class="en">bossy</td><td>командаджия</td></tr>
<tr><td class="en">patient</td><td>търпелив</td><td class="en">moody</td><td>с променливо настроение</td></tr>
<tr><td class="en">hard-working</td><td>работлив</td><td class="en">selfish</td><td>егоистичен</td></tr>
<tr><td class="en">easy-going</td><td>спокоен, лесен за общуване</td><td class="en">stubborn</td><td>инат</td></tr>
</table>
<div class="tip">Въпросът за характер е <span class="en">What is she like?</span> За външност: <span class="en">What does she look like?</span></div>
""",
            "exercises": [
                C("He never pays for anything. He's so ___ .", ["mean", "generous", "patient"], 0),
                C("She always does what she promises. She's ___ .", ["reliable", "moody", "bossy"], 0),
                C("He loves meeting new people. He's very ___ .", ["outgoing", "stubborn", "selfish"], 0),
                C("Какъв е тя (характер)?", ["What is she like?", "What does she look like?", "How does she like?"], 0),
                F("My boss tells everyone what to do all the time. He's really ___ .", "bossy"),
                F("She's very ___ ; nothing makes her stressed. (спокойна)", "easy-going|relaxed|laid-back"),
            ],
        },
    ],
    "b1-speak-write": [
        {
            "slug": "b1-write-online-review", "title": "Пиши: онлайн отзив", "title_en": "Writing: an online review",
            "kind": "writing", "minutes": 8, "xp": 25, "summary": "Кратък, полезен отзив за хотел или ресторант.",
            "theory": model_text("Great location, noisy nights", [
                "★★★★☆ We stayed at the Hotel Marina for three nights in July.",
                "The location is perfect: the beach is two minutes away, and there are lots of restaurants nearby. The staff were friendly and the breakfast was excellent.",
                "However, our room faced the main street, so it was quite noisy at night. If you are a light sleeper, ask for a room at the back.",
                "Overall, good value for money, and we would stay here again.",
            ], [("We stayed... for three nights in July.", "кога и колко"),
                ("The location is perfect:...", "плюсове с конкретни детайли"),
                ("However,...", "минуси, честно и спокойно"),
                ("If you are..., ask for...", "полезен съвет за другите"),
                ("Overall,...", "обща оценка")]),
            "exercises": [
                C("Кое прави отзива полезен?", ["Конкретни детайли и съвет", "Само „Супер!!!“", "Много удивителни"], 0),
                C("Учтив минус:", ["However, the room was quite noisy.", "The room was the worst ever!!!", "Noisy. Bad."], 0),
                C("Подходящ съвет:", ["Ask for a room at the back.", "Never go there.", "Whatever."], 0),
                F("___ , it's good value for money. (Като цяло)", "Overall|All in all"),
                W("Напиши кратък онлайн отзив за ресторант или кафене, където си бил/а: какво беше добре, какво не и съвет.",
                  "We had dinner at Green Garden last Friday. The pasta was delicious and the waiters were really friendly. However, the music was too loud to talk. If you want a quiet evening, book a table outside. Overall, we'd definitely go back.",
                  ["Кога си бил/а", "Поне един плюс с детайл", "Минус с However", "Съвет за другите", "Обща оценка"]),
            ],
        },
    ],
    # ---------------- B2 ----------------
    "b2-listening": [
        {
            "slug": "b2-listen-flight-delay", "title": "Закъснял полет", "title_en": "A delayed flight", "kind": "listening",
            "minutes": 8, "xp": 30, "summary": "Пропуснат връзка, нов полет и права на пътника.", "theory": INTRO,
            "dialogue": dialogue(
                ("Agent", "Next, please. How can I help?", "Следващият, моля. С какво мога да помогна?"),
                ("Boris", "My flight from Sofia was delayed by three hours, so I've missed my connection to Dublin.", "Полетът ми от София закъсня с три часа, така че изпуснах връзката си за Дъблин."),
                ("Agent", "I'm sorry about that. Let me see... The next flight with seats available leaves at 7:15 tomorrow morning. I can rebook you on that one.", "Съжалявам. Нека видя... Следващият полет със свободни места тръгва в 7:15 утре сутринта. Мога да ви пренасоча за него."),
                ("Boris", "Tomorrow? So where am I supposed to stay tonight?", "Утре? И къде трябва да спя тази нощ?"),
                ("Agent", "As the delay was within our control, we'll provide a hotel room near the airport and meal vouchers for dinner and breakfast.", "Тъй като закъснението е по наша вина, ще осигурим хотелска стая близо до летището и ваучери за вечеря и закуска."),
                ("Boris", "And what about compensation? I'll arrive almost a day late.", "А обезщетение? Ще пристигна почти с ден закъснение."),
                ("Agent", "Under EU rules, you may be entitled to compensation. You can claim it on our website; just keep your boarding passes and receipts.", "Според правилата на ЕС може да имате право на обезщетение. Можете да го поискате на сайта ни; просто пазете бордните си карти и касовите бележки."),
                ("Boris", "Fine. And my suitcase?", "Добре. А куфарът ми?"),
                ("Agent", "It's checked through to Dublin, so you don't need to collect it.", "Чекиран е директно до Дъблин, така че не е нужно да го взимате."),
            ),
            "exercises": [
                C("Защо Борис е изпуснал полета за Дъблин?", ["Първият полет закъсня с три часа", "Не е чул обявлението", "Полетът е отменен"], 0, instruction=DQ),
                C("Кога е новият полет?", ["Утре в 7:15", "Днес в 19:15", "След три часа"], 0, instruction=DQ),
                C("Какво осигурява авиокомпанията?", ["Хотел и ваучери за храна", "Само ваучер за вечеря", "Нищо"], 0, instruction=DQ),
                C("Какво трябва да пази за обезщетението?", ["Бордните карти и бележките", "Паспорта", "Багажната разписка"], 0, instruction=DQ),
                C("Трябва ли да вземе куфара си?", ["Не, чекиран е до Дъблин", "Да, на лентата", "Не е ясно"], 0, instruction=DQ),
                L("Какво означава rebook you?", "I can rebook you on that one.", ["да ви пренасоча на друг полет", "да ви върна парите", "да ви запиша отново за изпит"], 0),
                D("I've missed my connection."),
            ],
        },
    ],
    "b2-complex-structures": [
        {
            "slug": "b2-whatever", "title": "Whatever, wherever, however", "title_en": "Words ending in -ever",
            "kind": "grammar", "minutes": 7, "xp": 25, "summary": "Каквото и да..., където и да..., колкото и да...",
            "theory": """
<table>
<tr><th>Дума</th><th>Значение</th><th>Пример</th></tr>
<tr><td class="en">whatever</td><td>каквото и да</td><td class="en">Whatever you decide, I'll support you.</td></tr>
<tr><td class="en">wherever</td><td>където и да</td><td class="en">Sit wherever you like.</td></tr>
<tr><td class="en">whenever</td><td>когато и да, всеки път когато</td><td class="en">Call me whenever you need help.</td></tr>
<tr><td class="en">whoever</td><td>който и да</td><td class="en">Whoever wins, it'll be a great match.</td></tr>
<tr><td class="en">however + прилагателно</td><td>колкото и да</td><td class="en">However hard I try, I can't remember it.</td></tr>
<tr><td class="en">no matter what / where / how</td><td>без значение</td><td class="en">No matter what happens, stay calm.</td></tr>
</table>
<div class="tip">След тези думи <strong>не</strong> използваме <span class="en">will</span> за бъдещето: <span class="en">Whatever happens</span>, не <em>whatever will happen</em>.</div>
""",
            "exercises": [
                C("You can sit ___ you want.", ["wherever", "whatever", "whoever"], 0),
                C("___ hard she works, she never seems tired.", ["However", "Whatever", "Whenever"], 0),
                C("___ calls, tell them I'm busy.", ["Whoever", "Whatever", "However"], 0),
                C("___ happens, don't panic.", ["Whatever", "Whatever will", "However"], 0),
                F("Come and visit ___ you like. (когато и да)", "whenever"),
                O("Каквото и да кажеш, няма да повярвам.", "Whatever you say I won't believe it|Whatever you say I will not believe it"),
            ],
        },
    ],
    "b2-skills": [
        {
            "slug": "b2-read-multiple-choice", "title": "Четене: въпроси с избор", "title_en": "Reading: multiple-choice technique",
            "kind": "reading", "minutes": 10, "xp": 30, "summary": "Умение: изпитна техника за въпроси с няколко отговора.",
            "theory": """<div class="tip"><strong>Умение: multiple choice.</strong> 1) Прочети въпроса, но не и отговорите. 2) Намери мястото в текста и формулирай отговора със свои думи. 3) Чак тогава избери най-близкия вариант. 4) Изключи вариантите, които са верни като факт, но не отговарят на въпроса.</div>""" + reading("Why I gave up my car", [
                "When I sold my car last spring, my friends assumed I had money problems. In fact, I had simply worked out that I was paying around €300 a month for something that spent 95% of its life parked.",
                "The first weeks were frustrating. A trip to the supermarket that used to take twenty minutes now took an hour, and I missed the freedom of leaving whenever I wanted.",
                "Gradually, though, I adapted. I started shopping online, joined a car-sharing club for the occasional long trip, and discovered that cycling to work was quicker than driving through rush-hour traffic.",
                "I won't pretend it suits everyone. If I had children or lived in a village, I'd almost certainly still need a car. But for a city-dweller like me, it's been one of the best decisions I've made.",
            ], [("assumed", "предположиха"), ("worked out", "пресметнах, разбрах"), ("frustrating", "дразнещ"),
                ("gradually", "постепенно"), ("occasional", "рядък, от време на време"), ("city-dweller", "градски жител")]),
            "exercises": [
                C("Защо авторът е продал колата?", ["Сметнал е, че плаща много за нещо, което почти не ползва", "Имал е финансови проблеми", "Колата е била стара"], 0, instruction=RQ),
                C("Как се е чувствал в началото?", ["Раздразнен и ограничен", "Веднага по-щастлив", "Безразличен"], 0, instruction=RQ),
                C("Какво използва за дълги пътувания?", ["Клуб за споделени коли", "Такси", "Влак"], 0, instruction=RQ),
                C("Какво мисли авторът за решението за другите?", ["Не е подходящо за всички", "Всички трябва да продадат колите си", "Съжалява за решението"], 0, instruction=RQ),
                C("Отговорът „Имал е финансови проблеми“ е капан, защото:", ["Това предполагат приятелите му, но не е вярно", "Не се споменава", "Е твърде кратък"], 0),
            ],
        },
        {
            "slug": "b2-travel-idioms", "title": "Идиоми за пътуване", "title_en": "Travel idioms",
            "kind": "vocabulary", "minutes": 7, "xp": 30, "summary": "Hit the road, off the beaten track, travel light.",
            "theory": """
<table>
<tr><th>Идиом</th><th>Значение</th></tr>
<tr><td class="en">hit the road</td><td>тръгвам на път</td></tr>
<tr><td class="en">off the beaten track</td><td>далеч от туристическите места</td></tr>
<tr><td class="en">travel light</td><td>пътувам с малко багаж</td></tr>
<tr><td class="en">itchy feet</td><td>желание да пътуваш, да не стоиш на едно място</td></tr>
<tr><td class="en">a tourist trap</td><td>място, което е скъпо и пълно с туристи</td></tr>
<tr><td class="en">catch some rays</td><td>пека се на слънце</td></tr>
<tr><td class="en">a red-eye (flight)</td><td>нощен полет</td></tr>
<tr><td class="en">jet lag</td><td>умора от часовата разлика</td></tr>
</table>
""",
            "exercises": [
                C("We want to see the real country, ___ .", ["off the beaten track", "in a tourist trap", "on a red-eye"], 0),
                C("That restaurant is a ___ : €8 for a coffee!", ["tourist trap", "beaten track", "jet lag"], 0),
                C("I only take a backpack. I like to ___ .", ["travel light", "hit the road", "catch some rays"], 0),
                C("It's 6 am. Time to ___ !", ["hit the road", "travel light", "get itchy feet"], 0),
                F("After the flight from Japan I had terrible jet ___ .", "lag"),
                F("I've been home for a month and I've already got itchy ___ .", "feet"),
            ],
        },
    ],
    # ---------------- C1 ----------------
    "c1-listening": [
        {
            "slug": "c1-listen-tipping", "title": "Подкаст: бакшиш по света", "title_en": "Podcast: tipping around the world",
            "kind": "listening", "minutes": 9, "xp": 35, "summary": "Културни различия и защо американците оставят 20%.", "theory": INTRO,
            "dialogue": dialogue(
                ("Host", "Tipping is one of those things travellers get anxious about. Leave too little and you're rude; too much and you look naive. Nadia, where do people get it most wrong?", "Бакшишът е едно от нещата, които притесняват пътуващите. Оставиш малко – груб си; много – изглеждаш наивен. Надя, къде хората грешат най-често?"),
                ("Nadia", "Without a doubt, the United States. Waiting staff there are often paid well below the minimum wage, on the assumption that tips will make up the difference. So twenty percent isn't a reward for great service; it's effectively part of the price.", "Без съмнение в САЩ. Сервитьорите там често получават много под минималната заплата, с допускането, че бакшишите ще покрият разликата. Така че двайсет процента не са награда за отлично обслужване; на практика са част от цената."),
                ("Host", "Whereas in Japan, I hear, tipping can actually cause offence.", "Докато в Япония, чувам, бакшишът може дори да обиди."),
                ("Nadia", "It can cause confusion, certainly. Good service is regarded as the norm, not something extra you pay for. A waiter may well run after you to return the money you've 'forgotten'.", "Може да предизвика объркване, със сигурност. Доброто обслужване се смята за норма, а не за нещо допълнително, за което плащаш. Сервитьорът може да изтича след вас, за да ви върне „забравените“ пари."),
                ("Host", "And Europe sits somewhere in between?", "А Европа е някъде по средата?"),
                ("Nadia", "Broadly speaking, yes. Rounding up the bill or leaving five to ten percent is appreciated, but always check whether a service charge has already been added. Many tourists end up tipping twice without realising it.", "Като цяло, да. Закръгляне на сметката или пет до десет процента се оценяват, но винаги проверявайте дали вече не е добавена такса за обслужване. Много туристи в крайна сметка дават бакшиш два пъти, без да усетят."),
            ),
            "exercises": [
                C("Защо в САЩ бакшишът е около 20%?", ["Заплатите на сервитьорите разчитат на бакшишите", "Обслужването е изключително", "Такъв е законът"], 0, instruction=DQ),
                C("Какво може да се случи в Япония?", ["Сервитьорът да ви върне парите", "Да ви поискат повече", "Да ви обидят"], 0, instruction=DQ),
                C("Какъв е съветът за Европа?", ["Проверете дали няма такса за обслужване", "Винаги оставяйте 20%", "Никога не оставяйте бакшиш"], 0, instruction=DQ),
                C("Какво означава it's effectively part of the price?", ["На практика е част от цената", "Ефективен е", "Не е задължителен"], 0, instruction=DQ),
                L("Какво означава rounding up the bill?", "Rounding up the bill is appreciated.", ["закръгляне на сметката нагоре", "разделяне на сметката", "плащане в брой"], 0),
                L("Какво означава broadly speaking?", "Broadly speaking, yes.", ["като цяло", "на висок глас", "откровено казано"], 0),
                D("Always check whether a service charge has been added."),
            ],
        },
    ],
    "c1-complex": [
        {
            "slug": "c1-past-modals", "title": "Needn't have, should have, could have", "title_en": "Past modals",
            "kind": "grammar", "minutes": 8, "xp": 30, "summary": "Съжаления, критика и излишни усилия в миналото.",
            "theory": """
<table>
<tr><th>Форма</th><th>Значение</th><th>Пример</th></tr>
<tr><td class="en">should have + 3-та форма</td><td>трябваше (но не го направих)</td><td class="en">I should have booked earlier.</td></tr>
<tr><td class="en">shouldn't have</td><td>не трябваше (но го направих)</td><td class="en">You shouldn't have told him.</td></tr>
<tr><td class="en">could have</td><td>можеше (възможност, която не се случи)</td><td class="en">You could have called me!</td></tr>
<tr><td class="en">needn't have</td><td>направих го, но не е било нужно</td><td class="en">I needn't have cooked; they'd already eaten.</td></tr>
<tr><td class="en">didn't need to</td><td>не беше нужно (и обикновено не го направих)</td><td class="en">I didn't need to cook, so I relaxed.</td></tr>
</table>
<div class="tip"><span class="en">I needn't have taken an umbrella</span> = взех чадър напразно. <span class="en">I didn't need to take an umbrella</span> = не беше нужно (обикновено не съм взел).</div>
""",
            "exercises": [
                C("We ___ so much food. Half of it was left over. (купихме напразно)", ["needn't have bought", "didn't need to buy", "shouldn't buy"], 0),
                C("It was a sunny day, so I ___ take an umbrella. I left it at home.", ["didn't need to", "needn't have"], 0),
                C("You ___ me! I would have helped. (можеше да ми кажеш)", ["could have told", "could tell", "must have told"], 0),
                C("I failed. I ___ more.", ["should have studied", "should study", "must have studied"], 0),
                F("You shouldn't ___ (say) that to her. She was really upset.", "have said"),
                O("Трябваше да тръгнем по-рано.", "We should have left earlier"),
            ],
        },
    ],
    "c1-speak-write": [
        {
            "slug": "c1-write-compensation", "title": "Пиши: искане за обезщетение", "title_en": "Writing: a compensation claim",
            "kind": "writing", "minutes": 10, "xp": 35, "summary": "Официално, твърдо и с факти: искане към авиокомпания.",
            "theory": model_text("Claim for compensation: flight FB 218, 3 March", [
                "Dear Customer Relations Team,",
                "I am writing to claim compensation for the delay to flight FB 218 from Sofia to Dublin on 3 March, booking reference KX72PL.",
                "The flight departed over three hours late, as a result of which I missed my connecting flight and arrived at my destination 19 hours later than scheduled. At no point were passengers given a clear explanation for the delay.",
                "Under EU Regulation 261/2004, I believe I am entitled to compensation of €400, in addition to reimbursement of the €38 I spent on meals, receipts for which are attached.",
                "I would appreciate a response within 14 days.",
                "Yours faithfully,",
                "Boris Petrov",
            ], [("I am writing to claim compensation for...", "цел, с точни данни"),
                ("as a result of which...", "последица, официално"),
                ("At no point were passengers given...", "инверсия за силна критика"),
                ("Under EU Regulation..., I believe I am entitled to...", "правно основание и сума"),
                ("I would appreciate a response within 14 days.", "твърд краен срок, учтиво")]),
            "exercises": [
                C("Кое е най-силното, но учтиво изречение?", ["At no point were we given an explanation.", "You never tell us anything!!!", "Nobody said nothing."], 0),
                C("Какво задължително трябва да включиш?", ["Номер на полет, дата и резервация", "Мнението си за храната", "Историята на пътуването"], 0),
                C("I would appreciate a response within 14 days. Това е:", ["твърд, но учтив срок", "заплаха", "въпрос"], 0),
                F("I believe I am ___ to compensation. (имам право)", "entitled"),
                W("Напиши първите два абзаца на официално оплакване до хотел: стаята не отговаря на резервираната и искаш частично възстановяване на сумата.",
                  "I am writing regarding my stay at your hotel from 2 to 5 May, booking reference 88213. Although I had booked a sea-view room, I was given a room facing the car park, and no alternative was offered. I would therefore like to request a partial refund of the difference in price.",
                  ["Цел и точни данни", "Фактите, без емоции", "Ясно искане", "Официален стил, без съкращения"]),
            ],
        },
    ],
    # ---------------- C2 ----------------
    "c2-listening": [
        {
            "slug": "c2-listen-adult-learning", "title": "Интервю: езици в зряла възраст", "title_en": "Interview: learning languages as an adult",
            "kind": "listening", "minutes": 9, "xp": 40, "summary": "Митът за „твърде късно“ и предимствата на възрастните.", "theory": INTRO,
            "dialogue": dialogue(
                ("Host", "Many adults believe they've simply left it too late to learn a language. Is there any truth in that?", "Много възрастни вярват, че просто е твърде късно да научат език. Има ли истина в това?"),
                ("Expert", "Only up to a point. There's reasonable evidence that children who start young are more likely to end up with a native-like accent. But accent is only one part of the picture, and arguably the least important.", "Само до известна степен. Има доста доказателства, че децата, които започват рано, по-често постигат акцент като на носител. Но акцентът е само част от картината и вероятно най-маловажната."),
                ("Host", "So what do adults have going for them?", "Тогава какви предимства имат възрастните?"),
                ("Expert", "Quite a lot. Adults learn grammar and vocabulary faster in the early stages, because they can draw on what they already know and use deliberate strategies. They can look a rule up, rather than waiting to absorb it.", "Доста. Възрастните учат граматика и речник по-бързо в началото, защото могат да разчитат на вече наученото и да използват съзнателни стратегии. Могат да проверят правило, вместо да чакат да го попият."),
                ("Host", "Then why do so many give up?", "Тогава защо толкова много се отказват?"),
                ("Expert", "Mostly time and expectations. Children get thousands of hours of exposure; adults squeeze in an hour a week and wonder why they're not fluent. And adults tend to fear sounding foolish, which keeps them silent precisely when they most need to practise.", "Предимно време и очаквания. Децата получават хиляди часове контакт с езика; възрастните вмъкват по час седмично и се чудят защо не говорят свободно. А възрастните се страхуват да не прозвучат глупаво, което ги държи мълчаливи точно когато най-много трябва да упражняват."),
                ("Host", "Your advice, then?", "Съветът ви тогава?"),
                ("Expert", "Little and often beats long and rare, and make peace with making mistakes. Fluency comes from speaking badly for quite a long time.", "Малко и често е по-добре от много и рядко, и се примирете с грешките. Свободата в говоренето идва от това дълго време да говориш лошо."),
            ),
            "exercises": [
                C("В какво децата наистина имат предимство?", ["Акцент като на носител", "Граматиката", "Речника"], 0, instruction=DQ),
                C("Защо възрастните учат по-бързо в началото?", ["Използват наученото и съзнателни стратегии", "Имат повече време", "Слушат повече"], 0, instruction=DQ),
                C("Кои са двете основни причини възрастните да се отказват?", ["Време и очаквания", "Пари и учители", "Памет и възраст"], 0, instruction=DQ),
                C("Какво пречи на възрастните да упражняват?", ["Страхът да не звучат глупаво", "Липсата на учебници", "Акцентът"], 0, instruction=DQ),
                C("Little and often beats long and rare означава:", ["малко и често е по-добре от много и рядко", "дългите уроци са най-добри", "учи рядко, но много"], 0, instruction=DQ),
                L("Какво означава only up to a point?", "Only up to a point.", ["само до известна степен", "само до края", "точно така"], 0),
                D("Fluency comes from speaking badly for a long time."),
            ],
        },
    ],
}

MISTAKES = {
    "a1-pron-h": [
        ("a hour", "an hour", "В hour h е нямо: an."),
    ],
    "a1-place-prepositions": [
        ("in front the hotel", "in front of the hotel", "In front of: три думи."),
        ("opposite of the bank", "opposite the bank", "Opposite е без of."),
    ],
    "a1-containers": [
        ("a bottle water", "a bottle of water", "Винаги с of."),
    ],
    "a2-simple-vs-continuous": [
        ("I am working in a bank. (по принцип)", "I work in a bank.", "Постоянна работа: Present Simple."),
        ("I'm knowing the answer.", "I know the answer.", "Know не се използва в -ing форма."),
        ("Look! It rains.", "Look! It's raining.", "Сега, в момента: Present Continuous."),
    ],
    "a2-time-expressions": [
        ("before two years", "two years ago", "„Преди“ + период: ago след периода."),
        ("since two years", "for two years", "Период: for. Начална точка: since."),
    ],
    "a2-write-hotel-request": [
        ("I want check in early.", "Is it possible to check in early?", "Учтива молба, не заповед."),
    ],
    "b1-perfect-vs-past": [
        ("I have been to Paris last year.", "I went to Paris last year.", "Last year: Past Simple."),
        ("When have you arrived?", "When did you arrive?", "When...?: Past Simple."),
    ],
    "b1-word-order": [
        ("I like very much English.", "I like English very much.", "Нищо между глагола и допълнението."),
        ("I go often to the gym.", "I often go to the gym.", "Often е преди основния глагол."),
    ],
    "b1-personality": [
        ("How is she like?", "What is she like?", "Характер: What is she like?"),
    ],
    "b2-whatever": [
        ("Whatever will happen, stay calm.", "Whatever happens, stay calm.", "Без will след whatever."),
    ],
    "c1-past-modals": [
        ("I should studied more.", "I should have studied more.", "Should have + 3-та форма."),
        ("I needn't have taken an umbrella, so I left it at home.", "I didn't need to take an umbrella, so I left it at home.", "Не си го направил: didn't need to."),
    ],
}
