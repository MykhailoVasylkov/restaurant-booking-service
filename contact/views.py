from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Review
from .forms import ReviewForm

def review_create(request):
    
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
    })