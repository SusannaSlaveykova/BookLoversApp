from django.contrib.auth import get_user_model
from django.db import models

from BookLoversApp.books.models import Book

UserModel = get_user_model()


class Quote(models.Model):
    MAX_TEXT_LENGTH = 400

    quote_text = models.TextField(
        max_length=MAX_TEXT_LENGTH,
    )

    date_and_time_of_publication = models.DateTimeField(
        auto_now=True,
        null=False,
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
