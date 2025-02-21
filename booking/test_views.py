from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, time
from .models import Reservation


class TestBookingViews(TestCase):

    def setUp(self):
        """Create a test user and a reservation"""
        self.client = Client()  # Instantiate the test client
        self.user = User.objects.create_user(username="admin", password="password123")  # Create a user
        self.client.login(username="admin", password="password123")  # Log in the user

        self.reservation = Reservation.objects.create(
            client=self.user,
            phone_number='+123456789',
            date=date(2025, 2, 20),
            time=time(19, 0),
            people_count=4,
            table_count=1,
            comment="Test reservation"
        )

    def test_booking_page_get(self):
        """Test that the booking page is accessible"""
        response = self.client.get(reverse("booking"))
        self.assertEqual(response.status_code, 200, msg="Page should return HTTP 200")
        self.assertTemplateUsed(response, "booking/booking_page.html")

    def test_create_booking_view_post(self):
        """Test successful booking creation via POST request"""
        response = self.client.post(reverse("booking"), {
            "phone_number": '+123456789',
            "date": '2025-02-20',
            "time": '19:00',
            "people_count": 4,
            "table_count": 1,
            "comment": "Test reservation"
        })
        self.assertEqual(response.status_code, 302, msg="Form submission should redirect")
        self.assertTrue(Reservation.objects.filter(comment="Test reservation").exists(), msg="Reservation should be created")

    def test_delete_booking_view_post(self):
        """Test deleting an existing reservation"""
        response = self.client.post(reverse("delete_booking", args=[self.reservation.pk]))  # Send DELETE request for reservation
        self.assertEqual(response.status_code, 302, msg="Response should redirect after deletion")
        self.assertFalse(Reservation.objects.filter(id=self.reservation.id).exists(), msg="Reservation should be deleted")
    
    def test_edit_booking_view_post(self):
        """Test editing an existing reservation"""
        self.client.login(username="admin", password="password123")

        response = self.client.post(reverse("edit_booking", args=[self.reservation.pk]), {
            "client": self.reservation.client.id,  # Added comma
            "date": "2025-02-21",
            "time": "18:30",  # Updated time
            "comment": "Updated reservation"
        })
    
        # Check for form errors
        if response.status_code == 200:
            print("Form errors:", response.context["form"].errors)

        self.reservation.refresh_from_db()  # Reload the reservation object from the database
        # Verify that the comment has been updated
        self.assertEqual(self.reservation.comment, "Updated reservation", msg="The reservation comment should be updated")
