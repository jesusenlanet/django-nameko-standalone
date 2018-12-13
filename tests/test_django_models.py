import sys
from unittest import TestCase
import django
from mock import Mock

from django_nameko_standalone import DjangoModels


class DjangoModelsTest(TestCase):
    def setUp(self):
        self.django_models = DjangoModels()

    def test_django_models_setup(self):
        sys.modules['django'] = Mock()
        mock_django = sys.modules['django']

        self.django_models.setup()
        self.assertTrue(mock_django.setup.called)
        self.assertEqual(mock_django.setup.call_count, 1)

    def test_django_models_get_dependency(self):
        from types import ModuleType

        class fake_module:
            pass

        fake_module = ModuleType("fake_module")

        mock_apps = Mock()
        mock_conf = Mock()

        fake_module.apps = mock_apps
        sys.modules['django.apps'] = fake_module

        mock_conf.DJANGO_NAMEKO_STANDALONE_APPS = ('app1', 'app2')
        fake_module.settings = mock_conf
        sys.modules['django.conf'] = fake_module

        config_1 = Mock()
        items_1 = (('app1_model', Mock(models=Mock(items=Mock(return_value=('App1', Mock()))))),)
        config_1.models.items.return_value = items_1

        config_2 = Mock()
        items_2 = (('app2_model', Mock(models=Mock(items=Mock(return_value=('App2', Mock()))))),)
        config_2.models.items.return_value = items_2

        apps_config = [config_1, config_2]

        mock_apps.get_app_config.side_effect = apps_config

        models = self.django_models.get_dependency(Mock())

        self.assertEqual(models.App1_model, items_1[0][1])
        self.assertEqual(models.App2_model, items_2[0][1])

    def test_django_worker_teardown(self):
        from types import ModuleType

        class fake_module:
            pass

        mock_connections = Mock()
        fake_module = ModuleType("fake_module")
        fake_module.connections = mock_connections
        sys.modules['django.db'] = fake_module

        self.django_models.worker_teardown(Mock())
        self.assertTrue(mock_connections.close_all.called)
        self.assertEqual(mock_connections.close_all.call_count, 1)
