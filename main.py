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
    elif decision == 2:
        realizar_venta(
            productos,
            proveedores,
            precios,
            cantidades,
            codigos
        )
    elif decision == 3:
        verificar_inventario(
            productos,
            proveedores,
            precios,
            cantidades,
            codigos
        )
    elif decision == 4:
        funcionamiento = False
        print("\nTen un buen dia.")
    else:
        print("\nError. Esa opción no existe.")
