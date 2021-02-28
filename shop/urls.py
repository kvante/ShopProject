from django.urls import path

from .views import *

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
app_name = 'shop'


urlpatterns = [
    path('stream/create', ProductCreateView.as_view()),
]