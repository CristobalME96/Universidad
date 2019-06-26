# crear tuplas

nombre = "juan"
alumno = (nombre, 21, "primero")
print(alumno)

# tuplas en tuplas

alumno2 = ("pedro", 19, "primero", ("programacion", "matematica", "fisica"))
print(alumno2)

#acceder a los elementos
print(alumno2[0])
print(alumno2[3])
print(alumno2[3][1])

for v in alumno:
    print(v)

# empaquetar y desempaquetar tuplas
a = 1
b = "hola"
c = 3
tupla = (a, b, c)   #empaquetar
print(tupla)

x, y, z = tupla     #desempaquetar
print(x, " ", y, " ", z)
