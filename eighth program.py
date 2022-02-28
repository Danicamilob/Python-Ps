print("Ingrese la cantidad de dulces a comprar:",end="")
cant = int(input())
print(cant)
print("Ingrese tipo de dulces [1,2,3]:", end="")
lista = [1,2,3]
tipo = int(input())

while tipo not in lista:
    print("")
    print("Ingrese tipo de dulces [1,2,3]:", end="")
    tipo = int(input())
    if tipo ==1:
        precio = 3
        monto = precio*cant
    if cant<=5:
        monto = monto - 0.5
    elif cant<=10:
        monto = monto*.93

    elif tipo==2:
        precio=4
        monto = precio*cant
        if cant<= 7:
            monto = monto
        else:
            monto = monto*.95
    elif tipo==3:
        precio = 5
        monto= precio*cant
        if cant >4:
            monto = monto*.85

print(tipo)
print("")

print(f'tipo de dulce: ' ,tipo)
print(f'precio unitario: ' ,precio)
print(f'cantidad de dulce:' ,cant)
print(f'monto de la venta' ,monto)
