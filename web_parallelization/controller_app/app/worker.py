from flask_restful import Resource, reqparse

from app.tasks import TaskWorker
from time import sleep


class Worker(Resource):
    
    def get(self):
        tw = TaskWorker()
        return 'Task not found (Slave)', 404

    def post(self):
        tw = TaskWorker()
        parser = reqparse.RequestParser()
        #parser.add_argument('url')
        parser.add_argument('task')
        parser.add_argument('code')
        params = parser.parse_args()
        tw.manage_task(params['task'], code=params['code'])
        return 200

