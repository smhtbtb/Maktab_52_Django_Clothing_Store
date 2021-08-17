from rest_framework import serializers

from product.models import *


class BrandSerializer(serializers.ModelSerializer):
    product = serializers.HyperlinkedRelatedField(view_name='product:api_product_detail_view', source='product_set',
                                                  many=True, read_only=True)

    class Meta:
        model = Brand
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    product = serializers.HyperlinkedRelatedField(view_name='product:api_product_detail_view', source='product_set',
                                                  many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):
    product = serializers.HyperlinkedRelatedField(view_name='product:api_product_detail_view', source='product_set',
                                                  many=True, read_only=True)

    class Meta:
        model = Discount
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.HyperlinkedRelatedField(view_name='product:api_brand_detail_view', read_only=True,
                                                lookup_field='name', lookup_url_kwarg='name')
    category = serializers.HyperlinkedRelatedField(view_name='product:api_category_detail_view', read_only=True)
    discount = serializers.HyperlinkedRelatedField(view_name='product:api_discount_detail_view', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
