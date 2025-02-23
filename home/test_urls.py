from django.test import TestCase
from django.urls import resolve, reverse
from home.views import home_page

"""
I used Chat-GPT to set-up tests
"""


class HomeURLPatternsTest(TestCase):

    def test_home_page_url_resolves(self):
        """Test that ' ' resolves to home_page view"""
        resolver = resolve(reverse('home'))
        self.assertEqual(
            resolver.func, home_page,
            msg="URL ' ' should call home_page view"
        )
