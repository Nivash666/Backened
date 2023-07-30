from rest_framework import serializers
from .models import Shirts,Cartmodel,Shop,Shopproducts,Cartshop

class ConvertData(serializers.ModelSerializer):
    class Meta:
        model = Shirts
        fields = ['id', 'head', 'image', 'shop_name', 'shop_image', 'int_discount_price', 'int_orginal_price']

class Cart(serializers.ModelSerializer):
    class Meta:
        model = Cartmodel
        fields = '__all__' 

class Convertshopmodel(serializers.ModelSerializer):
    class Meta:
        model=Shop
        fields='__all__'
class Convertshopproductmodel(serializers.ModelSerializer):
    class Meta:
        model=Shopproducts
        fields='__all__' 
class Covertcart(serializers.ModelSerializer):
    class Meta:
        model=Cartshop
        fields='__all__'  
class cartpage1(serializers.ModelSerializer):
    class Meta:
        model=Shop
        fields=['shopname','shopimage'] 
                                       