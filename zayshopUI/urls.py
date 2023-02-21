from django.urls import path
from .views import Home,AboutUs,Contact,ShopList,ShopDetail


app_name = 'zayshopUI'


urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('aboutus/',AboutUs.as_view(),name='about'),
    path('contact/',Contact.as_view(),name='contact'),
    path('shop/',ShopList.as_view(),name='shop'),
    path('shop/<str:slug>/',ShopDetail.as_view(),name='shop-single'),
]
