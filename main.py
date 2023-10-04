from celery import Celery

app = Celery('main', broker='pyamqp://guest@localhost//', backend='db+sqlite:///db.sqlite3')

@app.task
def add(x, y):
    return x + y