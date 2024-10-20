# import os
# import django
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryManager.settings')
# django.setup()
#
# from catalog.models import Book, Borrow, Review
# from django.contrib.auth import get_user_model
# from django.utils import timezone
#
# User = get_user_model()
#
# def create_superuser():
#     # Проверяваме дали вече съществува суперпотребител
#     if not User.objects.filter(username='admin').exists():
#         User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
#         print("Суперпотребителят е създаден успешно.")
#     else:
#         print("Суперпотребителят вече съществува.")
#
# def create_books():
#     books = [
#         {
#             "title": "Harry Potter and the Sorcerer's Stone",
#             "author": "J.K. Rowling",
#             "genre": "Fantasy",
#             "publication_year": 1997,
#             "isbn": "9780747532699",
#             "summary": "First book in the Harry Potter series.",
#             "available_copies": 5
#         },
#         {
#             "title": "A Game of Thrones",
#             "author": "George R.R. Martin",
#             "genre": "Fantasy",
#             "publication_year": 1996,
#             "isbn": "9780553103540",
#             "summary": "First book in A Song of Ice and Fire series.",
#             "available_copies": 3
#         },
#         {
#             "title": "The Hobbit",
#             "author": "J.R.R. Tolkien",
#             "genre": "Fantasy",
#             "publication_year": 1937,
#             "isbn": "9780261102217",
#             "summary": "Fantasy novel and precursor to The Lord of the Rings.",
#             "available_copies": 4
#         },
#     ]
#
#     for book_data in books:
#         book, created = Book.objects.get_or_create(
#             isbn=book_data["isbn"],
#             defaults={
#                 "title": book_data["title"],
#                 "author": book_data["author"],
#                 "genre": book_data["genre"],
#                 "publication_year": book_data["publication_year"],
#                 "summary": book_data["summary"],
#                 "available_copies": book_data["available_copies"],
#             },
#         )
#         if created:
#             print(f"Книгата '{book.title}' е добавена успешно.")
#         else:
#             print(f"Книгата '{book.title}' вече съществува.")
#
# def create_borrows():
#     # Взимаме първия съществуващ потребител и книгаLibraryManager
#     user = User.objects.first()
#     book = Book.objects.first()
#
#     if user and book:
#         borrow, created = Borrow.objects.get_or_create(
#             user=user,
#             book=book,
#             defaults={
#                 "borrow_date": timezone.now(),
#             },
#         )
#         if created:
#             print(f"Потребителят '{user.username}' е заел книгата '{book.title}'.")
#         else:
#             print(f"Потребителят '{user.username}' вече е заел книгата '{book.title}'.")
#     else:
#         print("Няма налични потребители или книги за заемане.")
#
# def create_reviews():
#     user = User.objects.first()
#     book = Book.objects.first()
#
#     if user and book:
#         review, created = Review.objects.get_or_create(
#             user=user,
#             book=book,
#             defaults={
#                 "rating": 5,
#                 "comment": "Great book, highly recommended!",
#                 "created_at": timezone.now()
#             }
#         )
#         if created:
#             print(f"Отзивът за книгата '{book.title}' е добавен успешно.")
#         else:
#             print(f"Отзивът за книгата '{book.title}' вече съществува.")
#     else:
#         print("Няма налични потребители или книги за добавяне на отзив.")
#
# def initialize_data():
#     create_superuser()
#     create_books()
#     create_borrows()
#     create_reviews()
#     print("Инициализацията на данните завърши успешно.")
#
# if __name__ == '__main__':
#     initialize_data()

