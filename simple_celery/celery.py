from celery import Celery

app = Celery('simple_celery',
        broker='pyamqp://',
        backend='redis://',
        include=['simple_celery.tasks'])

app.conf.update(
        result_expires=3600,
        )

#if __name__=='__main__':
#    app.start()
