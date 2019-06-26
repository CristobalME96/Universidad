# crear diccionarios

dict = {}   #diccionario vacio
llave = "fruta"
valor = "manzana"
dict2 = {llave: valor} #diccionario con llave "fruta" y valor "manzana"
dict3 = {"fruta": "pera", "numero": 2, "palabra": "hola"} #multiples objetos
dict4 = {"lista":[1,"a","letras"]}  # lista como valor

print("impresion del diccionario 3:")
print(dict3)
print("impresion del diccionario 4 con lista:")
print(dict4)
print(dict4["lista"])
print(dict4["lista"][1])

# agregar objetos al diccionario

dict2["pais"]="Chile"
dict2.update({"ciudad":"santiago"})

print("impresion diccionario 2 con nuevos valores:")
print(dict2)

# combinar diccionarios

dict.update(dict2)
dict.update(dict3)

print("diccionarios 2 y 3 combinados en el primero:")
print(dict)

# acceder a los objetos

if "pais" in dict:  #consulta por la llave en el diccionario
    print("pais existe con el valor: ", dict["pais"])
else:
    print("no se encuentra en el diccionario")

for L in dict3:     # itera en las llaves del diccionario
    print(L)

for V in dict3.values():   # itera en los valores del diccionario
    print(V)

for L, V in dict3.items():  # itera en llaves y valores
    print(L, " ", V)

# modificar objetos

dict3["fruta"] = "naranja"   # modifica el objeto con la llave "fruta"
print(dict3)

del dict3["numero"]   # elimina el objeto con la llave "numero"
print(dict3)
