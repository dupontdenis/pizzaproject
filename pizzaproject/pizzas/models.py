from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=50, unique=True)
    ingredients = models.JSONField()  # liste ["🍅","🧀",...]


    def __str__(self):
        return self.name
