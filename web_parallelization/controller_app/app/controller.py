from flask_restful import Resource, reqparse

from app.tasks import TaskManager
from time import sleep


class Controller(Resource):
    
    def get(self, id=0):
        tm = TaskManager()
        return 'Task not found', 404

    def post(self, id):
        tm = TaskManager()
        parser = reqparse.RequestParser()
        parser.add_argument('url')
        parser.add_argument('task')
        params = parser.parse_args()
        #for quote in ai_quotes:
            #if(id == quote["id"]):
                #return f"Quote with id {id} already exists", 400
        #quote = {
            #"id": int(id),
            #"author": params["author"],
            #"quote": params["quote"]
        #}
        tm.add_task(params['task'], url=params['url'])
        print('+')
        sleep(10)
        return 200

    def put(self, id):
        tm = TaskManager()
        parser = reqparse.RequestParser()
        parser.add_argument("url")
        parser.add_argument("task")
        params = parser.parse_args()
        tm.add_task(params['task'], url=params['url'])
        return 200

    def delete(self, id):
        tm = TaskManager()
        return f"Task with id {id} is deleted.", 200
