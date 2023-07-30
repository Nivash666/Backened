from django.db import models

# Create your models here.
import random
 
class Shirts(models.Model):
    image=models.CharField(max_length=200)
    head=models.CharField(max_length=200)
    discount_price=models.CharField(max_length=10)
    orginal_price=models.CharField(max_length=10)
    discount=models.CharField(max_length=10)
    advertise=models.BooleanField(default="False")
    rating_img=models.ImageField(upload_to='pics')
    day=models.CharField(max_length=10)
    date=models.IntegerField(default=1)
    users=models.CharField(max_length=30)
    type=models.CharField(max_length=20)
    int_discount_price=models.IntegerField()
    int_orginal_price=models.IntegerField() 
    fashion_model=models.CharField(max_length=100) 
    shop_name=models.CharField(max_length=100,default="None")
    shop_image=models.CharField(max_length=1000,default="None")     
    
    def all_datas(cls):
         return cls.objects.all()
class Cartmodel(models.Model):
    shop_image=models.CharField(max_length=100000)
    shop_name=models.CharField(max_length=100)
    product_image=models.CharField(max_length=10000)
    product_name=models.CharField(max_length=100)
    product_price=models.IntegerField()     


class Shop(models.Model):
    shopname=models.CharField(max_length=50)
    shopimage=models.CharField(max_length=100000)
class Shopproducts(models.Model):
    product_image=models.CharField(max_length=10000)
    product_name=models.CharField(max_length=100)
    product_price=models.IntegerField()
    shop=models.ForeignKey(Shop,on_delete=models.CASCADE,related_name='children')

class Cartshop(models.Model):
    Cartproductname=models.CharField(max_length=300)
    Cartproductimage=models.CharField(max_length=100000)
    Cartproductprice=models.IntegerField()
    shop=models.ForeignKey(Shop,on_delete=models.CASCADE,related_name='cartshopchildren')

