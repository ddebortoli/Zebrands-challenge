# Description of the task

We need to build a basic catalog system to manage _products_. A _product_ should have basic info such as sku, name, price and brand.

In this system, we need to have at least two type of users: (i) _admins_ to create / update / delete _products_ and to create / update / delete other _admins_; and (ii) _anonymous users_ who can only retrieve _products_ information but can't make changes.

As a special requirement, whenever an _admin_ user makes a change in a product (for example, if a price is adjusted), we need to notify all other _admins_ about the change, either via email or other mechanism.

We also need to keep track of the number of times every single product is queried by an _anonymous user_, so we can build some reports in the future.

Your task is to build this system implementing a REST or GraphQL API using the stack of your preference. 

## What we expect
We are going to evaluate all your choices from API design to deployment, so invest enough time in every step, not only coding. The test may feel ambiguous at points because we want you to feel obligated to make design decisions. In real life you will often find this to be the case.

We are going to evaluate these dimensions:
- Code quality: We expect clean code and good practices
- Technology: Use of paradigms, frameworks and libraries. Remember to use the right tool for the right problem
- Creativity: Don't let the previous instructions to limit your choices, be free
- Organization: Project structure, versioning, coding standards
- Documentation: Anyone should be able to run the app and to understand the code (this doesn't mean you need to put comments everywhere :))

If you want to stand out by going the extra mile, you could do some of the following:
- Add tests for your code
- Containerize the app
- Deploy the API to a real environment
- Use AWS SES or another 3rd party API to implement the notification system
- Provide API documentation (ideally, auto generated from code)
- Propose an architecture design and give an explanation about how it should scale in the future

# Solution

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