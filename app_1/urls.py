from django.urls import path
from . import views
urlpatterns = [
    path("hello/",views.protected_api_view,name="hello"),
   #path("list_datas/",views.Shops.as_view(),name="listdatas"),
   #path("allshops/",views.list_all_products,name="allshops"),
]
