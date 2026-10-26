"""Third batch of grammar lessons: remaining core topics from the British Council level lists."""

from .courses import C, F, O, T

UNITS = [
    # ---------------- A1 ----------------
    {
        "level": "A1", "title": "Въпроси и умения", "slug": "a1-questions-skills", "icon": "fa-circle-question", "order": 5,
        "summary": "Въпросителни думи, can и have got.",
        "lessons": [
            {
                "slug": "a1-question-words", "title": "Въпросителни думи", "title_en": "Question words",
                "kind": "grammar", "minutes": 7, "xp": 15, "summary": "Who, what, where, when, why, how.",
                "theory": """
<table>
<tr><th>Дума</th><th>Значение</th><th>Пример</th></tr>
<tr><td class="en">What</td><td>какво</td><td class="en">What's your name?</td></tr>
<tr><td class="en">Who</td><td>кой</td><td class="en">Who is that man?</td></tr>
<tr><td class="en">Where</td><td>къде</td><td class="en">Where do you live?</td></tr>
<tr><td class="en">When</td><td>кога</td><td class="en">When does the train leave?</td></tr>
<tr><td class="en">Why</td><td>защо</td><td class="en">Why are you late?</td></tr>
<tr><td class="en">How</td><td>как</td><td class="en">How do you spell that?</td></tr>
<tr><td class="en">How much / How many</td><td>колко</td><td class="en">How much is it? How many kids do you have?</td></tr>
<tr><td class="en">Which</td><td>кой (от няколко)</td><td class="en">Which bus goes to the centre?</td></tr>
</table>
<h3>Ред на думите</h3>
<p><strong>Въпросителна дума + спомагателен глагол + подлог + глагол</strong></p>
<p><span class="en">Where do you work?</span> <span class="en">What does she want?</span> <span class="en">Why are they here?</span></p>
<div class="tip">В българския казваме „Къде работиш?“. В английския е нужно <span class="en">do</span>: <span class="en">Where do you work?</span>, не <em>Where you work?</em></div>
""",
                "exercises": [
                    C("___ do you live? In Burgas.", ["What", "Where", "When"], 1),
                    C("___ is your birthday? In May.", ["When", "Who", "Why"], 0),
                    C("___ apples do you want? Three, please.", ["How much", "How many"], 1),
                    C("Кой въпрос е правилен?", ["Where you work?", "Where do you work?", "Where work you?"], 1),
                    F("___ are you sad? Because I lost my keys.", "Why"),
                    O("Какво правиш през уикенда?", "What do you do at the weekend"),
                ],
            },
            {
                "slug": "a1-can", "title": "Can и can't: умения и молби", "title_en": "Can and can't",
                "kind": "grammar", "minutes": 6, "xp": 15, "summary": "Мога, не мога, може ли.",
                "theory": """
<p><span class="en">can</span> е еднакво за всички лица и след него глаголът е в основна форма, без <span class="en">to</span>.</p>
<ul>
<li><span class="en">I can swim. She can drive.</span> Умения.</li>
<li><span class="en">I can't (cannot) cook.</span> Отрицание.</li>
<li><span class="en">Can you help me?</span> Молба.</li>
<li><span class="en">Can I sit here?</span> Разрешение.</li>
</ul>
<div class="tip">С he/she/it няма -s: <span class="en">He can play</span>, не <em>He cans play</em> или <em>He can plays</em>.</div>
<p>Произношение: <span class="en">can</span> в изречение е кратко „кън“, а <span class="en">can't</span> е дълго и ясно „кант“.</p>
""",
                "exercises": [
                    C("She ___ speak three languages.", ["can", "cans", "can to"], 0),
                    C("He can ___ the guitar.", ["play", "plays", "to play"], 0),
                    C("___ I use your phone?", ["Can", "Do", "Am"], 0),
                    F("I'm sorry, I ___ come tonight. (не мога)", "can't|cannot"),
                    O("Можеш ли да ми помогнеш?", "Can you help me"),
                    T("Тя не може да плува.", "She can't swim|She cannot swim"),
                ],
            },
            {
                "slug": "a1-have-got", "title": "Have got: имам", "title_en": "Have got",
                "kind": "grammar", "minutes": 6, "xp": 15, "summary": "I've got a sister: британският начин да кажеш „имам“.",
                "theory": """
<p>В британския английски често се казва <span class="en">have got</span> вместо <span class="en">have</span> за притежание, роднини и болести.</p>
<table>
<tr><th></th><th>I, you, we, they</th><th>he, she, it</th></tr>
<tr><td>Утвърдително</td><td class="en">I've got a car.</td><td class="en">She's got two brothers.</td></tr>
<tr><td>Отрицание</td><td class="en">We haven't got time.</td><td class="en">He hasn't got a phone.</td></tr>
<tr><td>Въпрос</td><td class="en">Have you got a pen?</td><td class="en">Has she got a dog?</td></tr>
</table>
<div class="tip">С <span class="en">have got</span> въпросът е без <span class="en">do</span>: <span class="en">Have you got...?</span> Но с обикновеното <span class="en">have</span>: <span class="en">Do you have...?</span> И двете са правилни.</div>
""",
                "exercises": [
                    C("She ___ got blue eyes.", ["have", "has", "is"], 1),
                    C("___ you got any brothers?", ["Do", "Have", "Are"], 1),
                    C("He ___ got a car.", ["hasn't", "haven't", "doesn't"], 0),
                    F("I've ___ a headache.", "got"),
                    O("Имаш ли химикалка?", "Have you got a pen"),
                    T("Нямаме време.", "We haven't got time|We don't have time|We have no time"),
                ],
            },
        ],
    },
    # ---------------- A2 ----------------
    {
        "level": "A2", "title": "Как правим нещата", "slug": "a2-how-we-do", "icon": "fa-person-running", "order": 5,
        "summary": "Прилагателни на -ed и -ing, глагол + -ing или to, цел и наречия.",
        "lessons": [
            {
                "slug": "a2-ed-ing-adjectives", "title": "Bored или boring?", "title_en": "Adjectives ending in -ed and -ing",
                "kind": "grammar", "minutes": 6, "xp": 20, "summary": "Как се чувстваш и какво го причинява.",
                "theory": """
<table>
<tr><th>-ed: как се чувства човек</th><th>-ing: какво причинява чувството</th></tr>
<tr><td class="en">I'm bored. (отегчен/а съм)</td><td class="en">The film is boring. (скучен)</td></tr>
<tr><td class="en">She's interested in art.</td><td class="en">Art is interesting.</td></tr>
<tr><td class="en">We were tired.</td><td class="en">The trip was tiring.</td></tr>
<tr><td class="en">He's confused.</td><td class="en">The instructions are confusing.</td></tr>
</table>
<div class="tip"><span class="en">I'm boring</span> означава „аз съм скучен човек“, а не „скучно ми е“. Внимавай!</div>
""",
                "exercises": [
                    C("The lesson was really ___ .", ["bored", "boring"], 1),
                    C("I'm ___ in history.", ["interested", "interesting"], 0),
                    C("Скучно ми е:", ["I'm boring.", "I'm bored."], 1),
                    F("The news was very surpris___ .", "ing"),
                    C("After the long walk we were ___ .", ["tired", "tiring"], 0),
                    O("Филмът беше много интересен.", "The film was very interesting"),
                ],
            },
            {
                "slug": "a2-verb-ing-to", "title": "Глагол + -ing или to", "title_en": "Verbs followed by -ing or to",
                "kind": "grammar", "minutes": 8, "xp": 20, "summary": "I enjoy swimming, I want to swim.",
                "theory": """
<table>
<tr><th>+ -ing</th><th>+ to + глагол</th></tr>
<tr><td class="en">enjoy, like, love, hate, finish, mind, stop, avoid</td><td class="en">want, need, decide, hope, plan, would like, learn, forget</td></tr>
<tr><td class="en">I enjoy cooking.</td><td class="en">I want to cook.</td></tr>
<tr><td class="en">Do you mind waiting?</td><td class="en">We decided to stay.</td></tr>
</table>
<p>След предлог винаги е <strong>-ing</strong>: <span class="en">I'm good at drawing. Thanks for helping.</span></p>
<div class="tip"><span class="en">Would like</span> е с <span class="en">to</span> (<span class="en">I'd like to go</span>), а <span class="en">like</span> обикновено с -ing (<span class="en">I like going</span>).</div>
""",
                "exercises": [
                    C("I enjoy ___ in the mountains.", ["walking", "to walk"], 0),
                    C("We decided ___ a taxi.", ["taking", "to take"], 1),
                    C("Would you like ___ something?", ["drinking", "to drink"], 1),
                    C("She's good at ___ .", ["singing", "to sing"], 0, "След предлог: -ing."),
                    F("Have you finished ___ (read) the book?", "reading"),
                    O("Надявам се да те видя скоро.", "I hope to see you soon"),
                ],
            },
            {
                "slug": "a2-purpose", "title": "За да: to + глагол", "title_en": "Infinitive of purpose",
                "kind": "grammar", "minutes": 5, "xp": 20, "summary": "I went to the shop to buy bread.",
                "theory": """
<p>За да кажем <strong>защо</strong> правим нещо, използваме <span class="en">to</span> + глагол.</p>
<ul>
<li><span class="en">I went to the shop to buy bread.</span> Отидох до магазина, за да купя хляб.</li>
<li><span class="en">She's learning English to get a better job.</span></li>
</ul>
<p>За отрицателна цел: <span class="en">so as not to / in order not to</span>: <span class="en">I left early so as not to miss the bus.</span></p>
<div class="tip">„За да“ не е <em>for to</em> и не е <em>for + глагол</em>: <span class="en">I came to see you</span>, не <em>I came for see you</em>.</div>
""",
                "exercises": [
                    C("I'm saving money ___ a car.", ["to buy", "for buy", "for to buy"], 0),
                    C("He went to Spain ___ Spanish.", ["for learning", "to learn", "learn"], 1),
                    F("She called ___ say sorry.", "to"),
                    C("I set an alarm so as ___ oversleep.", ["not to", "to not", "don't"], 0),
                    O("Отидох до аптеката, за да купя лекарство.", "I went to the pharmacy to buy medicine"),
                ],
            },
            {
                "slug": "a2-adverbs", "title": "Наречия: quickly, well", "title_en": "Adverbs of manner",
                "kind": "grammar", "minutes": 6, "xp": 20, "summary": "Как правиш нещо: бързо, добре, внимателно.",
                "theory": """
<p>Прилагателното описва съществително, наречието описва глагол: <span class="en">a careful driver</span>, но <span class="en">She drives carefully.</span></p>
<table>
<tr><th>Прилагателно</th><th>Наречие</th></tr>
<tr><td class="en">quick</td><td class="en">quickly</td></tr>
<tr><td class="en">careful</td><td class="en">carefully</td></tr>
<tr><td class="en">easy</td><td class="en">easily</td></tr>
<tr><td class="en">good</td><td class="en">well (неправилно)</td></tr>
<tr><td class="en">fast / hard / late</td><td class="en">fast / hard / late (без промяна)</td></tr>
</table>
<div class="tip"><span class="en">Hardly</span> не е „усилено“, а „почти не“: <span class="en">I hardly slept.</span> Почти не спах.</div>
""",
                "exercises": [
                    C("She speaks English very ___ .", ["good", "well"], 1),
                    C("Please drive ___ .", ["careful", "carefully"], 1),
                    C("He works very ___ .", ["hard", "hardly"], 0),
                    F("He ran ___ (quick) to the bus stop.", "quickly"),
                    C("I hardly know her. означава:", ["Почти не я познавам.", "Познавам я много добре."], 0),
                    O("Тя пее много добре.", "She sings very well"),
                ],
            },
        ],
    },
    # ---------------- B1 ----------------
    {
        "level": "B1", "title": "Времена в детайли", "slug": "b1-tenses-detail", "icon": "fa-hourglass-half", "order": 5,
        "summary": "Just, yet, already, Present Perfect Continuous, въпроси-опашки и too/enough.",
        "lessons": [
            {
                "slug": "b1-just-yet-already", "title": "Just, yet, already, still", "title_en": "Present perfect: just, yet, already, still",
                "kind": "grammar", "minutes": 7, "xp": 20, "summary": "Току-що, вече, още не.",
                "theory": """
<table>
<tr><th>Дума</th><th>Значение</th><th>Място</th><th>Пример</th></tr>
<tr><td class="en">just</td><td>току-що</td><td>между have и глагола</td><td class="en">I've just eaten.</td></tr>
<tr><td class="en">already</td><td>вече (по-рано от очакваното)</td><td>между have и глагола</td><td class="en">She's already left.</td></tr>
<tr><td class="en">yet</td><td>още (не), вече (във въпрос)</td><td>в края, във въпроси и отрицания</td><td class="en">Have you finished yet? I haven't finished yet.</td></tr>
<tr><td class="en">still</td><td>все още (не)</td><td>пред haven't</td><td class="en">I still haven't called him.</td></tr>
</table>
""",
                "exercises": [
                    C("Have you done your homework ___ ?", ["already", "yet", "just"], 1),
                    C("Don't worry, I've ___ paid.", ["already", "yet", "still"], 0),
                    C("I've ___ arrived. I'm still at the door.", ["just", "yet", "still"], 0),
                    C("She ___ hasn't answered my email.", ["yet", "still", "already"], 1),
                    F("The film hasn't started ___ .", "yet"),
                    O("Току-що видях Мария.", "I have just seen Maria|I've just seen Maria"),
                ],
            },
            {
                "slug": "b1-present-perfect-continuous", "title": "Present Perfect Continuous", "title_en": "Present perfect continuous",
                "kind": "grammar", "minutes": 8, "xp": 20, "summary": "I've been waiting for an hour!",
                "theory": """
<p><strong>have/has been + -ing</strong>. Подчертава <strong>продължителността</strong> на действие, което е започнало в миналото и продължава (или току-що е спряло).</p>
<ul>
<li><span class="en">I've been waiting for an hour!</span> Чакам от час!</li>
<li><span class="en">She's been learning English since January.</span></li>
<li><span class="en">You look tired. Have you been running?</span> (видим резултат)</li>
</ul>
<h3>Simple или Continuous?</h3>
<table>
<tr><th>Present Perfect Simple</th><th>Present Perfect Continuous</th></tr>
<tr><td>резултат, колко: <span class="en">I've written three emails.</span></td><td>процес, колко време: <span class="en">I've been writing emails all morning.</span></td></tr>
</table>
<div class="tip">„Чакам от един час“ на английски не е <em>I wait</em> или <em>I am waiting for an hour</em>, а <span class="en">I've been waiting for an hour.</span></div>
""",
                "exercises": [
                    C("I ___ here since 2019.", ["work", "am working", "have been working"], 2),
                    C("Your eyes are red. ___ you been crying?", ["Have", "Did", "Are"], 0),
                    C("She's written / She's been writing: кое е за резултат?", ["She has written two books.", "She has been writing all day."], 0),
                    F("How long have you been ___ (learn) English?", "learning"),
                    O("Чакаме автобуса от двайсет минути.", "We have been waiting for the bus for twenty minutes|We've been waiting for the bus for twenty minutes"),
                ],
            },
            {
                "slug": "b1-question-tags", "title": "Въпроси-опашки: isn't it?", "title_en": "Question tags",
                "kind": "grammar", "minutes": 7, "xp": 20, "summary": "Нали?, по английски.",
                "theory": """
<p>Английското „нали?“ се образува от <strong>спомагателния глагол</strong> на изречението, с обратен знак.</p>
<table>
<tr><th>Изречение</th><th>Опашка</th></tr>
<tr><td class="en">It's cold,</td><td class="en">isn't it?</td></tr>
<tr><td class="en">You aren't busy,</td><td class="en">are you?</td></tr>
<tr><td class="en">She lives here,</td><td class="en">doesn't she?</td></tr>
<tr><td class="en">They went home,</td><td class="en">didn't they?</td></tr>
<tr><td class="en">You can swim,</td><td class="en">can't you?</td></tr>
<tr><td class="en">I'm late,</td><td class="en">aren't I? (изключение)</td></tr>
</table>
<div class="tip">Не превеждай „нали“ с <em>isn't it</em> навсякъде. Опашката зависи от глагола: <span class="en">You like coffee, don't you?</span></div>
""",
                "exercises": [
                    C("You're from Varna, ___ ?", ["aren't you", "isn't it", "don't you"], 0),
                    C("She speaks French, ___ ?", ["isn't she", "doesn't she", "don't she"], 1),
                    C("They didn't call, ___ ?", ["did they", "didn't they", "do they"], 0),
                    C("I'm right, ___ ?", ["amn't I", "aren't I", "isn't I"], 1),
                    F("You can drive, ___ you?", "can't"),
                    O("Хубав ден е, нали?", "It is a nice day isn't it|It's a nice day isn't it"),
                ],
            },
            {
                "slug": "b1-too-enough", "title": "Too, enough, so и such", "title_en": "Too, enough, so, such",
                "kind": "grammar", "minutes": 7, "xp": 20, "summary": "Твърде скъпо, достатъчно голямо, толкова хубаво.",
                "theory": """
<table>
<tr><th>Дума</th><th>Значение</th><th>Ред</th><th>Пример</th></tr>
<tr><td class="en">too</td><td>твърде (проблем)</td><td>пред прилагателното</td><td class="en">It's too expensive.</td></tr>
<tr><td class="en">enough</td><td>достатъчно</td><td>след прилагателното, пред съществителното</td><td class="en">It's big enough. We have enough time.</td></tr>
<tr><td class="en">so</td><td>толкова</td><td>+ прилагателно</td><td class="en">It's so beautiful!</td></tr>
<tr><td class="en">such</td><td>толкова (+ съществително)</td><td>such (a) + прилагателно + съществително</td><td class="en">It's such a beautiful day!</td></tr>
</table>
<div class="tip"><span class="en">Too</span> винаги значи проблем. „Много хубаво“ е <span class="en">very nice</span>, не <em>too nice</em>.</div>
""",
                "exercises": [
                    C("I can't buy it. It's ___ expensive.", ["too", "enough", "such"], 0),
                    C("Is the room ___ ?", ["enough big", "big enough"], 1),
                    C("It was ___ a good film!", ["so", "such"], 1),
                    C("The weather is ___ nice today!", ["so", "such", "too"], 0),
                    F("We don't have ___ money for a holiday.", "enough"),
                    O("Той е твърде млад, за да шофира.", "He is too young to drive|He's too young to drive"),
                ],
            },
        ],
    },
    # ---------------- B2 ----------------
    {
        "level": "B2", "title": "Свързване и бъдеще", "slug": "b2-linking-future", "icon": "fa-link", "order": 4,
        "summary": "Although и despite, Future Continuous и Perfect, глаголи за състояние.",
        "lessons": [
            {
                "slug": "b2-contrast", "title": "Although, despite, however", "title_en": "Contrasting ideas",
                "kind": "grammar", "minutes": 8, "xp": 25, "summary": "Въпреки че, въпреки, обаче.",
                "theory": """
<table>
<tr><th>Връзка</th><th>След нея следва</th><th>Пример</th></tr>
<tr><td class="en">although / even though</td><td>изречение</td><td class="en">Although it was raining, we went out.</td></tr>
<tr><td class="en">despite / in spite of</td><td>съществително или -ing</td><td class="en">Despite the rain, we went out. Despite being tired, she kept working.</td></tr>
<tr><td class="en">however</td><td>ново изречение (със запетая)</td><td class="en">It was raining. However, we went out.</td></tr>
<tr><td class="en">while / whereas</td><td>контраст между две неща</td><td class="en">I love tea, whereas my wife prefers coffee.</td></tr>
</table>
<div class="tip"><em>Despite of</em> е грешно. Или <span class="en">despite</span>, или <span class="en">in spite of</span>.</div>
""",
                "exercises": [
                    C("___ the traffic, we arrived on time.", ["Although", "Despite", "However"], 1),
                    C("___ he studied hard, he failed.", ["Although", "Despite", "In spite of"], 0),
                    C("Кое е правилно?", ["Despite of the cold...", "Despite the cold...", "Despite that it was cold..."], 1),
                    F("In spite ___ being ill, she came to work.", "of"),
                    C("The hotel was cheap. ___, it was very clean.", ["However", "Although", "Despite"], 0),
                    O("Въпреки дъжда отидохме на плаж.", "Despite the rain we went to the beach|In spite of the rain we went to the beach"),
                ],
            },
            {
                "slug": "b2-future-continuous-perfect", "title": "Future Continuous и Future Perfect", "title_en": "Future continuous and future perfect",
                "kind": "grammar", "minutes": 8, "xp": 25, "summary": "По това време утре ще летя. До петък ще съм свършил/а.",
                "theory": """
<table>
<tr><th>Време</th><th>Форма</th><th>Употреба</th><th>Пример</th></tr>
<tr><td>Future Continuous</td><td class="en">will be + -ing</td><td>действие в процес в даден момент в бъдещето</td><td class="en">This time tomorrow I'll be flying to Rome.</td></tr>
<tr><td>Future Perfect</td><td class="en">will have + причастие</td><td>завършено преди даден момент в бъдещето</td><td class="en">By Friday I'll have finished the report.</td></tr>
</table>
<p>Future Continuous се използва и за учтиви въпроси за планове: <span class="en">Will you be using the car tonight?</span></p>
<div class="tip"><span class="en">By</span> + време („до“) е типичен сигнал за Future Perfect.</div>
""",
                "exercises": [
                    C("At 9 tomorrow I ___ an exam.", ["will be taking", "will have taken", "take"], 0),
                    C("By 2030 they ___ the new airport.", ["will be building", "will have built", "build"], 1),
                    C("Don't call at 8. We ___ dinner.", ["will be having", "will have had"], 0),
                    F("By the time you arrive, I will ___ cooked dinner.", "have"),
                    O("До понеделник ще съм прочел/а книгата.", "By Monday I will have read the book|By Monday I'll have read the book"),
                ],
            },
            {
                "slug": "b2-stative-verbs", "title": "Глаголи за състояние", "title_en": "Stative verbs",
                "kind": "grammar", "minutes": 7, "xp": 25, "summary": "Защо не казваме I'm knowing.",
                "theory": """
<p>Някои глаголи описват <strong>състояние</strong>, а не действие, и обикновено не се използват с -ing.</p>
<table>
<tr><th>Група</th><th>Глаголи</th></tr>
<tr><td>мисли и знание</td><td class="en">know, believe, understand, remember, mean</td></tr>
<tr><td>чувства</td><td class="en">like, love, hate, want, prefer, need</td></tr>
<tr><td>притежание</td><td class="en">have (притежавам), own, belong</td></tr>
<tr><td>сетива</td><td class="en">seem, look like, sound, taste, smell</td></tr>
</table>
<h3>С различно значение</h3>
<ul>
<li><span class="en">I think it's a good idea.</span> (мнение) / <span class="en">I'm thinking about moving.</span> (обмислям)</li>
<li><span class="en">She has a car.</span> (притежава) / <span class="en">She's having lunch.</span> (действие)</li>
</ul>
""",
                "exercises": [
                    C("I ___ what you mean.", ["understand", "am understanding"], 0),
                    C("This soup ___ delicious.", ["tastes", "is tasting"], 0),
                    C("We ___ dinner right now.", ["have", "are having"], 1, "Have dinner е действие, затова -ing е възможно."),
                    C("I ___ about changing my job.", ["think", "am thinking"], 1, "Тук think значи обмислям."),
                    F("This bag ___ (belong) to my sister.", "belongs"),
                    O("Не те разбирам.", "I don't understand you|I do not understand you"),
                ],
            },
        ],
    },
    # ---------------- C1 ----------------
    {
        "level": "C1", "title": "Сложни конструкции", "slug": "c1-complex", "icon": "fa-layer-group", "order": 4,
        "summary": "Безличен страдателен залог, нереално време и инверсия в условни изречения.",
        "lessons": [
            {
                "slug": "c1-advanced-passive", "title": "It is said that...", "title_en": "Advanced passives",
                "kind": "grammar", "minutes": 9, "xp": 30, "summary": "Безлични конструкции в медиите и официалния език.",
                "theory": """
<p>В новини и официални текстове мнението често се представя безлично.</p>
<table>
<tr><th>Конструкция</th><th>Пример</th></tr>
<tr><td class="en">It is said / believed / reported that...</td><td class="en">It is believed that the painting is a fake.</td></tr>
<tr><td class="en">Subject + is said to + глагол</td><td class="en">The painting is believed to be a fake.</td></tr>
<tr><td>за минало: <span class="en">to have + причастие</span></td><td class="en">He is reported to have left the country.</td></tr>
<tr><td>за процес: <span class="en">to be + -ing</span></td><td class="en">The company is said to be planning cuts.</td></tr>
</table>
<div class="tip">Българското „Твърди се, че...“ е <span class="en">It is claimed that...</span> или <span class="en">X is claimed to...</span>.</div>
""",
                "exercises": [
                    C("The minister is reported ___ the meeting.", ["to leave", "to have left", "leaving"], 1, "Събитието е в миналото."),
                    C("It ___ that the castle is haunted.", ["says", "is said", "is saying"], 1),
                    C("The suspect is believed ___ in Spain now.", ["to be hiding", "to hide", "hiding"], 0),
                    F("He is thought ___ have stolen the money.", "to"),
                    O("Смята се, че цените ще растат.", "It is thought that prices will rise|It is believed that prices will rise"),
                ],
            },
            {
                "slug": "c1-unreal-past", "title": "It's time, would rather", "title_en": "Unreal past",
                "kind": "grammar", "minutes": 8, "xp": 30, "summary": "Минало време, което говори за сегашното.",
                "theory": """
<p>След някои изрази минало време не значи минало, а <strong>нереалност</strong> или желание.</p>
<table>
<tr><th>Израз</th><th>Пример</th><th>Смисъл</th></tr>
<tr><td class="en">It's (high) time + Past Simple</td><td class="en">It's time we left.</td><td>Време е да тръгваме.</td></tr>
<tr><td class="en">would rather + someone + Past Simple</td><td class="en">I'd rather you didn't smoke here.</td><td>Предпочитам да не пушиш тук.</td></tr>
<tr><td class="en">as if / as though</td><td class="en">He talks as if he knew everything.</td><td>Говори, сякаш знае всичко.</td></tr>
<tr><td class="en">suppose / imagine</td><td class="en">Suppose you lost your job...</td><td>Да предположим, че...</td></tr>
</table>
<div class="tip">За себе си: <span class="en">I'd rather go</span> (без to). За друг човек: <span class="en">I'd rather you went</span> (минало време).</div>
""",
                "exercises": [
                    C("It's high time you ___ a job.", ["find", "found", "will find"], 1),
                    C("I'd rather you ___ tell anyone.", ["don't", "didn't", "won't"], 1),
                    C("I'd rather ___ at home tonight.", ["stay", "stayed", "to stay"], 0),
                    C("She acts as if she ___ the boss.", ["is", "were", "be"], 1),
                    O("Време е да си ходим.", "It is time we went home|It's time we went home|It is time we left|It's time we left"),
                ],
            },
            {
                "slug": "c1-conditional-inversion", "title": "Had I known...: условни без if", "title_en": "Inversion in conditionals",
                "kind": "grammar", "minutes": 8, "xp": 30, "summary": "Официален вариант на условните изречения.",
                "theory": """
<p>В официален стил <span class="en">if</span> може да отпадне, а спомагателният глагол отива в началото.</p>
<table>
<tr><th>С if</th><th>С инверсия</th></tr>
<tr><td class="en">If I had known, I would have helped.</td><td class="en">Had I known, I would have helped.</td></tr>
<tr><td class="en">If you should need help, call me.</td><td class="en">Should you need help, call me.</td></tr>
<tr><td class="en">If I were in your position, ...</td><td class="en">Were I in your position, ...</td></tr>
</table>
<div class="tip">Отрицание: <span class="en">Had I not seen it...</span>, не <em>Hadn't I seen it...</em></div>
""",
                "exercises": [
                    C("___ you have any questions, please contact us.", ["Should", "Would", "Had"], 0),
                    C("___ I known about the problem, I would have called.", ["Had", "Have", "If had"], 0),
                    C("___ he rich, he would travel the world.", ["Was", "Were", "Is"], 1),
                    C("Кое е правилно?", ["Hadn't she missed the bus, ...", "Had she not missed the bus, ..."], 1),
                    O("Ако имате нужда от помощ, обадете ни се.", "Should you need help call us"),
                ],
            },
        ],
    },
    # ---------------- C2 ----------------
    {
        "level": "C2", "title": "Академичен стил", "slug": "c2-academic", "icon": "fa-scroll", "order": 3,
        "summary": "Подчинително наклонение и номинализация.",
        "lessons": [
            {
                "slug": "c2-subjunctive", "title": "I insist that he be...", "title_en": "The subjunctive",
                "kind": "grammar", "minutes": 8, "xp": 35, "summary": "Официални изисквания и препоръки.",
                "theory": """
<p>След глаголи и изрази за изискване, препоръка и важност английският използва <strong>основната форма</strong> на глагола за всички лица.</p>
<table>
<tr><th>Глаголи и изрази</th><th>Пример</th></tr>
<tr><td class="en">insist, demand, recommend, suggest, request</td><td class="en">The doctor recommended that he rest for a week.</td></tr>
<tr><td class="en">It is essential / vital / important that</td><td class="en">It is essential that every student be present.</td></tr>
</table>
<p>Отрицание: <span class="en">not</span> + основна форма: <span class="en">We request that guests not smoke in the rooms.</span></p>
<div class="tip">В британския английски често се използва <span class="en">should</span>: <span class="en">I suggest that he should apply.</span> И двете са правилни.</div>
""",
                "exercises": [
                    C("The manager insisted that she ___ the report today.", ["finishes", "finish", "finished"], 1),
                    C("It is vital that he ___ informed.", ["is", "be", "was"], 1),
                    C("We recommend that guests ___ their valuables in the safe.", ["leave", "leaves", "left"], 0),
                    C("They asked that we ___ late.", ["not be", "don't be", "aren't"], 0),
                    O("Предлагам той да подаде документи.", "I suggest that he apply|I suggest that he should apply"),
                ],
            },
            {
                "slug": "c2-nominalisation", "title": "Номинализация", "title_en": "Nominalisation in formal writing",
                "kind": "grammar", "minutes": 9, "xp": 35, "summary": "Как глаголите стават съществителни в академичния текст.",
                "theory": """
<p>Академичният и официалният английски предпочита <strong>съществителни</strong> пред глаголи. Така текстът е по-стегнат и безличен.</p>
<table>
<tr><th>Разговорно</th><th>Номинализирано</th></tr>
<tr><td class="en">Prices rose quickly, so people protested.</td><td class="en">The rapid rise in prices led to protests.</td></tr>
<tr><td class="en">We analysed the data and found that...</td><td class="en">Analysis of the data revealed that...</td></tr>
<tr><td class="en">Because the company failed to act...</td><td class="en">The company's failure to act...</td></tr>
</table>
<h3>Чести двойки</h3>
<p><span class="en">decide, decision; fail, failure; increase, an increase; develop, development; reduce, reduction; arrive, arrival</span></p>
<div class="tip">Не прекалявай: прекалено много съществителни правят текста тежък. Целта е яснота, не сложност.</div>
""",
                "exercises": [
                    C("Номинализирай: The government decided to... :", ["The government's decision to...", "The government deciding to...", "The government decides to..."], 0),
                    C("Съществително от reduce:", ["reducement", "reduction", "reducing"], 1),
                    C("Кое звучи най-академично?", ["Costs went up a lot.", "There was a significant increase in costs.", "Costs got really high."], 1),
                    F("The ___ (arrive) of the new manager changed everything.", "arrival"),
                    O("Анализът на данните показа ясна тенденция.", "Analysis of the data revealed a clear trend|The analysis of the data revealed a clear trend"),
                ],
            },
        ],
    },
]

