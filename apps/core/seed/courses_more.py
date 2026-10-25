"""Core topics from the British Council LearnEnglish level lists that the first course units did not cover."""

from .courses import C, F, O, T

UNITS = [
    # ---------------- A1 ----------------
    {
        "level": "A1", "title": "Ежедневие и места", "slug": "a1-daily-places", "icon": "fa-map-pin", "order": 3,
        "summary": "Какво правиш сега, какво има наоколо и къде е.",
        "lessons": [
            {
                "slug": "a1-present-continuous", "title": "Present Continuous: какво правиш сега",
                "title_en": "Present Continuous", "kind": "grammar", "minutes": 7, "xp": 15,
                "summary": "I am reading: действия, които стават в момента.",
                "theory": """
<p>Използваме Present Continuous за нещо, което се случва <strong>точно сега</strong> или около сегашния момент.</p>
<p><strong>am / is / are + глагол с -ing</strong></p>
<ul>
<li><span class="en">I am reading.</span> Чета (в момента).</li>
<li><span class="en">She is cooking dinner.</span> Тя готви вечеря.</li>
<li><span class="en">They are watching TV.</span> Те гледат телевизия.</li>
</ul>
<h3>Present Simple или Present Continuous?</h3>
<table>
<tr><th>Present Simple</th><th>Present Continuous</th></tr>
<tr><td>навик, винаги</td><td>сега, в момента</td></tr>
<tr><td class="en">I work in a bank.</td><td class="en">I'm working from home today.</td></tr>
</table>
<div class="tip">В българския и двете се казват „работя“. В английския трябва да избереш: навик или в момента. Думи като <span class="en">now, at the moment, look!</span> подсказват Continuous.</div>
<h3>Правопис</h3>
<p><span class="en">make, making</span> (без -e), <span class="en">sit, sitting</span> (удвояване), <span class="en">play, playing</span>.</p>
""",
                "exercises": [
                    C("Look! It ___ .", ["rains", "is raining", "rain"], 1, "Look! показва, че става сега."),
                    C("I usually ___ tea, but today I'm drinking coffee.", ["drink", "am drinking"], 0, "Usually е навик: Present Simple."),
                    F("They ___ (play) football at the moment.", "are playing|'re playing"),
                    F("She is ___ (write) an email.", "writing"),
                    C("___ you listening to me?", ["Do", "Are", "Is"], 1),
                    O("Какво правиш сега?", "What are you doing now"),
                    T("Чакам автобуса.", "I am waiting for the bus|I'm waiting for the bus"),
                ],
            },
            {
                "slug": "a1-there-is-are", "title": "There is и there are", "title_en": "There is / there are",
                "kind": "grammar", "minutes": 6, "xp": 15, "summary": "Как да кажеш, че нещо има или няма.",
                "theory": """
<p>„Има“ на английски не е <em>have</em>, когато говорим какво има някъде. Използваме <strong>there is / there are</strong>.</p>
<table>
<tr><th></th><th>Единствено число</th><th>Множествено число</th></tr>
<tr><td>Утвърдително</td><td class="en">There is a bank near here.</td><td class="en">There are two cafés.</td></tr>
<tr><td>Отрицание</td><td class="en">There isn't a lift.</td><td class="en">There aren't any shops.</td></tr>
<tr><td>Въпрос</td><td class="en">Is there a pharmacy?</td><td class="en">Are there any buses?</td></tr>
</table>
<div class="tip">Кратка форма: <span class="en">there's</span>. С множествено число във въпроси и отрицания често добавяме <span class="en">any</span>.</div>
""",
                "exercises": [
                    C("___ a supermarket near the hotel?", ["Is there", "Are there", "Has it"], 0),
                    C("There ___ three bedrooms in the flat.", ["is", "are"], 1),
                    C("There ___ any milk in the fridge.", ["isn't", "aren't"], 0, "Milk е неброимо, затова isn't."),
                    F("___ there any good restaurants here?", "Are"),
                    O("В стаята няма телевизор.", "There is no TV in the room|There isn't a TV in the room"),
                    T("Има ли аптека наблизо?", "Is there a pharmacy near here|Is there a pharmacy nearby|Is there a chemist near here"),
                ],
            },
            {
                "slug": "a1-prepositions-in-on-at", "title": "Предлози in, on, at", "title_en": "Prepositions: in, on, at",
                "kind": "grammar", "minutes": 7, "xp": 15, "summary": "За време и място: кога in, кога on, кога at.",
                "theory": """
<h3>Време</h3>
<table>
<tr><th>at</th><th>on</th><th>in</th></tr>
<tr><td>точен час: <span class="en">at 7 o'clock, at noon, at night</span></td><td>дни и дати: <span class="en">on Monday, on 5 May, on my birthday</span></td><td>месеци, години, сезони, части от деня: <span class="en">in June, in 2026, in summer, in the morning</span></td></tr>
</table>
<h3>Място</h3>
<table>
<tr><th>at</th><th>on</th><th>in</th></tr>
<tr><td>точка, адрес, събитие: <span class="en">at the bus stop, at home, at work</span></td><td>повърхност, етаж: <span class="en">on the table, on the wall, on the second floor</span></td><td>вътре, град, държава: <span class="en">in the box, in Sofia, in Bulgaria</span></td></tr>
</table>
<div class="tip">Българското „в“ понякога е <span class="en">in</span>, понякога <span class="en">on</span> или <span class="en">at</span>: „в понеделник“ е <span class="en">on Monday</span>, „в 5 часа“ е <span class="en">at 5</span>.</div>
""",
                "exercises": [
                    C("The meeting is ___ Monday.", ["in", "on", "at"], 1),
                    C("I was born ___ 1995.", ["in", "on", "at"], 0),
                    C("See you ___ 6 o'clock.", ["in", "on", "at"], 2),
                    C("My flat is ___ the third floor.", ["in", "on", "at"], 1),
                    F("She lives ___ Plovdiv.", "in"),
                    F("I'm ___ home tonight.", "at"),
                    O("Работя сутрин.", "I work in the morning"),
                ],
            },
            {
                "slug": "a1-possessives", "title": "Притежание: my, your и 's", "title_en": "Possessives: my, your, 's",
                "kind": "grammar", "minutes": 6, "xp": 15, "summary": "Моят, твоят, колата на Мария.",
                "theory": """
<h3>Притежателни думи</h3>
<table>
<tr><th>Лице</th><th>Притежателно</th><th>Пример</th></tr>
<tr><td class="en">I</td><td class="en">my</td><td class="en">my phone</td></tr>
<tr><td class="en">you</td><td class="en">your</td><td class="en">your bag</td></tr>
<tr><td class="en">he / she / it</td><td class="en">his / her / its</td><td class="en">his car, her name</td></tr>
<tr><td class="en">we / they</td><td class="en">our / their</td><td class="en">our house, their kids</td></tr>
</table>
<h3>'s за хора</h3>
<p>„Колата на Мария“ е <span class="en">Maria's car</span>. В множествено число на -s: <span class="en">my parents' house</span>.</p>
<div class="tip">В българския казваме „майка ми“, „колата ми“. В английския притежателната дума е <strong>пред</strong> съществителното: <span class="en">my mother, my car</span>.</div>
""",
                "exercises": [
                    C("This is Anna. ___ brother is a doctor.", ["His", "Her", "Their"], 1),
                    C("Колата на Петър:", ["Peter car", "Peter's car", "the car Peter"], 1),
                    F("We love ___ new flat.", "our"),
                    F("Is this ___ (you) coat?", "your"),
                    C("The children are in ___ room.", ["their", "there", "they're"], 0, "Their = техен. There = там. They're = they are."),
                    O("Брат ми живее в Лондон.", "My brother lives in London"),
                ],
            },
        ],
    },
    # ---------------- A2 ----------------
    {
        "level": "A2", "title": "Сравнения и количества", "slug": "a2-comparisons-quantities", "icon": "fa-scale-balanced",
        "order": 3, "summary": "По-голям, най-добър, колко много и какво правеше, когато...",
        "lessons": [
            {
                "slug": "a2-comparatives", "title": "Сравнения: bigger, the biggest", "title_en": "Comparatives and superlatives",
                "kind": "grammar", "minutes": 8, "xp": 20, "summary": "По-голям, най-голям, по-интересен.",
                "theory": """
<table>
<tr><th>Прилагателно</th><th>Сравнителна степен</th><th>Превъзходна степен</th></tr>
<tr><td>кратко: <span class="en">cheap</span></td><td class="en">cheaper (than)</td><td class="en">the cheapest</td></tr>
<tr><td>на -y: <span class="en">easy</span></td><td class="en">easier</td><td class="en">the easiest</td></tr>
<tr><td>дълго: <span class="en">expensive</span></td><td class="en">more expensive</td><td class="en">the most expensive</td></tr>
<tr><td>неправилни: <span class="en">good / bad</span></td><td class="en">better / worse</td><td class="en">the best / the worst</td></tr>
</table>
<p>„От“ при сравнение е <span class="en">than</span>: <span class="en">Sofia is bigger than Varna.</span></p>
<p>Еднакво: <span class="en">as ... as</span>: <span class="en">It's as cold as yesterday.</span></p>
<div class="tip">Не смесвай двете: <em>more bigger</em> е грешно. Или <span class="en">bigger</span>, или <span class="en">more</span> + дълга дума.</div>
""",
                "exercises": [
                    C("A bike is ___ than a car.", ["cheap", "cheaper", "more cheap"], 1),
                    C("This is ___ hotel in the city.", ["the most expensive", "the expensivest", "more expensive"], 0),
                    C("Today is ___ than yesterday.", ["more bad", "worse", "worst"], 1),
                    F("Maths is ___ (easy) than physics.", "easier"),
                    F("Sofia is bigger ___ Plovdiv.", "than"),
                    O("Това е най-добрият ресторант в града.", "This is the best restaurant in town"),
                ],
            },
            {
                "slug": "a2-countable-uncountable", "title": "Some, any, much, many", "title_en": "Countable and uncountable nouns",
                "kind": "grammar", "minutes": 8, "xp": 20, "summary": "Броими и неброими съществителни.",
                "theory": """
<p><strong>Броими</strong> са нещата, които можем да преброим: <span class="en">an apple, two apples</span>. <strong>Неброими</strong> нямат множествено число: <span class="en">water, money, bread, information, advice</span>.</p>
<table>
<tr><th></th><th>Броими (мн. ч.)</th><th>Неброими</th></tr>
<tr><td>Колко?</td><td class="en">How many eggs?</td><td class="en">How much milk?</td></tr>
<tr><td>Много (въпроси, отрицания)</td><td class="en">many</td><td class="en">much</td></tr>
<tr><td>Малко</td><td class="en">a few</td><td class="en">a little</td></tr>
<tr><td>Много (утвърдително)</td><td colspan="2" class="en">a lot of / lots of</td></tr>
</table>
<h3>Some и any</h3>
<p><span class="en">some</span> в утвърдителни изречения и в предложения: <span class="en">I need some help. Would you like some tea?</span><br>
<span class="en">any</span> във въпроси и отрицания: <span class="en">Have you got any questions? I don't have any money.</span></p>
""",
                "exercises": [
                    C("How ___ money do you have?", ["much", "many"], 0),
                    C("How ___ people came?", ["much", "many"], 1),
                    C("We don't have ___ bread.", ["some", "any"], 1),
                    C("Would you like ___ coffee?", ["some", "any"], 0, "В предложения използваме some."),
                    C("Can you give me some ___ ?", ["advices", "advice", "an advice"], 1, "Advice е неброимо."),
                    O("Имам няколко въпроса.", "I have a few questions"),
                ],
            },
            {
                "slug": "a2-past-continuous", "title": "Past Continuous: какво правеше", "title_en": "Past continuous and past simple",
                "kind": "grammar", "minutes": 8, "xp": 20, "summary": "I was cooking when the phone rang.",
                "theory": """
<p><strong>was / were + -ing</strong> описва действие, което <strong>е било в процес</strong> в даден момент в миналото.</p>
<p><span class="en">At 8 o'clock I was having dinner.</span> В 8 часа вечерях.</p>
<h3>С Past Simple</h3>
<p>Дългото действие е в Past Continuous, а краткото, което го прекъсва, в Past Simple:</p>
<p><span class="en">I was cooking when the phone rang.</span> Готвех, когато телефонът звънна.</p>
<p><span class="en">While we were walking, it started to rain.</span></p>
<div class="tip">Българското минало несвършено („готвех“) често съответства на Past Continuous, а минало свършено („звънна“) на Past Simple.</div>
""",
                "exercises": [
                    C("I ___ TV when you called.", ["watched", "was watching", "am watching"], 1),
                    C("While she was driving, her phone ___ .", ["rang", "was ringing"], 0),
                    F("They ___ (sleep) at midnight.", "were sleeping"),
                    F("What ___ you doing at 9 last night?", "were"),
                    C("When I arrived, they ___ dinner.", ["were having", "have", "are having"], 0),
                    O("Валеше, когато излязохме.", "It was raining when we left"),
                ],
            },
        ],
    },
    # ---------------- B1 ----------------
    {
        "level": "B1", "title": "Минало и описания", "slug": "b1-past-descriptions", "icon": "fa-book-bookmark",
        "order": 3, "summary": "Навици в миналото, по-ранно минало и подчинени изречения.",
        "lessons": [
            {
                "slug": "b1-used-to", "title": "Used to: навици в миналото", "title_en": "Past habits: used to",
                "kind": "grammar", "minutes": 8, "xp": 20, "summary": "I used to play the piano: вече не свиря.",
                "theory": """
<p><span class="en">used to + глагол</span> описва навик или състояние в миналото, което <strong>вече не е вярно</strong>.</p>
<ul>
<li><span class="en">I used to smoke.</span> Пушех (но вече не).</li>
<li><span class="en">We used to live in Burgas.</span> Живеехме в Бургас.</li>
</ul>
<p>Отрицание и въпрос: <span class="en">I didn't use to like coffee. Did you use to play sports?</span> (без -d след did)</p>
<h3>Не бъркай с be used to</h3>
<p><span class="en">I'm used to</span> + -ing = свикнал/а съм: <span class="en">I'm used to getting up early.</span></p>
""",
                "exercises": [
                    C("When I was a child, I ___ in the village every summer.", ["used to stay", "use to stay", "am used to stay"], 0),
                    C("Did you ___ have long hair?", ["used to", "use to"], 1, "След did: use to, без -d."),
                    F("She didn't ___ to like vegetables.", "use"),
                    C("I'm used to ___ in a big city now.", ["live", "living", "lived"], 1, "Be used to + -ing."),
                    O("Някога играех тенис.", "I used to play tennis"),
                    T("Тук имаше кино.", "There used to be a cinema here"),
                ],
            },
            {
                "slug": "b1-past-perfect", "title": "Past Perfect: по-ранно минало", "title_en": "Past perfect",
                "kind": "grammar", "minutes": 8, "xp": 20, "summary": "Когато пристигнахме, филмът вече беше започнал.",
                "theory": """
<p><strong>had + минало причастие</strong>. Показва, че нещо е станало <strong>преди</strong> друго минало събитие.</p>
<p><span class="en">When we arrived, the film had already started.</span> Когато пристигнахме, филмът вече беше започнал.</p>
<p><span class="en">She had never flown before her trip to London.</span></p>
<div class="tip">Ако редът е ясен от <span class="en">before</span> или <span class="en">after</span>, Past Simple също е наред: <span class="en">After I finished work, I went home.</span></div>
""",
                "exercises": [
                    C("When I got to the station, the train ___ .", ["left", "had left", "has left"], 1),
                    C("I ___ never seen snow before I moved to Canada.", ["have", "had", "was"], 1),
                    F("By the time she called, I had ___ (go) to bed.", "gone"),
                    C("They were tired because they ___ all day.", ["had worked", "have worked", "work"], 0),
                    O("Тя вече беше яла.", "She had already eaten"),
                ],
            },
            {
                "slug": "b1-relative-clauses", "title": "Подчинени изречения: who, which, that", "title_en": "Relative clauses",
                "kind": "grammar", "minutes": 9, "xp": 20, "summary": "Човекът, който..., книгата, която...",
                "theory": """
<table>
<tr><th>Дума</th><th>За какво</th><th>Пример</th></tr>
<tr><td class="en">who</td><td>хора</td><td class="en">The woman who lives next door is a nurse.</td></tr>
<tr><td class="en">which</td><td>неща, животни</td><td class="en">The car which I bought is red.</td></tr>
<tr><td class="en">that</td><td>хора и неща (неформално)</td><td class="en">The film that we saw was great.</td></tr>
<tr><td class="en">where</td><td>места</td><td class="en">This is the café where we met.</td></tr>
<tr><td class="en">whose</td><td>притежание</td><td class="en">The man whose wallet was stolen.</td></tr>
</table>
<h3>Допълнителна информация (със запетаи)</h3>
<p><span class="en">My sister, who lives in Paris, is a designer.</span> Тук не може <span class="en">that</span>.</p>
<div class="tip">Когато думата е допълнение, може да се изпусне: <span class="en">The book (that) I'm reading is long.</span></div>
""",
                "exercises": [
                    C("The man ___ called you is my boss.", ["who", "which", "where"], 0),
                    C("This is the hotel ___ we stayed.", ["which", "where", "who"], 1),
                    C("The phone ___ I bought is broken.", ["who", "which", "whose"], 1),
                    C("My brother, ___ is a doctor, lives in Varna.", ["that", "who"], 1, "При запетаи не използваме that."),
                    F("That's the girl ___ dog bit me.", "whose"),
                    O("Това е книгата, която ти препоръчах.", "This is the book that I recommended to you|This is the book which I recommended to you"),
                ],
            },
        ],
    },
    # ---------------- B2 ----------------
    {
        "level": "B2", "title": "Предположения и желания", "slug": "b2-guesses-wishes", "icon": "fa-wand-sparkles",
        "order": 2, "summary": "Must be, might have, I wish и have something done.",
        "lessons": [
            {
                "slug": "b2-modals-deduction", "title": "Must, might, can't: предположения", "title_en": "Modals of deduction",
                "kind": "grammar", "minutes": 9, "xp": 25, "summary": "Колко сигурен си: must be, might be, can't be.",
                "theory": """
<table>
<tr><th>Сигурност</th><th>За сега</th><th>За миналото</th></tr>
<tr><td>почти сигурно да</td><td class="en">She must be tired.</td><td class="en">She must have been tired.</td></tr>
<tr><td>възможно</td><td class="en">He might / may / could be at home.</td><td class="en">He might have missed the bus.</td></tr>
<tr><td>почти сигурно не</td><td class="en">It can't be true.</td><td class="en">They can't have finished already.</td></tr>
</table>
<div class="tip">Обратното на <span class="en">must be</span> като предположение е <span class="en">can't be</span>, а не <em>mustn't be</em>. <span class="en">Mustn't</span> е забрана.</div>
""",
                "exercises": [
                    C("She's been working for 12 hours. She ___ be exhausted.", ["must", "can't", "mustn't"], 0),
                    C("That ___ be Tom. He's in Spain this week.", ["must", "can't", "might"], 1),
                    C("I can't find my keys. I ___ have left them at work.", ["might", "can't", "mustn't"], 0),
                    F("The streets are wet. It must ___ rained.", "have"),
                    C("He didn't answer. He ___ been asleep.", ["must have", "must", "can't"], 0),
                    O("Сигурно се шегуваш.", "You must be joking"),
                ],
            },
            {
                "slug": "b2-wish", "title": "Wish и if only: съжаления", "title_en": "Wishes: wish and if only",
                "kind": "grammar", "minutes": 9, "xp": 25, "summary": "I wish I had more time.",
                "theory": """
<table>
<tr><th>Желание за</th><th>Форма</th><th>Пример</th></tr>
<tr><td>настоящето</td><td><span class="en">wish</span> + Past Simple</td><td class="en">I wish I lived by the sea.</td></tr>
<tr><td>миналото (съжаление)</td><td><span class="en">wish</span> + Past Perfect</td><td class="en">I wish I had studied harder.</td></tr>
<tr><td>промяна в поведение (дразни ни)</td><td><span class="en">wish</span> + would</td><td class="en">I wish you would stop talking.</td></tr>
</table>
<p><span class="en">If only</span> е по-силно: <span class="en">If only I had more time!</span></p>
<div class="tip">„Иска ми се да можех“ е <span class="en">I wish I could</span>, а не <em>I wish I can</em>.</div>
""",
                "exercises": [
                    C("I wish I ___ speak Japanese.", ["can", "could", "will"], 1),
                    C("I wish I ___ that. I'm sorry.", ["didn't say", "hadn't said", "don't say"], 1),
                    C("I wish it ___ so cold today.", ["isn't", "weren't", "won't be"], 1),
                    F("If only I ___ (know) the answer!", "knew"),
                    C("I wish my neighbours ___ the music down.", ["would turn", "turn", "turned down"], 0),
                    O("Иска ми се да имах повече свободно време.", "I wish I had more free time"),
                ],
            },
            {
                "slug": "b2-causative", "title": "Have something done", "title_en": "The causative: have something done",
                "kind": "grammar", "minutes": 8, "xp": 25, "summary": "Когато някой друг го прави вместо теб.",
                "theory": """
<p>Когато някой друг върши работата вместо нас (обикновено срещу заплащане): <strong>have + предмет + минало причастие</strong>.</p>
<ul>
<li><span class="en">I had my hair cut.</span> Подстригах се (при фризьор).</li>
<li><span class="en">We're having the kitchen painted.</span> Боядисват ни кухнята.</li>
<li><span class="en">She had her phone stolen.</span> Откраднаха ѝ телефона.</li>
</ul>
<p>В разговорен английски често се използва <span class="en">get</span>: <span class="en">I need to get my car repaired.</span></p>
<div class="tip"><span class="en">I cut my hair</span> значи, че сам/а си се подстригал/а. За фризьора: <span class="en">I had my hair cut.</span></div>
""",
                "exercises": [
                    C("I ___ my car repaired yesterday.", ["had", "did", "made"], 0),
                    C("We're having our windows ___ .", ["clean", "cleaned", "cleaning"], 1),
                    F("You should get your eyes ___ (test).", "tested"),
                    C("Фризьор ме подстрига:", ["I cut my hair.", "I had my hair cut.", "I had cut my hair."], 1),
                    O("Трябва да си поправя телефона.", "I need to get my phone repaired|I need to have my phone repaired"),
                ],
            },
        ],
    },
    # ---------------- C1 ----------------
    {
        "level": "C1", "title": "Стегнат и плавен текст", "slug": "c1-concise-text", "icon": "fa-align-left",
        "order": 2, "summary": "Причастни изречения и как да избягваш повторения.",
        "lessons": [
            {
                "slug": "c1-participle-clauses", "title": "Причастни изречения", "title_en": "Participle clauses",
                "kind": "grammar", "minutes": 10, "xp": 30, "summary": "Having finished the report, she went home.",
                "theory": """
<p>Причастните изречения правят текста по-кратък и по-официален. Те заменят изречение с <span class="en">when, because, after, who</span>.</p>
<table>
<tr><th>Форма</th><th>Значение</th><th>Пример</th></tr>
<tr><td>-ing</td><td>едновременно действие или причина</td><td class="en">Feeling tired, I went to bed early.</td></tr>
<tr><td>Having + причастие</td><td>завършено преди това</td><td class="en">Having finished the report, she left.</td></tr>
<tr><td>минало причастие</td><td>страдателно значение</td><td class="en">Built in 1890, the house needs repairs.</td></tr>
</table>
<div class="tip">Подлогът на двете части трябва да е <strong>един и същ</strong>. <em>Walking home, the rain started</em> звучи като че дъждът се е прибирал. Правилно: <span class="en">Walking home, I got caught in the rain.</span></div>
""",
                "exercises": [
                    C("___ the email, she closed her laptop.", ["Having sent", "Sent", "Having send"], 0),
                    C("___ in 1990, the company now employs 500 people.", ["Founding", "Founded", "Having founded"], 1),
                    C("___ no money, he couldn't buy the ticket.", ["Having", "Had", "Has"], 0),
                    C("Кое изречение е правилно?", ["Walking home, the rain started.", "Walking home, I got caught in the rain."], 1),
                    F("___ (not know) what to say, I stayed silent.", "Not knowing"),
                    O("След като прочете писмото, тя се усмихна.", "Having read the letter she smiled"),
                ],
            },
        ],
    },
]

