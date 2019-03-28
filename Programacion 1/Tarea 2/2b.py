print("Ingrese una nota para entre 0 y 70 para conocer la calificacion")
nota = int(input())
while nota < 0 or nota > 70:
    print("nota invalida, ingrese otra nota")
    nota = int(input())
if nota == 70:
    print("Matricula de Honor")
elif nota > 60:
    print("Sobresaliente")
elif nota > 50:
    print("Notable")
elif nota > 40:
    print("Aprobado")
else: print("Reprobado")
