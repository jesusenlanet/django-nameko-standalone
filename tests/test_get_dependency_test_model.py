import os
from unittest import TestCase

from django.db.models.base import ModelBase

from django_nameko_standalone import DjangoModels


class GetDependencyLoadingTestModelTestCase(TestCase):
    def setUp(self):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_settings")
        os.environ.setdefault("DJANGO_NAMEKO_STANDALONE_SETTINGS_MODULE", "test_settings")
        self.django_models = DjangoModels()
        self.django_models.setup()

    def test_get_dependency_loading_test_model_capitalized_fail(self):
        models = self.django_models.get_dependency(None)
        with self.assertRaises(AttributeError):
            models.Mytestmodel

    def test_get_dependency_loading_test_model_camel_case(self):
        models = self.django_models.get_dependency(None)
        self.assertTrue(models.MyTestModel)
        self.assertIsInstance(models.MyTestModel, ModelBase)

    def test_get_dependency_loading_test_model_uppercase_fail(self):
        models = self.django_models.get_dependency(None)
        with self.assertRaises(AttributeError):
            models.MYTESTMODEL
