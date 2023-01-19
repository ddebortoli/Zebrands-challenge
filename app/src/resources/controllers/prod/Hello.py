from flask import current_app
from flask_restful import Resource, request
from resources.factories.celery import create_celery

class Hello(Resource):
    route = '/hello'
    def get(self):
        print('Hello World')
        return {"message": "Hello World app"},200    