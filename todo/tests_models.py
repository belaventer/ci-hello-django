from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Testing Model Item')
        self.assertFalse(item.done)
        item.delete()

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='Testing Model Item')
        self.assertEqual(str(item), item.name)
