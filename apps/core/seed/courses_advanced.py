"""B1 to C2 (Proficiency) grammar and vocabulary lessons."""

from .courses import C, F, T

UNITS = [
    # ---------------- B1 ----------------
    {
        "level": "B1", "title": "Планове и възможности", "slug": "b1-plans-possibilities", "icon": "fa-calendar-check",
        "order": 2, "summary": "Бъдеще време и първи условни изречения.",
        "lessons": [
            {
                "slug": "b1-will-going-to", "title": "Бъдеще: will или going to", "title_en": "Future: will vs going to",
                "kind": "grammar", "minutes": 8, "xp": 20,
                "summary": "Решение на момента или вече направен план?",
                "theory": """
<p>И двете форми говорят за бъдещето, но с различен смисъл. На български често казваме просто „ще“.</p>
<table>
<tr><th>Форма</th><th>Кога</th><th>Пример</th></tr>
<tr><td class="en">will</td><td>решение в момента на говорене, обещание, предложение</td><td class="en">It's cold. I'll close the window.</td></tr>
<tr><td class="en">going to</td><td>план, решен преди</td><td class="en">I'm going to visit Rome in May.</td></tr>
<tr><td class="en">going to</td><td>предвиждане по видими признаци</td><td class="en">Look at those clouds. It's going to rain.</td></tr>
<tr><td class="en">will</td><td>мнение, предположение за бъдещето</td><td class="en">I think she'll pass the exam.</td></tr>
</table>
<div class="tip">За уговорени срещи с точен час и място често се използва Present Continuous: <span class="en">I'm meeting Ana at six.</span></div>
""",
                "exercises": [
                    C("The phone is ringing. I ___ answer it.", ["'ll", "'m going to"], 0, "Решение в момента: will."),
                    C("We've booked the hotel. We ___ spend a week in Crete.", ["will", "are going to"], 1, "Планът е направен предварително."),
                    C("Look at that car! It ___ crash!", ["will", "is going to"], 1, "Виждаме признаците сега."),
                    C("I think Bulgaria ___ win the match.", ["will", "is going to"], 0, "Лично мнение: will."),
                    F("Don't worry, I ___ help you with your bags.", "will|'ll", "Предложение за помощ: will."),
                    T("Ще уча медицина след училище. (планът вече е решен)", "I'm going to study medicine after school|I am going to study medicine after school"),
                ],
            },
            {
                "slug": "b1-first-conditional", "title": "Първи условни изречения", "title_en": "First conditional",
                "kind": "grammar", "minutes": 8, "xp": 20,
                "summary": "Ако вали, ще остана вкъщи: реални ситуации в бъдещето.",
                "theory": """
<p>Използваме го за <strong>реална възможност</strong> в бъдещето.</p>
<p><strong>If + Present Simple, will + глагол</strong></p>
<ul>
<li><span class="en">If it rains, I'll stay at home.</span> Ако вали, ще си остана вкъщи.</li>
<li><span class="en">If you study, you'll pass.</span> Ако учиш, ще издържиш.</li>
</ul>
<div class="tip">Най-честата грешка на българите: <em>If it will rain</em>. След <span class="en">if</span> <strong>не</strong> слагаме will, въпреки че на български казваме „ако ще вали“ понякога.</div>
<h3>Unless = if not</h3>
<p><span class="en">You won't pass unless you study.</span> Няма да издържиш, освен ако не учиш.</p>
<p>Частите могат да си разменят местата: <span class="en">I'll call you if I'm late.</span> (без запетая, когато if е по средата)</p>
""",
                "exercises": [
                    C("If it ___ tomorrow, we'll go to the beach.", ["is sunny", "will be sunny", "would be sunny"], 0, "След if: Present Simple."),
                    C("If you don't hurry, you ___ the bus.", ["miss", "will miss", "would miss"], 1),
                    F("If she ___ (miss) the bus, she'll be late.", "misses"),
                    F("I ___ (call) you if I hear any news.", "will call|'ll call"),
                    C("You won't get fit ___ you exercise.", ["if", "unless", "when"], 1, "Unless = if not."),
                    T("Ако имам време, ще ти помогна.", "If I have time I will help you|If I have time I'll help you|I will help you if I have time|I'll help you if I have time"),
                ],
            },
        ],
    },
    # ---------------- B2 ----------------
    {
        "level": "B2", "title": "Сложни структури", "slug": "b2-complex-structures", "icon": "fa-diagram-project",
        "order": 1, "summary": "Хипотетични ситуации, страдателен залог и непряка реч.",
        "lessons": [
            {
                "slug": "b2-second-conditional", "title": "Втори условни изречения", "title_en": "Second conditional",
                "kind": "grammar", "minutes": 9, "xp": 25,
                "summary": "Ако бях милионер...: въображаеми ситуации в настоящето.",
                "theory": """
<p>Говорим за нещо <strong>нереално или малко вероятно</strong> сега или в бъдещето.</p>
<p><strong>If + Past Simple, would + глагол</strong></p>
<ul>
<li><span class="en">If I had more money, I would travel more.</span> Ако имах повече пари, щях да пътувам повече.</li>
<li><span class="en">If she lived closer, we'd see each other every day.</span></li>
</ul>
<div class="tip">С глагола to be в официален английски се използва <span class="en">were</span> за всички лица: <span class="en">If I were you, I'd apologise.</span> (Аз на твое място бих се извинил/а.)</div>
<h3>Първо или второ условно?</h3>
<table>
<tr><th>Първо</th><th>Второ</th></tr>
<tr><td class="en">If I get the job, I'll move to Sofia.</td><td class="en">If I got the job, I'd move to Sofia.</td></tr>
<tr><td>реално възможно</td><td>по-малко вероятно, мечта</td></tr>
</table>
""",
                "exercises": [
                    C("If I ___ a car, I would drive to work.", ["have", "had", "would have"], 1),
                    C("If I ___ you, I'd take the offer.", ["am", "were", "would be"], 1, "If I were you: съвет."),
                    F("What ___ you do if you won the lottery?", "would"),
                    F("If he ___ (speak) French, he could work in Paris.", "spoke"),
                    C("Кое изречение е за нереална ситуация?", ["If it rains, we'll stay in.", "If I lived by the sea, I'd swim every day.", "If you call, I'll answer."], 1),
                    T("Ако имах повече време, щях да чета повече.", "If I had more time I would read more|If I had more time I'd read more|I would read more if I had more time|I'd read more if I had more time"),
                ],
            },
            {
                "slug": "b2-passive-voice", "title": "Страдателен залог", "title_en": "The passive voice",
                "kind": "grammar", "minutes": 9, "xp": 25,
                "summary": "Кога важно е действието, а не кой го е извършил.",
                "theory": """
<p>Образува се с <strong>be + минало причастие</strong>. Времето се показва чрез be.</p>
<table>
<tr><th>Време</th><th>Деятелен залог</th><th>Страдателен залог</th></tr>
<tr><td>Present Simple</td><td class="en">They make cars here.</td><td class="en">Cars are made here.</td></tr>
<tr><td>Past Simple</td><td class="en">Someone stole my bike.</td><td class="en">My bike was stolen.</td></tr>
<tr><td>Present Perfect</td><td class="en">They have opened a new café.</td><td class="en">A new café has been opened.</td></tr>
<tr><td>с модален глагол</td><td class="en">You must sign the form.</td><td class="en">The form must be signed.</td></tr>
</table>
<p>Ако искаме да кажем кой е извършил действието, използваме <span class="en">by</span>: <span class="en">The book was written by Ivan Vazov.</span></p>
<div class="tip">В българския често използваме „се“: „Колите се правят тук“. В английския това е страдателен залог.</div>
""",
                "exercises": [
                    C("English ___ all over the world.", ["speaks", "is spoken", "is speaking"], 1),
                    C("The Rila Monastery ___ in the 10th century.", ["founded", "was founded", "has founded"], 1),
                    F("My phone ___ (steal) yesterday.", "was stolen"),
                    F("The results will ___ announced tomorrow.", "be"),
                    C("The bridge ___ for two years now.", ["has been repaired", "is repaired", "was repaired"], 0,
                      "For two years now: Present Perfect."),
                    T("Писмото беше изпратено вчера.", "The letter was sent yesterday|Yesterday the letter was sent"),
                ],
            },
            {
                "slug": "b2-reported-speech", "title": "Непряка реч", "title_en": "Reported speech",
                "kind": "grammar", "minutes": 9, "xp": 25,
                "summary": "Как да предадеш какво е казал някой друг.",
                "theory": """
<p>Когато предаваме думи след <span class="en">said</span> или <span class="en">told</span>, времето обикновено „отстъпва“ една стъпка назад.</p>
<table>
<tr><th>Пряка реч</th><th>Непряка реч</th></tr>
<tr><td class="en">"I am tired."</td><td class="en">She said (that) she was tired.</td></tr>
<tr><td class="en">"I'm working."</td><td class="en">He said he was working.</td></tr>
<tr><td class="en">"I saw it."</td><td class="en">She said she had seen it.</td></tr>
<tr><td class="en">"I will call."</td><td class="en">He said he would call.</td></tr>
<tr><td class="en">"I can swim."</td><td class="en">She said she could swim.</td></tr>
</table>
<h3>Say или tell?</h3>
<p><span class="en">tell</span> изисква човек след себе си: <span class="en">She told <strong>me</strong> that...</span> При <span class="en">say</span> няма: <span class="en">She said that...</span></p>
<h3>Въпроси</h3>
<p>В непряк въпрос редът е като в утвърдително изречение: <span class="en">"Where do you live?"</span> става <span class="en">He asked where I lived.</span></p>
<div class="tip">Думите за време също се променят: <span class="en">today</span> става <span class="en">that day</span>, <span class="en">tomorrow</span> става <span class="en">the next day</span>.</div>
""",
                "exercises": [
                    C('"I am hungry." She said she ___ hungry.', ["is", "was", "has been"], 1),
                    C('"I will help you." He said he ___ help me.', ["will", "would", "can"], 1),
                    C("She ___ me that she was leaving.", ["said", "told", "asked"], 1, "Tell + човек."),
                    C('"Where do you work?" He asked me where ___.', ["did I work", "I worked", "do I work"], 1,
                      "В непрекия въпрос няма инверсия."),
                    F('"I saw the film." She said she had ___ the film.', "seen"),
                    T("Той каза, че е уморен.", "He said he was tired|He said that he was tired"),
                ],
            },
        ],
    },
    # ---------------- C1 ----------------
    {
        "level": "C1", "title": "Прецизен изказ", "slug": "c1-precise-expression", "icon": "fa-bullseye",
        "order": 1, "summary": "Условни изречения за миналото, инверсия и фразови глаголи за работа.",
        "lessons": [
            {
                "slug": "c1-third-mixed-conditionals", "title": "Трети и смесени условни изречения",
                "title_en": "Third and mixed conditionals", "kind": "grammar", "minutes": 10, "xp": 30,
                "summary": "Съжаления, критика и въображаемо минало.",
                "theory": """
<h3>Трето условно: нереално минало</h3>
<p><strong>If + Past Perfect, would have + причастие</strong></p>
<p><span class="en">If I had left earlier, I wouldn't have missed the train.</span> Ако бях тръгнал/а по-рано, нямаше да изпусна влака. (Но тръгнах късно.)</p>
<h3>Смесени условни</h3>
<p>Свързват различни времена.</p>
<ul>
<li>Минало условие, настоящ резултат: <span class="en">If I had studied medicine, I would be a doctor now.</span></li>
<li>Настоящо условие, минал резултат: <span class="en">If she were more organised, she wouldn't have forgotten the meeting.</span></li>
</ul>
<div class="tip">В разговор <span class="en">would have</span> звучи като <span class="en">would've</span> или дори „woulda“. Не пиши <em>would of</em>: това е често срещана грешка дори сред носителите на езика.</div>
""",
                "exercises": [
                    C("If we ___ the map, we wouldn't have got lost.", ["had checked", "checked", "would check"], 0),
                    C("If I had taken that job, I ___ in London now.", ["would have lived", "would live", "would be living"], 2,
                      "Минало условие, настоящ резултат: would be (living) now."),
                    F("She would have passed if she ___ (study) harder.", "had studied|'d studied"),
                    C("Кое е правилно?", ["I would of come.", "I would have come.", "I would had come."], 1),
                    C("If he weren't so stubborn, he ___ the argument yesterday.", ["wouldn't have started", "won't start", "didn't start"], 0),
                    T("Ако бяхме знаели, щяхме да ти кажем.", "If we had known we would have told you|If we'd known we would have told you|If we had known we'd have told you|If we'd known we'd have told you|If we had known we would've told you|If we'd known we would've told you"),
                ],
            },
            {
                "slug": "c1-inversion", "title": "Инверсия за емфаза", "title_en": "Inversion for emphasis",
                "kind": "grammar", "minutes": 10, "xp": 30,
                "summary": "Never have I seen...: официален и силен изказ.",
                "theory": """
<p>След някои отрицателни или ограничителни изрази в началото на изречението редът е като във въпрос: <strong>спомагателен глагол + подлог</strong>.</p>
<table>
<tr><th>Израз</th><th>Пример</th></tr>
<tr><td class="en">Never</td><td class="en">Never have I seen such a beautiful view.</td></tr>
<tr><td class="en">Rarely / Seldom</td><td class="en">Rarely do we get a chance like this.</td></tr>
<tr><td class="en">Not only ... but also</td><td class="en">Not only did she win, but she also broke the record.</td></tr>
<tr><td class="en">Hardly ... when</td><td class="en">Hardly had I arrived when it started to rain.</td></tr>
<tr><td class="en">No sooner ... than</td><td class="en">No sooner had we sat down than the phone rang.</td></tr>
<tr><td class="en">Under no circumstances</td><td class="en">Under no circumstances should you open this door.</td></tr>
</table>
<div class="tip">Инверсията звучи официално и драматично. В ежедневен разговор е по-естествено: <span class="en">I've never seen such a view.</span></div>
""",
                "exercises": [
                    C("Never ___ such a mess!", ["I have seen", "have I seen", "I saw"], 1),
                    C("Not only ___ late, but he also forgot the tickets.", ["he was", "was he", "he is"], 1),
                    F("No sooner ___ we left than it started snowing.", "had"),
                    C("Under no circumstances ___ leave the building.", ["you should", "should you", "you must"], 1),
                    F("Rarely ___ (do) she complain about anything.", "does"),
                    C("Hardly had I closed my eyes ___ the alarm went off.", ["than", "when", "then"], 1, "Hardly ... when, No sooner ... than."),
                ],
            },
            {
                "slug": "c1-phrasal-verbs-work", "title": "Фразови глаголи за работа", "title_en": "Phrasal verbs at work",
                "kind": "vocabulary", "minutes": 8, "xp": 25,
                "summary": "Изразите, които ще чуеш на всяка среща.",
                "theory": """
<table>
<tr><th>Фразов глагол</th><th>Значение</th><th>Пример</th></tr>
<tr><td class="en">carry out</td><td>извършвам, провеждам</td><td class="en">We carried out a survey.</td></tr>
<tr><td class="en">come up with</td><td>измислям, предлагам</td><td class="en">She came up with a great idea.</td></tr>
<tr><td class="en">put off</td><td>отлагам</td><td class="en">The meeting was put off until Friday.</td></tr>
<tr><td class="en">follow up (on)</td><td>проследявам, връщам се към</td><td class="en">I'll follow up on this by email.</td></tr>
<tr><td class="en">take on</td><td>поемам (работа, отговорност)</td><td class="en">I can't take on any more projects.</td></tr>
<tr><td class="en">run out of</td><td>свършва ми (се)</td><td class="en">We've run out of time.</td></tr>
<tr><td class="en">bring up</td><td>повдигам (тема)</td><td class="en">He brought up the budget issue.</td></tr>
<tr><td class="en">step down</td><td>оттеглям се от длъжност</td><td class="en">The CEO stepped down last month.</td></tr>
</table>
""",
                "exercises": [
                    C("We need to ___ a solution by Monday.", ["come up with", "put off", "step down"], 0),
                    C("The launch has been ___ until next year.", ["carried out", "put off", "taken on"], 1),
                    F("Sorry, we've run ___ of printer paper.", "out"),
                    C("Who will ___ the new client? I'm too busy.", ["take on", "bring up", "follow up"], 0),
                    F("I'd like to ___ up an issue from last week's meeting.", "bring"),
                    C("После срещата ще ти пиша, за да проследим задачите.", ["I'll follow up by email.", "I'll put it off by email.", "I'll carry it on by email."], 0,
                      instruction="Кой е правилният превод?"),
                ],
            },
        ],
    },
    # ---------------- C2 ----------------
    {
        "level": "C2", "title": "Нюанси и стил", "slug": "c2-nuance-style", "icon": "fa-feather-pointed",
        "order": 1, "summary": "Идиоми, изречения за акцент и усет за стил.",
        "lessons": [
            {
                "slug": "c2-everyday-idioms", "title": "Идиоми в ежедневието", "title_en": "Everyday idioms",
                "kind": "vocabulary", "minutes": 8, "xp": 30,
                "summary": "Изрази, които звучат естествено, когато ги разбираш.",
                "theory": """
<table>
<tr><th>Идиом</th><th>Значение</th></tr>
<tr><td class="en">to bite off more than you can chew</td><td>да се захванеш с повече, отколкото можеш</td></tr>
<tr><td class="en">to burn the candle at both ends</td><td>да се преуморяваш, работиш до късно и ставаш рано</td></tr>
<tr><td class="en">to cut corners</td><td>да правиш нещо набързо и некачествено, за да спестиш</td></tr>
<tr><td class="en">a blessing in disguise</td><td>нещо лошо, което се оказва за добро</td></tr>
<tr><td class="en">to sit on the fence</td><td>да не заемаш позиция</td></tr>
<tr><td class="en">to get the hang of something</td><td>да усвоиш, да „хванеш цаката“</td></tr>
<tr><td class="en">the elephant in the room</td><td>очевиден проблем, за който никой не говори</td></tr>
<tr><td class="en">once in a blue moon</td><td>много рядко</td></tr>
</table>
<div class="tip">Идиомите не се превеждат дума по дума. Учи ги с цял пример и в контекст.</div>
""",
                "exercises": [
                    C("Losing that job was a blessing in disguise. Какво означава?", ["Беше за добро в крайна сметка", "Беше голяма трагедия", "Беше тайна"], 0),
                    C("Stop sitting on the fence and ___!", ["make a decision", "sit down", "climb over"], 0),
                    C("We only eat out once in a blue moon. Колко често?", ["Много рядко", "Всяка вечер", "При пълнолуние"], 0),
                    F("Don't cut ___. Do the job properly.", "corners"),
                    F("It's tricky at first, but you'll get the ___ of it.", "hang"),
                    C("Nobody mentioned the budget cuts, the elephant in the ___.", ["room", "house", "office"], 0),
                ],
            },
            {
                "slug": "c2-cleft-sentences", "title": "Изречения за акцент", "title_en": "Cleft sentences",
                "kind": "grammar", "minutes": 10, "xp": 35,
                "summary": "It was Maria who...: как да подчертаеш точно това, което искаш.",
                "theory": """
<p>В българския подчертаваме с интонация или словоред. В английския често „разцепваме“ изречението.</p>
<h3>It is/was ... that/who</h3>
<p>Обикновено: <span class="en">Maria found the keys.</span><br>
С акцент: <span class="en">It was Maria who found the keys.</span> (Мария, а не някой друг.)<br>
<span class="en">It was in 2010 that we met.</span></p>
<h3>What ... is/was</h3>
<p><span class="en">What I need is a long holiday.</span> Това, от което имам нужда, е дълга почивка.<br>
<span class="en">What surprised me was his reaction.</span></p>
<h3>All ... is/was</h3>
<p><span class="en">All I want is some peace and quiet.</span> Единственото, което искам, е малко спокойствие.</p>
<div class="tip">С действие използваме <span class="en">do</span>: <span class="en">What she did was (to) call the police.</span></div>
""",
                "exercises": [
                    C("___ was Tom who broke the window, not me.", ["It", "What", "That"], 0),
                    C("What I really need ___ a good night's sleep.", ["is", "are", "it is"], 0),
                    F("___ I want is to be left alone.", "All|What"),
                    C("What he did ___ resign on the spot.", ["was", "did", "is to"], 0),
                    C("Подчертай КОГА: We met in Paris in 2015.", ["It was in 2015 that we met in Paris.", "What we met was in 2015.", "It was we who met in 2015."], 0),
                    T("Това, което ме изненада, беше цената.", "What surprised me was the price"),
                ],
            },
            {
                "slug": "c2-register", "title": "Официален и неофициален стил", "title_en": "Formal and informal register",
                "kind": "reading", "minutes": 9, "xp": 35,
                "summary": "Как да звучиш уместно в имейл, на интервю и сред приятели.",
                "theory": """
<p>На ниво C2 не е достатъчно да е правилно. Трябва да е <strong>уместно</strong>. Сравни двата имейла:</p>
<table>
<tr><th>Неофициално</th><th>Официално</th></tr>
<tr><td class="en">Hi Sam, thanks for getting back to me.</td><td class="en">Dear Mr Hill, thank you for your prompt reply.</td></tr>
<tr><td class="en">Can you send me the file?</td><td class="en">I would be grateful if you could send me the file.</td></tr>
<tr><td class="en">Sorry, I can't make it.</td><td class="en">Unfortunately, I will be unable to attend.</td></tr>
<tr><td class="en">Let me know.</td><td class="en">I look forward to hearing from you.</td></tr>
<tr><td class="en">Cheers, Ana</td><td class="en">Kind regards, Ana Petrova</td></tr>
</table>
<h3>Признаци на официален стил</h3>
<ul>
<li>думи с латински произход: <span class="en">obtain</span> вместо <span class="en">get</span>, <span class="en">assist</span> вместо <span class="en">help</span></li>
<li>без съкращения: <span class="en">I will not</span> вместо <span class="en">I won't</span></li>
<li>страдателен залог и безлични конструкции: <span class="en">It has been decided that...</span></li>
</ul>
""",
                "exercises": [
                    C("Кое е най-подходящо за официален имейл?", ["Hey, what's up?", "Dear Ms Grant,", "Yo Grant!"], 1),
                    C("Официален вариант на „Can you help me?“", ["Could you possibly assist me?", "Help me, OK?", "You gotta help me."], 0),
                    C("Неофициален вариант на „I will be unable to attend.“", ["I can't make it.", "Attendance is impossible.", "I shall not be present."], 0),
                    F("I look forward to ___ from you.", "hearing", "След look forward to следва -ing форма."),
                    C("Кой глагол е по-официален от get?", ["obtain", "grab", "pick up"], 0),
                    C("Кое завършване е подходящо за писмо до непознат?", ["Cheers,", "Kind regards,", "Love,"], 1),
                ],
            },
        ],
    },
]
