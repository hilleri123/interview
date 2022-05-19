from flask import Flask
import os
from flask_restful import Api
from config import basedir, urls
from app.controller import Controller
from app.tasks import TaskManager

tm = TaskManager(urls)
app = Flask(__name__)
api = Api(app)
api.add_resource(Controller, "/tasks", "/tasks/", "/tasks/<int:id>")


