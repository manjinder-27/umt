import requests
import time
from celery import shared_task
from .models import Monitor

@shared_task
def check_url_status(monitor_id):
    print("Checking URL Status...")
    monitor = Monitor.objects.get(id=monitor_id)
    try:
        start_time = time.time()
        
        response = requests.get(monitor.url, timeout=15)
        latency = (time.time() - start_time) * 1000 # in ms
        
        status = "Up" if response.status_code == monitor.expected_status else "Down"
        
        monitor.status = status
        monitor.latency = round(latency, 2)
        monitor.save()
    except Exception as e:
        monitor.status = "Down"
        monitor.latency = 0
        monitor.save()

@shared_task
def check_all_active_monitors():
    print("Starting Process...")
    monitors = Monitor.objects.all().values_list('id', flat=True)
    for m_id in monitors:
        check_url_status.delay(m_id)