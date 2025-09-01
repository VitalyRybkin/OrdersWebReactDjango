from django.db import models

from orders_app.models import Unit


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    base_unit = models.ForeignKey(
        "Unit", on_delete=models.CASCADE, related_name="products"
    )
    base_unit_weight = models.DecimalField(
        max_digits=12, decimal_places=6,
        help_text="For example: 1 pcs = 0.5 kg, 1 kg = 1.0, 1 ton = 1000.0"
    )

    palette_volume = models.SmallIntegerField(null=True)
    description = models.TextField(null=True, blank=True)

    def convert(self, quantity: float, from_unit: "Unit", to_unit: "Unit") -> float:
        """Converts a quantity from one unit to another based on their conversion factors to a base unit."""
        kg = quantity * float(self.base_unit_weight) * float(from_unit.to_kg_factor)
        return kg / float(self.base_unit_weight) / float(to_unit.to_kg_factor)

    def __str__(self):
        return (
            f"<Product product_name={self.product_name} "
            f"base_unit={self.base_unit} "
            f"palette_volume={self.palette_volume} "
            f"description={self.description}"
        )
