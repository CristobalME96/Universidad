#desarrollar un software que le permita al usuario calcular el factorial de un numero, la potencia, y finalmente fibonacci, las opciones deben ser escogidas por el usuario.
#al final vuelve al inicio
opt = 0
while opt != 4:
    print("Hola, que desea calcular \n1. Factorial\n2. Potencia \n3. Fibonacci\n4. Salir")
    opt = int(input())
    if opt == 1:
        print("Ingrese un numero")
        num = int(input())
        fact = 1
        for i in range(1, num + 1):
            fact = fact * i
        print("El factorial de", num, "es", fact)
    if opt == 2:
        print("Ingrese un numero")
        num = int(input())
        print("La potencia de", num, "es", num ** num)
    if opt == 3:
        print("Ingrese un numero")
        num = int(input())
        a = 0
        b = 1
        fib = 0
        for i in range(0, num):
            fib = a + b
            a = b
            b = fib
        if num == 1: fib = 1
        print("El valor Fibonacci de", num, "es", fib)
print("Adios")
