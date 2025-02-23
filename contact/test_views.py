from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Review

"""
I used Chat-GPT to set-up tests
"""


class TestReviewViews(TestCase):

    def setUp(self):
        """Create a test user and a review"""
        self.client = Client()  # Instantiate the test client
        self.user = User.objects.create_user(
            username="admin",
            password="password123"
        )  # Create a user
        self.client.login(
            username="admin",
            password="password123"
        )  # Log in the user

        self.review = Review.objects.create(
            author=self.user,
            rating=4,
            body="Good food!",
            approved=True
        )

    def test_review_create_view_get(self):
        """Test that the review creation page is accessible"""
        response = self.client.get(
            reverse("contact")
        )  # Access the 'contact' view
        self.assertEqual(
            response.status_code, 200,
            msg="Page should return HTTP 200"
        )
        try:
            self.assertTemplateUsed(
                response, "contact/contact_us.html"
            )  # The correct template should be used
        except AssertionError:
            print(
                  "Error: The expected template 'contact/contact_us.html' "
                  "was not used."
                 )
            raise  # Re-raise the error so the test will fail

    def test_review_create_view_post(self):
        """Test successful review creation via POST request"""
        self.client.login(
            username="admin",
            password="password123"
        )  # Ensure user is logged in

        response = self.client.post(reverse("contact"), {
            "rating": 5,
            "body": "Amazing experience!",
            "author": self.user.id  # Include the 'author' as it's required
        })

        if response.status_code == 200:
            print(
                "Form errors:",
                response.context["form"].errors
            )  # Output form errors for debugging

        # Ensure the response status code is a redirect (302)
        self.assertEqual(
            response.status_code, 302,
            msg="Form submission should redirect"
        )
        # Verify the new review is saved in the database
        self.assertTrue(
            Review.objects.filter(body="Amazing experience!").exists(),
            msg="Review should be created"
        )

    def test_edit_review_view(self):
        """Test editing an existing review"""
        self.client.login(
            username="admin",
            password="password123"
        )  # Log in as the user

        response = self.client.post(
            reverse("edit_review", args=[self.review.pk]),
            {
                "rating": 5,
                "body": "Updated review",
                "author": self.review.author.id
            }
        )
        # Check for form errors
        if response.status_code == 200:
            print("Form errors:", response.context["form"].errors)

        self.review.refresh_from_db()  # Reload the review object from the db
        # Verify that the review body has been updated
        self.assertEqual(
            self.review.body, "Updated review",
            msg="Review body should be updated"
        )

    def test_delete_review_view(self):
        """Test deleting a review"""
        response = self.client.post(
            reverse("delete_review", args=[self.review.id])
        )  # Send DELETE request for review
        self.assertEqual(
            response.status_code, 302,
            msg="After deletion, the response should redirect"
        )  # Ensure the review has been deleted from the database
        self.assertFalse(
            Review.objects.filter(id=self.review.id).exists(),
            msg="Review should be deleted"
        )

    def test_review_is_saved_correctly(self):
        """Test that a valid review is saved in the db with correct data"""
        self.client.login(username="admin", password="password123")

        self.client.post(reverse("contact"), {
            "rating": 5,
            "body": "Great service!",
            "author": self.user.id
        })

        review = Review.objects.filter(body="Great service!").first()
        self.assertIsNotNone(
            review,
            msg="Review should be saved in the database"
        )
        self.assertEqual(
            review.author, self.user,
            msg="Review author should be correct"
        )
        self.assertEqual(
            review.rating, 5,
            msg="Review rating should be correct"
        )
        self.assertFalse(
            review.approved,
            msg="Review should not be approved by default"
        )
