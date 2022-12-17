from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from BookLoversApp.accounts.models import AppUser

UserModel = get_user_model()


class AppUserModelTests(TestCase):

    def test_appuser_first_name__contains_only_letters__correct_result(self):
        user = AppUser(

            first_name='Susanna',
            last_name='Slaveykova',
            username='susie',
            password='Susanna789!',
            email='susie@gmail.com',
            gender='Female',
        )

        user.full_clean()
        user.save()

        self.assertIsNotNone(user.pk)

    def test_appuser_first_name_and_last_name__contain_only_letters__expect_exception(self):
        user = AppUser(

            first_name='Susanna7',
            last_name='Slaveykova12!',
            username='susie',
            password='Susanna789!',
            email='susie@gmail.com',
            gender='Female',
        )

        with self.assertRaises(ValidationError) as context:
            user.full_clean()
            user.save()

        self.assertIsNotNone(context.exception)

    def test_create_profile_success(self):
        username = 'Susie7'
        user_data = {

            'email': 'susie@gmail.com',
            'gender': 'Female'
        }
        credentials = {
            "username": username,
            'password': 'Susanna123!'
        }

        UserModel.objects.create_user(**credentials)

        print(AppUser.objects.all(), flush=True)
        response = self.client.post(reverse('login'), data=user_data)
        created_profile = AppUser.objects.filter(username='Susie7').get()

        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(created_profile)
        self.assertEqual(1, len(AppUser.objects.all()))

    def test_login_profile_success(self):
        username = 'Susie7'
        user_data = {

            'email': 'susie@gmail.com',
            'gender': 'Female'
        }
        credentials = {
            "username": username,
            'password': 'Susanna123!'
        }

        UserModel.objects.create_user(**credentials)
        self.client.login()

        response = self.client.post(reverse('login'), data=user_data)
        created_profile = AppUser.objects.filter(username='Susie7').get()

        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(created_profile)
        self.assertEqual(1, len(AppUser.objects.all()))

    def test_logout_profile_success(self):
        username = 'Susie7'

        credentials = {
            "username": username,
            'password': 'Susanna123!'
        }

        UserModel.objects.create_user(**credentials)
        self.client.login(**credentials)
        response = self.client.post(path=reverse("logout"), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse("show index"))
        self.assertTrue(UserModel.is_anonymous)

    def test_user_edit_success(self):
        user_data = {
            'first_name': 'Susanna',
            'last_name': 'Slaveykova',
            'username': 'susie',
            'password': 'Susanna789!',
            'email': 'susie@gmail.com',
            'gender': 'Female'}

        username = 'Susie7'

        credentials = {
            "username": username,
            'password': 'Susanna123!'
        }

        user = UserModel.objects.create_user(**credentials)
        self.client.login(**credentials)

        response = self.client.post(reverse('edit profile', kwargs={'pk': user.pk}), data=user_data)
        created_profile = AppUser.objects.filter(username='Susie7').get()

        self.assertEqual(response.status_code, 302)
        user.refresh_from_db()

        self.assertEqual('Susanna', user.first_name)
        self.assertEqual('Slaveykova', user.last_name)
        self.assertEqual('susie@gmail.com', user.email)

    def test_delete_user_success(self):
        username = 'Susie7'

        credentials = {
            "username": username,
            'password': 'Susanna123!'
        }

        user = UserModel.objects.create_user(**credentials)
        self.client.login(**credentials)
        response = self.client.delete(reverse('delete profile', kwargs={'pk': user.pk}), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse("show index"))
        self.assertTrue(UserModel.is_anonymous)