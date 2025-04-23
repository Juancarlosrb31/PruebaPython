inventario = int(input("Cuantos pares de zapatos hay en la zapateria?: "))
print(f"El inventario contiene {inventario} pares de zapatos")
transaccion = 0

while inventario > 0:
    vendidos =  int(input("Cuantos pares de zapatos se vendieron?: "))
    
    if vendidos > inventario:
        print("No hay suficientes pares de zapatos en stock. Solo hay" , inventario, "pares de zapatos disponibles." )

    else: 
        inventario -= vendidos
        print(f"Quedan {inventario} pares de zapatos")
        transaccion += 1

print(f"Se han realizado {transaccion} transacciones" )