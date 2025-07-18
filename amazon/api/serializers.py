from rest_framework import serializers
from .models import AffiliateProduct

class AffiliateProductSerializer(serializers.ModelSerializer):
    # Add computed fields for better API response
    pros_list = serializers.ReadOnlyField(source='get_pros_list')
    cons_list = serializers.ReadOnlyField(source='get_cons_list')
    star_rating = serializers.ReadOnlyField(source='get_star_rating')

    class Meta:
        model = AffiliateProduct
        fields = '__all__'

    def to_representation(self, instance):
        """Customize the serialized output"""
        data = super().to_representation(instance)

        # Add helpful computed fields
        data['has_review'] = bool(instance.review_content)
        data['review_word_count'] = len(instance.review_content.split()) if instance.review_content else 0

        return data
