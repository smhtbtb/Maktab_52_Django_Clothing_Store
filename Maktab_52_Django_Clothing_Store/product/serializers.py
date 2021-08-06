from rest_framework import serializers

from product.models import *


class BrandSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Brand
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Discount
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # brands = BrandSerializer(read_only=True, many=True)
    # category = CategorySerializer(read_only=True, many=True)
    # discount = DiscountSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = '__all__'
