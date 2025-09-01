import math
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import F
from django.db.models.query_utils import Q


class OrderItem(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        db_table = "orders_app_order_items"
        unique_together = ("order", "product")
        indexes = [
            models.Index(fields=["order", "product"]),
        ]

    @property
    def num_of_palettes(self):
        """Returns the number of palettes needed to order the product."""
        return math.ceil(self.quantity / self.product.palette_volume)

    @property
    def line_weight(self) -> Decimal:
        """Returns the weight of the order item in kg."""
        return self.product.base_unit_weight * self.quantity

    def __str__(self):
        return (
            f"<OrderItem "
            f"order={self.order} "
            f"product={self.product} "
            f"quantity={self.quantity}>"
        )
