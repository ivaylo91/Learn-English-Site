"""Typical mistakes of Bulgarian speakers, shown as cards under the lesson theory.

lesson slug -> [(wrong, right, why)]. Most come from Bulgarian interference: articles at the end of
the word, the dropped subject, the present tense where English uses the present perfect, and so on.
"""

MISTAKES = {
    "a1-greetings": [
        ("Good night! Nice to meet you.", "Good evening! Nice to meet you.", "Good night е само за раздяла или преди сън. При среща вечер: Good evening."),
        ("Nice to meet you again.", "Nice to see you again.", "Meet е за първа среща. Когато се виждате пак: see."),
    ],
    "a1-verb-to-be": [
        ("I am agree with you.", "I agree with you.", "Agree е глагол сам по себе си. „Съгласен съм“ не е I am agree."),
        ("Is cold today.", "It is cold today.", "В английския подлогът е задължителен. За времето използваме it."),
        ("He is doctor.", "He is a doctor.", "Пред професия в единствено число слагаме a или an."),
    ],
    "a1-numbers": [
        ("I have 25 years.", "I am 25.", "Възрастта се казва с to be, а не с have."),
        ("thirteen = 30", "thirteen = 13, thirty = 30", "13 е с ударение в края (thirTEEN), 30 в началото (THIRty)."),
    ],
    "a1-articles": [
        ("I am teacher.", "I am a teacher.", "Български няма неопределен член, но английският го изисква."),
        ("The life is beautiful.", "Life is beautiful.", "За неща по принцип (живот, любов, музика) не слагаме the."),
        ("I play guitar in the evening.", "I play the guitar in the evening.", "С музикални инструменти обикновено се използва the."),
    ],
    "a1-plural-nouns": [
        ("I have two childs.", "I have two children.", "Child е неправилно съществително: children."),
        ("The informations are useful.", "The information is useful.", "Information, advice, news нямат множествено число в английския."),
    ],
    "a1-present-simple": [
        ("She work in a bank.", "She works in a bank.", "С he, she, it глаголът получава -s."),
        ("Does he likes coffee?", "Does he like coffee?", "След does глаголът е без -s."),
        ("I not like fish.", "I don't like fish.", "Отрицанието изисква don't или doesn't."),
    ],
    "a2-was-were": [
        ("I am born in 1990.", "I was born in 1990.", "На български казваме „роден съм“, но на английски е минало време: was born."),
        ("We was at home.", "We were at home.", "С we, you, they: were."),
    ],
    "a2-past-simple-regular": [
        ("Did you watched the film?", "Did you watch the film?", "След did глаголът е в основна форма."),
        ("I have seen him yesterday.", "I saw him yesterday.", "С yesterday, ago, last week използваме Past Simple."),
    ],
    "a2-irregular-verbs": [
        ("I goed to the shop.", "I went to the shop.", "Go е неправилен глагол: went."),
        ("She buyed a dress.", "She bought a dress.", "Buy, bought, bought."),
    ],
    "a2-asking-directions": [
        ("Where is the station? Tell me!", "Excuse me, could you tell me where the station is?", "Учтивият въпрос звучи по-естествено. В него редът е the station is."),
    ],
    "a2-at-the-restaurant": [
        ("I want a coffee.", "I'd like a coffee, please.", "I want звучи грубо, когато поръчваш. I'd like е учтивото."),
        ("Can I have the account?", "Can I have the bill, please?", "Сметката в ресторант е the bill (в САЩ the check)."),
    ],
    "b1-present-perfect": [
        ("I live here for five years.", "I have lived here for five years.", "Когато нещо продължава от минало до сега, английският използва Present Perfect, не сегашно време."),
        ("I have been in London last year.", "I was in London last year.", "Конкретно минало време (last year) изисква Past Simple."),
        ("How long are you married?", "How long have you been married?", "„Откога“ се пита с Present Perfect."),
    ],
    "b1-modals-advice": [
        ("You should to see a doctor.", "You should see a doctor.", "След should, must, can няма to."),
        ("You mustn't come tomorrow. (не е нужно)", "You don't have to come tomorrow.", "Mustn't е забрана. „Не е нужно“ е don't have to."),
    ],
    "b1-will-going-to": [
        ("I will to call you.", "I will call you.", "След will глаголът е без to."),
        ("Look at the clouds! It will rain.", "Look at the clouds! It's going to rain.", "Когато виждаш признаците сега, по-естествено е going to."),
    ],
    "b1-first-conditional": [
        ("If it will rain, we'll stay at home.", "If it rains, we'll stay at home.", "След if не използваме will за бъдещето."),
        ("When I will finish, I'll call you.", "When I finish, I'll call you.", "Същото важи за when, as soon as, before, after."),
    ],
    "b2-second-conditional": [
        ("If I would have money, I would buy it.", "If I had money, I would buy it.", "Would не стои в частта с if."),
        ("If I was you...", "If I were you...", "В този израз се използва were, особено в писмен език."),
    ],
    "b2-passive-voice": [
        ("The house built in 1920.", "The house was built in 1920.", "Страдателният залог изисква be."),
        ("It is speaking English here.", "English is spoken here.", "Българското „се говори“ става страдателен залог: is spoken."),
    ],
    "b2-reported-speech": [
        ("She said me that she was tired.", "She told me that she was tired.", "Tell + човек. Say без човек (или say to me)."),
        ("He asked where did I live.", "He asked where I lived.", "В непряк въпрос редът е като в утвърдително изречение."),
    ],
    "c1-third-mixed-conditionals": [
        ("If I would have known, I would have come.", "If I had known, I would have come.", "В частта с if: had + причастие."),
        ("I would of helped you.", "I would have helped you.", "Would of е правописна грешка заради произношението would've."),
    ],
    "c1-inversion": [
        ("Never I have seen such a view.", "Never have I seen such a view.", "След never в началото: спомагателен глагол + подлог."),
        ("Not only she sings, but she also dances.", "Not only does she sing, but she also dances.", "Not only в началото изисква инверсия с do/does/did."),
    ],
    "c1-phrasal-verbs-work": [
        ("We need to postpone it back.", "We need to put it off.", "Put off = отлагам. Без back."),
        ("Let's discuss about the budget.", "Let's discuss the budget.", "Discuss е без about. Но talk about е правилно."),
    ],
    "c2-everyday-idioms": [
        ("It's raining cats and dogs. (за тъжен човек)", "He's feeling blue.", "Идиомите имат точно значение. Raining cats and dogs е само за силен дъжд."),
    ],
    "c2-cleft-sentences": [
        ("What I need it is a holiday.", "What I need is a holiday.", "Без it: подлогът вече е изречението с What."),
        ("It was Maria which found the keys.", "It was Maria who found the keys.", "За хора: who или that."),
    ],
    "c2-register": [
        ("Dear Sir, I wanna ask about the job.", "Dear Sir or Madam, I would like to enquire about the position.", "В официално писмо избягвай съкращения като wanna и неформални думи."),
        ("Thanks a lot! Cheers, Ana", "Thank you for your time. Kind regards, Ana Petrova", "Завършекът трябва да е в същия стил като писмото."),
    ],
}
