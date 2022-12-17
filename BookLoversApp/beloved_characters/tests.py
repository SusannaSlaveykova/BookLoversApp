from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from BookLoversApp.beloved_characters.models import BelovedCharacter
from BookLoversApp.books.models import Book
from django.test.client import RequestFactory

UserModel = get_user_model()


class TestBelovedCharacter(TestCase):

    def test_create_beloved_character_success(self):
        username = 'Susie7'

        credentials = {
            "username": username,
            'password': 'Susanna123!'
        }

        user = UserModel.objects.create_user(**credentials)

        book = Book.objects.create(title='The Little Prince', cover_photo="http://abv.bg/image.png",
                                   author="Antoine de Saint-Exupéry", pages=214, year_of_first_publication=1940,
                                   user_id=user.id)

        beloved_character = BelovedCharacter.objects.create(name='The Little Prince',
                                                            reason_to_like="very interesting character",
                                                            favourite_story="the story with the rose", book_id=book.id,
                                                            user_id=user.id)

        response = self.client.post(
            reverse('add beloved character', kwargs={'book_pk': book.id}),
            {'name': 'The Little Prince', 'reason_to_like': "very interesting character",
             'favourite_story': "the story with the rose", 'book_id': book.id,
             'year_of_first_publication': 2000,
             'user_id': user.id})

        self.assertEqual(302, response.status_code)
        self.assertIsNotNone(beloved_character)
        self.assertEqual(1, len(BelovedCharacter.objects.all()))
        self.assertEqual('The Little Prince', beloved_character.name)
        self.assertEqual("Antoine de Saint-Exupéry", beloved_character.book.author)

    def test_edit_beloved_character_success(self):
        username = 'Susie7'

        credentials = {
            "username": username,
            'password': 'Susanna123!'
        }

        user = UserModel.objects.create_user(**credentials)
        self.client.login(**credentials)

        book = Book.objects.create(title='The Little Prince', cover_photo="http://abv.bg/image.png",
                                   author="Antoine de Saint-Exupéry", pages=214, year_of_first_publication=1940,
                                   user_id=user.id)

        beloved_character = BelovedCharacter.objects.create(name='The Little Prince',
                                                            reason_to_like="very interesting character",
                                                            favourite_story="the story with the rose", book_id=book.id,
                                                            user_id=user.id)

        response = self.client.post(
            reverse('edit beloved character', kwargs={'char_pk': beloved_character.id}),
            {'name': 'The Little Prince!', 'reason_to_like': "Very interesting character!",
             'favourite_story': "The story with the rose!",
             'year_of_first_publication': 2000,
             })
        self.assertEqual(302, response.status_code)
        beloved_character.refresh_from_db()
        self.assertEqual('The Little Prince!', beloved_character.name)
        self.assertEqual("Very interesting character!", beloved_character.reason_to_like)
        self.assertEqual("The story with the rose!", beloved_character.favourite_story)
