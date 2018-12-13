import os
from nameko.extensions import DependencyProvider


class DjangoModels(DependencyProvider):
    def setup(self):
        """Initialize the dependency"""
        import django
        if os.environ.get('DJANGO_NAMEKO_STANDALONE_SETTINGS_MODULE'):
            os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.environ.get('DJANGO_NAMEKO_STANDALONE_SETTINGS_MODULE'))
        elif not os.environ.get('DJANGO_SETTINGS_MODULE'):
            os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
        django.setup()

    def get_dependency(self, worker_ctx):
        """Get the dependency for the concrete service"""
        from django.apps import apps
        from django.conf import settings

        apps_config = map(apps.get_app_config, settings.DJANGO_NAMEKO_STANDALONE_APPS)
        models = type('NonExistingClass_', (), {})

        for config in apps_config:
            for name, model in config.models.items():
                setattr(models, name.capitalize(), model)
        return models

    def worker_teardown(self, worker_ctx):
        """Close all the connections on teardown

        TODO: Autocommit??
        """
        from django.db import connections
        connections.close_all()


__all__ = ["DjangoModels"]
