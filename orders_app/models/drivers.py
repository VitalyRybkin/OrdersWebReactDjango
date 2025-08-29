from django.db import models


class Drivers(models.Model):
    carrier_id = models.ForeignKey('Carriers', on_delete=models.CASCADE, related_name='drivers')
    driver_name = models.CharField(max_length=100)
