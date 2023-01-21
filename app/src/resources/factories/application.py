from flask              import Flask, Blueprint
from flask_restful      import Api

### Controladores Produccion
from resources.controllers.prod.Hello   import Hello
from resources.controllers.prod.productos.productos   import Productos
from resources.controllers.prod.admins.admins   import Admin

### Controladores Test

def create_app():
        
        app = Flask(__name__)
        api_bp = Blueprint('api', __name__)
        test_bp = Blueprint('test', __name__)
        api = Api(api_bp)
        test = Api(test_bp)
        
        ### Endpoints Produccion
        api.add_resource(Hello,     Hello.route)
        api.add_resource(Productos, Productos.route)
        api.add_resource(Admin,     Admin.route)
        
        #app.config['CELERY_BROKER_URL'] = 'amqp://admin:cambalache@rabbitmq_3:5672'
        app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379'
        app.register_blueprint(api_bp, url_prefix='/api')
        app.register_blueprint(test_bp, url_prefix='/test')
        
        
        return app
 