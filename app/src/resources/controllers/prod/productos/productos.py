import mysql.connector
from flask_restful import Resource, reqparse,request
from resources.controllers.prod.productos.controller import ProductController
from utils.generalControllers import valueOrNull

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

    def put(self):
        json_data = (request.json)
        products = valueOrNull(json_data,'products')
        
        if json_data:
            result = ProductController().updateProducts(products)
            return result
            
        return 'Bad body, check the parameters and try again', 400

    def delete(self):
        args = self.parser.parse_args()
        ids = args['ids'].split(',')
        for id in ids:
            self.cursor.execute("DELETE FROM productos WHERE id = ?", id)
            self.connection.commit()
        return 'Productos eliminados', 200