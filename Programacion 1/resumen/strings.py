#guardar un string

cadena = "hola mundo"
print(cadena)

# concatenar strings

cadena2 = "concatenando " + cadena
print(cadena2)

# repetir string

cadena3 = "ja"
print(cadena3 * 4)

# leer caracteres

cadena = "hola"
for i in range(len(cadena)): # iteracion segun el largo
    print(cadena[i])

for C in cadena:    #iteracion por los caracteres
    print(C)

# transformaciones

a = int("5") # transformar el 5 de string a tipo int
b = 3
c = a + b
print(c)
