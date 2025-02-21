from django.test import TestCase
from django.urls import resolve, reverse
from menu.views import menu_by_category

class MenuURLPatternsTest(TestCase):

    def test_menu_by_category_url_resolves(self):
        """Test that 'menu/' resolves to menu_by_category view"""
        resolver = resolve(reverse('menu'))
        self.assertEqual(resolver.func, menu_by_category, msg="URL 'menu/' should call menu_by_category view")
