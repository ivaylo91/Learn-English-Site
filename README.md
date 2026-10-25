# Говори: английски на български

A free English course for Bulgarian speakers, from A1 to C2, with a travel phrasebook. Built with Django, Tailwind CSS v4 (standalone CLI, no Node), Font Awesome Free and Supabase Postgres.

The product plan and roadmap are in [docs/PLAN.md](docs/PLAN.md).

## Quick start (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\pip install -r requirements.txt
Copy-Item .env.example .env          # edit if needed
.\.venv\Scripts\python manage.py migrate
.\.venv\Scripts\python manage.py seed_content
.\.venv\Scripts\python manage.py createsuperuser
.\.venv\Scripts\python manage.py tailwind runserver
```

`tailwind runserver` runs Django and the Tailwind watcher together. The first run downloads the Tailwind CLI binary into `.django_tailwind_cli/`.

Open http://127.0.0.1:8000. The admin is at `/admin/`.

## Using Supabase

1. Create a project at supabase.com.
2. Open **Connect** and copy the **Session pooler** connection string (port `5432`). Do not use the transaction pooler (`6543`); it breaks Django's prepared statements.
3. Put it in `.env` as `DATABASE_URL=postgresql://postgres.<ref>:<password>@<host>:5432/postgres`.
4. Run `migrate` and `seed_content` again.

With `DATABASE_URL` empty the site uses local SQLite.

## Project layout

| Path | What |
|---|---|
| `config/` | settings and root URLs |
| `apps/core/` | landing page, seed data (`apps/core/seed/`), `seed_content` command |
| `apps/accounts/` | email-login user, XP, streak, plan (free/premium), dashboard |
| `apps/courses/` | levels, units, lessons, exercises, progress, server-side grading |
| `apps/vocabulary/` | word topics, travel phrasebook, flashcards |
| `apps/placement/` | placement test |
| `templates/` | Django templates |
| `frontend/tailwind.css` | Tailwind source (theme tokens, component classes) |
| `assets/` | static files: built CSS, JS |

## Content

- Edit lessons, exercises, topics and test questions in the admin.
- `seed_content` loads the starter content from `apps/core/seed/`. It is safe to run again, but it **replaces the exercises, words and placement questions** of the seeded items, so run it only before you start editing that content in the admin.
- Lesson theory is HTML. Useful classes: `<span class="en">` for English examples, `<div class="tip">` for a tip box, plain `<table>`, `<h3>`, `<ul>`.
- Exercise types: `choice` (add choices, mark the correct one), `fill` (use `___` in the prompt), `translate`, `dictation`. Several accepted answers are separated with `|`. Checking ignores case, punctuation and curly apostrophes.
- Any exercise with **audio text** plays it to the learner (browser speech). For `dictation` the audio text is also the correct answer.

### Audio (listening) lessons

- Set the lesson kind to **Слушане**. They are listed at `/courses/listening/`.
- **Dialogue**: one line per reply, `Speaker | English | Bulgarian`. The page plays it with two voices, at normal or slow speed, with the transcript and translation hidden until the learner opens them.
- **Audio file** (optional): upload an MP3 to use a real recording instead of the browser voice. Files go to `media/` locally; move them to Supabase Storage before production.

### Word review (spaced repetition)

Learners save words from any topic (bookmark icon) into "Моите думи". `/vocabulary/review/` shows due cards; a remembered word moves up a Leitner box (1, 3, 7, 14, 30 days), a forgotten one goes back to box 1. Only due words give XP. `seed_content` updates words in place, so saved words survive a reseed.

### Exercise type: word order

`order`: the prompt is the Bulgarian sentence, the first accepted answer is the English sentence without punctuation. The learner taps shuffled word tiles to build it.

### Colors

Level, lesson-kind and topic colors live in `apps/core/theme.py`. Topics have a `color` field in the admin.

## Premium (later)

`User.plan`, `User.premium_until`, `Lesson.is_premium` and `Topic.is_premium` already exist. Marking content premium shows a locked page for free users. Payments are not built yet.

## Tests

```powershell
.\.venv\Scripts\python manage.py test
```

## Production checklist

- `DEBUG=False`, a real `SECRET_KEY`, `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`.
- `python manage.py tailwind build` then `python manage.py collectstatic`.
- Serve with gunicorn; WhiteNoise serves static files.
