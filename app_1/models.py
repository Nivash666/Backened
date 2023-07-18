from django.db import models

# Create your models here.

 
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
    @classmethod
    def all_datas(cls):
         return cls.objects.all()