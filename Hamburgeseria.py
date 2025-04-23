inventario = 100
print(f"El inventario contiene {inventario} hambuerguesas")
 
while inventario > 0:
    if inventario <= 10:
        print("ADVERTANCIA: EL INVENTARIO ESTA CASI VACIO.") 
    num_hamburguesas = int(input("cuantas hamburguesas quiere cliente?"))
    if num_hamburguesas > inventario:
        print(f"No hay suficientes hamburguesas en stock. Solo hay {inventario}")
    else:
        inventario -= num_hamburguesas
        print(f"El cliente ha pedido {num_hamburguesas} hamburguesas el inventario ahora tiene {inventario} Hamburguesas")