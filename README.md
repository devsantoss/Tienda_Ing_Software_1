# Tienda_Ing_Software_1


# Historias de usuario - Rol de tendero

## Historia 1:
Yo como Tendero deseo poder ingresar al aplicativo utilizando un usuario y una contraseña.
### Criterios de aceptación

1. Muestra un mensaje si el usuario no existe
2. Muestra error si la contraseña es incorrecta
3. Deja pasar al tendero a la landing page una vez se verifiquen los datos


## Historia 2:
Yo como Tendero, después de realizar el login, debo ser redirigido a una página de landing que me muestre la cantidad de pedidos pendientes y pedidos entregados en un intervalo de tiempo.
### Criterios de aceptación
1. La cantidad de pedidos es correcta con los registrados
2. La landing page carga los datos requeridos

## Historia 3:
Yo como Tendero, deseo registrar una nueva venta.
### Criterios de aceptación
1. La venta queda registrada correctamente
2. Los productos vendidos quedan descontados del inventario de manera correcta

## Historia 4:
Yo como Tendero, después de realizar una venta, deseo poder realizar la devolución del dinero en caso de que se presente cualquier eventualidad y que quede registro de la devolución.
### Criterios de aceptación
1. Descuento del dinero correcto en el estado de caja
2. Guarda el registro de la devolución de la compra exacta

## Historia 5:
Yo como Tendero, después de recibir un nuevo pedido, deseo ser capaz de poder mover el estado del pedido hacia adelante (Recibido, Preparación, Despacho) con el fin de actualizar el estado del pedido para el cliente
### Criterios de aceptación
1. El pedido se actualiza correctamente y únicamente hacia adelante
2. La información queda disponible para el perfil de cliente

## Historia 6:
Yo como Tendero, después de poner el pedido en estado de despacho, deseo ser capaz de asignarle un domiciliario que se encuentre disponible para la entrega.
### Criterios de aceptación
1. Asignación de domiciliario y actualización del estado del pedido
2. Queda guardado que ese pedido va a ser llevado por ese domiciliario seleccionado


## Historia 7:
Yo como Tendero, después de realizar el login, debo poder ver una pantalla que me muestre la lista de los pedidos junto con su estado actual, además de esto poder filtrarlos por estado o cliente

### Criterios de aceptación
1. La lista de pedidos es fiel a la realidad
2. Se puede filtrar por estado del pedido
3. Se puede filtrar el pedido por cliente

# Historias de usuario - Rol de Cliente
1.	Como cliente quiero registrarme con un login y contraseña, para poder acceder a la aplicación.
2.	Como cliente quiero resetear mi contraseña cuando mi login falla, para poder intentar acceder de nuevo.
3.	Como usuario quiero tener la opción de registrar una cuenta de correo electrónico nueva si no puedo acceder con la actual para poder acceder a la aplicación.
4.	Como cliente quiero buscar artículos por tipo de producto para poder encontrar rápidamente un artículo que se adapte a mis deseos.
5.	Como cliente quiero adicionar artículos a un carrito de compras para poder tener un registro de los productos que he seleccionado para comprar.

### Criterios de aceptación
La lista de articulos es fiel a la realidad
Se puede adicionar uno o mas articulos al carrito
La lista de articulos es actualizada de manera correcta

6. Como cliente, quiero visualizar los descuentos en los artículos.
### Criterios de aceptacion
Se debe mostrar la lista de articulos con descuento.

Se puede adicionar uno o más artículos al carrito.

7.	Como cliente, quiero consultar mi carrito de las compras para poder saber lo que he elegido hasta el momento.
8.	Como cliente, quiero actualizar las unidades de cada artículo, para poder comprar varios ejemplares de un producto.
9.	Como cliente, quiero eliminar productos de mi carrito de la compra, para poder comprar los productos seleccionados.
10.	Como cliente, quiero usar la ubicación de mi GPS para poder completar la dirección del pedido.
11.	Como cliente, quiero cambiar la dirección de envío de un pedido, para que me pueda llegar a casa o a la oficina.
12.	Como cliente, quiero que mi información de tipo de pago quede guardada después de la primera vez que la registre, para crear una experiencia de pago más fluida.
13.	Como comprador, quiero pagar los artículos de mi carrito de la compra, para poder recibirlos en mi casa.
14.	Como cliente, quiero utilizar Pypal, para poder informar de forma automática mis datos personales y efectuar el pago.
15.	Como cliente, quiero confirmar y revisar mi carrito de compra, para poder confirmar antes de pagar.

