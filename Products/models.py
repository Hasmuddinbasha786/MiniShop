from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Brand(models.Model):
    name = models.CharField(max_length=100,unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='brands',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='products')
    # each product belongs to one category
    # one category has many products

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products',null=True,blank=True)
    # brand

    name = models.CharField(max_length=200)

    image = models.ImageField(upload_to='products')
    price = models.DecimalField(max_digits=10,decimal_places=2)
    # don't use float in money it causes rounding(round figure) errors
    description = models.TextField()
    stock = models.PositiveIntegerField(default=0) #allows 0 or positive numbers no -ve no's
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
