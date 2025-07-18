from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

class AffiliateProduct(models.Model):
    # Basic product information
    name = models.CharField(max_length=255)
    product_image_link = models.URLField(max_length=1024)
    affiliate_full_link = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    # Review section for Google AdSense content
    review_title = models.CharField(max_length=300, blank=True, help_text="SEO-friendly review title")
    review_content = models.TextField(blank=True, help_text="Detailed review content for AdSense")
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True, blank=True,
        help_text="Rating from 1 to 5 stars"
    )
    pros = models.TextField(blank=True, help_text="Product advantages (one per line)")
    cons = models.TextField(blank=True, help_text="Product disadvantages (one per line)")
    review_summary = models.TextField(blank=True, help_text="Brief summary of the review")
    slug = models.SlugField(max_length=300, blank=True, help_text="SEO-friendly URL slug")

    # Additional metadata
    is_featured = models.BooleanField(default=False, help_text="Feature this product review")
    review_published = models.BooleanField(default=False, help_text="Publish the review")

    def save(self, *args, **kwargs):
        # Auto-generate slug from name if not provided
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_pros_list(self):
        """Return pros as a list"""
        return [pro.strip() for pro in self.pros.split('\n') if pro.strip()]

    def get_cons_list(self):
        """Return cons as a list"""
        return [con.strip() for con in self.cons.split('\n') if con.strip()]

    def get_star_rating(self):
        """Return star rating as string for display"""
        if self.rating:
            return '★' * self.rating + '☆' * (5 - self.rating)
        return 'No rating'

# Remove Click model
# Add Eye model to track product views
class ProductClick(models.Model):
    product_name = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)