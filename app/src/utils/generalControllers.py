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