MISTAKES = {
    "a1-question-words": [
        ("Where you live?", "Where do you live?", "Въпросът изисква do/does."),
        ("How many money?", "How much money?", "Money е неброимо: how much."),
    ],
    "a1-can": [
        ("She cans swim.", "She can swim.", "Can няма -s."),
        ("I can to drive.", "I can drive.", "След can няма to."),
    ],
    "a1-have-got": [
        ("Do you have got a car?", "Have you got a car?", "С have got въпросът е без do."),
        ("She have got a dog.", "She has got a dog.", "С she: has got."),
    ],
    "a2-ed-ing-adjectives": [
        ("I'm boring.", "I'm bored.", "Boring описва нещо скучно, bored описва как се чувстваш."),
        ("I'm interesting in music.", "I'm interested in music.", "Чувство: -ed."),
    ],
    "a2-verb-ing-to": [
        ("I enjoy to swim.", "I enjoy swimming.", "След enjoy: -ing."),
        ("I want going home.", "I want to go home.", "След want: to + глагол."),
    ],
    "a2-purpose": [
        ("I came for see you.", "I came to see you.", "„За да“ е to + глагол."),
    ],
    "a2-adverbs": [
        ("She speaks English very good.", "She speaks English very well.", "Глаголът се описва с наречие: well."),
        ("Drive careful!", "Drive carefully!", "Наречие: careful + -ly."),
    ],
    "b1-just-yet-already": [
        ("I didn't finish yet.", "I haven't finished yet.", "С yet в британския английски: Present Perfect."),
        ("I have yet eaten.", "I have already eaten.", "„Вече“ в утвърдително изречение е already."),
    ],
    "b1-present-perfect-continuous": [
        ("I am waiting for an hour.", "I have been waiting for an hour.", "За продължителност до сега: Present Perfect Continuous."),
        ("I have been knowing him for years.", "I have known him for years.", "Know не се използва с -ing."),
    ],
    "b1-question-tags": [
        ("You like coffee, isn't it?", "You like coffee, don't you?", "Опашката повтаря спомагателния глагол."),
        ("I'm late, amn't I?", "I'm late, aren't I?", "Изключение: aren't I."),
    ],
    "b1-too-enough": [
        ("It's too nice! (комплимент)", "It's very nice!", "Too означава проблем."),
        ("It isn't enough big.", "It isn't big enough.", "Enough стои след прилагателното."),
    ],
    "b2-contrast": [
        ("Despite of the rain...", "Despite the rain...", "Despite е без of."),
        ("Although the rain, we went out.", "Despite the rain, we went out.", "След although следва цяло изречение."),
    ],
    "b2-future-continuous-perfect": [
        ("By Friday I will finish.", "By Friday I will have finished.", "By + време: Future Perfect."),
    ],
    "b2-stative-verbs": [
        ("I am understanding you.", "I understand you.", "Understand е глагол за състояние."),
        ("This is belonging to me.", "This belongs to me.", "Belong не се използва с -ing."),
    ],
    "c1-advanced-passive": [
        ("It is saying that...", "It is said that...", "Безличната конструкция е страдателна."),
        ("He is believed to leave yesterday.", "He is believed to have left yesterday.", "За минало: to have + причастие."),
    ],
    "c1-unreal-past": [
        ("It's time we go.", "It's time we went.", "След it's time + подлог: минало време."),
        ("I'd rather you don't come.", "I'd rather you didn't come.", "Would rather + друг човек: минало време."),
    ],
    "c1-conditional-inversion": [
        ("Hadn't I seen it...", "Had I not seen it...", "При инверсия not е след подлога."),
    ],
    "c2-subjunctive": [
        ("I insist that he comes.", "I insist that he come.", "След insist that: основна форма (или should come)."),
    ],
    "c2-nominalisation": [
        ("The reducement of costs", "The reduction of costs", "Съществителното от reduce е reduction."),
    ],
}
