from django.contrib import admin
from .models import Restaurant, Item


class AdminRestaurants(admin.ModelAdmin):
    list_display = ('name', 'location',)


class AdminItems(admin.ModelAdmin):
    list_display = ('item_name', 'item_price', 'restaurant',)


admin.site.register(Restaurant, AdminRestaurants)
admin.site.register(Item, AdminItems)
