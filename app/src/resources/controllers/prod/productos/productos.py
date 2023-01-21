from flask_restful import Resource, reqparse,request
from resources.controllers.prod.productos.controller import ProductController
from resources.controllers.prod.admins.controller import AdminController
from threading import Thread
import os
from utils.generalControllers import valueOrNull,checkMandatory,checkMandatoryArr
from utils.utils import requires_auth
import boto3

class Productos(Resource):
    
    route = "/Productos"
    def __init__(self):
        self.product_ids = request.args.getlist('id')

    
    def get(self):
        print(self.product_ids,flush=True)
        products = ProductController(
            self.product_ids
            ).getProducts()
                
        return products

    @requires_auth
    def post(self):
        json_data = (request.json)
        products = valueOrNull(json_data,'products')
        
        if products and checkMandatoryArr(products,['amount','brand','name','price']):
            result = ProductController().createProducts(products)
            return result
            
        return 'Bad body, check the parameters and try again', 400
    
    @requires_auth
    def put(self):
        json_data = (request.json)
        products = valueOrNull(json_data,'products')
        
        if products and checkMandatoryArr(products,['amount','brand','name','price','sku']):
            result = ProductController().updateProducts(products)
            
            ### The mail sent runs in paralel, the user doesn't need to wait
            email_thread = Thread(target=self._send_email, args=(products,))
            email_thread.start()
            return result
            
        return 'Bad body, check the parameters and try again', 400

    @requires_auth
    def delete(self):
        json_data = (request.json)
        products = valueOrNull(json_data,'products')
        
        if products and checkMandatoryArr(products,['sku']):
            result = ProductController().deleteProducts(products)
            return result
            
        return 'Bad body, check the parameters and try again', 400

    def _getMails(self):
        mails = []
        users = (AdminController().getAdmins(None))[0]
        print(users,flush=True)
        for user in users['result']:
            print(user,flush=True)
            mails.append(user['mail'])
        return mails
    
    def _send_email(self,valores):
        # Connect to AWS SES
        destinatarios = self._getMails()
        print(destinatarios,flush=True)
        client = boto3.client('ses',
                            aws_access_key_id= os.environ.get('aws_acces_key_id'),
                            aws_secret_access_key= os.environ.get('aws_secret_access_key') ,
                            region_name= os.environ.get('region_name')
                            )

        # Get the email data
        message = ""
        for valor in valores:
            message = message + """
            Product with code %s has changed, new values:\n
            name: %s\n
            price: %s\n
            brand: %s\n
            amount: %s\n
            """ % (valor['sku'],valor['name'],valor['price'],valor['brand'],valor['amount'])
        
        # Send the email
        response = client.send_email(
            Destination={
                'ToAddresses': destinatarios
            },
            Message={
                'Subject': {
                    'Data': "Cambios en productos"
                },
                'Body': {
                    'Text': {
                        'Data': message
                    }
                }
            },
            Source= os.environ.get('sourceEmail')
        )
        print(response,flush=True)

        return response    
    