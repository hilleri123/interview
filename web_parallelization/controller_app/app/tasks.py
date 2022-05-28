from apscheduler.schedulers.background import BackgroundScheduler
import requests

from time import sleep 

class TaskManager:

    def __init__(self, urls = None):
        if not urls is None:
            self._tasks = {url:[] for url in urls}
        if not hasattr(self, '_tasks'):
            self._tasks = {}

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(TaskManager, cls).__new__(cls)
        return cls._instance

    def manage_task(self, task=None, url=None, code=None):
        if code is None:
            self.__add_task(task, url)
            return
        d = {
                'done':self.__done_task,
                'add':self.__add_task,
                'failed':self.__failed_url,
                'started':self.__started_url,
                }
        d[code](task=task, url=url)
        print('MASTER', self._tasks)

        
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
            size = None
            for key_url, task_list in self._tasks.items():
                if size is None:
                    size = len(task_list)
                else:
                    size = min(size, len(task_list))
                if url_to_append is None or size == len(task_list):
                    url_to_append = key_url
            if not url_to_append is None:
                self._tasks[url_to_append].append(task)
        else:
            self._tasks[url_to_append].append(task)
        if not url_to_append is None:
            r = requests.post('http://'+url_to_append, params=payload)


class TaskWorker:
    def __init__(self, slave_url=None, master_url='localhost:5000'):
        if not hasattr(self, '_tasks'):
            self._tasks = []
        if not hasattr(self, '_master_url'):
            self._master_url = master_url
        if not hasattr(self, '_slave_url'):
            self._slave_url = slave_url
        if not hasattr(self, '_scheduler'):
            self._scheduler = BackgroundScheduler()
            self._scheduler.add_job(TaskWorker.do_something, 'interval', seconds=5, id='main')
            self._scheduler.start()


    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(TaskWorker, cls).__new__(cls)
        return cls._instance

    def manage_task(self, task=None, code=None):
        if code is None:
            self.__add_task(task)
            return
        d = {
                'add':self.__add_task,
                'del':self.__del_task
                }
        d[code](task=task)
        print('SLAVE', self._tasks)


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
        print(self._tasks)
        payload = {'task': task, 'url':self._slave_url, 'code':'done'}
        r = requests.post('http://'+self._master_url, params=payload)
        return True

    def fail(self):
        payload = {'url':self._slave_url, 'code':'failed'}
        r = requests.post('http://'+self._master_url, params=payload)

    def start(self):
        payload = {'url':self._slave_url, 'code':'started'}
        r = requests.post('http://'+self._master_url, params=payload)

    @classmethod
    def do_something(cls):
        slave = TaskWorker()
        while slave.do_task():
            print('Slave is doing something...')




