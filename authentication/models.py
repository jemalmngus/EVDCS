# authentication/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('superAdmin', 'superAdmin'),
        ('cityAdmin', 'cityAdmin'),
        ('subcityAdmin', 'subcityAdmin'),
        ('cityStaff', 'cityStaff'),
        ('subcityStaff', 'subcityStaff'),
    )

    roll = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.username

    class Meta:
        app_label = 'authentication'  # Make sure the app label matches the app name
