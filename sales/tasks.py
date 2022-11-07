from celery import shared_task
from celery.utils.log import get_task_logger

from django.utils import timezone

from sales.models import Sale, SaleStatus
from pizza.celery import app


logger = get_task_logger(__name__)


@shared_task(name='sales.tasks.change_sale_status_to_finished')
def change_sale_status_to_finished():
    """
    Установить статус заказа "Завершён"
    """
    sales = Sale.objects.all()
    for sale in sales:
        if sale.status == SaleStatus.IN_PROGRESS and (timezone.now() - sale.created).total_seconds() >= 3600:
            sale.status_to_finished()

