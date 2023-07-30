from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
 
    path("hello/",views.MyProtectedView.as_view(),name="hello"),
    path("retriveshop/<str:pk>",views.retiveShop.as_view(),name="retriveshop"),
    path("postcart/",views.CartView.as_view(),name="postcart"),
    path("retrivecart/<str:pk>",views.RetriveCartShop.as_view(),name="retrivecart")
   #path("list_datas/",views.Shops.as_view(),name="listdatas"),
   #path("allshops/",views.list_all_products,name="allshops"),
]
