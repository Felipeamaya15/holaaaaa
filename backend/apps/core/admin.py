from django.contrib import admin
from apps.core.models import Usuario, Tienda, Producto, VarianteProducto

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'correo', 'nombre', 'apellido', 'rol')
    search_fields = ('correo', 'nombre', 'apellido')

@admin.register(Tienda)
class TiendaAdmin(admin.ModelAdmin):
    list_display = ('id_tienda', 'nombre', 'id_usuario_propietario', 'fecha_creacion')
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre', 'precio', 'stock', 'id_tienda')
    search_fields = ('nombre',)
    list_filter = ('id_tienda',)

@admin.register(VarianteProducto)
class VarianteProductoAdmin(admin.ModelAdmin):
    list_display = ('id_variante', 'sku', 'id_producto', 'precio', 'stock', 'es_activa')
    search_fields = ('sku',)
    list_filter = ('es_activa',)
