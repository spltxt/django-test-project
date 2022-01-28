from django.urls import path
from .views import my_product_view, product_detail_view

app_name = 'products'

urlpatterns = [
    path('', my_product_view, name='products'),
    path('<str:pk>/', product_detail_view, name='product_detail'),
]