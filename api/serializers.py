from rest_framework import serializers
from address.models import Address
from billing_profile.models import BillingProfile
from cart.models import Cart
from order_manager.models import Order
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'

class BillingSerializer(serializers.ModelSerializer):

    class Meta:
        model = BillingProfile
        fields = '__all__'

