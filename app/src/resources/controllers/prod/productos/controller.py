from resources.controllers.prod.database.database import Database


class ProductController():
    def __init__(self, ids=None):
        self.ids = ids

    def getProducts(self):
        """_summary_

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
            return {"result": products},200
        except Exception as error:
            db.close()
            return {"message:": "Unexpected Error", "description": error},500

    def updateProducts(self, products):
        """_summary_

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
