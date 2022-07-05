from __future__ import absolute_import
import time
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

import django
django.setup()
from django.core.management import call_command

from datetime import timedelta, datetime

from django_celery_beat.models import PeriodicTask, IntervalSchedule
from celery import Celery, shared_task



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery("library-django")
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True, default_retry_delay=5)
def task(self):
    print("Hello world")
