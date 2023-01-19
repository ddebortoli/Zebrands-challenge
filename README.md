### Mapa Componentes de Integraciones

Mapa para ver componentes ambos lados, endpoints, metodos, parametros, y todo lo que se necesita testear para
que cada flujo corra correctamente

https://github.com/Cambalache-Technologies/salesforce-grupocn
https://documenter.getpostman.com/view/15481845/UzBnrmxK
https://lucid.app/lucidchart/2aa0f546-7997-4804-9391-f40b76a96089/edit?invitationId=inv_1b717bc1-7fa4-482d-b41d-bdeae60a3623&page=LZlAiNnI9LEk#?referringapp=slack
EC2             - t2.medium
ElasticIP       - 52.204.203.34
Connected App   - integracion_v4
Docker-Compose/Dockerfile/Flask/Multiprocess(Async)



Flujo                       SF                  Cambalapi                           CN
--------------------------------------------------------------------------------------------------------------------------------------
GET Auxiliares                                  Cronjobs                           (Vistas Varias)
GET Accounts                                   POST/account <-                     Vista Accounts  (Vusr_ClientesCompleto)      
GET Dir Entrega                                POST/account <-                     Vista Dir Entr  (Vusr_DirEntregaCompleto)
GET Contactos                                  POST/account <-                     Vista Contacts  (Vusr_ContactosCompleto)
GET Productos                                  POST/product <-                     Vista Products  (Vusr_ProductosCompleto)
GET Precios                                    POST/product <-                     Vista Products  (Vusr_ProductosCompleto)
GET Stock                   Button-Apex     -> GET/consultas-product ?resource     SP Stock        (USP_CNAPP_ConsultaStock)
GET Analisis                Button-Apex     -> GET/consultas-cliente ?resource     SP Analisis     (usr_CNAPP_ClientesRiesgo)
GET Acopios                 Button-Apex     -> GET/consultas-cliente ?resource     SP Acopios      (usr_CNAPP_AcopioPendPorCliente)
GET LimiteCredito           Button-Apex     -> GET/consultas-cliente ?resource     SP LimiteCre    (usr_CNAPP_LimiteCredNV)
POST Account                Button-Apex     -> POST/account-cn                     SP Account      (usp_CNAPP_InsertaCliente)
POST Dir Entrega            Button-Apex*    -> POST/account-cn                     SP Dir Entr     (usp_CNAPP_InsertaDirEntrega)
POST Contact                Button-Apex*    -> POST/account-cn                     SP Contact      (usp_CNAPP_InsertaContacto)




### External Codes Formating and Important Fields (Important! in 'database' use the format from databaseDependent method)

In {database} the value saved is the picklistvalue
Codigo__c - All SF Objects will have a value from picklist in the field (ALL)
Codigo_Interno__c - If the record has a identifier code IN the database, the pure value is saved in this field (Ej. accountCode)

 - Account Parent / Child   -> {region}-{account}
 - Direccion Entrega        -> DE-{region}-{accountCode}-{direccionCode}  !!! Importante Codigo Unico DE (Actualmente uso Name)
 - Contactos                -> CO-{region}-{accountCode}-{contactoCode}-{nombre}  !!! Importante Codigo Unico CO (Actualmente uso Name)
 - Product                  -> PR-{region}-{productCode}
 - PricebookEntry STD       -> PE-{region}-{productCode}-STD
 - PricebookEntry DB        -> PE-{region}-{productCode}
 - Stock                    -> ST-{databasregione}-{productCode}-{deposito}
 - Analisis de Riesgo       -> AR-{region}-{accountCode}
 - Acopios                  -> AC-{databregionase}-{accountCode}-{productType}-{productCode}
 - Limite de riesgo         -> LI-{region}-{CuentaCliente}



### Consultas Tecnicas Facundo
 - Los SP de creacion de cuentas / direcciones / contactos, pueden manejar batches o solo unicos registros
 - Los SP de creacion [idem arriba], se supone que tienen que devolver una respuesta? como validamos la creacion
 - Acopios - Fecha de consumo de acopios
 - Acopios - Formato External Id, (Que campos tomo en cuenta)
 - SP Limites de credito, por que usamos un parametro basado en la nota de venta?
 - Campos para formar externa ID en Contactos / Direccion Entrega (Ahora uso Name)


### Pendientes
 - Configure cron for linux environ (auxs)


### RecordTypes 
Account        
Pricebook2              


### Desarrollo Componentes
Calculo Potencial (Migrado)
 - Apex Class   calcularPotencial
 - Apex Class   calcularPotencial_test
 - LWC          calcularPotencial

### Nomenclatura