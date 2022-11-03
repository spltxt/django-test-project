from django.db import models
from profiles.models import Profile
from django.urls import reverse


# Create your models here.

class Report(models.Model):
    """
    Модель Отчёт
    """
    name = models.CharField(max_length=120, verbose_name='Наименование отчёта')
    image = models.ImageField(upload_to='reports', blank=True)
    remarks = models.TextField(verbose_name='Текст отчёта')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("reports:detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ('-created',)
