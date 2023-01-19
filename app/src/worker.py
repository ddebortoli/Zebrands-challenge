from resources.factories.celery import create_celery
from resources.factories.application import create_app
print("Algo",flush=True)
celery = create_celery(create_app())