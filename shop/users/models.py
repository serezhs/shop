from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    phone_number = PhoneNumberField(unique=True, blank=True, null=True)
    adress = models.TextField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)
