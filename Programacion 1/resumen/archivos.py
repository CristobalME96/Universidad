# escribir en un archivo o crearlo si no existe

file = open("texto.txt", "w")
file.write("Hola mundo")
file.write("\n")
file.write("chao mundo")
file.close()

# leer un archivo

file = open("texto.txt", "r")
print(file.read())      # lee el archivo completo
file.close()

file = open("texto.txt", "r")
print(file.read(3))     #lee los siguientes N caracteres
print(file.readline())  # lee hasta el final de la linea
print(file.read(6))
file.close()

file = open("texto.txt", "r")
lista = file.readline().split(" ")  # separa la linea y devuelve una lista
print(lista[0])
print(lista[1])
file.close()

file = open("texto.txt", "r")
for linea in file:  # itera linea por linea
    print(linea)
file.close()

# agregar texto a un archivo
var = 12
file = open("texto.txt", "a")
file.write("\ntexto agregado " + str(var))
file.close()

file = open("texto.txt", "r")
print(file.read())      # lee el archivo completo
file.close()
