from django.contrib import admin

from orders_app.models import (
    AppUnit,
    Carrier,
    Driver,
    Product,
    ProductWeight,
    Stock,
    Truck,
    TruckCapacity,
    TruckType,
)


class ProductUnitInline(admin.TabularInline):
    model = ProductWeight
    extra = 0
    fields = ("unit", "kg_per_unit")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductUnitInline,)

    list_display = ("product_name", "palette_volume", "description")
    list_filter = ("product_name",)
    search_fields = ("product_name",)
    ordering = ("product_name",)
    filter_horizontal = ()
    fieldsets = ()
    readonly_fields = ()


@admin.register(AppUnit)
class UnitAdmin(admin.ModelAdmin):
    inlines = (ProductUnitInline,)

    list_display = ("unit_name", "unit_shortcut", "to_kg_factor", "is_weight_based")
    list_display_links = ("unit_name",)
    list_filter = ("unit_name",)
    search_fields = ("unit_name",)
    ordering = ("unit_name",)


@admin.register(ProductWeight)
class ProductWeightAdmin(admin.ModelAdmin):
    list_display = ("product", "unit_shortcut", "kg_per_unit")
    list_filter = ("product", "product_unit")
    search_fields = ("product",)
    ordering = ("product", "product_unit")

    def unit_shortcut(self, obj):
        return obj.unit.unit_shortcut


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("stock_name", "address", "description")
    ordering = ("stock_name",)


@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    list_display = ("carrier", "truck_type", "truck_capacity", "description")
    ordering = ("carrier", "truck_type", "truck_capacity")


@admin.register(TruckType)
class TruckTypeAdmin(admin.ModelAdmin):
    list_display = ("truck_type", "description")
    ordering = ("truck_type",)


@admin.register(TruckCapacity)
class TruckCapacityAdmin(admin.ModelAdmin):
    list_display = ("truck_capacity", "description")
    ordering = ("truck_capacity",)


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("driver_name", "carrier")


@admin.register(Carrier)
class CarrierAdmin(admin.ModelAdmin):
    list_display = ("carrier_name", "description")
    ordering = ("carrier_name",)
