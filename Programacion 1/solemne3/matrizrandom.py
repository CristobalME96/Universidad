import random
m = random.randint(3,10)
n = random.randint(3,10)
matriz = []
for i in range(m):
    fila = []
    for j in range(n):
        fila.append(random.randint(1,100))
    matriz.append(fila)
for fila in matriz:
    print(fila)
