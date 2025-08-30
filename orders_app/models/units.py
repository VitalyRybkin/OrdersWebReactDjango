from django.db import models


class Unit(models.Model):
    unit_name = models.CharField(max_length=20)
    unit_shortcut = models.CharField(max_length=2)
    description = models.TextField()
