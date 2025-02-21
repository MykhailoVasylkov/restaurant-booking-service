from django.test import TestCase
from django.urls import reverse
from menu.models import Dish, Category
from decimal import Decimal


class MenuByCategoryViewTests(TestCase):

    def setUp(self):
        """Set up test data: categories and dishes"""
        self.category1 = Category.objects.create(name="Starters", order=1)
        self.category2 = Category.objects.create(name="Main Course", order=2)

        # Available dishes
        self.dish1 = Dish.objects.create(
            name="Soup",
            description="Delicious soup",
            price=Decimal("5.99"),
            currency="EUR",
            category=self.category1,
            status="available",
            publishing_status=1,
            order=1
        )
        self.dish2 = Dish.objects.create(
            name="Steak",
            description="Juicy steak",
            price=Decimal("15.99"),
            currency="EUR",
            category=self.category2,
            status="available",
            publishing_status=1,
            order=2
        )

        # Unpublished dish (should not appear)
        self.hidden_dish = Dish.objects.create(
            name="Secret Dish",
            description="Hidden",
            price=Decimal("99.99"),
            currency="EUR",
            category=self.category1,
            status="available",
            publishing_status=0,
            order=3
        )

    def test_menu_by_category_status_code(self):
        """Test that the view returns a 200 status code"""
        response = self.client.get(reverse("menu"))
        self.assertEqual(response.status_code, 200)

    def test_menu_by_category_template_used(self):
        """Test that the correct template is used"""
        response = self.client.get(reverse("menu"))
        self.assertTemplateUsed(response, "menu/menu_page.html")

    def test_menu_by_category_context(self):
        """Test that only published dishes are included and grouped by category"""
        response = self.client.get(reverse("menu"))
        self.assertIn("menu_categories", response.context)

        menu_categories = response.context["menu_categories"]

        # There should be exactly 2 categories (unpublished dishes should be ignored)
        self.assertEqual(len(menu_categories), 2)

        # Check categories are correctly grouped
        self.assertEqual(menu_categories[0]["category"], self.category1)
        self.assertIn(self.dish1, menu_categories[0]["dishes"])
        self.assertNotIn(self.hidden_dish, menu_categories[0]["dishes"])  # Unpublished dish should be absent

        self.assertEqual(menu_categories[1]["category"], self.category2)
        self.assertIn(self.dish2, menu_categories[1]["dishes"])

    def test_menu_by_category_ordering(self):
        """Test that categories and dishes are ordered correctly"""
        response = self.client.get(reverse("menu"))
        menu_categories = response.context["menu_categories"]

        # Categories should be ordered by 'order' field
        self.assertEqual(menu_categories[0]["category"], self.category1)
        self.assertEqual(menu_categories[1]["category"], self.category2)

        # Dishes should be ordered by 'order' field within each category
        self.assertEqual(menu_categories[0]["dishes"][0], self.dish1)
        self.assertEqual(menu_categories[1]["dishes"][0], self.dish2)
