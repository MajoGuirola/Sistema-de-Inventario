def ingresar_producto(productos, proveedores, precios, cantidades, codigos, siguiente_codigo):
    if len(productos) == 0:
        print("\nNo hay productos registrados.")
        print("Se ingresará un producto nuevo.")
        existe = 2
    else:
        print("\n¿Es un producto ya existente?")
        print("1 - Si")
        print("2 - No")
        print("0 - Cancelar")
        existe = int(input("Opción: "))
        while existe not in [0, 1, 2]:
            print("Opción no válida.")
            print("1 - Si")
            print("2 - No")
            print("0 - Cancelar")
            existe = int(input("Opción: "))
        if existe == 0:
            print("Ingreso de producto cancelado.")
            return siguiente_codigo
    if existe == 1:
        codigo = int(input("\nIngresa el codigo del producto: "))
        if codigo not in codigos:
            print("Error. Ese codigo no está asociado a ningún producto.")
            return siguiente_codigo
        posicion = codigos.index(codigo)
        cantidad_mas = int(
            input("¿Cuantas unidades desea ingresar? (0 para cancelar): ")
        )
        if cantidad_mas == 0:
            print("Ingreso cancelado.")
            return siguiente_codigo

        while cantidad_mas < 0:
            print("Error. La cantidad no puede ser negativa.")
            cantidad_mas = int(
                input("¿Cuantas unidades desea ingresar? (0 para cancelar): ")
            )
            if cantidad_mas == 0:
                print("Ingreso cancelado.")
                return siguiente_codigo
        cantidades[posicion] += cantidad_mas
        print("Stock actualizado correctamente.")
    else:
        print("\n--- NUEVO PRODUCTO ---")
        print("Escribe 0 para cancelar.")
        nombre = input("Escribe el nombre del producto: ")
        if nombre == "0":
            print("Ingreso de producto cancelado.")
            return siguiente_codigo
        while nombre.strip() == "":
            print("El nombre no puede estar vacío.")
            nombre = input("Escribe el nombre del producto: ")
            if nombre == "0":
                print("Ingreso de producto cancelado.")
                return siguiente_codigo
            
        print("\n¿Es proveedor nuevo?")
        print("1 - Si")
        print("2 - No")
        print("0 - Cancelar")
        existe_proveedor = int(input("Opción: "))
        while existe_proveedor not in [0, 1, 2]:
            print("Opción no válida.")
            print("1 - Si")
            print("2 - No")
            print("0 - Cancelar")
            existe_proveedor = int(input("Opción: "))
        if existe_proveedor == 0:
            print("Ingreso de producto cancelado.")
            return siguiente_codigo
        
        if existe_proveedor == 1:
            proveedor = input("Escribe el nombre del proveedor: ")
            if proveedor == "0":
                print("Ingreso de producto cancelado.")
                return siguiente_codigo
            while proveedor.strip() == "":
                print("El nombre del proveedor no puede estar vacío.")
                proveedor = input(
                    "Escribe el nombre del proveedor: "
                )
                if proveedor == "0":
                    print("Ingreso de producto cancelado.")
                    return siguiente_codigo
        else:

            proveedores_unicos = []
            for proveedor_existente in proveedores:
                if proveedor_existente not in proveedores_unicos:
                    proveedores_unicos.append(proveedor_existente)
            print("\n--- PROVEEDORES REGISTRADOS ---")
            for i in range(len(proveedores_unicos)):
                print(i + 1, "-", proveedores_unicos[i])
            print("0 - Cancelar")
            codigo_proveedor = int(
                input("Ingrese el numero del proveedor: ")
            )
            if codigo_proveedor == 0:
                print("Ingreso de producto cancelado.")
                return siguiente_codigo
            while (codigo_proveedor < 1 or codigo_proveedor > len(proveedores_unicos)):
                print("Error. Ese proveedor no existe.")
                codigo_proveedor = int(
                    input("Ingrese el numero del proveedor: ")
                )
                if codigo_proveedor == 0:
                    print("Ingreso de producto cancelado.")
                    return siguiente_codigo
            proveedor = proveedores_unicos[codigo_proveedor - 1]
        precio = float(
            input("Escribe el precio del producto (0 para cancelar): ")
        )
        if precio == 0:
            print("Ingreso de producto cancelado.")
            return siguiente_codigo
        while precio < 0:
            print("Error. El precio no puede ser negativo.")
            precio = float(
                input("Escribe el precio del producto (0 para cancelar): ")
            )
            if precio == 0:
                print("Ingreso de producto cancelado.")
                return siguiente_codigo
        cantidad = int(
            input("¿Cuantas unidades desea ingresar? (0 para cancelar): ")
        )
        if cantidad == 0:
            print("Ingreso de producto cancelado.")
            return siguiente_codigo
        while cantidad < 0:
            print("Error. La cantidad no puede ser negativa.")
            cantidad = int(
                input("¿Cuantas unidades desea ingresar? (0 para cancelar): ")
            )
            if cantidad == 0:
                print("Ingreso de producto cancelado.")
                return siguiente_codigo

        codigos.append(siguiente_codigo)
        productos.append(nombre)
        proveedores.append(proveedor)
        precios.append(precio)
        cantidades.append(cantidad)

        print("\nProducto agregado correctamente.")
        print("Codigo del producto:", siguiente_codigo)
        siguiente_codigo += 1
    return siguiente_codigo

