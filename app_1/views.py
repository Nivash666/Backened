from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import json
from django.utils.decorators import method_decorator
from app_1.models import Shirts
import random
from .serializers import ConvertData
from rest_framework.response import Response
from rest_framework.views import APIView
from .decorators import validate_aws_cognito_token
from rest_framework.permissions import IsAuthenticated
from .authentication import CognitoJWTAuthentication
#@validate_aws_cognito_token
#class Hello(APIView):
#    def get(self, request):
#          response={'msg':'hello'}
#          return Response(response)
# views.py

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def protected_api_view(request):
    # Your protected API logic here
    return JsonResponse({"message": "This is a protected API."})
    

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
