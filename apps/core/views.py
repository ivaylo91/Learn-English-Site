from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET

from apps.courses.models import Exercise, Lesson, Level
from apps.courses.views import category_counts
from apps.vocabulary.models import Topic, Word

from .metrics import learning_metrics


def site_stats():
    """Real numbers for trust signals (never invented)."""
    return {
        "lessons": Lesson.objects.filter(is_published=True).count(),
        "exercises": Exercise.objects.filter(lesson__is_published=True).count(),
        "words": Word.objects.count(),
        "listening": Lesson.objects.filter(is_published=True, kind=Lesson.Kind.LISTENING).count(),
    }


def home(request):
    if request.user.is_authenticated and request.GET.get("landing") is None:
        return redirect("accounts:dashboard")
    context = {
        "stats": site_stats(),
        "categories": category_counts(list(Lesson.objects.filter(is_published=True).only("id", "kind")), set()),
        "levels": Level.objects.all(),
        "travel_topics": Topic.objects.filter(is_travel=True)[:6],
        "listening_lessons": Lesson.objects.filter(is_published=True, kind=Lesson.Kind.LISTENING)
        .select_related("unit__level")[:4],
    }
    return render(request, "core/home.html", context)


@staff_member_required
def metrics(request):
    return render(request, "core/metrics.html", learning_metrics())


@require_GET
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Disallow: /accounts/",
        "Disallow: /staff/",
        "Disallow: /vocabulary/review/",
        "Disallow: /vocabulary/my-words/",
        f"Sitemap: {request.build_absolute_uri(reverse('sitemap'))}",
    ]
    return HttpResponse("\n".join(lines) + "\n", content_type="text/plain")


FAQ = [
    ("Наистина ли е безплатно?",
     "Да. Всички уроци, упражнения, речникът и тестът за ниво са безплатни. В бъдеще може да има допълнителни "
     "премиум функции, но сегашното съдържание остава безплатно."),
    ("Откъде да започна?",
     "Направи теста за ниво. Той отнема около 5 минути и ти препоръчва ниво от A1 до C2. Ако си пълен начинаещ, "
     "започни направо от A1."),
    ("Колко време на ден трябва да уча?",
     "Редовността е по-важна от продължителността. 10-15 минути всеки ден дават по-добър резултат от два часа "
     "веднъж седмично, защото паметта се укрепва чрез повторение през интервали."),
    ("Как работи преговорът на думи?",
     "Запазваш думи от речника. Всяка дума се връща за преговор точно когато започваш да я забравяш: след 1, 3, 7, "
     "14 и 30 дни. Ако не се сетиш, думата започва отначало."),
    ("Защо сайтът не разпознава гласа ми?",
     "Разпознаването на реч работи в Chrome, Edge и Safari. Браузърът трябва да има достъп до микрофона. "
     "Във Firefox можеш да упражняваш на глас и да потвърдиш сам."),
    ("Мога ли да уча от телефона?",
     "Да. Сайтът е направен за телефон, таблет и компютър. Можеш да го добавиш към началния екран като приложение."),
    ("Как да изтрия профила си?",
     "От Настройки, най-долу, „Изтрий профила“. Всички твои данни се изтриват веднага и окончателно."),
]


def about(request):
    return render(request, "core/about.html", {"stats": site_stats(), "levels": Level.objects.all()})


def faq(request):
    return render(request, "core/faq.html", {"faq": FAQ})


def page(request, template):
    return render(request, template)
