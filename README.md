# Celery Canvas: Designing Work-flows

https://docs.celeryproject.org/en/stable/userguide/canvas.html#guide-canvas


simple_celery/__init__.py
            /celery.py
            /tasks.py
            

## Start worker

From outside simple_celery folder

```celery -A simple_celery worker -l info```

## Calling tasks

  ```jupyter notebook```


