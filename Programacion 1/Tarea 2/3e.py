print("Ingese 4 numeros para ser ordenados")
n1 = int(input("numero 1:"))
n2 = int(input("numero 2:"))
n3 = int(input("numero 3:"))
n4 = int(input("numero 4:"))
if n1 < n3:
    var = n1
    n1 = n3
    n3 = var
if n2 < n4:
    var = n2
    n2 = n4
    n4 = var
if n1 < n2:
    var = n1
    n1 = n2
    n2 = var
if n3 < n4:
    var = n3
    n3 = n4
    n4 = var
if n2 < n3:
    var = n2
    n2 = n3
    n3 = var
print(n1, n2, n3, n4)
