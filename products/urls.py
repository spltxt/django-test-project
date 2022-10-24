from django.urls import path
from products.views import ProductListView, product_detail_view

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('<str:pk>/', product_detail_view, name='product_detail'),
]