import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'umt_server.settings')

app = Celery('umt_server')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()