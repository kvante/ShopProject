from rest_framework import serializers
from .models import Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name')


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'price', 'stock', 'available', 'created', 'updated')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'text')
