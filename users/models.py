from django.contrib.gis.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
    last_location = models.PointField(
        editable=False,
        blank=True,
        null=True,
        default=None)

    # Returns the string representation of the model.
    def __str__(self):
        return self.name