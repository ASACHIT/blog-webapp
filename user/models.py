from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, unique=True)
    password = models.CharField(max_length=100, blank=True)
    profile_pic = models.ImageField(default="default.jpg", upload_to="pictures/")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.email
