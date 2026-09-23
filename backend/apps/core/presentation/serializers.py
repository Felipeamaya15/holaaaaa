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
        # Determinamos el producto (desde el contexto o desde la instancia existente)
        id_producto = self.context.get('id_producto')
        if not id_producto and self.instance:
            id_producto = self.instance.id_producto

        atributos = data.get('atributos', self.instance.atributos if self.instance else {})

        if id_producto and atributos:
            consulta = VarianteProducto.objects.filter(
                id_producto=id_producto,
                atributos=atributos
            )
            # Si estamos editando una variante existente, la excluimos de la búsqueda de duplicados
            if self.instance:
                consulta = consulta.exclude(pk=self.instance.pk)

            if consulta.exists():
                raise serializers.ValidationError(
                    {"atributos": "Ya existe otra variante con esta misma combinación de atributos para este producto."}
                )
        return data