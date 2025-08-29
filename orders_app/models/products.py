from django.db import models


class Products(models.Model):
    product_name = models.CharField(max_length=100)
    base_unit = models.ForeignKey("Units", on_delete=models.CASCADE, related_name="base_unit")
    base_unit_weight = models.SmallIntegerField(null=True)
    report_unit = models.ForeignKey("Units", on_delete=models.CASCADE, related_name="report_unit")
    report_unit_ratio = models.SmallIntegerField(null=True)
    palette_volume = models.SmallIntegerField(null=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return (
            f"<Product product_name={self.product_name} "
            f"base_unit={self.base_unit} "
            f"report_unit={self.report_unit}> "
            f"report_unit_ratio={self.report_unit_ratio} "
            f"palette_volume={self.palette_volume} "
            f"description={self.description}"
        )
