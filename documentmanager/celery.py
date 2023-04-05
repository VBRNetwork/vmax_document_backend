import os
from django.conf import settings
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "documentmanager.settings-dev")

 
# if "DJANGO_ENV" in os.environ and os.environ["DJANGO_ENV"] == "prod":
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "planner.settings")
# elif "DJANGO_ENV" in os.environ and os.environ["DJANGO_ENV"] == "staging":
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "planner.settings-staging")
# else:
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "planner.settings-dev")

 
app = Celery()
 
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")
 
# Load task modules from all registered Django apps.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'add-every-60-seconds':{'task': 'contracts.tasks.initialize_email_receiver', 'schedule': 60.0},

    'add-every-30-days': {'task': 'payroll.tasks.generate_monthly_payroll_installments', 'schedule': crontab(day_of_month='*/30', hour=0, minute=0)},
}

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
