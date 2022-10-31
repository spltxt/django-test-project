from django.urls import path
from .views import (
    home_view,
    SaleListView,
    SaleDetailView, CreatePositionView,
)

app_name = 'sales'

urlpatterns = [
    path('', home_view, name='home'),
    path('sales-list/', SaleListView.as_view(), name='list'),
    path('sales-list/create-position/', CreatePositionView.as_view(), name='create_sale'),
    path('sales-list/<pk>/', SaleDetailView.as_view(), name='detail'),
]