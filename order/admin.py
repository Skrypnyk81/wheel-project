from django.contrib import admin
from .models import *


class ImagesInLine(admin.TabularInline):  # or use admin.StackedInline for a different layout
    model = WheelsImage
    extra = 1


class CustomerAdmin(admin.ModelAdmin):
    inlines = [ImagesInLine]


admin.site.register(Wheel, CustomerAdmin)
admin.site.register(Order)
