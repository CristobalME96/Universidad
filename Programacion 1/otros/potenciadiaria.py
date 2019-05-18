def ingresarPotencia():
    Potencia = []
    semana = []
    for i in range(52):
        print("Semana ", i + 1)
        for j in range(7):
            semana.append(int(input("Potencia suministrada dia " + str(j) + ": ")))
            if semana[0] == -1:
                break
        if semana[0] == -1:
            break
        else:
            Potencia.append(semana)
            semana = []
    return Potencia

potencia = ingresarPotencia()
for S in potencia:
    for D in S:
        print(D)
