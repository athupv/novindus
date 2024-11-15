from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart, name ='cart'),    
    path('add/<int:product_id>/',views.cart_add, name='cart_add'),
    path('increment/<int:id>/',views.cart_increment,name='cart_increment'),
    path('decrement/<int:id>/',views.cart_decrement,name='cart_decrement'),
    path('remove/<int:id>/',views.remove,name='remove'),
]