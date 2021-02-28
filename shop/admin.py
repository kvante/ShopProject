from django.contrib import admin

from .models import Product, Category, Type, Comment

admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Type)
