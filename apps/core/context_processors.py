from django.conf import settings

from apps.courses.categories import all_categories


def site(request):
    return {
        "SITE_NAME": settings.SITE_NAME,
        "OPERATOR_NAME": settings.OPERATOR_NAME,
        "CONTACT_EMAIL": settings.CONTACT_EMAIL,
        "LESSON_CATEGORIES": all_categories(),
    }
