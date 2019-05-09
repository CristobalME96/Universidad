#letra = 10
#ñ á é í ó ú = 30
# numero = 20

letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
          "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numeros = ["0","1","2","3","4","5","6","7","8","9"]

def buscar_letra(L, letras):
    for i in letras:
        if i == L:
            return True
    return False

def buscar_numero(L, numeros):
    for i in numeros:
        if i == L:
            return True
    return False

def check(mensaje, letras, numeros):
    total = 0
    for i in range(len(mensaje)):
        if buscar_letra(mensaje[i], letras):
            total += 10
        elif buscar_numero(mensaje[i], numeros):
            total += 20
        elif mensaje[i] != ' ':
            total += 30
    return total

mensaje = input("Ingrese su mensaje: ")
valor = check(mensaje, letras, numeros)
print("El valor de su mensaje es $", valor)
