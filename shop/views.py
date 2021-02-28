from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView
)
from .models import Product, Category, Type, Comment
from .serializers import ProductSerializer, CategorySerializer, TypeSerializer, CommentSerializer


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = TypeSerializer


class CategoryDeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = TypeSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = TypeSerializer


class TypeCreateView(CreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class TypeUpdateView(RetrieveAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class TypeDeleteView(DestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class TypeListView(ListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentUpdateView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDeleteView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = CommentSerializer
