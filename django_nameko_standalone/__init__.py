from nameko.extensions import DependencyProvider


class DjangoModels(DependencyProvider):
    def setup(self):
        """Initialize the dependency"""
        import os
        import django
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
        django.setup()

    def get_dependency(self, worker_ctx):
        """Get the dependency for the concrete service"""
        from service_models import models
        return models

    def worker_teardown(self, worker_ctx):
        """Close all the connections on teardown

        TODO: Autocommit??
        """
        from django.db import connections
        connections.close_all()

__all__ = ["DjangoModels"]
