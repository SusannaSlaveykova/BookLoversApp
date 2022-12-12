from django.contrib.auth import get_user_model
from django.db import models

from BookLoversApp.books.models import Book

UserModel = get_user_model()


class BelovedCharacter(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
    )

    reason_to_like = models.TextField()

    favourite_story = models.TextField()

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
