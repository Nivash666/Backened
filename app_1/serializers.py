from rest_framework import serializers
from .models import Shirts

class ConvertData(serializers.ModelSerializer):
    class Meta:
        model=Shirts
        fields=['id','head','image','shop_name','shop_image','int_discount_price','int_orginal_price']
       