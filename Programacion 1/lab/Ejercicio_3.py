numero = int(input("Ingrese un numero positivo menor que 2^58: "))
while numero > 2 ** 58 or numero < 1:
    numero = int(input("Numero invalido, por favor ingrese otro: "))
while numero != 1:
    if numero % 2 == 0:
        numero = int(numero / 2)
    else:
        numero = (numero * 3) + 1
    print(numero)
