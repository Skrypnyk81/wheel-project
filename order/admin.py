from django.contrib import admin
from .models import *


class ImagesInLine(admin.TabularInline):
    model = WheelsImage
    extra = 1


class OrderInline(admin.StackedInline):
    model = Order
    extra = 0  # set to 0 if you don't want empty forms
    readonly_fields = [
        'first_name', 'second_name', 'phone', 'street',
        'city', 'state', 'postal_code', 'email', 'created_at'
    ]


class CustomerAdmin(admin.ModelAdmin):
    inlines = [ImagesInLine, OrderInline]


admin.site.register(Wheel, CustomerAdmin)
admin.site.register(Order)
