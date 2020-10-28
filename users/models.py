from django.contrib.gis.db import models


class Profile(models.Model):


    # Returns the string representation of the model.
    def __str__(self):
        return self.name