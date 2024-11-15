from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')

    def __str__(self) -> str:
        return self.title