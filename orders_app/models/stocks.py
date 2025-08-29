from django.db import models


class Stocks(models.Model):
    stock_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
