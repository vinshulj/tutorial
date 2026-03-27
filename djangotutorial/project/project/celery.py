import os
from celery import Celery

# Set default settings, load config, and autodiscover tasks
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
app = Celery('project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Europe/Oslo',
    enable_utc=True,
)
app.conf.beat_schedule = {
    'add-every-minute-task': {
        'task': 'Viewset.tasks.add',
        'schedule': 60.0,  
        'args': (16, 16),
    },
}






# it mean when we give the task to the celery it serialize it and send meta data and arguments in form of massage 
# to the specific redius queue. now worker process the polling message and now if the new tack apper it detect it,pull it and 
# deserilize it ,and get the meta data and arguments and after it exicute that tasks