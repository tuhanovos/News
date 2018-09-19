from django.contrib import admin

from .models import UserCreateNews, CategoriesNews

# Register your models here.


admin.site.register(UserCreateNews)
admin.site.register(CategoriesNews)
