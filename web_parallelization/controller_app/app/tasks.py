from apscheduler.schedulers.background import BackgroundScheduler
import requests

from time import sleep 

class TaskManager:

    def __init__(self, urls = None):
        if not urls is None:
            self._tasks = {url:[] for url in urls}
        if not hasattr(self, '_tasks'):
            self._tasks = {}
        print(self._tasks)

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(TaskManager, cls).__new__(cls)
        return cls._instance

    def manage_task(self, task=None, url=None, code=None):
        if code is None:
            self.add_task(task, url)
            return
        d = {
                'done':self.__done_task,
                'add':self.__add_task,
                'failed':self.__failed_url,
                'started':self.__started_url,
                }
        d[code](task=task, url=url)

        
    def __failed_url(self, task=None, url=None):
        pass

    def __started_url(self, task=None, url=None):
        pass

    def __done_task(self, task=None, url=None):
        self.__tasks[url].remove(task)

    def __add_task(self, task, url=None):
        payload = {'task': task, 'code':'add'}  
        url_to_append = url
        if url_to_append is None:
            for key_url, task_list in self._tasks:
                size = min(size, len(task_list))
                if url_to_append is None or size == len(task_list):
                    url_to_append = key_url
            if not url_to_append is None:
                self._tasks[url_to_append].append(task)
        else:
            self._tasks[url_to_append].append(task)
        if not url_to_append is None:
            r = requests.post(url_to_append, params=payload)


class TaskWorker:
    def __init__(self, master_url='localhost:5000', slave_url):
        if not hasattr(self, '_tasks'):
            self._tasks = []
        if not hasattr(self, '_master_url'):
            self._master_url = master_url
        if not hasattr(self, '_slave_url'):
            self._slave_url = slave_url

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(TaskWorker, cls).__new__(cls)
        return cls._instance

    def manage_task(self, task=None, code=None):
        if code is None:
            self.__add_task(task)
        d = {
                'add':self.__add_task,
                'del':self.__del_task
                }
        d[code](task=task)


    def __del_task(self, task):
        self._tasks.remove(task)

    def __add_task(self, task):
        self._tasks.append(task)

    def do_task(self):
        if len(self._tasks) == 0:
            return False
        task = self._tasks[0]
        sleep(5)
        self._tasks.remove(task)
        payload = {'task': task, 'url':self._slave_url, 'code':'done'}
        r = requests.post(self._master_url, params=payload)
        return True



    @classmethod
    def do_something():
        slave = TaskWorker()
        while slave.do_task():
            print('doing something...')




