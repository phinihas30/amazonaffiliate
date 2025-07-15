from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, track_product_click

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('track-product-click/<int:product_id>/', track_product_click, name='track_product_click'),
]
