from rest_framework import generics
from rest_framework.exceptions import NotFound
from apps.core.models import Producto, VarianteProducto
from .serializers import VarianteProductoSerializer


class VarianteProductoListCreateView(generics.ListCreateAPIView):
    serializer_class = VarianteProductoSerializer
    authentication_classes = []

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
        serializer.save(id_producto=self.get_producto())


class VarianteProductoDetailView(generics.RetrieveUpdateAPIView):
    """
    Permite consultar (GET) y actualizar (PUT / PATCH) 
    los datos editables de una variante específica.
    """
    serializer_class = VarianteProductoSerializer
    authentication_classes = []
    lookup_field = 'id_variante'
    lookup_url_kwarg = 'id_variante'

    def get_producto(self):
        id_producto = self.kwargs.get('id_producto')
        try:
            return Producto.objects.get(id_producto=id_producto)
        except Producto.DoesNotExist:
            raise NotFound(detail=f"No existe un producto con el id {id_producto}.")

    def get_queryset(self):
        # Valida que el producto exista y restringe la búsqueda a sus variantes
        return VarianteProducto.objects.filter(id_producto=self.get_producto())

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['id_producto'] = self.kwargs.get('id_producto')
        return context