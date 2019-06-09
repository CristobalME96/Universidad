matriz = []
n = int(input("ingrese cantidad de clientes"))
for i in range(n):
    fila = []
    i = 0
    while i < 4:
        if i == 0:
            print("Nota atencion al cliente")
        if i == 1:
            print("Nota calidad")
        if i == 2:
            print("Nota precio")
        if i == 3:
            print("Nota ambiente")
        nota = int(input())
        if nota > 0 and nota <= 10:
            fila.append(nota)
            i += 1
        else:
            print("nota invalida")
    matriz.append(fila)
