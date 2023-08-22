# LAB. LENGUAJES FORMALES Y DE PROGRAMACION Sección B
## Practica # 1
### SEGUNDO SEMESTRE 2023
```js
Universidad San Carlos de Guatemala
Programador: Josué Nabí Hurtarte Pinto
Carne: 202202481
Correo: josuepinto013@gmail.com
```
---
## Descripción general del proyecto
El proyecto es sobre un sistema de gestión de inventario en el cual permite a los usuarios realizar tareas como crear y gestionar productos, realizar seguimiento de la cantidad disponible en diferentes ubicaciones, agregar stock o vender productos. Tambien cuenta con la opción de generar informes detallados de inventario para un mejor control y ver los detalles de los productos.

## Requerimientos mínimos del entorno de desarrollo
* Python 3.11: Debes de tener instalado python de la versión 3 en adelante. [Link de Descarga](https://www.python.org/downloads/).
* IDE (Entorno de Desarrollo Integrado) en nuestro caso usamos el editor de texto Visual Studio Code.
* Git: Es muy recomendable un control de versiones para gestionar y no perder cambios.


---
## Diccionario de clases 
* ### Producto 
     Esta clase es el costructor de producto
* ### InventoryManager
     Esta clase permite crear, editar y eliminar producots, asi como hacer acciones como agregar stock y vender productos. Ademas, puede generar informes sobre los productos y sus detalles. Todo esto gracias a los metodos y funciones que contiene.



## Diccionario de metodos y funciones

### producto.py
* #### \__init__( ) :
    Este metodo es un constructor que inicializa los atributos del producto cuando se crea una instancia de la clase.

    ![Producto](https://i.ibb.co/dknXW2n/Producto.png)

### cargar.py    
* ####   cargarArchivoInv( ): 
    Es responsable de cargar los datos de un archivo con extension .inv y leer linea por linea para agregar los productos al inventario.

    ![cargarArchivoInv](https://i.ibb.co/SJSLNmw/cargar-Archivo-Inv.png)
* #### cargarArchivoMov( ):
    Es responsable de cargar los datos de un archivo con extensión .mov y leer linea por linea para hacer los movimientos a realizar. 

    ![cargarArchivoMov](https://i.ibb.co/gyVvgxV/cargar-Archivo-Mov.png)

### inventario.py
* #### \__init__( ) :
    Este metodo se utiliza para inicializar el atributo inventario, que es un lista que almacenará los productos en el inventario.

    ![listaProductos](https://i.ibb.co/yhRPdfC/lista-Productos.png)
    
* #### Encontrar_producto( ):
    Esta es una funcion para encontrar productos en el inventario y si coinciden los datos devuelve el objeto.

    ![encontrarProdcuto](https://i.ibb.co/1ZNPPLc/encontrar-Producto.png)

* #### crear_producto( ):
    Esta es una funcion la cual crea un nuevo producto usando la clase producto y lo agrega al inventario, pero antes verifica si ya existe con el mismo nombre y ubicacion para que no hallan repetidos.  

    ![crearProdcuto](https://i.ibb.co/pJyhrXr/crear-Producto.png)

* #### agregar_stock( ):
    Esta funcion busca en el inventario un producto y si lo encuentra le suma la cantidad agregada.

    ![agregarStock](https://i.ibb.co/8M4yhbb/agregar-Stock.png)

* #### vender_producto( ):
    Esta funcion busca en el inventario un producto y si lo encuentra le resta la cantidad especificada.

    ![venderProducto](https://i.ibb.co/QpFk18r/vender-Producto.png)

* #### generar_inventario( ):
    Esta funcion genera un inventario de nuestro inventario mostrando el nombre, cantidad, precio unitario, valor total y la ubicacion.

    ![generarInforme](https://i.ibb.co/vVYktFy/generar-Informe.png)

### main.py

* #### main( ):
    Esta funcion contiene un menu con 4 opciones las cuales son: 1. Cargar Inventario Inicial 2. Cargar Instrucciones de Movimientos 3. Crear Informe de Inventario 4. Salir. Se hizo con un while e ifs y cuando seleccione la opcion que desea llama al metodo.

    ![Main](https://i.ibb.co/fp209T8/main.png)




