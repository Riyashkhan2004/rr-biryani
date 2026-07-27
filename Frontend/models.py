from django.db import models

class Food(models.Model):
    CATEGORY = (
        ('Normal', 'Normal'),
        ('Event', 'Event'),
    )

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY)
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='food/')
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
