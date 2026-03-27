from celery import Celery
from celery import shared_task
import time

# app = Celery('tasks', broker='pyamqp://guest@localhost//')
# app = Celery('tasks', backend='rpc://', broker='amqp://')
# app = Celery('tasks', backend='rpc://', broker='redis://localhost')

@shared_task
def add(x, y):
    # time.sleep(8)
    return x + y
