from django.db import models

from orders_app.models import Unit
from django.core.exceptions import ObjectDoesNotExist
from orders_app.models.product_units import ProductWeight


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    palette_volume = models.SmallIntegerField(null=True)
    description = models.TextField(null=True, blank=True)

    product_units = models.ManyToManyField(
        "Unit", through="ProductWeight", related_name="product_units"
    )

    def convert(self, quantity: float, from_unit: "Unit", to_unit: "Unit") -> float:
        """Converts quantity from one unit to another"""
        try:
            if from_unit.is_weight_based:
                from_factor = float(from_unit.to_kg_factor)
            else:
                from_factor = float(self.units.get(unit=from_unit).kg_per_unit)

            if to_unit.is_weight_based:
                to_factor = float(to_unit.to_kg_factor)
            else:
                to_factor = float(self.units.get(unit=to_unit).kg_per_unit)

        except ProductWeight.DoesNotExist:
            raise ValueError(
                f"No conversion defined for product '{self}' and unit '{from_unit}' or '{to_unit}'"
            )

        kg = quantity * from_factor
        return kg / to_factor

    def __str__(self):
        return f"МАТЕРИАЛ: {self.product_name.capitalize()}"
