from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(blank=True,null=True)
    ram = models.IntegerField()
    color = models.CharField(max_length=20)
    memory = models.IntegerField()

    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.name} {self.ram}"
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product =  models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id}"
    
class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 

    def __str__(self) -> str:
        return f"{self.text}..."
    
class Like(models.Model):
    like = models.BooleanField(default=False, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 

    def __str__(self) -> str:
        return f"{self.id}"

