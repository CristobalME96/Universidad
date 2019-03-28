print("Ingrese un numero positivo de 4 digitos")
num = int(input())
while num < 1000 or num > 9999:
    print("Numero invalido, por favor ingrese otro numero")
    num = int(input())
mitad1 = num // 100
mitad2 = num % 100
if mitad1 ** 2 + mitad2 ** 2 == num:
    print("El numero", num, "es doble-cuadrado")
else: print("El numero", num, "no es doble-cuadrado")
