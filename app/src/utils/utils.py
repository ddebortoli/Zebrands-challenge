from functools import wraps
from flask_restful import request
import base64
from types import NoneType
import bcrypt

from resources.controllers.prod.database.database import Database
### Auth and Body
def requires_auth(f):
    def wrapper(*args, **kwargs):
        if request.headers.get('Authorization') is not None:
            
            ### Use bcrypt to check password
            credentials = base64.b64decode(request.headers.get('Authorization').split(' ')[1]).decode("utf-8").split(':') 
            
            query = "SELECT password FROM users WHERE name = %s"
            values = (
                credentials[0],
                )
            result = Database().executeQueryFetch(query,values)
            if result and bcrypt.checkpw(credentials[1].encode('utf-8'), result[0]['password'].encode('utf-8')):
                try: req_body = request.get_json()
                except Exception as e:
                    print('Utils/Auth - No payload on body', flush=True)
                    return { "message": 'No payload on body'}, 400                                                      ### Body Errors
            else: return {"message": "invalid User or password"}, 401                                                               ### Auth Errors
        else: return {"message":"Error, no Authorization headers on http request."}, 403    ### Auth Errors
        return f(*args, **kwargs)
    return wrapper

def isAdmin():
    if request.headers.get('Authorization') is not None:
            
            ### Use bcrypt to check password
            credentials = base64.b64decode(request.headers.get('Authorization').split(' ')[1]).decode("utf-8").split(':') 
            
            query = "SELECT password FROM users WHERE name = %s"
            values = (
                credentials[0],
                )
            result = Database().executeQueryFetch(query,values)
            if result and bcrypt.checkpw(credentials[1].encode('utf-8'), result[0]['password'].encode('utf-8')):
                return True
    return False
