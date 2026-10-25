# Learn English Site - Product & Build Plan

Working name: **Говори** (Govori, "speak"). English learning for Bulgarian speakers, A1 to C2, with a dedicated travel track for adults.

## 1. Research summary

What the market leaders do and what we take from them:

| Product | Strength | What we borrow |
|---|---|---|
| Duolingo | Short lessons, streaks, XP, leaderboards | Streaks, XP, daily goal, bite-sized lessons |
| Busuu | CEFR-structured A1-B2 course, explicit grammar | CEFR levels as the backbone, grammar explained in the learner's language |
| BBC Learning English | Free, high quality listening and grammar | Free core content, real-life topics |
| Ella Language / travel courses | Situation-based travel modules (airport, hotel) | Travel phrasebook organised by situation |
| Most apps | English-only or poorly localised UI | **Our gap:** every explanation, hint and UI string in natural Bulgarian |

Positioning: the free, Bulgarian-first course that takes you from zero to confident, with a fast lane for "I travel in three weeks".

Technical findings:
- Django 6.1 runs on Python 3.15 (installed 6.1.2).
- Supabase: Django is a persistent client, so use the **Session pooler** connection string (port 5432, IPv4-friendly). Avoid transaction mode (6543) because it breaks prepared statements/server-side cursors.
- Tailwind v4 without Node: `django-tailwind-cli` downloads the standalone binary. No plugins (no DaisyUI), which is fine.
- Pronunciation audio: browser Web Speech API (`speechSynthesis`, `en-GB`/`en-US`). Free, no audio files to host. Recorded audio can be a premium feature later.

## 2. Audience

- Complete beginners (A1) who need Bulgarian explanations for everything.
- Intermediate learners (B1-B2) who want structure and practice.
- Advanced learners (C1-C2) polishing grammar, idioms and vocabulary.
- Adults preparing to travel: need survival phrases fast, by situation.

## 3. Feature roadmap

### Phase 1 - Foundation (this sprint)
- Project scaffold: Django 6.1, Tailwind v4, Font Awesome Free, env-based config, Supabase-ready DB.
- Bulgarian UI (`LANGUAGE_CODE = "bg"`), light/dark theme, responsive layout.
- Accounts: email sign-up/login, profile with goal, level, XP, streak, plan (free/premium flag ready).
- Course structure: Level (A1-C2) > Unit > Lesson > Exercises.
- Lesson player: Bulgarian theory block, then interactive exercises (multiple choice, fill-in, translate) with instant, server-graded feedback.
- Progress: completed lessons, best score, XP, daily streak.
- Vocabulary topics with flashcards + "listen" button (TTS). Travel topics flagged and shown as the Travel phrasebook.
- Placement test: short multi-level quiz that recommends a starting level.
- Dashboard: continue where you left off, streak, XP, level progress.
- Seed content: A1 + A2 sample units, 6 travel situations, placement questions.
- Django admin configured for content editing.

### Phase 2 - Practice depth
- Spaced repetition review for saved words (Leitner boxes).
- Listening exercises (TTS-driven dictation), word-order exercises.
- Badges and weekly XP leaderboard.
- Full A1-B1 content.
- SEO: sitemap, meta tags, Open Graph, Bulgarian slugs where useful.

### Phase 3 - Premium
- Stripe checkout (BGN/EUR), `plan = premium`, paywall on `is_premium` lessons.
- Premium ideas: recorded native audio, AI conversation partner, speaking feedback, downloadable PDFs, offline travel packs, certificates per level.
- Email reminders for streaks.

### Phase 4 - Scale
- B2-C2 content, exam prep (IELTS/Cambridge).
- PWA install for mobile.

## 4. Architecture

```
config/            settings, urls, wsgi/asgi
apps/core/         landing page, static pages, context processors
apps/accounts/     custom User (email login), profile, onboarding, dashboard
apps/courses/      Level, Unit, Lesson, Exercise, Choice, LessonProgress
apps/vocabulary/   Topic, Word (travel topics = phrasebook)
apps/placement/    PlacementQuestion, PlacementChoice, test flow
templates/         base layout + per-app templates
assets/            Tailwind source CSS, JS, images (STATICFILES_DIRS)
```

Key decisions:
- **Auth:** Django's own auth on the Supabase Postgres database. Supabase is used as managed Postgres. Simpler than Supabase Auth with Django sessions, and keeps the admin working.
- **Grading on the server:** answers are checked by the backend so XP cannot be faked.
- **Anonymous learning allowed:** anyone can open lessons; saving progress needs an account.
- **Premium-ready:** `User.plan` and `Lesson.is_premium` exist from day one; all content is free for now.
- **Content in the DB:** editable from Django admin; seed command loads starter content.

## 5. Environments

- Local: SQLite fallback when `DATABASE_URL` is empty.
- Supabase: set `DATABASE_URL` to the Session pooler URI from Supabase > Connect.
- Production (later): `DEBUG=False`, WhiteNoise for static files, gunicorn, host on Render/Railway/Fly.

## 6. Design direction

- Friendly, clear, trustworthy. Neutral stone palette, one teal accent, light and dark mode.
- Font: Onest (made for Cyrillic and Latin).
- Icons: Font Awesome Free 6.
- Short lessons, big tap targets, mobile-first.
