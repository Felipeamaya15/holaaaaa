from rest_framework import serializers
from apps.core.models import Producto, VarianteProducto

class VarianteProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VarianteProducto
        fields = [
            'id_variante',
            'id_producto',
            'sku',
            'precio',
            'stock',
            'atributos',
            'es_activa',
            'fecha_creacion'
        ]
        read_only_fields = ['id_variante', 'id_producto', 'fecha_creacion']

    def validate_sku(self, value):
        sku_formateado = value.strip().upper()
        if not sku_formateado:
            raise serializers.ValidationError("El SKU no puede ser una cadena vacía.")
        return sku_formateado

    def validate(self, data):
        # Evita duplicar combinaciones de atributos en un mismo producto
        id_producto = self.context.get('id_producto')
        atributos = data.get('atributos', {})

        if id_producto and atributos:
            existe = VarianteProducto.objects.filter(
                id_producto=id_producto,
                atributos=atributos
            ).exists()
            if existe:
                raise serializers.ValidationError(
                    {"atributos": "Ya existe una variante con esta misma combinación de atributos."}
                )
        return data