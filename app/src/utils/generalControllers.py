import json
def valueOrNull(args,value):
    "if the first argument have the key from the second parameter, then returns his value, else it returns None"
    try:
        return args[value]
    except KeyError:
        return None

def fixDataFromDataBase(data):
        "Funcion se come cualquier datetime, decimal o similar con formato roto y lo vuelve hecho Calamardo Guapisimo"
        data = json.dumps(data, indent=4, sort_keys=True, default=str)
        data = json.loads(data)
        return data

def checkMandatoryArr(array,parameters):
    """
    Check mandatory parameter
    where array is the array object, and parameters is a LIST of the mandatory parameters
    Also can use this function to check type, but it needs some changes
    """
    for arr in array:
        for parameter in parameters:
            try:
                i = arr[parameter]
            except KeyError:
                return False
    return True

def checkMandatory(body,parameters):
    """Check mandatory parameter
    where array is the object, and parameters is a LIST of the mandatory parameters
    Also can use this function to check type, but it needs some changes"""
    for parameter in parameters:
        try:
            i = body[parameter]
        except KeyError:
            return False
    return True