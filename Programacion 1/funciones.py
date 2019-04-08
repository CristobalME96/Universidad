def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    return a / b

print("ingrese 2 numeros")
num1 = int(input())
num2 = int(input())

print("elija una operacion:\n1) Suma \n2) Resta \n3) Multiplicacion \n4) Division")
opcion = int(input())
if opcion == 1:
    print(suma(num1, num2))
if opcion == 2:
    print(resta(num1, num2))
if opcion == 3:
    print(multiplicacion(num1, num2))
if opcion == 4:
    print(division(num1, num2))
