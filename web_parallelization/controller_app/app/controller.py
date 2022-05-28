from flask_restful import Resource, reqparse

from app.tasks import TaskManager
from time import sleep


class Controller(Resource):
    
    def get(self):
        tm = TaskManager()
        return 'Task not found (Master)', 404

    def post(self):
        tm = TaskManager()
        parser = reqparse.RequestParser()
        parser.add_argument('url')
        parser.add_argument('task')
        parser.add_argument('code')
        params = parser.parse_args()
        tm.manage_task(params['task'], url=params['url'], status=params['code'])
        return 200

    #def put(self):
        #tm = TaskManager()
        #parser = reqparse.RequestParser()
        #parser.add_argument("url")
        #parser.add_argument("task")
        #params = parser.parse_args()
        #tm.add_task(params['task'], url=params['url'])
        #return 200

    #def delete(self):
        #tm = TaskManager()
        #return f"Task with id {id} is deleted.", 200
