from funciones import (
    mostrar_menu,
    ingresar_producto,
    realizar_venta,
    verificar_inventario
)

productos = []
proveedores = []
precios = []
cantidades = []
codigos = []
siguiente_codigo = 1
funcionamiento = True

while funcionamiento:

    decision = mostrar_menu()

    if decision == 1:

        siguiente_codigo = ingresar_producto(
            productos,
            proveedores,
            precios,
            cantidades,
            codigos,
            siguiente_codigo
        )
