agenda = []
def agregar(agenda):
    nota = input("Ingrese el nombre de la nota: ")
    fecha = input("Ingrese la fecha de creacion: ")
    desc = input("Ingrese la descripcion de la nota: ")
    agenda.append([nota, fecha, desc])
    return agenda

def ver_notas(agenda):
    for nota in agenda:
        print(nota[0])

def buscar_nota(agenda):
    nombre = input("Ingrese el nombre de la nota a buscar: ")
    for i in range(len(agenda)):
        if agenda[i][0] == nombre:
            print(agenda[i][0])
            print(agenda[i][1])
            print(agenda[i][2])

while True:
    print("1) Agregar nota\n2) Visualizar notas\n3) Buscar nota")
    opcion = int(input("Elija una opcion: "))
    if opcion == 1:
        agenda = agregar(agenda)
    if opcion == 2:
        ver_notas(agenda)
    if opcion == 3:
        buscar_nota(agenda)
