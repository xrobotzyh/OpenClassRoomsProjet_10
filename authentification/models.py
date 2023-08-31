from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):

    can_be_contacted = models.BooleanField()
    can_data_be_shared = models.BooleanField()
    age = models.PositiveIntegerField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username}'
