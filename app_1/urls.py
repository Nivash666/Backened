from django.urls import path
from . import views
urlpatterns = [
    path("hello/",views.MyProtectedView.as_view(),name="hello"),
    #path("store/",views.store_values,name="store"),
   #path("list_datas/",views.Shops.as_view(),name="listdatas"),
   #path("allshops/",views.list_all_products,name="allshops"),
]
