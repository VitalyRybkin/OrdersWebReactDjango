from django.db import models


class Truck(models.Model):
    truck_type = models.ForeignKey(
        "TruckType",
        on_delete=models.CASCADE,
        related_name="trucks",
    )
    truck_capacity = models.ForeignKey(
        "TruckCapacity",
        on_delete=models.CASCADE,
        related_name="trucks",
    )
    description = models.TextField(null=True, blank=True)
    carrier = models.ForeignKey(
        "Carrier",
        on_delete=models.CASCADE,
        related_name="trucks",
    )

    def __str__(self):
        return (
            f"<Truck "
            f"truck_type_id={self.truck_type_id} "
            f"truck_capacity_id={self.truck_capacity_id} "
            f"description={self.description} "
            f"carrier_id={self.carrier_id}>"
        )
