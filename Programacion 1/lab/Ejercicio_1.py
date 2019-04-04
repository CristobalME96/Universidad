numero = 2
count = 1
while count <= 347:
    numero += 1
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
        if i == numero - 1 and primo:
            count += 1
print("El primo N° 347 es el", numero)
