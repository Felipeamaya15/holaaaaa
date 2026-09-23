from django.urls import path
from .views import PublicProductListAPIView, PublicProductDetailAPIView

urlpatterns = [
    path('productos/', PublicProductListAPIView.as_view(), name='api_public_product_list'),
    path('productos/<slug:slug>/', PublicProductDetailAPIView.as_view(), name='api_public_product_detail'),
]
