from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView
)
from .models import Product, Category, Type, Comment
from .serializers import ProductSerializer, CategorySerializer, TypeSerializer, CommentSerializer


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TypeCreateView(CreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
