from functools import wraps
from flask_restful import request
import os,sys,pyodbc, json, base64
from types import NoneType

### Auth and Body
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if request.headers.get('Authorization') is not None:
            credentials = base64.b64decode(request.headers.get('Authorization').split(' ')[1]).decode("utf-8").split(':') 
            if credentials[0] == os.getenv('HTTP_USER') and credentials[1] == os.getenv('HTTP_PASS'):
                try: req_body = request.get_json()
                except Exception as e:
                    print('Utils/Auth - No payload on body', flush=True)
                    return { "message": 'No payload on body'}, 400                                                      ### Body Errors
            else: return {"message": "invalid User or password"}, 401                                                               ### Auth Errors
        else: return {"message":"Error, no Authorization headers on http request."}, 403    ### Auth Errors
        return f(*args, **kwargs)
    return decorated
