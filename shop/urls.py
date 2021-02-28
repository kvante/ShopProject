from django.urls import path

from .views import *

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
app_name = 'shop'


urlpatterns = [
    path('stream/create', ProductCreateView.as_view()),
    path('product/create', ProductCreateView.as_view()),
    path('product/delete', ProductDeleteView.as_view()),
    path('product/update', ProductUpdateView.as_view()),
    path('product/list', ProductListView.as_view()),
    path('category/create', CategoryCreateView.as_view()),
    path('category/delete', CategoryDeleteView.as_view()),
    path('category/update', CategoryUpdateView.as_view()),
    path('category/list', CategoryListView.as_view()),
    path('comment/create', CommentCreateView.as_view()),
    path('comment/delete', CommentDeleteView.as_view()),
    path('comment/update', CommentUpdateView.as_view()),
    path('comment/list', CommentListView.as_view()),
]