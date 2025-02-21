from django.test import TestCase
from django.urls import resolve, reverse
from booking.views import booking_page, edit_booking, delete_booking

class ReservationURLPatternsTest(TestCase):

    def test_booking_page_url_resolves(self):
        """Test that 'booking/' resolves to booking_page view"""
        resolver = resolve(reverse('booking'))
        self.assertEqual(resolver.func, booking_page, msg="URL 'booking/' should call booking_page view")

    def test_edit_review_url_resolves(self):
        """Test that 'edit/<int:pk>' resolves to edit_booking view"""
        resolver = resolve(reverse('edit_booking', args=[1]))
        self.assertEqual(resolver.func, edit_booking, msg="URL 'edit/<pk>' should call edit_booking view")

    def test_delete_booking_url_resolves(self):
        """Test that 'delete/<int:pk>' resolves to delete_booking view"""
        resolver = resolve(reverse('delete_booking', args=[1]))
        self.assertEqual(resolver.func, delete_booking, msg="URL 'delete/<pk>' should call delete_booking view")
