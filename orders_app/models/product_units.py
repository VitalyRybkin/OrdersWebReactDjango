from django.db import models


class ProductWeight(models.Model):
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="units"
    )
    unit = models.ForeignKey("Unit", on_delete=models.CASCADE)

    kg_per_unit = models.DecimalField(
        max_digits=12,
        decimal_places=0,
        help_text="Например: 1 шт = 0.5 кг, 1 кг = 1.0, 1 ton = 1000.0",
    )

    class Meta:
        unique_together = ("product", "unit")
        db_table = "orders_app_product_weights"

    def __str__(self):
        return f"ВЕС: {self.product.product_name} - <{self.unit.unit_shortcut}, {self.kg_per_unit} кг>"
