from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(null=False,default=1)
    

    def __str__(self) -> str:
        return self.product.title
    
    def total_price(self):
        return self.product.price * self.quantity
