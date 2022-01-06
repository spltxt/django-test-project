from django.shortcuts import render
from .models import Product
from django.views.generic import ListView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def my_product_view(request):
    product = Product.objects.all()
    
    context = {
        'product': product
    }

    return render (request, 'products/main.html', context)
