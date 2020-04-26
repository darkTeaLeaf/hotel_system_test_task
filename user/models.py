from django.contrib.auth.models import User
from django.db import models

from hotel.models import Hotel


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, help_text='Hotel where user stay')

    def __str__(self):
        return self.user.username + "Profile"
