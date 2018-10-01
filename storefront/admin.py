from django import forms
from django.contrib import admin
from . import models

from .models import Order, OrderItem, Product


class OrderAdminForm(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea)

    class Meta:
        fields = '__all__'
        model = Order


class OrderItemsInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm

    list_display = ('name', 'email', 'phone', 'address')
    list_display_links = list_display

    fieldsets = (
        ('Details', {
            'fields': ('name', 'email', 'phone', 'address', 'order_date'),
        }),
    )

    inlines = [
        OrderItemsInline
    ]

    ordering = ['-id']


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        fields = '__all__'
        model = Product


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

    list_display = ('name', 'price', 'in_stock', 'description')
    list_display_links = list_display

    fieldsets = (
        ('Info', {
            'fields': ('name', 'description', 'price', 'in_stock'),
        }),
        ('Media', {
            'fields': ('picture', 'picture_thumbnail')
        })
    )

    ordering = ['name', 'price', 'in_stock', 'description']


admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
