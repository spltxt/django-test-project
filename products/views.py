from django.shortcuts import redirect, render

from products.forms import AddReview
from .models import Product, ProductReview


def my_product_view(request):
    product = Product.objects.all()

    context = {
        'product': product,
    }

    return render(request, 'products/main.html', context)


def product_detail_view(request, pk):
    product = Product.objects.get(id=pk)
    form = AddReview

    if request.method == "POST":
        rating = request.POST.get('rating', 3)
        content = request.POST.get('content', '')

        review = ProductReview.objects.create(product=product,
                                              author=request.user,
                                              rating=rating,
                                              content=content)

    context = {
        'product': product,
        'form': form
    }

    return render(request, 'products/details.html', context)
