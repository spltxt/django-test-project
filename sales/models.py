from django.db import models
from products.models import Product
from customers.models import Customer
from profiles.models import Profile
from django.utils import timezone
from .utils import generate_code
from django.shortcuts import reverse


class SaleStatus:
    """
    Статус заказа
    """
    IN_PROGRESS = 'В процессе выполнения'
    FINISHED = 'Завершён'
    CANCELLED = 'Отменён'

    STATUS_CHOICES = (
        (IN_PROGRESS, 'В процессе выполнения'),
        (FINISHED, 'Завершён'),
        (CANCELLED, 'Отменён')
    )


class Position(models.Model):
    """
    Модель "Позиция в заказе"
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    price = models.FloatField(blank=True)
    created = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args, **kwargs)

    def get_sales_id(self):
        sale_obj = self.sale_set.first()
        return sale_obj.id

    def get_customer_id(self):
        sale_obj = self.sale_set.first()
        return sale_obj.customer.name

    def __str__(self):
        return f"id: {self.id}, product: {self.product.name}, quantity: {self.quantity}"

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})


class Sale(models.Model):
    """
    Модель "Заказ"
    """
    transaction_id = models.CharField(max_length=12, blank=True)
    positions = models.ManyToManyField(Position)
    total_price = models.FloatField(blank=True, null=True)
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=SaleStatus.STATUS_CHOICES, max_length=25, default=SaleStatus.IN_PROGRESS)

    def __str__(self):
        return f"Заказ на сумму {self.total_price} руб."

    def get_absolute_url(self):
        return reverse("sales:detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        if self.transaction_id == "":
            self.transaction_id = generate_code()
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args, **kwargs)

    def get_positions(self):
        return self.positions.all()

    def status_to_finished(self):
        self.status = SaleStatus.FINISHED
        self.save()


class CSV(models.Model):
    file_name = models.FileField(upload_to='csvs')
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.filename)
