"""The five learning categories shown to learners.

Lessons keep their detailed kind in the database; each kind belongs to exactly one category.
"""

from apps.core.theme import theme

CATEGORIES = {
    "listening": {
        "label": "Слушане", "label_en": "Listening", "icon": "fa-headphones", "color": "rose",
        "kinds": ["listening", "pronunciation", "speaking"],
        "summary": "Диалози, произношение и говорене на глас.",
    },
    "reading": {
        "label": "Четене", "label_en": "Reading", "icon": "fa-book-open-reader", "color": "emerald",
        "kinds": ["reading"],
        "summary": "Кратки текстове по нива с речник и въпроси.",
    },
    "writing": {
        "label": "Писане", "label_en": "Writing", "icon": "fa-pen-nib", "color": "orange",
        "kinds": ["writing"],
        "summary": "Бележки, имейли, есета и резюмета по модел.",
    },
    "grammar": {
        "label": "Граматика", "label_en": "Grammar", "icon": "fa-spell-check", "color": "violet",
        "kinds": ["grammar"],
        "summary": "Правилата, обяснени на български, с упражнения.",
    },
    "vocabulary": {
        "label": "Речник", "label_en": "Vocabulary", "icon": "fa-book", "color": "amber",
        "kinds": ["vocabulary", "conversation"],
        "summary": "Думи, изрази и фрази за ежедневни разговори.",
    },
}

KIND_TO_CATEGORY = {kind: key for key, cat in CATEGORIES.items() for kind in cat["kinds"]}


def category(key):
    """Category dict with its key and color theme merged in."""
    cat = CATEGORIES[key]
    return {**cat, "key": key, **theme(cat["color"])}


def category_for_kind(kind):
    return category(KIND_TO_CATEGORY.get(kind, "grammar"))


def all_categories():
    return [category(key) for key in CATEGORIES]
