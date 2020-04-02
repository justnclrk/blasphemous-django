from django.db import models


class Sound(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    mood = models.CharField(max_length=50)
    active = models.BooleanField()

    def __str__(self):
        return self.name
