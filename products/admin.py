from django.contrib import admin
from .models import Products,Email
# Register your models here.
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["name","price"]

admin.site.register(Email)