MISTAKES = {
    "a1-present-continuous": [
        ("I am work now.", "I am working now.", "След am/is/are глаголът е с -ing."),
        ("Look! It rains.", "Look! It's raining.", "За нещо, което става в момента: Present Continuous."),
        ("I am knowing the answer.", "I know the answer.", "Know, like, want, need обикновено не се използват с -ing."),
    ],
    "a1-there-is-are": [
        ("It has a bank near here.", "There is a bank near here.", "„Има“ за наличие е there is, не it has."),
        ("There is two cafés.", "There are two cafés.", "С множествено число: there are."),
    ],
    "a1-prepositions-in-on-at": [
        ("in Monday", "on Monday", "С дни от седмицата: on."),
        ("at the morning", "in the morning", "Части от деня: in the morning, in the evening, но at night."),
        ("I am in home.", "I am at home.", "Устойчив израз: at home, at work, at school."),
    ],
    "a1-possessives": [
        ("brother my", "my brother", "Притежателната дума стои пред съществителното."),
        ("the car of Maria", "Maria's car", "За хора използваме 's."),
        ("Their going home.", "They're going home.", "They're = they are. Their = техен."),
    ],
    "a2-comparatives": [
        ("more bigger", "bigger", "Не съчетавай more и -er."),
        ("bigger from Varna", "bigger than Varna", "„От“ при сравнение е than."),
        ("the most good", "the best", "Good е неправилно: better, the best."),
    ],
    "a2-countable-uncountable": [
        ("How many money?", "How much money?", "Money е неброимо: much."),
        ("some informations", "some information", "Information, advice, furniture нямат множествено число."),
        ("I don't have some time.", "I don't have any time.", "В отрицания: any."),
    ],
    "a2-past-continuous": [
        ("When you called, I watched TV.", "When you called, I was watching TV.", "Действието в процес е в Past Continuous."),
        ("I was knowing him.", "I knew him.", "Know не се използва с -ing."),
    ],
    "b1-used-to": [
        ("I use to play football.", "I used to play football.", "В утвърдително изречение: used to."),
        ("Did you used to smoke?", "Did you use to smoke?", "След did: use to."),
        ("I'm used to get up early.", "I'm used to getting up early.", "Be used to + -ing."),
    ],
    "b1-past-perfect": [
        ("When I arrived, she left.", "When I arrived, she had left.", "Ако е тръгнала преди да пристигна: had left."),
    ],
    "b1-relative-clauses": [
        ("The man which called you", "The man who called you", "За хора: who (или that)."),
        ("My mother, that lives in Varna, ...", "My mother, who lives in Varna, ...", "При запетаи не използваме that."),
        ("This is the place which I was born.", "This is the place where I was born.", "За място: where (или which ... in)."),
    ],
    "b2-modals-deduction": [
        ("He mustn't be at home, the lights are off.", "He can't be at home, the lights are off.", "Отрицателното предположение е can't be."),
        ("She must went home.", "She must have gone home.", "За миналото: must have + причастие."),
    ],
    "b2-wish": [
        ("I wish I can come.", "I wish I could come.", "След wish: could, не can."),
        ("I wish I didn't say that yesterday.", "I wish I hadn't said that yesterday.", "Съжаление за миналото: Past Perfect."),
    ],
    "b2-causative": [
        ("I cut my hair at the hairdresser's.", "I had my hair cut at the hairdresser's.", "Когато друг го прави: have + предмет + причастие."),
        ("I had repaired my car.", "I had my car repaired.", "Редът е have + предмет + причастие."),
    ],
    "c1-participle-clauses": [
        ("Walking home, the rain started.", "Walking home, I got caught in the rain.", "Подлогът на двете части трябва да е един и същ."),
        ("Having finish the work, ...", "Having finished the work, ...", "Having + минало причастие."),
    ],
}
