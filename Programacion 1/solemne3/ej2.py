matriz = []
for i in range(4):
    lista = []
    for j in range(4):
        if i == j:
            lista.append(1)
        else:
            lista.append(0)
    matriz.append(lista)
