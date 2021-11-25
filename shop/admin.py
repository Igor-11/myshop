from django.contrib import admin
from .models import Category, Product, Stock

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'rating', 'price', 'category')

class StockAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Stock, StockAdmin)

