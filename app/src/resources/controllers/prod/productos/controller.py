from resources.controllers.prod.database.database import Database
from datadog import initialize, api
import os
from utils.utils import isAdmin

class ProductController():
    def __init__(self, ids=None):
        self.ids = ids

    def getProducts(self):
        """_summary_
        get products by id or all products
        Returns:
            {
                "result": [ 
                    {
                        "amount": 5, (int)
                        "brand": 1, (int)
                        "name": "Test", (varchar)
                        "price": "4500", (decimal)
                        "sku": 1 (int)
                    }
                ],
                "statusCode": 200 (int)
            }
        """
        db = Database()
        # Format the query
        if self.ids:
            query = "SELECT * FROM products WHERE sku IN (%s)" % ','.join([
                '%s']*len(self.ids))
        else:
            query = "SELECT * FROM products"

        try:
            products = db.executeQueryFetch(query, self.ids)
            self._loadDatadog('')
            return {"result": products},200
        except Exception as error:
            db.close()
            return {"message:": "Unexpected Error", "description": error},500

    def createProducts(self,products):
        """_summary_
        create products
        Args:
            "products": [ (Object array)
                {
                    "amount": 5, (int)(mandatory)
                    "brand": 1, (int)(mandatory)
                    "name": "Test", (string)(mandatory)
                    "price": "4500", (decimal)(mandatory)
                }
            ]
        Returns:
            {
                "message": "Sucessfull created."
            }
        """

        db = Database()
        errorOnUpdate = False
        for data in products:
            query = 'INSERT INTO products (name, price, brand, amount) VALUES (%s, %s, %s, %s)'
            values = (data["name"], data["price"],
                      data["brand"], data["amount"])
            try:
                db.executeQueryPreCommit(query, values)
            except Exception as error:
                errorOnUpdate = True

        if not errorOnUpdate:
            try:
                db.executeCommit()
                db.close()
            except Exception as error:
                db.executeRollback()
                db.close()
                return {"message:": "Unexpected Error", "description": error}, 500
            else:
                return {"message": "Created."}, 201
        
    def updateProducts(self, products):
        """_summary_
        update products by sku
        Args:
            "result": [ (Object array)
                {
                    "amount": 5, (int)(mandatory)
                    "brand": 1, (int)(mandatory)
                    "name": "Test", (string)(mandatory)
                    "price": "4500", (decimal)(mandatory)
                    "sku": 1 (int)(mandatory)
                }
            ]

        Returns:
            {
                "message": "Sucessfull updated."
            }
        """

        db = Database()
        errorOnUpdate = False
        for data in products:
            query = "UPDATE products SET name = %s, price = %s, brand = %s, amount = %s WHERE sku = %s \n"
            values = (data["name"], data["price"],
                      data["brand"], data["amount"], data["sku"])
            try:
                db.executeQueryPreCommit(query, values)
            except Exception as error:
                errorOnUpdate = True

        if not errorOnUpdate:
            try:
                db.executeCommit()
                db.close()
            except Exception as error:
                db.executeRollback()
                db.close()
                return {"message:": "Unexpected Error", "description": error}, 500
            else:
                return {"message": "Sucessfull updated."}, 200

    def deleteProducts(self,products):
        """_summary_
        delete products by sku
        Args:
            "result": [ (Object array)
                {
                    "sku": 1 (int)(mandatory)
                }
            ]

        Returns:
            {
                "message": "Sucessfull deleted."
            }
        """
        db = Database()
        errorOnUpdate = False
        query = "DELETE FROM products WHERE sku = %s"
        
        for product in products:
            try:
                db.executeQueryPreCommit(query, (product['sku'],))
            except Exception as error:
                errorOnUpdate = True
                print(error,flush=True)

        if not errorOnUpdate:
            try:
                db.executeCommit()
                db.close()
            except Exception as error:
                db.executeRollback()
                db.close()
                return {"message:": "Unexpected Error", "description": error}, 500
            else:
                return {"message": "Sucessfull deleted."}, 200
            
    def _loadDatadog(self,message):
        """Loads data into datadog"""
        if isAdmin:
            options = {
                'api_key': os.environ.get('datadog_api_key'),
                'app_key': os.environ.get('datadog_app_key')
            }
            initialize(**options)

            message = "all products"
            if self.ids is not None and len(self.ids) > 0:
                message = str(self.ids)
                
            
            event_title = "Product query event"
            event_text = f"The following IDs were queried: {message}"

            api.Event.create(title=event_title, text=event_text, tags=["product", "query"])