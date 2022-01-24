from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = ((GENDER_MALE, "남자"), (GENDER_FEMALE, "여자"), (GENDER_OTHER, "기타"))

    KOREAN = "korean"
    ENGLISH = "english"
    LANGUAGE_CHOICES = ((KOREAN, "한국어"), (ENGLISH, "english"))

    KRW = "krw"
    USD = "usd"
    CURRENCY_CHOICES = ((KRW, "원"), (USD, "usd"))

    avatar = models.ImageField(null=True, blank=True)
    bio = models.TextField(default="", blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=10, null=True, blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=10, null=True, blank=True
    )
    superhost = models.BooleanField(default=False)