### Criterios de aceptación
Se puede consultar la lista de articulos antes de pagar.
Se puede aceptar o rechazar la lista de articulos del carrito.
La lista de productos es fiel a la realidad
La cantidad de articulos por producto es correcta

# Requerimiento No funcional  del Cliente
1. La app debe ser capaz de procesar y almacenar cualquier cantidad de articulos rapidamente.
2. La tasa de errores cometidos por el cliente al manejar la app, deberá ser menor del 1% de las transacciones totales ejecutadas en el sistema.
3. La aplicación deberá consumir menos de 200 Mb de memoria RAM y no podrá ocupar más de 1 GB de espacio en disco.



# Historias de usuario - Rol dueño de la tienda
- Como dueño de la tienda deseo actualizar la información sistema para que el cliente elija con facilidad.
- Como dueño de la tienda quiero responder al pedido que realiza el cliente según la cantidad de productos que adquiera para mejorar las ventas.
- Como dueño de la tienda quiero sugerir productos similares a los que el cliente pida información para aumentar las ventas. 
- Como dueño de la tienda quiero capturar los datos del cliente para ofrecerle otros productos y servicios.
- Como dueño de la tienda quiero mostrar producto que tengo en mi inventario para mejorar la rotación del producto
- Como dueño de la tienda quiero retirar productos cuando ya no existan en el inventario para mantener rotación y no se quede ningún producto sin vender.


##  Historias de usuario - Rol Domiciliario


- Como domiciliario deseo registrarme en aplicación para poder realizar domicilios.
- Como domiciliario deseo seleccionar que pedido atendere para llevarle al cliente.
- Como domiciliario deseo  cancelar pedido asignado para tomar otro pedido que si pueda atender.
- Como domiciliaro deseo ver el estado de pedidos para no realizar incumplimientos.
- Como domiciliario deseo comprobar que lo solicitado por el cliente este acorde a lo que voy a entregar para que el cliente quede satisfecho.
- Como domiciliario deseo poder seleccionar el tipo de pago realizado por el cliente para entregar su pedido.
- Como domiciliario deseo cambiar el estado del pedido para que el tendero sepa que fue entregado.
- Como domiciliario deseo descargar de la aplicación un reporte de los pedidos realizados en el día para entregar cuentas al tendero.
- Como domiciliario deseo descargar de la aplicación un reporte de los pedidos realizados en el día para realizar cobro.
- Como domiciliario deseo que me llegue un mensaje por whatsapp para saber que me asignaron un domicilio.
**

HU-1
Narrativa: 

Como domiciliario 
Deseo ver el estado de pedidos
Para no realizar incumplimientos.

### Criterio de Aceptación: 

Dado que Juan es domiciliaro
Cuando Juan consulte sección de pedidos
Entonces se ve el estado de los pedidos.

### HU-2

### Narrativa:

Como domiciliario 
Deseo cambiar el estado del pedido 
Para que el tendero sepa que fue entregado.

### Criterio de Aceptación: 

Dado que Juan es domiciliaro
Cuando Juan actualice el estado de pedidos
Entonces se ven los pedidos entregados y no entregados.


### HU-3

### Narrativa:

Como domiciliario 
Deseo poder seleccionar el tipo de pago realizado por el cliente 
Para entregar su pedido.

### Criterio de Aceptación: 

Dado que Juan es domiciliaro
Cuando Juan seleccione tipo de pago
Entonces se visualizan los tipos de pago para cancelar el pedido.



### Requerimiento no funcional:

Nombre: usabilidad.rendimiento.
Escala: milisegundos entre que el domiciliario selecciona el pedido y se muestra la página con el resultado.
Métrica: promedio de los tiempos de búsqueda de pedido.
#### Criterio de aceptación
- La aplicación debe de contar con un tiempo de respuesta de máximo 5 segundos en todas las tareas, ya que de no ser así se considera que la aplicacion no cuenta con el tiempo esperado en respuesta. 

# Requerimientos no funcionales 

* Con la finalidad de un buen funcionamiento el tiempo de respuesta de la aplicación debe ser menor o igual a 5 segundos 
* Realizar transacciones seguras de los pagos realizados
* El tratamiento de datos debe ser privados y encriptados.
* Se desea que la aplicación tenga un buen manejo de concurrencia al momento de solicitar multiples personas un artículo en venta.

 
 
