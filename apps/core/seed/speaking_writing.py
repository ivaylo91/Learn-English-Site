"""Speaking and writing lessons, one unit per level.

Speaking uses shadowing (hear a sentence, repeat it aloud), which research links to better fluency and
intelligibility; the browser's speech recognition gives word-by-word feedback. Writing follows the CEFR
writing tasks: forms and notes (A1), short messages (A2), informal email (B1), formal email (B2),
argument essay (C1) and summary (C2). Each writing lesson shows a model text, then practises its structure.
"""

from html import escape

from .courses import C, F, O, S, T


def model_text(title, paragraphs, notes):
    """A model text box plus a table explaining its parts."""
    body = "".join(f"<p>{escape(p)}</p>" for p in paragraphs)
    rows = "".join(f'<tr><td class="en">{escape(a)}</td><td>{escape(b)}</td></tr>' for a, b in notes)
    return f"""
<p>Ето примерен текст. Разгледай как е построен, после упражни частите му.</p>
<div class="reading" lang="en"><h4><span>{escape(title)}</span></h4>{body}</div>
<h3>Как е построен</h3>
<table><tr><th>Израз</th><th>За какво служи</th></tr>{rows}</table>
"""


SPEAK_INTRO = """<p>Методът „сянка“ (<span class="en">shadowing</span>): чуй изречението, после го кажи на глас веднага, със същия ритъм и интонация. Натисни микрофона и говори ясно. Ще видиш кои думи разпознахме.</p>
<div class="tip">Разпознаването на реч работи в Chrome, Edge и Safari. Първия път браузърът ще поиска достъп до микрофона.</div>"""


def unit(level, slug, lessons):
    return {"level": level, "title": "Говорене и писане", "slug": slug, "icon": "fa-microphone", "order": 6,
            "summary": "Кажи го на глас и го напиши.", "lessons": lessons}


