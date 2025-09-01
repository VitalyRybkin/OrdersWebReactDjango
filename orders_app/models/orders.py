from decimal import Decimal

from django.db import models
from django.db.models import F, Sum


class Order(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.PROTECT)
    client = models.ForeignKey("Client", on_delete=models.PROTECT)
    stock = models.ForeignKey("Stock", on_delete=models.PROTECT)
    carrier = models.ForeignKey("Carrier", on_delete=models.PROTECT)
    driver = models.ForeignKey("Driver", on_delete=models.PROTECT)
    truck = models.ForeignKey("Truck", on_delete=models.PROTECT)

    products = models.ManyToManyField(
        "Product", through="OrderItem", related_name="orders"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Status(models.TextChoices):
        ACTIVE = "активно", "Активно"
        CANCELED = "отменено", "Отменено"
        DELIVERED = "доставлено", "Доставлено"

    status = models.CharField(
        max_length=12, choices=Status.choices, default=Status.ACTIVE
    )

    comment = models.TextField(null=True, blank=True)
    confirmation_file = models.FileField(
        upload_to="orders_app/confirmations/", null=True, blank=True
    )

    @property
    def items(self):
        return self.orderitem_set.select_related("product")

    @property
    def total_weight(self):
        result = self.items.aggregate(
            total=Sum(F("product__base_unit_weight") * F("quantity"))
        )["total"]
        return result or Decimal("0.000")

    def __str__(self):
        return (
            f"<Order user={self.user} "
            f"client={self.client} "
            f"stock={self.stock} "
            f"carrier={self.carrier} "
            f"driver={self.driver} "
            f"truck={self.truck} "
            f"status={self.status}>"
        )
