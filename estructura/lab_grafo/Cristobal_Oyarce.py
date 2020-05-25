class Grafo():
    # TIPO: L => LISTA DE ADYACENCIA
    #       M => MATRIZ DE ADYACENCIA
    def __init__(self, grafo, tipo):
        # VALIDO EL TIPO DE ENTRADA
        # SI ES LISTA DE ADYACENCIA
        if tipo == 'L':
            # SI ES LISTA, SE MANTIENE LA ESTRUCUTRA
            self.lista_adyacencia = grafo
            # SE APLICA LA FUNCIÓN PARA REALZIAR LA TRANSFORMACIÓN
            self.matriz_adyacencia = self.lista_a_matriz(grafo)
        # SI ES MATRIZ DE ADYACENCIA
        elif tipo == 'M':
            # SE APLICA LA FUNCIÓN PARA REALZIAR LA TRANSFORMACIÓN
            self.lista_adyacencia = self.matriz_a_lista(grafo)
            # SI ES LISTA, SE MANTIENE LA ESTRUCUTRA
            self.matriz_adyacencia = grafo
        else:
            print("Tipo de dato incorrecto.")

    def lista_a_matriz(self, lista_adyacencia):
        matriz_adyacencia = []
        for i in range(len(lista_adyacencia)):
            lista = []
            for j in range(len(lista_adyacencia)):
                lista.append(0)
            matriz_adyacencia.append(lista)
        for i in range(len(lista_adyacencia)):
            for conexion in lista_adyacencia[i]:
                matriz_adyacencia[i][conexion[0]] = conexion[1]
        return matriz_adyacencia

    def matriz_a_lista(self, matriz_adyacencia):
        # GENERAMOS UNA LISTA DE ADYACENCIA
        lista_adjacencia = []
        # RECORREMOS LOS NODOS DE LA MATRIZ
        for _nodo in matriz_adyacencia:
            conexion = []
            # RECORREMOS LAS ARISTAS DE LA MATRIZ POR POSICIÓN
            for id_nodo in range(len(_nodo)):
                # SI EL VALOR DE LA ARISTA DEL NODO ES MAYOR A 0, ES PORQ HAY CONEXIÓN
                if _nodo[id_nodo] > 0:
                    conexion.append(
                        # (ID DEL NODO, COSTO DE ARISTA)
                        (id_nodo, _nodo[id_nodo])
                    )
            # AGREGO EL NODO A LA LISTA DE ADYACENCIA
            lista_adjacencia.append(conexion)
        return lista_adjacencia


    # N DEL GRAFO
    def obtener_orden_matriz(self):
        return len(self.matriz_adyacencia)

    def obtener_orden_lista(self):
        return len(self.lista_adyacencia)

    # M TAMAÑO DEL GRAFO
    def obtener_tamano_matriz(self):
        t = 0
        for i in range(len(self.matriz_adyacencia)):
            for j in range(i+1):
                if self.matriz_adyacencia[i][j] != 0:
                    t += 1
        return t

    def obtener_tamano_lista(self):
        t = 0
        for i in range(len(self.lista_adyacencia)):
            for conexion in self.lista_adyacencia[i]:
                if conexion[0] < i:
                    t += 1
        return t

    def obtener_grados_matriz(self):
        grados = []
        for i in range(len(self.matriz_adyacencia)):
            count = 0
            for j in range(len(self.matriz_adyacencia)):
                if self.matriz_adyacencia[i][j] != 0:
                    count += 1
            grados.append(count)
        return grados

    def obtener_grados_lista(self):
        grados = []
        for i in self.lista_adyacencia:
            grados.append(len(i))
        return grados

# grafo_matriz = [
#     [ 0, 4, 0, 0, 0, 0, 0, 8, 0 ],
#     [ 4, 0, 8, 0, 0, 0, 0, 11, 0 ],
#     [ 0, 8, 0, 7, 0, 4, 0, 0, 2 ],
#     [ 0, 0, 7, 0, 9, 14, 0, 0, 0 ],
#     [ 0, 0, 0, 9, 0, 10, 0, 0, 0 ],
#     [ 0, 0, 4, 14, 10, 0, 2, 0, 0 ],
#     [ 0, 0, 0, 0, 0, 2, 0, 1, 6 ],
#     [ 8, 11, 0, 0, 0, 0, 1, 0, 7 ],
#     [ 0, 0, 2, 0, 0, 0, 6, 7, 0 ],
# ]
#
#
# grafo_M = Grafo(grafo_matriz, 'M')
# for _nodo in grafo_M.lista_adyacencia:
#     print(_nodo)
# print(grafo_M.obtener_orden_matriz())
# print(grafo_M.obtener_tamano_matriz())
# print(grafo_M.obtener_grados_matriz())

grafo_lista = [
    [(1, 4), (7, 8)],
    [(0, 4), (2, 8), (7, 11)],
    [(1, 8), (3, 7), (5, 4), (8, 2)],
    [(2, 7), (4, 9), (5, 14)],
    [(3, 9), (5, 10)],
    [(2, 4), (3, 14), (4, 10), (6, 2)],
    [(5, 2), (7, 1), (8, 6)],
    [(0, 8), (1, 11), (6, 1), (8, 7)],
    [(2, 2), (6, 6), (7, 7)],
]


grafo_L = Grafo(grafo_lista, 'L')
for _nodo in grafo_L.matriz_adyacencia:
    print(_nodo)
print(grafo_L.obtener_orden_lista())
print(grafo_L.obtener_tamano_lista())
print(grafo_L.obtener_grados_lista())
