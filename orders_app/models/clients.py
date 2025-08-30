from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
