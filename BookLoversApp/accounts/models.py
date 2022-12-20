from enum import Enum

from django.contrib.auth import models as auth_models

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.deconstruct import deconstructible

from BookLoversApp.accounts.validators import validate_only_letters

IMAGE_MAX_SIZE_IN_MB = 10


@deconstructible
class MaxFileSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size

        if filesize > self.max_size * 1024 * 1024:
            raise ValidationError(f"Max file size is {self.max_size} MB")


class AppUser(auth_models.AbstractUser):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30

    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30

    MIN_AGE = 0
    MAX_AGE = 150

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Do not show', 'Do not show')
    )

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(MinLengthValidator(MIN_LEN_FIRST_NAME),
                    validate_only_letters,
                    ),
        null=True,
        blank=True,

    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(MinLengthValidator(MIN_LEN_LAST_NAME),
                    validate_only_letters,
                    ),
        null=True,
        blank=True,
    )

    email = models.EmailField(
        unique=True,
    )

    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=(MinValueValidator(MIN_AGE),
                    MaxValueValidator(MAX_AGE),)
    )

    profile_picture = models.ImageField(
        upload_to='photos/',
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        ),
    )