def realizar_venta(productos, proveedores, precios, cantidades, codigos):
    if len(productos) == 0:
        print("\nNo se puede realizar una venta.")
        print("No hay productos registrados.")
        return
    cuenta = 0
    continuar_venta = True
    productos_vendidos = 0
    while continuar_venta:

        print("\n--- PRODUCTOS DISPONIBLES ---")

        for i in range(len(productos)):

            print(f"Codigo: {codigos[i]} | {productos[i]}| Stock: {cantidades[i]},| Precio: {precios[i]}")
        print("\nEscribe 0 para cancelar la venta.")
        codigo = int(
            input("Escribe el codigo del producto: ")
        )
        if codigo == 0:
            if productos_vendidos == 0:
                print("\nVenta cancelada.")
                cuenta = 0
                continuar_venta = False
            else:
                print("\nYa se ha vendido al menos un producto.")
                print("La venta se terminará con la cuenta actual.")
                print(f"La cuenta a pagar es de: {cuenta}")
                continuar_venta = False
            continue

        if codigo not in codigos:
            print(f"Error. El codigo {codigo} no está asociado a ningún producto.")
            continue
        posicion = codigos.index(codigo)
        print("\nProducto:", productos[posicion])
        print("Proveedor:", proveedores[posicion])
        print("Precio:", precios[posicion])
        print("Stock disponible:", cantidades[posicion])
        cantidad_menos = int(input(
                "¿Cuantas unidades vas a vender? "
                "(0 para cancelar): "
            )
        )
        if cantidad_menos == 0:
            print("Operación cancelada.")
            continue
        while cantidad_menos < 0:
            print("Error. La cantidad no puede ser negativa.")
            cantidad_menos = int(
                input(
                    "¿Cuantas unidades vas a vender? "
                    "(0 para cancelar): "
                )
            )
            if cantidad_menos == 0:
                break
        if cantidad_menos == 0:
            continue

        if cantidad_menos > cantidades[posicion]:
            print("Error. No hay suficiente stock del producto.")
            print(f"Stock disponible: {cantidades[posicion]}")
            print("\n¿Quieres intentarlo de nuevo?")
            print("1 - Reintentar")
            print("2 - Terminar venta")
            intentar = int(input("Opción: "))
            if intentar == 2:
                if productos_vendidos == 0:
                    print("Venta cancelada.")
                    continuar_venta = False
                else:
                    print(
                        "La cuenta a pagar es de:",
                        cuenta
                    )
                    continuar_venta = False
            continue
        cantidades[posicion] -= cantidad_menos
        cuenta += precios[posicion] * cantidad_menos
        productos_vendidos += 1
        print("\nProducto agregado a la venta.")
        print(f"La cuenta actual es de {cuenta}")
        print("\n¿Continuar la venta?")
        print("1 - Terminar")
        print("2 - Continuar")
        intentar = int(input("Opción: "))
        while intentar not in [1, 2]:
            print("Opción no válida.")
            print("1 - Terminar")
            print("2 - Continuar")
            intentar = int(input("Opción: "))
        if intentar == 1:
            continuar_venta = False
            print(
                "\nLa cuenta a pagar del cliente es de:",
                cuenta
            )
