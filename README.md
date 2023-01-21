# Zebrands challenge

API de productos, la cual maneja una base de datos sencilla compuesta por dos tablas:
products (sku,name,price,brand,amount)
users (idusers,name,password,mail)


## Description

La api se compone de 4 endpoints del lado de productos:
Dato importante: Usuarios autenticados son administradores

GET /Product
Devuelve de 0 a N productos, filtrando por id(array)
Las llamadas por parte de usuarios no autenticados se registran con datadog para poder ser usados en reportes
POST /Product
Crea 0 a N productos - Requiere estar autenticado
PUT /Product 
Actualiza 0 a N productos - Requiere estar autenticado - Envia un correo a todos los administradores(Deben estar previamente verificados en AWS SES)
DELETE /Product
Borra de 0 a N productos - Requiere estar autenticado

GET /admin
Obtiene todos los administradores (usuario y mail) - Requiere estar autenticado

POST /admin
Crea un administrador por llamada - Requiere estar autenticado
PUT /admin
Acutaliza de 0 a N administradores (usuario y mail) - Requiere estar autenticado
DELETE /admin
Borra de 0 a N administradores (usuario y mail) - Requiere estar autenticado

Es importante mencionar que todas las llamadas de CUD realizan transacciones en la base de datos, por lo cual la falla de una, cancela toda la operacion
El servicio devuelve un mensaje explicando el error

## Getting Started

### Dependencies

* Docker, AWS SES, Datadog
* Requirements.txt

### Executing program

* Docker-compose build 
* Docker-compose up

## Help

Cualquier inconveniente
mail:damiandebortolilb@gmail.com
LinkedIn: https://www.linkedin.com/in/damian-debortoli/
## Authors

https://www.linkedin.com/in/damian-debortoli/


## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)


# Postman documentation:
https://documenter.getpostman.com/view/20470750/2s8ZDYXMHh