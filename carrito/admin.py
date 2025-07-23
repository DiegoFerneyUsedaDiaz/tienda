from django.contrib import admin

# Register your models here.
from .models import Producto, Carrito, ItemCarrito

admin.site.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cantidad')
    search_fields = ('nombre',)
    
admin.site.register(Carrito)    
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('id',)
    
    
admin.site.register(ItemCarrito)
class ItemCarritoAdmin(admin.ModelAdmin):
    list_display = ('carrito', 'producto', 'cantidad')
    search_fields = ('carrito__id', 'producto__nombre') 