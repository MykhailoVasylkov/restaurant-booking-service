from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date, time
from django.core.exceptions import ValidationError
from .models import Reservation

"""
I used Chat-GPT to set-up tests
"""


class ReservationModelTest(TestCase):

    def setUp(self):
        """Create a test user"""
        self.user = User.objects.create_user(
            username='testuser',
            password='password'
        )

    def test_create_reservation(self):
        """Checks if a reservation is created correctly"""
        reservation = Reservation.objects.create(
            client=self.user,
            phone_number='+123456789',
            date=date(2025, 2, 20),
            time=time(19, 0),
            people_count=4,
            table_count=1,
            comment="Test reservation"
        )
        self.assertEqual(reservation.client, self.user)
        self.assertEqual(reservation.phone_number, '+123456789')
        self.assertEqual(reservation.date, date(2025, 2, 20))
        self.assertEqual(reservation.time, time(19, 0))
        self.assertEqual(reservation.people_count, 4)
        self.assertEqual(reservation.table_count, 1)
        self.assertEqual(reservation.comment, "Test reservation")
        self.assertEqual(reservation.status, 0)  # Default status is Pending

    def test_status_default_value(self):
        """Check default values in the Reservation model"""
        reservation = Reservation.objects.create(
            client=self.user,
            phone_number='+1234567890',
            date=date(2025, 2, 20),
            time=time(19, 0),
            people_count=2,
            table_count=1
        )

        # Check that the default status is 0 (Pending)
        self.assertEqual(
            reservation.status, 0,
            msg=("New reservations should have 'status' set to 0 (Pending) "
                 "by default")
        )

        # Check that created_at is automatically set
        self.assertIsNotNone(
            reservation.created_at,
            msg="Created_at timestamp should be automatically set"
        )

        # Check that updated_at is automatically set
        self.assertIsNotNone(
            reservation.updated_at,
            msg="Updated_at timestamp should be automatically set"
        )

    def test_phone_number_max_length(self):
        """Checks that phone_number does not exceed 15 characters"""
        reservation = Reservation.objects.create(
            client=self.user,
            phone_number='+123456789012345',  # 15 characters is allowed
            date=date(2025, 2, 20),
            time=time(19, 0),
            people_count=2,
            table_count=1
        )
        with self.assertRaises(
            ValidationError,
            msg="Phone number should not exceed 15 characters"
        ):
            reservation.full_clean()

    def test_people_count_positive(self):
        """Checks that people_count cannot be negative or 0"""
        reservation = Reservation(
            client=self.user,
            phone_number='+123456789',
            date=date(2025, 2, 20),
            time=time(19, 0),
            people_count=0,  # Invalid value
            table_count=1
        )
        with self.assertRaises(
            ValidationError,
            msg="People count should be greater than 0"
        ):
            reservation.full_clean()

    def test_table_count_positive(self):
        """Checks that table_count cannot be negative or 0"""
        reservation = Reservation(
            client=self.user,
            phone_number='+123456789',
            date=date(2025, 2, 20),
            time=time(19, 0),
            people_count=4,
            table_count=0  # Invalid value
        )
        with self.assertRaises(
            ValidationError,
            msg="Table count should be greater than 0"
        ):
            reservation.full_clean()

    def test_delete_user_cascade(self):
        """Checks that deleting the user deletes their reservations"""
        reservation = Reservation.objects.create(
            client=self.user,
            phone_number='+123456789',
            date=date(2025, 2, 20),
            time=time(19, 0),
            people_count=4,
            table_count=1
        )
        self.assertEqual(Reservation.objects.count(), 1)
        self.user.delete()  # Delete the user
        self.assertEqual(
            Reservation.objects.count(),
            0
        )  # The reservation should be deleted

    def test_str_method(self):
        """Checks the string representation of the object"""
        reservation = Reservation.objects.create(
            client=self.user,
            phone_number='+123456789',
            date=date(2025, 2, 20),
            time=time(19, 0),
            people_count=2,
            table_count=1
        )
        expected_str = f'Reservation by testuser on 2025-02-20 at 19:00:00'
        self.assertEqual(str(reservation), expected_str)
