from celery import Celery

from app.config.constant import REDIS_URL

REDIS_CONNECTION = REDIS_URL
celery_app = Celery(
    "worker",
    broker=REDIS_CONNECTION,
    backend=REDIS_CONNECTION
)

celery_app.autodiscover_tasks(['app.task'])