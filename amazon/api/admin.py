from django.contrib import admin
from .models import AffiliateProduct

@admin.register(AffiliateProduct)
class AffiliateProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'rating', 'is_featured', 'review_published', 'created_at']
    list_filter = ['rating', 'is_featured', 'review_published', 'created_at']
    search_fields = ['name', 'review_title', 'review_content']
    list_editable = ['is_featured', 'review_published']
    prepopulated_fields = {'slug': ('name',)}

    fieldsets = (
        ('Product Information', {
            'fields': ('name', 'product_image_link', 'affiliate_full_link', 'price')
        }),
        ('Review Content (for AdSense)', {
            'fields': ('review_title', 'review_content', 'rating', 'review_summary'),
            'description': 'Add detailed review content to improve AdSense performance'
        }),
        ('Pros & Cons', {
            'fields': ('pros', 'cons'),
            'description': 'Enter one point per line'
        }),
        ('SEO & Publishing', {
            'fields': ('slug', 'is_featured', 'review_published'),
            'classes': ('collapse',)
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).order_by('-created_at')
