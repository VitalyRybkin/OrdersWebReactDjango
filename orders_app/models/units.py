from django.db import models


class Unit(models.Model):
    unit_name = models.CharField(max_length=20, unique=True)
    unit_shortcut = models.CharField(max_length=3, unique=True)
    is_weight_based = models.BooleanField(default=True)

    to_kg_factor = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        help_text="Conversion factor to kilograms (if weight-based). For non-weight units, leave as 1.",
    )

    def __str__(self):
        return f"ЕДИНИЦА ИЗМЕРЕНИЯ: {self.unit_name}"
