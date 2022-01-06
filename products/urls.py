from django.urls import path
from .views import my_product_view

app_name = 'products'

urlpatterns = [
    path('', my_product_view, name='products')
]