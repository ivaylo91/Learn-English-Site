from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "Говори: администрация"
admin.site.site_title = "Говори"
admin.site.index_title = "Съдържание и потребители"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls")),
    path("accounts/", include("apps.accounts.urls")),
    path("courses/", include("apps.courses.urls")),
    path("vocabulary/", include("apps.vocabulary.urls")),
    path("placement-test/", include("apps.placement.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
