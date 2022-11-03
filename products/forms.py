from .models import ProductReview
from django.forms import ModelForm


class AddReviewForm(ModelForm):
    class Meta:
        model = ProductReview
        fields = ['content', 'rating']
