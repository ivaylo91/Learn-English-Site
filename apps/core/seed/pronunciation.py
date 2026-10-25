"""Pronunciation lessons built on minimal pairs: the sounds Bulgarian speakers find hardest."""

from .courses import C, D, L

HEAR = "Коя дума чу?"


def pron_unit(level, slug, lessons):
    return {"level": level, "title": "Произношение", "slug": slug, "icon": "fa-microphone-lines", "order": 8,
            "summary": "Звуковете, които българите бъркат най-често.", "lessons": lessons}


UNITS = [
    pron_unit("A1", "a1-pronunciation", [
        {
            "slug": "a1-pron-th", "title": "Звукът th", "title_en": "The th sounds", "kind": "pronunciation",
            "minutes": 6, "xp": 15, "summary": "Think, this, three: звукът, който го няма в българския.",
            "theory": """
<p>В английския има два звука, изписвани с <strong>th</strong>, и нито един от тях не съществува в българския. Затова често ги заменяме със <em>с, ф, т</em> или <em>з, д</em>. Понякога това променя думата: <span class="en">think</span> (мисля) става <span class="en">sink</span> (мивка).</p>
<h3>Как се произнася</h3>
<ul>
<li>Сложи върха на езика <strong>леко между зъбите</strong>.</li>
<li>Издухай въздух покрай езика. Не докосвай устните.</li>
<li><strong>Беззвучен</strong> /θ/ (като „с“, но с езика между зъбите): <span class="en">think, three, thank, bath</span></li>
<li><strong>Звучен</strong> /ð/ (като „з“, но с езика между зъбите): <span class="en">this, they, mother, then</span></li>
</ul>
<h3>Минимални двойки</h3>
<table>
<tr><th>th</th><th>грешно като</th></tr>
<tr><td class="en">think</td><td class="en">sink</td></tr>
<tr><td class="en">three</td><td class="en">tree</td></tr>
<tr><td class="en">thank</td><td class="en">tank</td></tr>
<tr><td class="en">they</td><td class="en">day</td></tr>
<tr><td class="en">then</td><td class="en">den</td></tr>
</table>
<div class="tip">Натискай бутона за звук до всяка дума в упражненията. Казвай думата на глас веднага след като я чуеш.</div>
""",
            "exercises": [
                L(HEAR, "think", ["think", "sink", "fink"], 0),
                L(HEAR, "three", ["three", "tree", "free"], 0),
                L(HEAR, "they", ["they", "day", "lay"], 0),
                L(HEAR, "tank", ["thank", "tank", "sank"], 1, "Tank (резервоар) започва с обикновено т. Thank е с th."),
                C("Кой звук има в началото на this?", ["Звучен th /ð/", "Беззвучен th /θ/", "Обикновено д"], 0,
                  "This, they, the, mother: звучен th."),
                D("Thank you very much."),
            ],
        },
        {
            "slug": "a1-pron-w-v", "title": "W или V", "title_en": "W and V", "kind": "pronunciation",
            "minutes": 6, "xp": 15, "summary": "Wine или vine? Как да не ги бъркаш.",
            "theory": """
<p>В българския имаме само „в“. В английския <strong>w</strong> и <strong>v</strong> са различни звуци и сменят смисъла: <span class="en">wine</span> (вино) и <span class="en">vine</span> (лоза).</p>
<h3>Как се произнася</h3>
<table>
<tr><th>Звук</th><th>Устни и зъби</th><th>Примери</th></tr>
<tr><td class="en">w</td><td>Устните се закръглят като за „у“ и бързо се отварят. Зъбите не докосват устната.</td><td class="en">we, water, wine, west</td></tr>
<tr><td class="en">v</td><td>Горните зъби леко докосват долната устна, като българското „в“.</td><td class="en">very, vine, vest, love</td></tr>
</table>
<div class="tip">Трик: кажи бързо „уи“ и ще чуеш <span class="en">we</span>. Ако чуваш „ви“, това е грешката.</div>
<h3>Минимални двойки</h3>
<p><span class="en">wine / vine, west / vest, wet / vet, worse / verse</span></p>
""",
            "exercises": [
                L(HEAR, "wine", ["wine", "vine"], 0),
                L(HEAR, "vest", ["west", "vest"], 1),
                L(HEAR, "wet", ["wet", "vet"], 0),
                C("Как се произнася w?", ["Със закръглени устни, като кратко „у“", "Със зъби върху долната устна", "Като българското „в“"], 0),
                D("What do you want?"),
                D("We went to the west coast."),
            ],
        },
    ]),
    pron_unit("A2", "a2-pronunciation", [
        {
            "slug": "a2-pron-vowels", "title": "Кратки и дълги гласни", "title_en": "Short and long vowels",
            "kind": "pronunciation", "minutes": 7, "xp": 20, "summary": "Ship или sheep? Дължината на гласната променя думата.",
            "theory": """
<p>Българските гласни са с приблизително еднаква дължина. В английския <strong>дължината и качеството</strong> на гласната сменят думата.</p>
<table>
<tr><th>Кратка</th><th>Дълга</th><th>Разлика</th></tr>
<tr><td class="en">ship /ɪ/</td><td class="en">sheep /iː/</td><td>кораб / овца</td></tr>
<tr><td class="en">live /ɪ/</td><td class="en">leave /iː/</td><td>живея / тръгвам</td></tr>
<tr><td class="en">sit /ɪ/</td><td class="en">seat /iː/</td><td>седя / седалка</td></tr>
<tr><td class="en">full /ʊ/</td><td class="en">fool /uː/</td><td>пълен / глупак</td></tr>
</table>
<div class="tip">Кратката /ɪ/ е по-отпусната, между българските „и“ и „е“. Дългата /iː/ е като протяжно „ии“ с усмивка.</div>
""",
            "exercises": [
                L(HEAR, "sheep", ["ship", "sheep"], 1),
                L(HEAR, "leave", ["live", "leave"], 1),
                L(HEAR, "full", ["full", "fool"], 0),
                L(HEAR, "sit", ["sit", "seat"], 0),
                L("Какво означава изречението?", "I live here.", ["Живея тук.", "Тръгвам си оттук."], 0),
                D("Please take a seat."),
            ],
        },
        {
            "slug": "a2-pron-final-consonants", "title": "Звучни съгласни в края на думата",
            "title_en": "Voiced final consonants", "kind": "pronunciation", "minutes": 7, "xp": 20,
            "summary": "Bag не е back: защо краят на думата има значение.",
            "theory": """
<p>В българския звучната съгласна в края на думата обеззвучава: пишем „хляб“, казваме „хляп“. В английския това <strong>сменя думата</strong>:</p>
<table>
<tr><th>Звучна</th><th>Беззвучна</th></tr>
<tr><td class="en">bag (чанта)</td><td class="en">back (гръб)</td></tr>
<tr><td class="en">dog (куче)</td><td class="en">dock (пристан)</td></tr>
<tr><td class="en">eyes (очи)</td><td class="en">ice (лед)</td></tr>
<tr><td class="en">prize (награда)</td><td class="en">price (цена)</td></tr>
<tr><td class="en">have</td><td class="en">half</td></tr>
</table>
<div class="tip">Трик: гласната <strong>преди</strong> звучната съгласна е по-дълга. Кажи <span class="en">bag</span> бавно и протяжно, <span class="en">back</span> кратко и рязко.</div>
<p>Същото важи за окончанието <span class="en">-ing</span>: казва се /ɪŋ/ без „к“ накрая. <span class="en">Thinking</span>, а не „тинкинк“.</p>
""",
            "exercises": [
                L(HEAR, "bag", ["bag", "back"], 0),
                L(HEAR, "ice", ["eyes", "ice"], 1),
                L(HEAR, "dog", ["dog", "dock"], 0),
                L(HEAR, "prize", ["prize", "price"], 0),
                C("Защо bag и back звучат различно?", ["Гласната в bag е по-дълга, а g е звучно", "Пишат се еднакво", "Няма разлика"], 0),
                D("I need a new bag."),
            ],
        },
    ]),
]
