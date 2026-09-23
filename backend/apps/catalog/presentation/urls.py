from django.urls import path
from .views import PublicProductListAPIView

urlpatterns = [
    path('productos/', PublicProductListAPIView.as_view(), name='api_public_product_list'),
]