UNITS = [
    unit("A1", "a1-speak-write", [
        {
            "slug": "a1-speak-introduce", "title": "Говори: представи се", "title_en": "Speaking: introduce yourself",
            "kind": "speaking", "minutes": 5, "xp": 15, "summary": "Кажи името си, откъде си и какво работиш.",
            "theory": SPEAK_INTRO + """
<h3>Изречения за упражнение</h3>
<ul>
<li><span class="en">Hi, my name is Maria.</span></li>
<li><span class="en">I'm from Bulgaria.</span></li>
<li><span class="en">I live in Sofia.</span></li>
<li><span class="en">I work in a bank.</span></li>
<li><span class="en">Nice to meet you.</span></li>
</ul>
""",
            "exercises": [
                S("Hi, my name is Maria."),
                S("I'm from Bulgaria."),
                S("I live in Sofia."),
                S("I work in a bank."),
                S("Nice to meet you."),
            ],
        },
        {
            "slug": "a1-write-form", "title": "Пиши: формуляр и кратка бележка", "title_en": "Writing: a form and a short note",
            "kind": "writing", "minutes": 7, "xp": 15, "summary": "Попълни регистрация в хотел и остави бележка.",
            "theory": model_text("A note on the fridge", [
                "Hi Tom,",
                "I'm at the gym. Back at 7. There's pizza in the fridge.",
                "See you later,",
                "Anna",
            ], [("Hi Tom,", "поздрав към близък човек"), ("I'm at...", "къде си"), ("Back at 7.", "кога се връщаш (кратко, без подлог)"),
                ("See you later,", "неформален край")]) + """
<h3>Формуляр в хотел</h3>
<table>
<tr><th>Поле</th><th>Значение</th></tr>
<tr><td class="en">First name / Surname</td><td>име / фамилия</td></tr>
<tr><td class="en">Date of birth</td><td>дата на раждане</td></tr>
<tr><td class="en">Nationality</td><td>националност (Bulgarian)</td></tr>
<tr><td class="en">Address / Postcode</td><td>адрес / пощенски код</td></tr>
<tr><td class="en">Signature</td><td>подпис</td></tr>
</table>
<div class="tip">Националността се пише с главна буква: <span class="en">Bulgarian</span>. Датата във Великобритания е ден/месец/година: 25/10/1990.</div>
""",
            "exercises": [
                C("Surname означава:", ["фамилия", "прякор", "презиме"], 0),
                C("Какво пишеш в полето Nationality?", ["Bulgarian", "Bulgaria", "bulgarian"], 0, "Националността е прилагателно с главна буква."),
                C("Date of birth:", ["дата на раждане", "дата на пристигане", "рожден ден на хотела"], 0),
                F("I'm at the shop. ___ at 6.", "Back"),
                O("Обядът е в хладилника.", "Lunch is in the fridge"),
                T("Ще се видим по-късно!", "See you later"),
            ],
        },
    ]),
    unit("A2", "a2-speak-write", [
        {
            "slug": "a2-speak-cafe", "title": "Говори: в кафенето и магазина", "title_en": "Speaking: ordering and shopping",
            "kind": "speaking", "minutes": 6, "xp": 20, "summary": "Учтиви молби на глас.",
            "theory": SPEAK_INTRO,
            "exercises": [
                S("Can I have a coffee, please?"),
                S("How much is this jacket?"),
                S("Do you have it in a bigger size?"),
                S("Could I pay by card?"),
                S("Thank you, have a nice day!"),
            ],
        },
        {
            "slug": "a2-write-message", "title": "Пиши: кратко съобщение и покана", "title_en": "Writing: short messages and invitations",
            "kind": "writing", "minutes": 8, "xp": 20, "summary": "Кани, приемай и отказвай с кратко съобщение.",
            "theory": model_text("Party on Saturday!", [
                "Hi Sara,",
                "I'm having a small party on Saturday for my birthday. Would you like to come?",
                "It starts at 8 pm at my flat. Bring a friend if you want!",
                "Let me know by Thursday.",
                "Love, Elena",
            ], [("Would you like to come?", "покана"), ("It starts at...", "кога и къде"),
                ("Let me know by Thursday.", "до кога да отговорят"), ("Love, / Best,", "край за приятели")]) + """
<h3>Отговори</h3>
<ul>
<li>Приемане: <span class="en">Thanks for the invitation! I'd love to come.</span></li>
<li>Отказ: <span class="en">Thanks, but I'm afraid I can't make it. I'm away that weekend.</span></li>
</ul>
""",
            "exercises": [
                C("Как каниш учтиво?", ["Would you like to come?", "You come?", "Come to my party."], 0),
                C("Учтив отказ:", ["No.", "I'm afraid I can't make it.", "I don't want."], 1),
                C("Let me know by Thursday. означава:", ["Кажи ми до четвъртък.", "Ела в четвъртък.", "Знам до четвъртък."], 0),
                F("Thanks for the ___ ! I'd love to come.", "invitation"),
                O("Купонът започва в осем вечерта.", "The party starts at 8 pm|The party starts at eight pm"),
                T("Благодаря за поканата!", "Thanks for the invitation|Thank you for the invitation"),
            ],
        },
    ]),
    unit("B1", "b1-speak-write", [
        {
            "slug": "b1-speak-weekend", "title": "Говори: разкажи за уикенда", "title_en": "Speaking: talk about your weekend",
            "kind": "speaking", "minutes": 7, "xp": 25, "summary": "Свързана реч в минало време.",
            "theory": SPEAK_INTRO + """
<div class="tip">Обърни внимание на ритъма: ударени са думите със съдържание (<span class="en">WENT, MOUNtains, SATurday</span>), а малките думи са кратки.</div>
""",
            "exercises": [
                S("Last weekend I went to the mountains with my friends."),
                S("The weather was perfect, so we went hiking."),
                S("In the evening we had dinner in a small restaurant."),
                S("I didn't want to come back on Sunday!"),
                S("What did you do at the weekend?"),
            ],
        },
        {
            "slug": "b1-write-email", "title": "Пиши: неформален имейл", "title_en": "Writing: an informal email",
            "kind": "writing", "minutes": 9, "xp": 25, "summary": "Имейл до приятел: новини, въпроси, край.",
            "theory": model_text("Long time no see!", [
                "Hi Mark,",
                "Thanks for your email. Sorry I haven't written for ages, I've been really busy with my new job.",
                "Guess what? I'm coming to London in May for a conference! Are you free on the 12th? It would be great to meet up.",
                "Anyway, how are things with you? How's the new flat?",
                "Write back soon,",
                "Ivan",
            ], [("Thanks for your email.", "отговор на писмо"), ("Sorry I haven't written for ages", "извинение за мълчанието"),
                ("Guess what?", "въвеждане на новина"), ("Anyway,", "смяна на темата"),
                ("Write back soon,", "неформален край")]),
            "exercises": [
                C("Подходящо начало на неформален имейл:", ["Dear Sir,", "Hi Mark,", "To whom it may concern,"], 1),
                C("Guess what? се използва, за да:", ["въведеш интересна новина", "се извиниш", "завършиш писмото"], 0),
                C("Неформален край:", ["Yours faithfully,", "Write back soon,", "Kind regards, Mr Petrov"], 1),
                F("Sorry I haven't written ___ ages.", "for"),
                O("Би било страхотно да се видим.", "It would be great to meet up|It would be great to see you"),
                T("Как вървят нещата при теб?", "How are things with you|How are things"),
            ],
        },
    ]),
    unit("B2", "b2-speak-write", [
        {
            "slug": "b2-speak-opinion", "title": "Говори: изрази мнение", "title_en": "Speaking: giving your opinion",
            "kind": "speaking", "minutes": 7, "xp": 30, "summary": "Аргументирано мнение на глас.",
            "theory": SPEAK_INTRO,
            "exercises": [
                S("In my opinion, working from home has more advantages than disadvantages."),
                S("I see your point, but I'm not entirely convinced."),
                S("On the one hand it saves time, but on the other hand it can be lonely."),
                S("That's a fair point, although I'd look at it differently."),
                S("All things considered, I think it depends on the person."),
            ],
        },
        {
            "slug": "b2-write-formal-email", "title": "Пиши: официален имейл", "title_en": "Writing: a formal email",
            "kind": "writing", "minutes": 10, "xp": 30, "summary": "Молба за информация или оплакване в официален стил.",
            "theory": model_text("Complaint about order 48213", [
                "Dear Sir or Madam,",
                "I am writing to complain about an order I placed on your website on 3 March (order number 48213).",
                "Although I paid for next-day delivery, the parcel arrived a week later, and the laptop inside was damaged.",
                "I would therefore be grateful if you could arrange a replacement or a full refund as soon as possible.",
                "I look forward to hearing from you.",
                "Yours faithfully,",
                "Ivana Dimitrova",
            ], [("Dear Sir or Madam,", "когато не знаеш името"), ("I am writing to...", "причина за писмото"),
                ("Although...", "факти и проблем"), ("I would be grateful if you could...", "учтива молба"),
                ("Yours faithfully,", "край, когато не знаеш името (с име: Yours sincerely)")]),
            "exercises": [
                C("Писмото започва с Dear Sir or Madam. Как завършва?", ["Yours faithfully,", "Yours sincerely,", "Love,"], 0),
                C("Писмото започва с Dear Ms Brown. Как завършва?", ["Yours faithfully,", "Yours sincerely,", "Cheers,"], 1),
                C("Кое е най-подходящо за официален имейл?", ["I want my money back!", "I would be grateful if you could arrange a refund.", "Give me a refund."], 1),
                F("I am writing ___ complain about my order.", "to"),
                O("Очаквам отговора ви.", "I look forward to hearing from you"),
                T("Пиша, за да попитам за курса.", "I am writing to ask about the course|I'm writing to ask about the course|I am writing to enquire about the course|I am writing to inquire about the course"),
            ],
        },
    ]),
    unit("C1", "c1-speak-write", [
        {
            "slug": "c1-speak-present", "title": "Говори: мини презентация", "title_en": "Speaking: a short presentation",
            "kind": "speaking", "minutes": 8, "xp": 35, "summary": "Фрази за представяне, казани с увереност.",
            "theory": SPEAK_INTRO,
            "exercises": [
                S("Today I'd like to walk you through our results for the last quarter."),
                S("As you can see from this chart, sales have grown steadily."),
                S("That brings me to my next point."),
                S("The key takeaway here is that our customers want simpler products."),
                S("Thank you for listening. I'm happy to take any questions."),
            ],
        },
        {
            "slug": "c1-write-essay", "title": "Пиши: аргументирано есе", "title_en": "Writing: an argument essay",
            "kind": "writing", "minutes": 10, "xp": 35, "summary": "Увод, аргументи, контрааргумент, заключение.",
            "theory": model_text("Should university education be free?", [
                "Few issues divide opinion as sharply as the question of who should pay for higher education.",
                "Proponents of free tuition argue that it widens access and benefits society as a whole. Moreover, graduates who start their careers without debt are more likely to take risks, such as starting a business.",
                "Critics, however, point out that free tuition is funded by all taxpayers, including those who never attend university. They also argue that it may lower the perceived value of a degree.",
                "On balance, I believe the benefits outweigh the costs, provided that funding is linked to the quality of teaching.",
            ], [("Few issues divide opinion as sharply as...", "увод: защо темата е важна"),
                ("Proponents argue that... Moreover,...", "първа позиция и допълнителен аргумент"),
                ("Critics, however, point out that...", "контрааргумент"),
                ("On balance, I believe...", "заключение с твоята позиция"),
                ("provided that...", "уточнение, условие")]),
            "exercises": [
                C("Коя фраза въвежда допълнителен аргумент?", ["Moreover,", "However,", "On balance,"], 0),
                C("Коя фраза въвежда контрааргумент?", ["In addition,", "Critics, however, point out that", "Firstly,"], 1),
                C("On balance, I believe... е подходящо за:", ["заключението", "увода", "първия аргумент"], 0),
                C("В академично есе се избягва:", ["I think it's kinda bad.", "It could be argued that...", "There is evidence that..."], 0),
                F("The benefits ___ the costs. (надвишават)", "outweigh"),
                O("Като цяло ползите надвишават разходите.", "On balance the benefits outweigh the costs"),
            ],
        },
    ]),
    unit("C2", "c2-speak-write", [
        {
            "slug": "c2-write-summary", "title": "Пиши: резюме", "title_en": "Writing: summarising",
            "kind": "writing", "minutes": 10, "xp": 40, "summary": "Как да предадеш същината със свои думи.",
            "theory": model_text("A summary of 'Loved to death'", [
                "The article examines how several European cities are responding to overtourism.",
                "It notes that measures such as entry fees and caps on holiday rentals aim to protect residents from rising prices, while acknowledging criticism that such policies make travel more exclusive.",
                "The author concludes that the solution lies not in limiting tourism outright but in managing it more evenly.",
            ], [("The article examines...", "тема на текста, в сегашно време"),
                ("It notes that... while acknowledging...", "основни идеи, балансирано"),
                ("The author concludes that...", "изводът на автора"),
                ("Свои думи", "перифразирай, не копирай изречения")]),
            "exercises": [
                C("В какво време обикновено се пише резюме?", ["Сегашно просто", "Минало просто", "Бъдеще"], 0),
                C("Добро резюме:", ["Копира най-добрите изречения", "Предава основните идеи със свои думи", "Добавя твоето мнение навсякъде"], 1),
                C("Кой глагол е подходящ за резюме?", ["The author argues that...", "The author kinda says...", "The author thinks maybe..."], 0),
                F("The author ___ that tourism should be managed, not banned.", "concludes|argues|suggests|claims"),
                O("Статията разглежда проблемите на свръхтуризма.", "The article examines the problems of overtourism"),
                S("The article examines how cities are responding to overtourism."),
            ],
        },
    ]),
]