# import os
# import django
# import random
# from faker import Faker
# from django.utils import timezone
#
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryManager.settings')
# django.setup()
#
# from catalog.models import Book, Borrow, Review
# from django.contrib.auth import get_user_model
#
# User = get_user_model()
# fake = Faker()
#
#
# def create_superuser():
#     if not User.objects.filter(username='admin').exists():
#         User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
#         print("Суперпотребителят е създаден успешно.")
#     else:
#         print("Суперпотребителят вече съществува.")
#
#
# def create_users(count=20):
#     for i in range(count):
#         username = f'user{i + 1}'
#         email = f'user{i + 1}@example.com'
#         if not User.objects.filter(username=username).exists():
#             user = User.objects.create_user(username=username, email=email, password='password123')
#             print(f"Потребителят '{username}' е добавен успешно.")
#         else:
#             print(f"Потребителят '{username}' вече съществува.")
#
#
# def create_books(count=20):
#     genres = ["Fantasy", "Science Fiction", "Mystery", "Romance", "Thriller"]
#     for i in range(count):
#         title = fake.sentence(nb_words=4)
#         author = fake.name()
#         genre = random.choice(genres)
#         publication_year = random.randint(1900, 2024)
#         isbn = fake.isbn13(separator="")
#         summary = fake.paragraph()
#         available_copies = random.randint(1, 10)
#
#         book, created = Book.objects.get_or_create(
#             isbn=isbn,
#             defaults={
#                 "title": title,
#                 "author": author,
#                 "genre": genre,
#                 "publication_year": publication_year,
#                 "summary": summary,
#                 "available_copies": available_copies,
#             },
#         )
#         if created:
#             print(f"Книгата '{book.title}' е добавена успешно.")
#         else:
#             print(f"Книгата '{book.title}' вече съществува.")
#
#
# def create_borrows():
#     users = User.objects.all()
#     books = Book.objects.all()
#
#     for user in users:
#         # Избираме случайна книга за заемане
#         book = random.choice(books)
#         borrow, created = Borrow.objects.get_or_create(
#             user=user,
#             book=book,
#             defaults={
#                 "borrow_date": timezone.now(),
#             },
#         )
#         if created:
#             print(f"Потребителят '{user.username}' е заел книгата '{book.title}'.")
#         else:
#             print(f"Потребителят '{user.username}' вече е заел книгата '{book.title}'.")
#
#
# def create_reviews():
#     users = User.objects.all()
#     books = Book.objects.all()
#
#     for book in books:
#         user = random.choice(users)
#         rating = random.randint(1, 5)
#         comment = fake.paragraph()
#
#         review, created = Review.objects.get_or_create(
#             user=user,
#             book=book,
#             defaults={
#                 "rating": rating,
#                 "comment": comment,
#                 "created_at": timezone.now()
#             }
#         )
#         if created:
#             print(f"Отзивът за книгата '{book.title}' е добавен успешно.")
#         else:
#             print(f"Отзивът за книгата '{book.title}' вече съществува.")
#
#
# def initialize_data():
#     create_superuser()
#     create_users(20)
#     create_books(20)
#     create_borrows()
#     create_reviews()
#     print("Инициализацията на данните завърши успешно.")
#
#
# if __name__ == '__main__':
#     initialize_data()


import os
import django
import random
from faker import Faker


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryManager.settings')
django.setup()

from catalog.models import Book, Borrow, Review
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()
fake = Faker()

def create_superuser():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
        print("Суперпотребителят е създаден успешно.")
    else:
        print("Суперпотребителят вече съществува.")

def create_users():
    for _ in range(20):
        username = fake.unique.user_name()
        email = fake.unique.email()
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, email=email, password='password123')
            print(f"Потребител '{username}' е добавен успешно.")
        else:
            print(f"Потребител '{username}' вече съществува.")

def create_books():
    authors = ["J.K. Rowling", "George R.R. Martin", "J.R.R. Tolkien", "Agatha Christie", "Stephen King"]
    genres = ["Fantasy", "Science Fiction", "Mystery", "Thriller", "Romance"]

    for _ in range(20):
        title = fake.unique.sentence(nb_words=4)
        author = random.choice(authors)
        genre = random.choice(genres)
        publication_year = random.randint(1900, 2023)
        isbn = fake.unique.isbn13()
        summary = fake.text(max_nb_chars=200)
        available_copies = random.randint(1, 10)

        book, created = Book.objects.get_or_create(
            isbn=isbn,
            defaults={
                "title": title,
                "author": author,
                "genre": genre,
                "publication_year": publication_year,
                "summary": summary,
                "available_copies": available_copies,
            },
        )
        if created:
            print(f"Книгата '{title}' е добавена успешно.")
        else:
            print(f"Книгата '{title}' вече съществува.")

def create_borrows():
    users = User.objects.all()
    books = Book.objects.all()

    if users.exists() and books.exists():
        for user in users:
            for _ in range(3):  # Добавя по 3 заема на потребител
                book = random.choice(books)
                Borrow.objects.get_or_create(
                    user=user,
                    book=book,
                    defaults={
                        "borrow_date": timezone.now(),
                    },
                )
        print("Всички заеми са добавени успешно.")
    else:
        print("Няма налични потребители или книги за заемане.")

def create_reviews():
    users = User.objects.all()
    books = Book.objects.all()

    if users.exists() and books.exists():
        for user in users:
            for book in books:
                if random.choice([True, False]):  # 50% шанс за добавяне на отзив
                    Review.objects.get_or_create(
                        user=user,
                        book=book,
                        defaults={
                            "rating": random.randint(1, 5),
                            "comment": fake.text(max_nb_chars=200),
                            "created_at": timezone.now()
                        }
                    )
        print("Всички отзиви са добавени успешно.")
    else:
        print("Няма налични потребители или книги за добавяне на отзив.")

def initialize_data():
    create_superuser()
    create_users()
    create_books()
    create_borrows()
    create_reviews()
    print("Инициализацията на данните завърши успешно.")

if __name__ == '__main__':
    initialize_data()
