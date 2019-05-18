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

def potenciapromedio(Potencia):
    suma = 0
    for S in Potencia:
        for D in S:
            suma += D
    promedio = suma/len(Potencia)*7
    return promedio

def potenciapromediodia(Potencia):
    promedio = [0,0,0,0,0,0,0]
    for S in Potencia:
        for i in range(len(s)):
            promedio[i] += S[i]
    for i in range(len(suma)):
        promedio[i] = promedio[i]/len(Potencia)
    dia_mayor = 0
    for i in range(len(promedio)):
        if promedio[dia_mayor] < promedio[i]:
            dia_mayor = i

def mayores(Potencia):
    promedio = potenciapromedio(Potencia)
    Total = 0
    for S in Potencia:
        for D in S:
            if S > promedio:
                total += 1
    print(Total)

potencia = ingresarPotencia()
potenciapromedio(potencia)
