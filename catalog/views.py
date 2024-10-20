from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Book, Borrow
from .models import Review
from .forms import ReviewForm

from django.views.generic import ListView
from .models import Book
from django.views.generic import DetailView

from django import forms
from .models import Review

from django.shortcuts import render
from .models import Book

@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.available_copies > 0:
        Borrow.objects.create(user=request.user, book=book)
        book.available_copies -= 1
        book.save()
        return redirect('catalog:book_list')
    else:
        return render(request, 'catalog/book_unavailable.html', {'book': book})


@login_required
def return_book(request, borrow_id):
    borrow = get_object_or_404(Borrow, id=borrow_id)
    borrow.return_date = timezone.now()
    borrow.returned = True
    borrow.book.available_copies += 1
    borrow.book.save()
    borrow.save()
    return redirect('catalog:book_list')


@login_required
def add_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            return redirect('catalog:book_detail', book_id=book.id)
    else:
        form = ReviewForm()
    return render(request, 'catalog/add_review.html', {'form': form, 'book': book})


def search_books(request):
    query = request.GET.get('q')
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'catalog/search_results.html', {'books': books, 'query': query})


class BookListView(ListView):
    model = Book
    template_name = 'catalog/book_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'
    context_object_name = 'book'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']


@login_required
def add_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect('catalog:book_detail', pk=book_id)
    else:
        form = ReviewForm()

    return render(request, 'catalog/add_review.html', {'form': form, 'book': book})


def search_books(request):
    query = request.GET.get('q')
    books = Book.objects.filter(title__icontains=query) if query else Book.objects.all()
    return render(request, 'catalog/book_list.html', {'books': books})