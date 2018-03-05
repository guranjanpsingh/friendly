from django.db import models
from .users import User


class UserLocation(models.Model):
    """
    Stores location for a user
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='location')
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    last_updated = models.DateTimeField()

    REQUIRED_FIELDS = ['user', 'longitude', 'latitude']