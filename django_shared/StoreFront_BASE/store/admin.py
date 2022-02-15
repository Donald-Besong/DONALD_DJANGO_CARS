from django.contrib import admin
from .models import Product, Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    populated_fields = {'slug': ('name',)}
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','category', 'price', 'stock','available','created', 'updated']
    list_filter = ['category', 'available','created', 'updated']
    list_editable = ['price', 'stock','available']
    populated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
