from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.contrib.auth.hashers import make_password


class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True, blank=True)

#     def save(self, *args, **kwargs):
#         self.password = make_password(self.password)
#         super(User, self).save(*args, **kwargs)

