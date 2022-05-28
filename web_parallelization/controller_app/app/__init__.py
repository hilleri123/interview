from flask import Flask
import os
from flask_restful import Api
from config import basedir, urls, master_url
from app.controller import Controller
from app.worker import Worker
from app.tasks import TaskManager, TaskWorker

def make_app(master=False, slave_url=None):
    app = Flask(__name__)
    api = Api(app)
    if master:
        tm = TaskManager(urls)
        api.add_resource(Controller, "/")
    else:
        tw = TaskWorker(master_url=master_url, slave_url=slave_url)
        api.add_resource(Worker, "/")
    return app


