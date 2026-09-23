from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status

from apps.core.presentation.responses import success_response
from apps.core.infrastructure.tenant import resolver_tienda_id
from apps.catalog.infrastructure.repositories import ProductRepository
from apps.catalog.application.use_cases import ListPublicProductsUseCase
from .serializers import ProductPublicListItemSerializer


class PublicProductListAPIView(APIView):
    """Listado público de productos activos del catálogo (Scrum 218)."""
    permission_classes = [AllowAny]

    def get(self, request):
        tienda_id = resolver_tienda_id(request)

        use_case = ListPublicProductsUseCase(ProductRepository())
        productos = use_case.execute(tienda_id)

        data = ProductPublicListItemSerializer(productos, many=True).data

        return success_response(
            data=data,
            mensaje="Listado de productos obtenido correctamente",
            status=status.HTTP_200_OK,
        )
