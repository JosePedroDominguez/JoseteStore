from django.contrib import admin
from .models import Items, Tag, Marca, ImagenProducto
from .forms import FomularioItem
# Register your models here.


class ImagenProductoAdmin(admin.TabularInline):
    model = ImagenProducto

#### new####


# class ImagenProductoAdmin(modeladmin.StackedInline):
 #   model = ImagenProducto


class ItemsAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "description", "marca", "tag"]
    list_editable = ["price"]
    search_fields = ["name"]
    list_filter = ["tag", "marca"]
    list_per_page = 5
    form = FomularioItem
    inlines = [
        ImagenProductoAdmin
    ]


admin.site.register(Items, ItemsAdmin)
admin.site.register(Tag)
admin.site.register(Marca)
