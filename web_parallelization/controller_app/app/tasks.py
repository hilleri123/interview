from apscheduler.schedulers.background import BackgroundScheduler

class TaskManager:

    def __init__(self, urls = None):
        if not urls is None:
            self._tasks = {url:[] for url in urls}
        if not hasattr(self, '_tasks'):
            self._tasks = {}
        print(self._tasks)

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            #cls.instance = super(TaskManager, cls).__new__(cls, *args, **kwargs)
            cls._instance = super(TaskManager, cls).__new__(cls)
        return cls._instance

    def add_task(self, task, url=None):
        if url is None:
            print('!', task)
        else:
            self._tasks[url].append(task)


