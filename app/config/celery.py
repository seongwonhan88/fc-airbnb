from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
# SET default DJANGO SETTINGS MODULE
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_test(self):
    print('Request: {0!r}'.format(self.request))