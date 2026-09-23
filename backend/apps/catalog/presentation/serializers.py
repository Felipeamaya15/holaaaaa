from rest_framework import serializers


class ProductPublicListItemSerializer(serializers.Serializer):
    id = serializers.CharField(source="_id")
    nombre = serializers.CharField()
    slug = serializers.CharField()
    categoria = serializers.CharField()
    imagen = serializers.SerializerMethodField()
    precio = serializers.SerializerMethodField()
    precio_oferta = serializers.SerializerMethodField()
    disponible = serializers.SerializerMethodField()

    def get_imagen(self, producto):
        imagenes = producto.get("imagenes") or []
        return imagenes[0] if imagenes else None

    def _variantes(self, producto):
        return producto.get("variantes") or []

    def get_precio(self, producto):
        precios = [v["precio"] for v in self._variantes(producto) if v.get("precio") is not None]
        return min(precios) if precios else None

    def get_precio_oferta(self, producto):
        ofertas = [
            v["precio_oferta"] for v in self._variantes(producto)
            if v.get("precio_oferta") is not None
        ]
        return min(ofertas) if ofertas else None

    def get_disponible(self, producto):
        return any((v.get("stock") or 0) > 0 for v in self._variantes(producto))
