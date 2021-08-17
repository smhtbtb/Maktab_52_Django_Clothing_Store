from rest_framework import serializers

from customer.models import *


class UserBriefSerializer(serializers.ModelSerializer):
    # id = serializers.HyperlinkedRelatedField(view_name='customer:user_detail', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'phone', 'first_name', 'last_name']


class UserSerializer(serializers.ModelSerializer):
    # addresses = serializers.HyperlinkedRelatedField(view_name='customer:address_detail', read_only=True,
    #                                                 source='address_set')

    class Meta:
        model = User
        exclude = ['password']


class AddressBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'city', 'owner']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'














