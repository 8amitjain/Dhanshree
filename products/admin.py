from django.contrib import admin
from .models import (
    Category, Product, ParentCategory, ProductContact
)
from import_export.admin import ImportExportModelAdmin


class ProductsAdmin(ImportExportModelAdmin):
    pass


class VariationAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Product, ProductsAdmin)
admin.site.register(ProductContact)
# admin.site.register(Variation, VariationAdmin)

admin.site.register(Category)
admin.site.register(ParentCategory)