MISTAKES = {
    "a1-write-form": [
        ("Nationality: bulgarian", "Nationality: Bulgarian", "Националности се пишат с главна буква."),
        ("Nationality: Bulgaria", "Nationality: Bulgarian", "Нужно е прилагателното, не държавата."),
    ],
    "a2-write-message": [
        ("I can't come. (без нищо друго)", "Thanks, but I'm afraid I can't make it.", "Голият отказ звучи рязко."),
    ],
    "b1-write-email": [
        ("Dear Mark, ... Yours faithfully", "Hi Mark, ... Write back soon,", "Не смесвай официален и неформален стил."),
    ],
    "b2-write-formal-email": [
        ("Dear Sir or Madam, ... Yours sincerely,", "Dear Sir or Madam, ... Yours faithfully,", "Без име: faithfully. С име: sincerely."),
        ("I want a refund.", "I would be grateful if you could arrange a refund.", "Официалният стил изисква учтива, непряка молба."),
    ],
    "c1-write-essay": [
        ("I think it's kinda bad.", "It could be argued that this approach has drawbacks.", "Академичният стил избягва разговорни думи."),
    ],
    "c2-write-summary": [
        ("The author said that...", "The author argues that...", "Резюмето се пише в сегашно време с точни глаголи."),
    ],
}
