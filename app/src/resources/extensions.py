from celery import Celery

celery = Celery('celery_example', include=['resources.tasks'])