from django.apps import AppConfig
from django.db.models.signals import post_migrate


def enable_row_level_security(using, **kwargs):
    """Turn on RLS for every table this app's DB role owns in the public schema.

    Supabase exposes the public schema through its REST API. Django connects as the table
    owner, which bypasses RLS, so enabling it with no policies keeps the data private to Django.
    """
    from django.db import connections

    connection = connections[using]
    if connection.vendor != "postgresql":
        return
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT format('ALTER TABLE %I.%I ENABLE ROW LEVEL SECURITY', schemaname, tablename)
            FROM pg_tables
            WHERE schemaname = 'public' AND tableowner = current_user AND NOT rowsecurity
            """
        )
        for (statement,) in cursor.fetchall():
            cursor.execute(statement)


class CoreConfig(AppConfig):
    name = 'apps.core'
    verbose_name = "Основни"

    def ready(self):
        # No sender filter: Django only sends post_migrate for apps with models, and core has none.
        # The handler is idempotent, so running it once per app is harmless.
        post_migrate.connect(enable_row_level_security, dispatch_uid="core.enable_rls")
