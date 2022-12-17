from django.contrib.auth import get_user_model
from django.db import models

from BookLoversApp.accounts.validators import validate_only_letters

UserModel = get_user_model()


class Book(models.Model):
    MAX_TEXT_LENGTH = 5000
    title = models.CharField(
        max_length=50,
        unique=True,
    )

    cover_photo = models.URLField(
        # validators=(url_max_length,)
    )

    author = models.CharField(
        max_length=70,

    )

    pages = models.PositiveIntegerField()

    year_of_first_publication = models.PositiveIntegerField()

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    description = models.TextField(
        max_length=MAX_TEXT_LENGTH,
        null=True,
        blank=True,


    )

    def __str__(self):
        return f'{self.title}'
