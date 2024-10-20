from django.contrib import admin
from .models import Book, Borrow

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'publication_year', 'isbn', 'available_copies')
    search_fields = ('title', 'author', 'isbn')


@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrow_date', 'return_date', 'returned')
    list_filter = ('returned',)
    search_fields = ('user__username', 'book__title')