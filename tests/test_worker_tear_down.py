import os
from unittest import TestCase

from mock import Mock, patch, call

from django_nameko_standalone import DjangoModels


class TearDownTestCase(TestCase):
    def setUp(self):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_settings")
        os.environ.setdefault("DJANGO_NAMEKO_STANDALONE_SETTINGS_MODULE", "test_settings")
        self.django_models = DjangoModels()

    @patch('django.db.connections')
    def test_worker_tear_down(self, mock_connections):
        self.django_models.worker_teardown(None)
        self.assertTrue(mock_connections.close_all.called)
        self.assertEqual(mock_connections.close_all.call_count, 1)
        self.assertEqual(mock_connections.close_all.call_args, call())
