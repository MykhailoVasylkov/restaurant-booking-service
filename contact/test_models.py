from django.test import TestCase
from django.contrib.auth.models import User
from .models import Review
from django.core.exceptions import ValidationError

class ReviewModelTest(TestCase):

    def setUp(self):
        """Create a test user for reviews"""
        self.user = User.objects.create_user(username="admin", password="password123")
  
    def test_review_creation(self):
        """Check the creation of a review"""
        review = Review.objects.create(
            author=self.user,
            rating=5,
            body="Great food!"
        )
        self.assertEqual(review.author, self.user, msg="Review author should match the created user")
        self.assertEqual(review.rating, 5, msg="Rating should be correctly saved as 5")
        self.assertEqual(review.body, "Great food!", msg="Review body should match input")
        self.assertFalse(review.approved, msg="New reviews should not be approved by default")

    def test_review_rating_validation(self):
        """We check that the rating should be between 1 and 5"""
        with self.assertRaises(ValidationError, msg="Rating above 5 should raise a validation error"):
            review = Review(author=self.user, rating=6, body="Too high rating!")
            review.full_clean()

        with self.assertRaises(ValidationError, msg="Rating below 1 should raise a validation error"):
            review = Review(author=self.user, rating=0, body="Too low rating!")
            review.full_clean()

    def test_review_str_method(self):
        """Check the __str__ method"""
        review = Review.objects.create(
            author=self.user,
            rating=4,
            body="Good food"
        )
        self.assertEqual(str(review), "Review by admin - 4⭐", msg="String representation should be 'Review by admin - 4⭐'")

    def test_review_default_values(self):
        """Check default values ​in the model"""
        review = Review.objects.create(
            author=self.user,
            rating=3,
            body="Okay food"
        )
        self.assertEqual(review.approved, False, msg="New reviews should have 'approved' set to False by default")
        self.assertIsNotNone(review.created_on, msg="Created_on timestamp should be automatically set")
        self.assertIsNotNone(review.updated_at, msg="Updated_at timestamp should be automatically set")

    def test_review_ordering(self):
        """We check the correct sorting records"""
        review1 = Review.objects.create(
            author=self.user,
            rating=5,
            body="Excellent food!"
        )
        review2 = Review.objects.create(
            author=self.user,
            rating=4,
            body="Good food"
        )

        reviews = Review.objects.all()
        self.assertEqual(reviews[0], review1, msg="Review with a later creation date should come first")
        self.assertEqual(reviews[1], review2, msg="Earlier review should be ordered later")
