"""Color themes for levels, lesson kinds and topics.

Class strings are written out in full so the Tailwind scanner finds them.
Each theme has:
  solid  - filled badge/tile (white text)
  soft   - tinted chip with readable text in both modes
  text   - accent text color
  hover  - border color on hover for cards
  bar    - progress bar fill
  glow   - gradient for big decorative tiles
"""

THEMES = {
    "emerald": {
        "solid": "bg-emerald-700 text-white",
        "soft": "bg-emerald-100 text-emerald-800 dark:bg-emerald-500/15 dark:text-emerald-300",
        "text": "text-emerald-600 dark:text-emerald-400",
        "hover": "hover:border-emerald-400 dark:hover:border-emerald-500",
        "bar": "bg-emerald-500",
        "glow": "from-emerald-600 to-teal-600",
    },
    "sky": {
        "solid": "bg-sky-700 text-white",
        "soft": "bg-sky-100 text-sky-800 dark:bg-sky-500/15 dark:text-sky-300",
        "text": "text-sky-600 dark:text-sky-400",
        "hover": "hover:border-sky-400 dark:hover:border-sky-500",
        "bar": "bg-sky-500",
        "glow": "from-sky-600 to-blue-600",
    },
    "violet": {
        "solid": "bg-violet-600 text-white",
        "soft": "bg-violet-100 text-violet-800 dark:bg-violet-500/15 dark:text-violet-300",
        "text": "text-violet-600 dark:text-violet-400",
        "hover": "hover:border-violet-400 dark:hover:border-violet-500",
        "bar": "bg-violet-500",
        "glow": "from-violet-600 to-purple-600",
    },
    "amber": {
        "solid": "bg-amber-400 text-amber-950 dark:bg-amber-400 dark:text-amber-950",
        "soft": "bg-amber-100 text-amber-800 dark:bg-amber-500/15 dark:text-amber-300",
        "text": "text-amber-600 dark:text-amber-400",
        "hover": "hover:border-amber-400 dark:hover:border-amber-500",
        "bar": "bg-amber-400",
        "glow": "from-amber-600 to-orange-600",
    },
    "rose": {
        "solid": "bg-rose-600 text-white",
        "soft": "bg-rose-100 text-rose-800 dark:bg-rose-500/15 dark:text-rose-300",
        "text": "text-rose-600 dark:text-rose-400",
        "hover": "hover:border-rose-400 dark:hover:border-rose-500",
        "bar": "bg-rose-500",
        "glow": "from-rose-600 to-pink-600",
    },
    "indigo": {
        "solid": "bg-indigo-600 text-white",
        "soft": "bg-indigo-100 text-indigo-800 dark:bg-indigo-500/15 dark:text-indigo-300",
        "text": "text-indigo-600 dark:text-indigo-400",
        "hover": "hover:border-indigo-400 dark:hover:border-indigo-500",
        "bar": "bg-indigo-500",
        "glow": "from-indigo-600 to-violet-600",
    },
    "orange": {
        "solid": "bg-orange-700 text-white",
        "soft": "bg-orange-100 text-orange-800 dark:bg-orange-500/15 dark:text-orange-300",
        "text": "text-orange-600 dark:text-orange-400",
        "hover": "hover:border-orange-400 dark:hover:border-orange-500",
        "bar": "bg-orange-500",
        "glow": "from-orange-600 to-red-600",
    },
    "teal": {
        "solid": "bg-teal-700 text-white",
        "soft": "bg-teal-100 text-teal-800 dark:bg-teal-500/15 dark:text-teal-300",
        "text": "text-teal-600 dark:text-teal-400",
        "hover": "hover:border-teal-400 dark:hover:border-teal-500",
        "bar": "bg-teal-500",
        "glow": "from-teal-600 to-cyan-700",
    },
}

COLOR_CHOICES = [(name, name) for name in THEMES]

LEVEL_COLORS = {"A1": "emerald", "A2": "sky", "B1": "violet", "B2": "amber", "C1": "rose", "C2": "indigo"}

# kind -> (color, Font Awesome icon)
LESSON_KINDS = {
    "grammar": ("violet", "fa-spell-check"),
    "vocabulary": ("amber", "fa-book"),
    "conversation": ("sky", "fa-comments"),
    "reading": ("emerald", "fa-book-open-reader"),
    "listening": ("rose", "fa-headphones"),
    "pronunciation": ("teal", "fa-microphone-lines"),
    "speaking": ("indigo", "fa-microphone"),
    "writing": ("orange", "fa-pen-nib"),
}


def theme(color):
    return THEMES.get(color, THEMES["teal"])
