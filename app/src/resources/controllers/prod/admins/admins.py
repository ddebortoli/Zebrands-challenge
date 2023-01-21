from flask_restful import Resource, reqparse,request
from resources.controllers.prod.admins.controller import AdminController
from utils.generalControllers import valueOrNull,checkMandatory,checkMandatoryArr
from utils.utils import requires_auth

class Admin(Resource):
    
    decorators = [requires_auth]
    
    route = "/admin"
    def __init__(self):
        pass
    
    def get(self):
        ids = request.args.getlist('id')
        users = AdminController().getAdmins(ids)
                
        return users

    def post(self):
        json_data = (request.json)
        body = valueOrNull(json_data,'admin')
        
        if body and checkMandatory(body,['user','password','mail']):
            result = AdminController().createAdmin(body['user'],body['password'],body['mail'])
            return result
            
        return 'Bad body, check the parameters and try again', 400
    
    def put(self):
        json_data = (request.json)
        body = valueOrNull(json_data,'admins')
        
        if body and checkMandatoryArr(body,['user','mail','iduser']):
            result = AdminController().updateAdmins(body)
            return result
            
        return 'Bad body, check the parameters and try again', 400

    def delete(self):
        json_data = (request.json)
        body = valueOrNull(json_data,'admins')
        
        if body and checkMandatoryArr(body,['iduser']):
            result = AdminController().deleteAdmins(body)
            return result
            
        return 'Bad body, check the parameters and try again', 400
    