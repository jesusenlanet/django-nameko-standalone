import os
from unittest import TestCase

from django_nameko_standalone import DjangoModels


class SetUpTestCase(TestCase):

    def setUp(self):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_settings")
        os.environ.setdefault("DJANGO_NAMEKO_STANDALONE_SETTINGS_MODULE", "test_settings")
        django_models = DjangoModels()
        django_models.setup()

    def test_set_up(self):
        from django.conf import settings
        self.assertTupleEqual(settings.DJANGO_NAMEKO_STANDALONE_APPS, ("tests",))
        self.assertTupleEqual(settings.INSTALLED_APPS, ("tests",))
        self.assertEqual(settings.SECRET_KEY, '<your_secret_key>')
        self.assertDictEqual(settings.DATABASES, {})
