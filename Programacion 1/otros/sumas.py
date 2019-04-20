negativos = int()
positivos = int()
for i in range(0,15):
    num = int(input())
    if num >= 0:
        positivos += num
    else:
        negativos += num
print("Suma negativa: ", negativos)
print("Suma positiva: ", positivos)
