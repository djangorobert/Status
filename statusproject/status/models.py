# Create user and save to the database
from tkinter import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.urls import reverse

LOCATION = (
    ('ONSITE', 'Onsite'),
    ('REMOTE', 'Remote'),
    ('VACATION', 'Vacation'),
    ('SICK', 'Sick'),
    ('ON_LEAVE', 'On Leave'),
)


class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username


class Location(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    location = models.CharField(choices=LOCATION, max_length=9)
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('task_update_form', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.user)
