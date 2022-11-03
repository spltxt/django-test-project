from .models import ProductReview
from django.forms import ModelForm


class AddReviewForm(ModelForm):
    """
    Форма добавления отзыва
    """
    class Meta:
        model = ProductReview
        fields = ['content', 'rating']
