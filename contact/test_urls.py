from django.test import TestCase
from django.urls import resolve, reverse
from contact.views import review_create, edit_review, delete_review

class ReviewURLPatternsTest(TestCase):

    def test_review_create_url_resolves(self):
        """Test that 'contact/' resolves to review_create view"""
        resolver = resolve(reverse('contact'))
        self.assertEqual(resolver.func, review_create, msg="URL 'contact/' should call review_create view")

    def test_edit_review_url_resolves(self):
        """Test that 'edit/<int:pk>' resolves to edit_review view"""
        resolver = resolve(reverse('edit_review', args=[1]))
        self.assertEqual(resolver.func, edit_review, msg="URL 'edit/<pk>' should call edit_review view")

    def test_delete_review_url_resolves(self):
        """Test that 'delete/<int:pk>' resolves to delete_review view"""
        resolver = resolve(reverse('delete_review', args=[1]))
        self.assertEqual(resolver.func, delete_review, msg="URL 'delete/<pk>' should call delete_review view")
