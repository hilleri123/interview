

class TaskManager:

    def __init__(self, urls = None):
        if not urls is None:
            self.tasks = {url:[] for url in urls}
        if not hasattr(self, 'tasks'):
            self.tasks = {}
        print(self.tasks)

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            #cls.instance = super(TaskManager, cls).__new__(cls, *args, **kwargs)
            cls.instance = super(TaskManager, cls).__new__(cls)
        return cls.instance

    def add_task(self, task, url=None):
        if url is None:
            print('!', task)
        else:
            self.tasks[url].append(task)

