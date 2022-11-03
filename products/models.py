from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ProductRating:
    """
    Рейтинг товара
    """

    CHOICES = (
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
    )


class ProductCategory:
    """
    Категория товара
    """
    PIZZA = 'Пицца'
    DRINKS_AND_SNACKS = 'Напитки и закуски'

    CATEGORY_CHOICES = (
        (PIZZA, 'Пицца'),
        (DRINKS_AND_SNACKS, 'Напитки и закуски')
    )


class Product(models.Model):
    """
    Модель Товар
    """
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='products', default='no_picture.png')
    price = models.FloatField(help_text='рублей')
    category = models.CharField(choices=ProductCategory.CATEGORY_CHOICES, max_length=50, default=ProductCategory.PIZZA)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}-{self.created.strftime('%d/%m/%Y')}"

    @property
    def review_count(self):
        return self.reviews.count()


class ProductReview(models.Model):
    """
    Модель Отзыв на товар
    """
    product = models.ForeignKey(Product, related_name='reviews',
                                on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField('', blank=True, null=True)
    rating = models.IntegerField('Рейтинг', choices=ProductRating.CHOICES)
    created = models.DateTimeField(auto_now_add=True)



