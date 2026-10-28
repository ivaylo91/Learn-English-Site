"""A free-writing task at the end of every writing lesson: write your own text, then compare it with a model
answer and tick a short self-check list. Keyed by lesson slug; seed_content appends the task as the last exercise.
"""

from .courses import W

TASKS = {
    # ---------------- A1 ----------------
    "a1-write-form": W(
        "Напиши кратка бележка до съквартирант: излизаш, кога се връщаш и какво да купи.",
        "Hi Tom, I'm at the gym. I'm back at seven. Can you buy some bread and milk, please? Thanks! Ana",
        ["Обръщение и подпис", "Къде си и кога се връщаш", "Молба с Can you... please?"],
    ),
    "a1-write-postcard": W(
        "Напиши картичка до приятел от почивка: къде си, какво е времето, какво правиш.",
        "Dear Maria, I'm in Burgas with my family. The weather is hot and sunny. Every day we swim and eat ice cream. See you soon! Love, Petya",
        ["Обръщение (Dear...)", "Къде си и какво е времето", "Какво правите (Present Simple)", "Край: Love, / See you soon"],
    ),
    "a1-write-my-day": W(
        "Опиши обикновения си ден: кога ставаш, какво правиш, кога си лягаш.",
        "I get up at seven and have breakfast. I start work at nine. In the evening I cook dinner and read. I go to bed at eleven.",
        ["Часове с at", "Present Simple", "Поне една дума за честота (usually, sometimes)"],
    ),
    "a1-write-friend": W(
        "Опиши свой приятел или приятелка: възраст, външност, характер.",
        "My friend Ivan is 30. He is tall and he has short black hair. He is funny and kind. We often play football at the weekend.",
        ["Възраст с is, не has", "Външност с has", "Характер: is + прилагателно", "Какво правите заедно"],
    ),
    # ---------------- A2 ----------------
    "a2-write-message": W(
        "Напиши съобщение, с което каниш приятел на кино в събота. Кажи къде и кога да се срещнете.",
        "Hi Lily! Would you like to go to the cinema on Saturday? There's a new comedy at 8 pm. Let's meet outside the cinema at 7:45. Let me know!",
        ["Покана: Would you like to...?", "Ден, час и място", "Let's meet...", "Кратко и приятелско"],
    ),
    "a2-write-story": W(
        "Напиши кратка история за ден, в който нещо се обърка. Използвай минало време.",
        "Last Sunday we went to the mountains. Suddenly it started to rain and we got lost. Finally, we found a small hut and waited there. In the end we got home tired but happy.",
        ["Past Simple", "Начало, проблем, край", "Свързващи думи: suddenly, then, finally"],
    ),
    "a2-write-home": W(
        "Опиши дома си: къде е, какви стаи има и кое място обичаш най-много.",
        "I live in a flat in the centre of Sofia. There are three rooms and a small kitchen. My favourite room is the living room because it's bright and quiet.",
        ["There is / There are", "Предлози за място (in, on)", "Любимо място и защо (because)"],
    ),
    "a2-write-thank-you": W(
        "Напиши кратка благодарствена бележка на колега, който ти е помогнал с преместване.",
        "Dear Nick, thank you so much for helping me move last weekend. I couldn't do it without you! Let me buy you dinner next week. Best wishes, Elena",
        ["Thank you for + -ing", "Конкретно за какво благодариш", "Предложение или покана", "Подходящ край"],
    ),
    "a2-write-travel-blog": W(
        "Напиши кратък блог пост за пътуване: къде беше, какво видя, какво ти хареса най-много.",
        "Last summer I spent four days in Istanbul. We visited the Blue Mosque and took a boat on the Bosphorus. The best thing was the food! Next time I want to stay longer.",
        ["Past Simple", "Конкретни места и действия", "Превъзходна степен (the best...)", "План за следващия път"],
    ),
    # ---------------- B1 ----------------
    "b1-write-email": W(
        "Напиши неформален имейл до приятел: разкажи новина и го покани да дойде на гости.",
        "Hi Sam, how are you? Guess what, I've got a new job! I started last Monday and I love it. Why don't you come and visit next month? We could go hiking. Write soon, Kalin",
        ["Неформално начало", "Новина (Present Perfect или Past Simple)", "Покана с Why don't you...?", "Неформален край"],
    ),
    "b1-write-article": W(
        "Напиши начало на статия за списание на тема „Най-доброто хоби“. Започни с въпрос към читателя.",
        "Have you ever lost track of time doing something you love? For me, it's photography. A year ago I bought an old camera, and now I can't leave home without it.",
        ["Въпрос към читателя в началото", "Личен пример", "Неформален, жив стил"],
    ),
    "b1-write-enquiry": W(
        "Напиши имейл до хотел: питаш за свободни стаи и дали има паркинг. Не знаеш името на получателя.",
        "Dear Sir or Madam, I would like to know whether you have a double room available from 3 to 6 May. Could you also tell me if there is parking at the hotel? Yours faithfully, Maria Ivanova",
        ["Dear Sir or Madam / Yours faithfully", "Непреки въпроси (whether, if)", "Конкретни дати", "Учтив тон"],
    ),
    "b1-write-for-against": W(
        "Напиши кратко есе „за и против“: Добре ли е децата да имат телефон?",
        "On the one hand, a phone helps children stay in touch with their parents. On the other hand, they may spend too much time on social media. In my opinion, children should have a phone, but with clear rules.",
        ["On the one hand / On the other hand", "Поне по един аргумент за и против", "Мнение в края"],
    ),
    "b1-write-apology": W(
        "Напиши имейл с извинение до приятел, защото си забравил/а за срещата ви.",
        "Hi Dani, I'm so sorry I forgot about our coffee yesterday. I had a crazy day at work and it completely slipped my mind. I should have checked my calendar. Can we meet on Friday instead? My treat!",
        ["Извинение в началото", "Кратко обяснение", "should have + 3-та форма", "Предложение за поправяне"],
    ),
    # ---------------- B2 ----------------
    "b2-write-formal-email": W(
        "Напиши официално оплакване до онлайн магазин: поръчката ти е пристигнала повредена.",
        "Dear Sir or Madam, I am writing to complain about order 5521, which arrived yesterday. Unfortunately, the lamp was badly damaged. I would be grateful if you could send a replacement or a full refund. Yours faithfully, P. Georgiev",
        ["I am writing to complain about...", "Конкретни факти (номер, дата, проблем)", "Учтиво искане: I would be grateful if...", "Без съкращения"],
    ),
    "b2-write-review": W(
        "Напиши кратка рецензия за филм или сериал: представи го, оцени го и кажи на кого го препоръчваш.",
        "If you enjoy clever crime stories, 'The Lake House' is well worth watching. The acting is excellent and the twist at the end is genuinely surprising. The only drawback is the slow first episode. Overall, I'd highly recommend it.",
        ["Представяне и за кого е", "Конкретна похвала", "Една балансирана критика", "Ясна препоръка"],
    ),
    "b2-write-application": W(
        "Напиши кратко мотивационно писмо за летен стаж в туристическа агенция.",
        "Dear Mr Hill, I am writing to apply for the summer internship advertised on your website. I am studying tourism and I have worked as a volunteer guide for a year. I believe I would be well suited to the role. I look forward to hearing from you. Yours sincerely, Ana Petrova",
        ["За коя позиция и откъде знаеш", "Опит с Present Perfect", "Защо си подходящ", "Dear Mr... / Yours sincerely"],
    ),
    "b2-write-advice-email": W(
        "Приятел пише, че е много стресиран преди изпит. Отговори със съвети.",
        "Hi Leo, sorry to hear you're so stressed. If I were you, I'd make a simple study plan and take short breaks. It might also be worth going for a walk every day. Have you thought about studying with a friend? Good luck!",
        ["Съчувствие в началото", "If I were you, I'd...", "It might be worth + -ing", "Топъл край"],
    ),
    "b2-write-essay": W(
        "Напиши кратко есе с мнение: Трябва ли градският транспорт да е безплатен?",
        "Free public transport is an attractive idea, and I believe it would benefit most cities. Firstly, it would reduce traffic and pollution. Some argue that it is too expensive. However, the savings on roads and health could cover much of the cost.",
        ["Позиция в увода", "Аргумент с Firstly", "Противоположно мнение и отговор (However)"],
    ),
    # ---------------- C1 ----------------
    "c1-write-essay": W(
        "Напиши абзац от есе: Трябва ли университетското образование да е безплатно? Включи отстъпка и контрааргумент.",
        "Admittedly, free tuition places a significant burden on public finances. Nevertheless, a well-educated population ultimately generates more tax revenue and innovation, which suggests that the investment pays for itself over time.",
        ["Отстъпка (Admittedly / Granted)", "Контрааргумент (Nevertheless / However)", "Предпазлив език (suggests, may)", "Официален стил"],
    ),
    "c1-write-report": W(
        "Напиши раздела „Препоръки“ от доклад за подобряване на офиса въз основа на анкета.",
        "Recommendations: In light of the survey results, it is recommended that the company introduce flexible working hours. Furthermore, the meeting rooms should be equipped with better video equipment, as this was the most common complaint.",
        ["Подзаглавие", "It is recommended that + основна форма", "Безличен, официален стил", "Връзка с данните"],
    ),
    "c1-write-proposal": W(
        "Напиши кратко предложение до ръководството: въвеждане на един ден работа от вкъщи седмично.",
        "This proposal outlines a plan to allow staff to work from home one day a week. A recent survey shows that 70% of employees would welcome this. It would reduce commuting time and could improve productivity. I recommend a three-month trial.",
        ["Цел (This proposal outlines...)", "Факти в подкрепа", "Ползи с would / could", "Конкретна препоръка"],
    ),
    "c1-write-profile": W(
        "Напиши кратък професионален профил за CV или LinkedIn.",
        "Software developer with five years' experience building web applications for retail clients. Led the redesign of an online store that increased mobile sales by 25%. Fluent in English, with a strong interest in accessibility.",
        ["Кой си, без I в началото", "Силен глагол + резултат с число", "Без клишета", "Кратко"],
    ),
    "c1-write-decline": W(
        "Колега те моли да поемеш допълнителен проект. Откажи учтиво и предложи алтернатива.",
        "Thanks for thinking of me for this project. Unfortunately, I'm not in a position to take it on right now, as I'm committed to the client launch until June. That said, I'd be happy to share my notes with whoever leads it.",
        ["Благодарност преди отказа", "Ясен, но учтив отказ", "Кратка причина", "Алтернатива (That said,...)"],
    ),
    # ---------------- C2 ----------------
    "c2-write-summary": W(
        "Обобщи в 2-3 изречения основната идея на статия, която си чел/а наскоро. Използвай свои думи.",
        "The article argues that remote work has reshaped cities more than offices. While it has benefited many employees, the author warns that it has deepened inequality between those who can work from home and those who cannot.",
        ["Основната идея, без подробности", "Свои думи, не цитати", "Глагол за отчитане (argues, warns, suggests)", "Без лично мнение"],
    ),
    "c2-write-opinion": W(
        "Напиши начало на статия с позиция: Трябва ли да има ден без телефони всяка седмица?",
        "We check our phones, on average, more than a hundred times a day. It is tempting to call this convenience. Yet a weekly day without screens may be the simplest way to reclaim our attention.",
        ["Силно, конкретно начало", "Общото мнение, което оспорваш", "Ясна позиция (Yet...)"],
    ),
    "c2-write-review-critical": W(
        "Напиши балансиран абзац от критична рецензия за книга, филм или изложба.",
        "There is no denying the director's visual ambition; every frame could hang in a gallery. Where the film falters, however, is in its dialogue, which rarely rises above cliché. Watch it for the images; forgive it the script.",
        ["Силна похвала (There is no denying...)", "Критика с акцент (Where... is...)", "Запомнящ се край"],
    ),
    "c2-write-letter-editor": W(
        "Напиши писмо до редактора в отговор на статия, с която отчасти не си съгласен/на.",
        "Sir, your recent editorial on cycling lanes raised valid points, if somewhat selectively. While I share the concern about traffic, it seems unfair to blame cyclists. The question is not whether we build lanes, but where. Yours faithfully, D. Koleva",
        ["Учтива критика с отстъпка", "While I share..., it seems...", "Преформулиране на дебата", "Sir, / Yours faithfully"],
    ),
}
