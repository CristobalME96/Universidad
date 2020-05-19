class Nodo():
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

    def insertar(self, valor):
        # SI EL VALOR A INSERTAR ES MENOR QUE EL VALOR DEL NODO ACTUAL
        # SE INSERTA A LA IZQUIERDA
        if valor < self.valor:
            # SI EXISTE EL NODO IZQUIERDO APLICO RECURSIVIDAD
            if self.izq:
                self.izq.insertar(valor)
            else:
                # DE LO CONTRARIO, INSERTO EN EL IZQUIERDO
                self.izq = Nodo(valor)
        else:
            if self.der:
                self.der.insertar(valor)
            else:
                self.der = Nodo(valor)

        return True

    def buscar(self, valor):
        # SI EL VALOR ESTÁ EN EL NODO SE RETORNA EL NODO
        if self.valor == valor:
            return self
        # SI EL VALOR A BUSCAR ES MENOR QUE EL VALOR DEL NODO ACTUAL
        # SE BUSCA A LA IZQUIERDA
        if valor < self.valor:
            # SI EXISTE EL NODO IZQUIERDO APLICO RECURSIVIDAD
            if self.izq:
                return self.izq.buscar(valor)
        else:
            if self.der:
                return self.der.buscar(valor)
        return None

    def altura(self):
        # CUANDO LLEGO A LA HOJA CORTO LA RECURSIVIDAD Y RETORNO UN 1
        if not self.izq and not self.der:
            return 1

        # GENERO UNA ALTURA TANTO PARA LA IZQUIERDA O DERECHA
        altura_izq = 1
        altura_der = 1

        # SI HAY IZQUIERDO SIGO BAJANDO
        if self.izq:
            # SUMO 1 A
            altura_izq += self.izq.altura()

        if self.der:
            altura_der += self.der.altura()

        if altura_izq > altura_der:
            return altura_izq

        return altura_der

    def recorrer_inorden(self):
        if self.izq:
            self.izq.recorrer_inorden()
        print(self.valor)
        if self.der:
            self.der.recorrer_inorden()

    def cant_hojas(self):
        if not self.izq and not self.der:
            return 1

        hojas = 0

        if self.izq:
            hojas += self.izq.cant_hojas()

        if self.der:
            hojas += self.der.cant_hojas()

        return hojas

    def grado(self):
        if not self.izq and not self.der:
            return 0

        cant_grado = 0

        if self.izq:
            cant_grado += 1

        if self.der:
            cant_grado += 1

        return cant_grado

    def recorrer_preorden(self):
        print(self.valor)
        if self.izq:
            self.izq.recorrer_preorden()
        if self.der:
            self.der.recorrer_preorden()

    def recorrer_postorden(self):
        if self.izq:
            self.izq.recorrer_postorden()
        if self.der:
            self.der.recorrer_postorden()
        print(self.valor)

    def eliminar_nodo(self, key):
        if key < self.valor :
            self.izq.eliminar_nodo(key)

        elif key > self.valor:
            self.der.eliminar_nodo(key)

        else:
            if not self.izq:
                self = self.der

            elif not self.der:
                self = self.izq

            else:
                if self.izq:
                    temp = self.izq
                    while temp.der:
                        temp = temp.der
                    self.valor = temp.valor
                    temp = None
                else:
                    temp = self.der
                    while temp.izq:
                        temp = temp.izq
                    self.valor = temp.valor
                    temp = None



    def __str__(self):
        return "Valor del nodo: %s" % self.valor

raiz = Nodo(34)
raiz.insertar(4)
raiz.insertar(50)
raiz.insertar(22)
raiz.insertar(31)
raiz.insertar(90)
raiz.insertar(2)
raiz.insertar(15)
raiz.recorrer_inorden()
print("postorden")
raiz.recorrer_postorden()
print("hojas")
print(raiz.cant_hojas())
print("grado")
print(raiz.grado())
