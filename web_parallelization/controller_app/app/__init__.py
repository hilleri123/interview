from flask import Flask
import os
from flask_restful import Api
from config import basedir, urls
from app.controller import Controller
from app.worker import Worker
from app.tasks import TaskManager

def make_app(master=False):
    tm = TaskManager(urls)
    app = Flask(__name__)
    api = Api(app)
    if master:
        api.add_resource(Controller, "/tasks", "/tasks/")
    else:
        pass
    return app


