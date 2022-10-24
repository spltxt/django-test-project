from django.db.models import Avg
from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from products.models import Product, ProductReview
from products.forms import AddReviewForm


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Product.objects.annotate(avg_rating=Avg('reviews__rating'))


def product_detail_view(request, pk):
    product = Product.objects.get(id=pk)
    form = AddReviewForm

    if request.method == "POST":
        rating = request.POST.get('rating', 3)
        content = request.POST.get('content', '')

        ProductReview.objects.create(product=product,
                                     author=request.user,
                                     rating=rating,
                                     content=content)

    context = {
        'product': product,
        'form': form
    }

    return render(request, 'products/detail.html', context)
