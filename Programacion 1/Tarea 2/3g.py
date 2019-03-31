print("Ingrese el grado de dificultad y las notas de los jueces")
dif = float(input("grado de dificultad:"))
for i in range(7):
    print("Ingrese la nota del juez", i + 1)
    nota = float(input())
    if i == 0:
        min = nota
        max = nota
        suma = nota
    else:
        if nota < min:
            min = nota
        if nota > max:
            max = nota
        suma += nota
print("El puntaje total es:", (suma - max - min) * 0.6 * dif)
