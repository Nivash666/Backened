from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import json
from django.utils.decorators import method_decorator
from app_1.models import Shirts,Cartmodel,Shop,Shopproducts,Cartshop
import random
from .serializers import ConvertData,Cart,Convertshopmodel,Convertshopproductmodel,cartpage1,Covertcart
from rest_framework.response import Response
from rest_framework.views import APIView
from .decorators import requires_authentication
from rest_framework.generics import ListAPIView  
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# views.py
class MyProtectedView(ListAPIView):
    queryset=Shop.objects.all()
    serializer_class=Convertshopmodel#ConvertData

    def list(self, request,*args,**kwargs):
        queryset=self.get_queryset()
        print(request.user.username)
        serializer=self.get_serializer(queryset,many=True)
        return Response(serializer.data)    
class retiveShop(APIView):
    def get(self,request,pk):
          try:
               shop_data=Shop.objects.get(shopname=pk)
               related_datas=shop_data.children.all()
               serializer=Convertshopproductmodel(related_datas,many=True)
               return Response(serializer.data,status=status.HTTP_200_OK)
          except Shop.DoesNotExist:
               return Response({'error':'shop not found'})            
from django.db.models import Count
from .models import Shop,Shopproducts        
class CartView(APIView):
    def get(self,request):
        shop_datas=Shirts.objects.values_list('shop_name','shop_image').distinct()
        values=Cartmodel.objects.values('shop_name').annotate(count=Count('shop_name'))
        datas=Shop.objects.prefetch_related('cartshopchildren').filter(cartshopchildren__isnull=False).distinct()
        alldatas=Shop.objects.prefetch_related('cartshopchildren')
        cartonlyshop=datas.values_list('shopname','shopimage').distinct()
        cart1=datas.values('shopname','shopimage').distinct()
        serializer=Convertshopmodel(datas,many=True)
       #obj,created=Shop.objects.get_or_create(shop=data)
        #for i in values:
        #    shop_nam=i['shop_name']
        #    shop_nam=i['shop_name']
        #    cart_items=list(Cartmodel.objects.filter(shop_name=shop_nam))
        #    li.extend(cart_items)
    
        return Response(serializer.data)
    
    
    def post(self, request):
         data=request.data
         product_name=request.data['product_name']
         product_image=request.data['product_image']
         product_price=request.data['product_price']
         shopdatas=Shop.objects.get(id=request.data['shop'])
         
         cart=Cartshop.objects.create(Cartproductname=product_name,
                                  Cartproductimage=product_image,
                                  Cartproductprice=product_price,
                                  shop=shopdatas)
         cart.save()
         print("successfully created")
         return Response('success')
    #    serializer = Cart(data=request.data)
    #    
    #    if serializer.is_valid():
    #        serializer.save()
    #        print("successfully created")
    #        return Response({'msg': 'successfully created'})
    #    else:
    #       print("yess it error")
    #       print(serializer.errors)
    #       return Response(serializer.errors)
    #    
class RetriveCartShop(APIView):
     def get(self,request,pk):
          print(request.user)
          cart=Shop.objects.get(shopname=pk)
          datas=cart.cartshopchildren.all()
          serializer=Covertcart(datas,many=True)
          print(cart)
          return Response(serializer.data)


#def randon_name():
#   shop_names= ["chennaisilks", 
#                "parvathiys", 
#                "", 
#                "Fashionsilks"]
#   return random.choice(shop_names)
 
#print hello world











#from django.http import JsonResponse
#from django.contrib.auth.decorators import login_required
#
#def protected_api_view(request):
#    return JsonResponse({"msg": "This is a protected API."})
    

#@cognito_jwt_auth_required
#def list_all_products(request):
#    datas=Shirts.objects.all()
#    serializer = ConvertData(datas, many=True)
#    print(serializer.data)
#    return JsonResponse({'data':serializer.data})
#@method_decorator(cognito_jwt_auth_required,name='dispatch')
#class Shops(APIView):
#    def get(self, request):
#      datas = Shirts.objects.all()
#      serializer = ConvertData(datas, many=True)
#      return Response({'datas': serializer.data})





# ef create(request):
    #for item in Shirts.objects.all():
    #   random_field = random.choice(obj)
    #   item.shop_name=random_field['name']
    #   item.shop_image=random_field['image_url']
    #   item.save()
    #print("successfully completed")   
    #return render(request,"templates/create.html")     
#import codecs

#def create(request):
#
#     input_file = 'shirts.json'
#     output_file = 'data_utf8.json'
#     
#     with codecs.open(input_file, 'r', encoding='utf-16') as f_in:
#         content = f_in.read()
#     
#     with codecs.open(output_file, 'w', encoding='utf-8') as f_out:
#         f_out.write(content)
#
#
#    
#     return render(request,"index.html")
