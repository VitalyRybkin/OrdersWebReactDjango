from django.contrib import admin

from orders_app.models import Product, Unit, ProductWeight


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


@admin.register(Unit)
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
    list_filter = ("product", "unit")
    search_fields = "product",
    ordering = ("product", "unit")

    def unit_shortcut(self, obj):
        return obj.unit.unit_shortcut
