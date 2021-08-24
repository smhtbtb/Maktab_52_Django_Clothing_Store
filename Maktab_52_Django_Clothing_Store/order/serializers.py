from rest_framework import serializers, status
from rest_framework.response import Response

from order.models import *


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='customer:user_detail', read_only=True)
    Items = serializers.HyperlinkedRelatedField(view_name='order:api_order_item_detail_view', many=True,
                                                read_only=True, source='orders')

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    order = serializers.HyperlinkedRelatedField(view_name='order:api_orders_detail_view', read_only=True)
    product = serializers.HyperlinkedRelatedField(view_name='product:api_product_detail_view', read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'
