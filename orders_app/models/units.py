from django.db import models


class Unit(models.Model):
    unit_name = models.CharField(max_length=20, unique=True)
    unit_shortcut = models.CharField(max_length=3, unique=True)
    description = models.TextField()

    to_kg_factor = models.DecimalField(
        max_digits=12,
        decimal_places=6,
        help_text="How many kilograms are in 1 unit of this type.",
    )
