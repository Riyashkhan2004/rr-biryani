from django.contrib import admin
from .models import Food, Order


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "category",
        "price",
        "available",
    )

    list_filter = (
        "category",
        "available",
    )

    search_fields = (
        "name",
        "category",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "food",
        "customer_name",
        "mobile",
        "quantity",
        "total_amount",
        "payment_method",
        "payment_status",
        "order_status",
        "created_at",
    )

    list_filter = (
        "payment_method",
        "payment_status",
        "order_status",
    )

    search_fields = (
        "customer_name",
        "mobile",
        "food__name",
    )