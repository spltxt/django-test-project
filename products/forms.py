from .models import ProductReview
from django.forms import ModelForm


class AddReview(ModelForm):
    class Meta:
        model = ProductReview
        fields = ['content', 'rating']
