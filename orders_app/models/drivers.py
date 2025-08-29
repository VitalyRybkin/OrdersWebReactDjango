from django.db import models


class Drivers(models.Model):
    carrier = models.ForeignKey(
        "Carriers", on_delete=models.CASCADE, related_name="drivers"
    )
    driver_name = models.CharField(max_length=100)

    def __str__(self):
        return f"<Driver carrier_id={self.carrier_id} driver_name={self.driver_name}>"
