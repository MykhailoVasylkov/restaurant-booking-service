from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from .models import Review
from .forms import ReviewForm

"""
I used Chat-GPT
"""


def review_create(request):
    """
    Create a new :model:`contact.Review` or display existing ones.

    **Context**

    ``form``
        An instance of :form:`contact.ReviewForm` used to create a new review.

    ``reviews``
        List of approved reviews, ordered by creation date.

    ``user_reviews``
        Reviews submitted by the currently authenticated user, if any.

    **Template:**

    :template:`contact/contact_us.html`
    """
    reviews = Review.objects.filter(approved=True).order_by("-created_on")

    user_reviews = None
    if request.user.is_authenticated:
        user_reviews = Review.objects.filter(author=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            messages.success(request, 'Review submitted and awaiting approval')
            return redirect('contact')
        else:
            messages.error(request, f'Failed to submit review!')
    else:
        form = ReviewForm()

    return render(request, 'contact/contact_us.html', {
        'form': form,
        'reviews': reviews,
        'user_reviews': user_reviews,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
    })


def edit_review(request, pk):
    """
    Edit an existing :model:`contact.Review`.

    **Context**

    ``form``
        An instance of :form:`contact.ReviewForm`
        pre-filled with the existing booking details.

    **Parameters**

    ``pk``
        Primary key of the :model:`contact.Review` to be edited.

    **Template:**

    :template:`contact/contact_us.html`
    """
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':

        form = ReviewForm(data=request.POST, instance=review)

        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your review has been updated.'
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Error updating review!'
            )
    else:
        form = ReviewForm(instance=review)

    return HttpResponseRedirect(reverse('contact'))


def delete_review(request, pk):
    """
    Delete an existing :model:`booking.Reservation`.

    **Parameters**

    ``pk``
        Primary key of the :model:`booking.Reservation` to be deleted.

    **Template:**

    :template:`booking/booking_page.html`
    """
    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        if review.author == request.user:
            review.delete()
            messages.add_message(
                request, messages.SUCCESS,
                'Your review has been deleted.'
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                'Error deleting review!'
            )

    return HttpResponseRedirect(reverse('contact'))
