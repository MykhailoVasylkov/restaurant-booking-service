from django.test import TestCase
from django.contrib.auth.models import User
from .forms import ReviewForm


class TestReviewForm(TestCase):

    def setUp(self):
        """Create a test user"""
        self.user = User.objects.create_user(
            username="admin", password="password123"
        )

    def test_form_is_valid(self):
        """We check that the form is valid with the correct data"""
        review_form = ReviewForm({
            'author': self.user.id,
            'rating': int(5),
            'body': 'Good food!'
        })

        self.assertTrue(review_form.is_valid(), msg="Form is invalid")

    def test_form_invalid_rating(self):
        """We check that the form is invalid with the invalid rating"""
        review_form = ReviewForm({
            'author': self.user.id,
            'rating': int(6),
            'body': 'Good food!'
        })

        self.assertFalse(
            review_form.is_valid(),
            msg="Form should be invalid with rating > 5"
        )

    def test_form_missing_rating(self):
        """We check that the form is invalid with the missing rating"""
        review_form = ReviewForm({
            'author': self.user.id,
            'body': 'Good food!'
        })

        self.assertFalse(
            review_form.is_valid(),
            msg="Form should be invalid without rating"
        )

    def test_form_empty_body(self):
        """We check that the form is invalid with the empty body"""
        review_form = ReviewForm({
            'author': self.user.id,
            'rating': int(4),
            'body': ''
        })

        self.assertFalse(
            review_form.is_valid(),
            msg="Form should be invalid with empty body"
        )
