from enum import Enum

from django.contrib.auth import models as auth_models
from django.core import validators
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from BookLoversApp.accounts.validators import validate_only_letters


# class ChoicesEnumMixin:
#
#     @classmethod
#     def choices(cls):
#         return [(x.name, x.value) for x in cls]
#
#     @classmethod
#     def max_len(cls):
#         return max(len(name) for name, _ in cls.choices())

#
# class Gender(ChoicesEnumMixin, Enum):
#     male = 'Male'
#     female = 'Female'
#     doNotShow = 'No Information'


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
        max_length=200
    )
