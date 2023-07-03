from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    lat = models.FloatField()
    long = models.FloatField()
    cuisines = models.CharField(max_length=100,null=True)
    currency = models.CharField(max_length=50,null=True)
    price_range = models.IntegerField(null=True)
    has_table_booking = models.CharField(max_length=200,null=True)
    is_delevering_now = models.IntegerField(null=True)
    opentable_support = models.IntegerField(null=True)
    has_online_delivery = models.IntegerField(null=True)
    include_bogo_offer = models.BooleanField(null=True)
    average_cost_for_two = models.IntegerField(null=True)
    switch_to_order_menu = models.IntegerField(null=True)
    is_book_form_web_view = models.IntegerField(null=True)
    bookform_webview_url = models.URLField(null=True)
    istable_reservation_supported = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.name


class Item(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    item_price = models.IntegerField()
