from django.db import models


class Trucks(models.Model):
    truck_type = models.CharField(max_length=30)
    truck_capacity = models.SmallIntegerField()
    description = models.TextField(null=True, blank=True)
    carrier_id = models.ForeignKey(
        "Carriers",
        on_delete=models.CASCADE,
        related_name="trucks",
    )
