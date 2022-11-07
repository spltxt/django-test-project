import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizza.settings')

app = Celery('pizza')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'change_sale_status_to_finished': {
        'task': 'sales.tasks.change_sale_status_to_finished',
        'schedule': crontab(),
    }
}

app.conf.timezone = settings.TIME_ZONE


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
