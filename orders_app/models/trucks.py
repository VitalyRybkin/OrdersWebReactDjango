from django.db import models


class Trucks(models.Model):
    truck_type = models.ForeignKey(
        "TruckTypes",
        on_delete=models.CASCADE,
        related_name="trucks",
    )
    truck_capacity = models.ForeignKey(
        "TruckCapacities",
        on_delete=models.CASCADE,
        related_name="trucks",
    )
    description = models.TextField(null=True, blank=True)
    carrier = models.ForeignKey(
        "Carriers",
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
