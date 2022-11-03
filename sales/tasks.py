from celery import shared_task
from sales.models import Sale, SaleStatus
from django.utils import timezone


@shared_task(name='change_sale_status_to_finished', queue='normal')
def change_sale_status_to_finished():
    for sale in Sale.objects.all():
        if sale.status == SaleStatus.IN_PROGRESS and (timezone.now() - sale.created).total_seconds() >= 3600:
            sale.status_to_finished()
