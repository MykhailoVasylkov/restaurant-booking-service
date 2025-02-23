from django.test import TestCase
from django.urls import reverse

"""
I used Chat-GPT to set-up tests
"""


class HomePageViewTests(TestCase):
    def test_home_page_view(self):
        """Test that the home page returns a 200 status code
        and uses the correct template."""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")
