from django.db import models


class Food(models.Model):

    CATEGORY = (
        ('Normal', 'Normal'),
        ('Event', 'Event'),
    )

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='food/')
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Order(models.Model):

    PAYMENT = (
        ('Cash', 'Cash On Delivery'),
        ('UPI', 'UPI Payment'),
    )

    ORDER_STATUS = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('Out For Delivery', 'Out For Delivery'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )

    PAYMENT_STATUS = (
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Failed', 'Failed'),
    )


    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE
    )

    customer_name = models.CharField(
        max_length=100
    )

    mobile = models.CharField(
        max_length=10
    )

    address = models.TextField()

    quantity = models.PositiveIntegerField(
        default=1
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default='Pending'
    )

    order_status = models.CharField(
        max_length=30,
        choices=ORDER_STATUS,
        default='Pending'
    )

    location = models.TextField(
        blank=True,
        null=True
    )

    # Order date and time
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.customer_name} - {self.food.name}"