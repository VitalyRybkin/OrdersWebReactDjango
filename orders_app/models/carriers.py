from django.db import models


class Carriers(models.Model):
    carrier_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
