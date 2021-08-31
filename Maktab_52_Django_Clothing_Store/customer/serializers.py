from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from customer.models import *


# User Brief Serializer
class UserBriefSerializer(serializers.ModelSerializer):
    addresses = serializers.HyperlinkedRelatedField(view_name='customer:address_detail', source='address_set',
                                                    many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'phone', 'first_name', 'last_name', 'addresses']


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    addresses = serializers.HyperlinkedRelatedField(view_name='customer:address_detail', source='address_set',
                                                    many=True, read_only=True)

    class Meta:
        model = User
        exclude = ['password']


# Address Brief Serializer
class AddressBriefSerializer(serializers.ModelSerializer):
    owner = serializers.HyperlinkedRelatedField(view_name='customer:user_detail', read_only=True)

    class Meta:
        model = Address
        fields = ['id', 'city', 'owner']


# Address Serializer
class AddressSerializer(serializers.ModelSerializer):
    owner = serializers.HyperlinkedRelatedField(view_name='customer:user_detail', read_only=True)

    class Meta:
        model = Address
        fields = '__all__'


# Login Serializer
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['phone'] = user.phone
        return token


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all()), phone_validator]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('phone', 'password', 'password2', 'email', 'first_name', 'last_name')
        # extra_kwargs = {
        #     'first_name': {'required': True},
        #     'last_name': {'required': True}
        # }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            phone=validated_data['phone'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
