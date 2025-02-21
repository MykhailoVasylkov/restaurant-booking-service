from django.test import TestCase
from menu.models import Dish, Category
from decimal import Decimal


class CategoryModelTests(TestCase):
    
    def setUp(self):
        """Create test categories for later use."""
        self.category_1 = Category.objects.create(name="Category 1", order=1)
        self.category_2 = Category.objects.create(name="Category 2", order=2)
        self.category_3 = Category.objects.create(name="Category 3", order=0)

    def test_category_creation(self):
        """Test the creation of categories."""
        category = Category.objects.create(name="Category 4", order=3)
        self.assertEqual(category.name, "Category 4")
        self.assertEqual(category.order, 3)

    def test_category_str_method(self):
        """Test the __str__ method of the Category model."""
        self.assertEqual(str(self.category_1), "Category 1")
        self.assertEqual(str(self.category_2), "Category 2")
        self.assertEqual(str(self.category_3), "Category 3")

    def test_category_ordering(self):
        """Test that categories are ordered by the `order` field."""
        categories = Category.objects.all()
        self.assertEqual(list(categories), [self.category_3, self.category_1, self.category_2])

    def test_category_default_order(self):
        """Test the default value of the `order` field."""
        category = Category.objects.create(name="Category 5")
        self.assertEqual(category.order, 0)  # Default value

    def test_category_order_update(self):
        """Test updating the `order` field."""
        self.category_1.order = 5
        self.category_1.save()
        updated_category = Category.objects.get(pk=self.category_1.pk)
        self.assertEqual(updated_category.order, 5)

    def test_category_ordering_after_update(self):
        """Test that the ordering is correct after an update to the `order` field."""
        self.category_2.order = 0
        self.category_2.save()

        categories = Category.objects.all()
        self.assertEqual(list(categories), [self.category_2, self.category_3, self.category_1])


class DishModelTest(TestCase):
    
    def setUp(self):
        """Create a test category and a dish."""
        self.category = Category.objects.create(name="Appetizers", order=1)
        self.dish = Dish.objects.create(
            name="Test Dish",
            description="A delicious test dish.",
            price=Decimal("9.99"),
            currency="EUR",
            category=self.category,
            status="available",
            publishing_status=1,
            order=1
        )
    
    def test_dish_creation(self):
        """Test that the dish is correctly created."""
        self.assertEqual(self.dish.name, "Test Dish")
        self.assertEqual(self.dish.description, "A delicious test dish.")
        self.assertEqual(self.dish.price, Decimal("9.99"))
        self.assertEqual(self.dish.currency, "EUR")
        self.assertEqual(self.dish.category, self.category)
        self.assertEqual(self.dish.status, "available")
        self.assertEqual(self.dish.publishing_status, 1)
        self.assertEqual(self.dish.order, 1)
    
    def test_price_with_currency(self):
        """Test that the price is displayed with the correct currency symbol."""
        self.assertEqual(self.dish.price_with_currency(), "€9.99")
    
    def test_dish_str_representation(self):
        """Test the string representation of the dish."""
        self.assertEqual(str(self.dish), "Test Dish")
