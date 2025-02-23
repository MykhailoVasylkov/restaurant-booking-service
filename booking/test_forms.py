from django.test import TestCase
from django.contrib.auth.models import User
from .forms import ReservationForm
from datetime import date, time

"""
I used Chat-GPT to set-up tests
"""


class ReservationFormTest(TestCase):

    def setUp(self):
        """Create a test user for reservation"""
        self.user = User.objects.create_user(
            username="admin",
            password="password123"
        )

    def test_form_valid_data(self):
        """We test the form with the correct data"""
        data = {
            'client': self.user,
            'phone_number': '1234567890',
            'date': date.today(),
            'time': time(18, 30),
            'people_count': 4,
            'table_count': 1,  # We expect that for 4 people you need 1 table
            'comment': 'No special requests'
        }
        form = ReservationForm(data=data)
        self.assertTrue(
            form.is_valid(),
            msg="Form should be valid with correct data"
        )

    def test_form_invalid_phone_number(self):
        """We test the form with the wrong phone number"""
        data = {
            'client': self.user,
            'phone_number': '123abc',
            'date': date.today(),
            'time': time(18, 30),
            'people_count': 4,
            'table_count': 1,
            'comment': 'No special requests'
        }
        form = ReservationForm(data=data)
        self.assertFalse(
            form.is_valid(),
            msg="Form should be invalid with incorrect phone number"
        )
        self.assertIn(
            'phone_number', form.errors,
            msg="Phone number field should raise an error"
        )

    def test_form_empty_fields(self):
        """We test the shape with empty fields"""
        form = ReservationForm(data={})
        self.assertFalse(
            form.is_valid(),
            msg="Form should be invalid with empty fields"
        )
        self.assertIn('client', form.errors, msg="Client field is required")
        self.assertIn(
            'phone_number', form.errors,
            msg="Phone number field is required"
        )
        self.assertIn('date', form.errors, msg="Date field is required")
        self.assertIn('time', form.errors, msg="Time field is required")
        self.assertIn(
            'people_count', form.errors,
            msg="People count field is required"
        )
        self.assertIn(
            'table_count', form.errors,
            msg="Table count field is required"
        )
