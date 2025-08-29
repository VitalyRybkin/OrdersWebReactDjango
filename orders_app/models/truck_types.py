from django.db import models


class TruckTypes(models.Model):

    class Meta:
        db_table = "orders_app_truck_types"

    truck_type = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return (
            f"<TruckType truck_type={self.truck_type} description={self.description}>"
        )
