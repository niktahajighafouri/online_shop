from django.contrib import admin
from .models import Product, Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    raw_id_fields = ('sub_category',)
    list_display = ('name', 'slug', 'is_sub')

class ProductAdmin(admin.ModelAdmin):
    raw_id_fields = ['category',]
    list_display = ('id', 'name')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)