from django.core.exceptions import ValidationError
from django.test import TestCase

from BookLoversApp.accounts.models import AppUser


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