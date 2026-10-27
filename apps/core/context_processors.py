from django.conf import settings


def site(request):
    return {
        "SITE_NAME": settings.SITE_NAME,
        "OPERATOR_NAME": settings.OPERATOR_NAME,
        "CONTACT_EMAIL": settings.CONTACT_EMAIL,
    }
