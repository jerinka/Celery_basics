from celery import app
from simple_celery.celery import app

@app.task
def add(x,y):
    return x+y

@app.task
def mul(x,y):
    return x*y

@app.task
def xsum(vec):
    return sum(vec)


