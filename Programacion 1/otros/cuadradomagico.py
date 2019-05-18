def verificar(cuadrado):
    magico = True
    suma = sum(cuadrado[0])
    otra_suma = 0
    for i in range(len(cuadrado)):          #columnas
        for j in range(len(cuadrado)):
            otra_suma += cuadrado[i][j]
        if suma != otra_suma:
            magico = False
        otra_suma = 0
    for i in range(len(cuadrado)):          #filas
        for j in range(len(cuadrado)):
            otra_suma = cuadrado[j][i]
        if suma != otra_suma:
            magico = False
        otra_suma = 0
    for i in range(len(cuadrado)):
        otra_suma = cuadrado[i][i]
    if suma != otra_suma:
        magico = False
    otra_suma = 0
    j = len(cuadrado) - 1
    for i in range(len(cuadrado)):
        otra_suma = cuadrado[i][j-i]
    if suma != otra_suma:
        magico = False
    otra_suma = 0
    if magico:
        return 1
    else:
        return -1
