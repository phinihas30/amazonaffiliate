from rest_framework import viewsets, filters
from .models import AffiliateProduct, ProductClick
from .serializers import AffiliateProductSerializer
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    queryset = AffiliateProduct.objects.all()
    serializer_class = AffiliateProductSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at', 'price']

@api_view(['GET'])
def track_product_click(request, product_id):
    try:
        product = AffiliateProduct.objects.get(id=product_id)
        ProductClick.objects.create(product_name=product.name)
        return HttpResponseRedirect(product.affiliate_full_link)
    except AffiliateProduct.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)