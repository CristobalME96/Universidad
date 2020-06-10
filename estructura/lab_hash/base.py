class Hash():
    def __init__(self, tamano, umbral_desborde):
        # TAMAÑO DEL HASH
        self.tamano = tamano
        # CANTIDAD DE ELEMENTOS INSERTADOS
        self.elementos_insertados = 0
        # UMBRAL PARA APLICAR HASING
        self.umbral_desborde = umbral_desborde
        # ELEMENTOS DE LA TABLA
        ## None => NO SE INSERTARON ELEMENTOS
        ## Valor X => HAY ELEMENTO INSERTADO
        ## -1 => ESTÁ LIBRE, PERO UN ELEMENTO FUE ELIMINADO
        self.elementos = [None] * tamano

    def insertar(self, llave):
        # OBTENGO LA POSICIÓN A INSERTAR
        posicion = self.h(llave)
        # SI NO HAY ELEMENTO SE INSERTA
        # SI ES NONE Ó .....
        if not self.elementos[posicion]:
            self.elementos[posicion] = llave
        else:
            pass

    def eliminar(self, llave):
        pass

    def buscar(self, llave):
        pass

    def obtener_umbral_desborde(self):
        pass

    def rehashing(self):
        pass

    # EXPLORACIÓN LINEAL
    def exploracion_lineal(self, llave, i):
        return (self.h(llave) + self.f(i)) % self.tamano

    # H
    def h(self, llave):
        return llave % self.tamano

    # F
    def f(self, i):
        return i
