from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.name