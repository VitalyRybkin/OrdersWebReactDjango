from django.db import models


class TruckCapacities(models.Model):

    class Meta:
        db_table = "orders_app_truck_capacities"

    truck_capacity = models.SmallIntegerField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"<TruckCapacity truck_capacity={self.truck_capacity} description={self.description}>"
