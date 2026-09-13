# Sistema-de-Inventario
Proyecto de Fundamentos de la Programación

## Qué hace el programa
Nuestro programa de Python implementa las funciones principales para un sistema básico de control de inventario,  registro de productos, 
transacciones de venta y consultas de stock en consola. 
Utiliza estructuras de datos paralelas basadas en listas para almacenar la información de los artículos.

## Cómo ejecutarlo
python main.py
## Estructura de Datos
El sistema opera sobre cinco listas paralelas y una variable de control de códigos:
* `productos`: Almacena los nombres de los artículos.
* `proveedores`: Contiene los nombres de los proveedores asignados a cada producto.
* `precios`: Guarda el valor unitario de cada producto (tipo `float`).
* `cantidades`: Registra las existencias actuales en stock (tipo `int`).
* `codigos`: Identificadores únicos asignados secuencialmente a cada producto.
* `siguiente_codigo`: Entero que indica el próximo código disponible para asignar.

## Funciones Principales
### 1. `ingresar_producto()` - María Guirola
Gestiona el registro de nuevos artículos o la reposición de stock para productos ya existentes en el inventario.
* **Productos Existentes (`existe == 1`):** Permite buscar un artículo por su código único e incrementar su stock actual sumando la cantidad ingresada. Valida que el código exista y que la cantidad no sea negativa.
* **Productos Nuevos (`existe == 2`):** Solicita el nombre del producto, el proveedor (con opción de registrar uno nuevo o seleccionar de una lista de proveedores ya existentes), el precio unitario y el stock inicial. Asigna de forma automática el identificador correspondiente mediante `siguiente_codigo`.
  
### 2. `realizar_venta()` - Carlos Campos
Simula el proceso de cobro y despacho de productos a un cliente, calculando el total de la cuenta.

* Despliega la lista de productos disponibles con sus respectivos precios, códigos y existencias en tiempo real.
* Permite seleccionar múltiples artículos de forma consecutiva dentro de un ciclo de venta.
* Descuenta automáticamente la cantidad vendida del stock disponible y valida que no se intente vender más unidades de las existentes.
* Ofrece opciones para finalizar la transacción en cualquier momento o cerrar la venta de forma anticipada si ocurre un error de stock.

### 3. `verificar_inventario()` - Ítalo Vidaurre
Consulta rápida del estado de un producto específico mediante su código.

* Muestra el nombre, proveedor, precio y stock actual del artículo consultado.
* Incorpora un sistema de alerta automática que notifica en pantalla si la cantidad en inventario es menor a $15$ unidades.

### 4. `mostrar_menu()` - Ítalo Vidaurre
Despliega la interfaz de navegación principal en la consola, permitiendo al usuario seleccionar entre las distintas operaciones del sistema y retornar la opción elegida para su control en el flujo principal del programa.
## Funcionamiento de `main.py`
El código comienza importando las operaciones centrales desde el módulo externo `inventario`. Esto mantiene el proyecto modularizado, separando la lógica interna de las funciones de la interfaz general del usuario. Antes de iniciar la interacción con el usuario, el programa prepara el entorno creando las estructuras de datos vacías que simulan la base de datos en memoria declarando las lista a utilizar que se introducirán en las funciones. Se usa un while para mantener el programa en funcionamiento, y se reproducirá las veces que sea necesaria realizando las diferentes opciones hasta que `decision` sea diferente a un número válido (del 1 al 4), utilizando estructuras condicionales para decidir que función utilizar en cada caso.
