matriz = [[5,0,0],[0,3,0],[0,0,1]]
for fila in matriz:
    print(fila)
for fila in matriz:
    for x in fila:
        if x != 0:
            print(1)
        else:
            print(0)
