from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Review, Book
from .forms import ReviewForm
import datetime


def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


def Book_list(request):
    Book_list = Book.objects.order_by('-name')
    context = {'Book_list':Book_list}
    return render(request, 'reviews/Book_list.html', context)


def Book_detail(request, Book_id):
    Book = Book_detail(request, Book_id)
    form = ReviewForm()
    return render(request, 'reviews/Book_detail.html', {'Book': Book, 'form': form})


def add_review(request, Book_id):
    Book = get_object_or_404(Book, pk=Book_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = form.cleaned_data['user_name']
        review = Review()
        review.Book = Book
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('reviews:Book_detail', args=(Book.id,)))
    
    return render(request, 'reviews/Book_detail.html', {'Book': Book, 'form': form})