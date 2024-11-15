from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product, name ='products'),
    path('add-products', views.add_products, name ='add_products'),
]