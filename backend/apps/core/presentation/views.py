from rest_framework import generics
from rest_framework.exceptions import NotFound
from apps.core.models import Producto, VarianteProducto
from .serializers import VarianteProductoSerializer

class VarianteProductoListCreateView(generics.ListCreateAPIView):
    serializer_class = VarianteProductoSerializer

    def get_producto(self):
        id_producto = self.kwargs.get('id_producto')
        try:
            return Producto.objects.get(id_producto=id_producto)
        except Producto.DoesNotExist:
            raise NotFound(detail=f"No existe un producto con el id {id_producto}.")

    def get_queryset(self):
        return VarianteProducto.objects.filter(id_producto=self.get_producto())

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['id_producto'] = self.kwargs.get('id_producto')
        return context

    def perform_create(self, serializer):
        # Asocia automáticamente la variante al producto indicado en la URL
        serializer.save(id_producto=self.get_producto())