from rest_framework import serializers
from .models import products

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = [
            'title',
            'content',
            'price',
            'sales_price',
            'get_discount',
        ]