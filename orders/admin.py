from django.contrib import admin
from .models import Order, ShippingAddress, OrderItem


# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ('product',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'updated', 'paid')
    list_filter = ('paid',)
    inlines = (OrderItemInline,)


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('order', 'city', 'address', 'postalCode')
    raw_id_fields = ('order',)
    search_fields = ('postalCode',)


admin.site.register(Order, OrderAdmin)
admin.site.register(ShippingAddress)
