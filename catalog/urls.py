from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('return/<int:borrow_id>/', views.return_book, name='return_book'),
    path('add_review/<int:book_id>/', views.add_review, name='add_review'),
    path('search/', views.search_books, name='search_books'),
]
