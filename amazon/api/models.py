from django.db import models
from django.utils import timezone

class AffiliateProduct(models.Model):
    name = models.CharField(max_length=255)
    product_image_link = models.URLField(max_length=1024)
    affiliate_full_link = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

# Remove Click model
# Add Eye model to track product views
class ProductClick(models.Model):
    product_name = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)