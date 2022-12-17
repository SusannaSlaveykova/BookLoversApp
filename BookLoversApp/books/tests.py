import time

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from pyexpat import model

from BookLoversApp.accounts.models import AppUser
from BookLoversApp.books.models import Book

UserModel = get_user_model()


class BookModelTests(TestCase):
    def test_create_book_success(self):
        username = 'Susie7'

        credentials = {
            "username": username,
            'password': 'Susanna123!'
        }

        user = UserModel.objects.create_user(**credentials)


        book = Book.objects.create(title='The Little Prince', cover_photo="http://abv.bg/image.png",
                                   author="Antoine de Saint-Exupéry", pages=214, year_of_first_publication=1940,
                                   user_id=user.id)

        response = self.client.post(
            reverse('add book'))

        self.assertEqual(302, response.status_code)
        self.assertIsNotNone(book)
        self.assertEqual(1, len(Book.objects.all()))
        self.assertEqual('Antoine de Saint-Exupéry', book.author)

    def test_edit_book_view_success(self):
        credentials = {
            'username': 'susie',
            'password': 'Susanna789!',
        }
        user = UserModel.objects.create_user(**credentials)
        self.client.login(**credentials)

        book = Book.objects.create(title='The Catcher in the Rye', cover_photo="http://abv.bg/image.png",
                                   author="Sharl Pero", pages=325, year_of_first_publication=2000,
                                   user_id=user.id)

        response = self.client.post(
            reverse('edit book', kwargs={'pk': book.id}),
            {'title': 'The Catcher in the Rye', 'cover_photo': "http://abv.bg/image.png",
             'author': "J.D. Salinger", 'pages': 328,
             'year_of_first_publication': 2000,
             'user_id': user.id})

        self.assertEqual(response.status_code, 302)
        book.refresh_from_db()

        self.assertEqual("J.D. Salinger", book.author)
        self.assertEqual(book.pages, 328)
