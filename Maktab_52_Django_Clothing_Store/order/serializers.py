from rest_framework import serializers, status
from rest_framework.response import Response

from order.models import *


class OrderSerializer(serializers.ModelSerializer):
    # user = serializers.HyperlinkedRelatedField(view_name='customer:user_detail', read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = '__all__'

