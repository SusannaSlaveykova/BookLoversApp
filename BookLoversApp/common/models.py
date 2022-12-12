from django.contrib.auth import get_user_model
from django.db import models

from BookLoversApp.books.models import Book


UserModel = get_user_model()


class Comment(models.Model):
    MAX_TEXT_LENGTH = 300
    comment = models.TextField(
        max_length=MAX_TEXT_LENGTH,

    )
    date_and_time_of_publication = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,

    )