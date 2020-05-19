class BinHeap:
    def __init__(self, alist):
        self.heapList = [0] ### inicializo el arreglo
        self.currentSize = 0

        # EMPEZAMOS AGREAGR LOS ELEMENTOS AL HEAP
        for elemento in alist:
          self.insert(elemento)


    def flotar(self, i):
		# ENTREGA EL NÚMERO ENTERO DE LA DIVISION
        while i // 2 > 0:
            #### mientras que el padre del nodo exista y sea 1 o mas, hará flotar el nodo
            if self.heapList[i] > self.heapList[i // 2]:
				# GUARDAMOS EL VALOR DEL PADRE
                tmp = self.heapList[i // 2]
				# EL PADRE TENDRÁ EL VALOR DEL HIJO MAYOR
                self.heapList[i // 2] = self.heapList[i]
				# AHORA EL HIJO MAYOR TENDRÁ EL VALOR DEL PADRE
                self.heapList[i] = tmp
			# VOLVEMOS A CALCULAR EL PADRE PARA SABER SI ÉSTE TIENE QUE VOLVER A SUBIR
            i = i // 2

    def insert(self, k):
      self.heapList.append(k)
      ### Agrega el elemento al final de la lista

      self.currentSize = self.currentSize + 1
      ### suma 1 al tamaño de el arreglo y almacena la posicion del último elemento agregado

      self.flotar(self.currentSize)
	  ## Llama a la funcion flotar para ubicar el nuevo nodo donde corresponda

    def hundir(self, i):
      while (i * 2) <= self.currentSize:
          ### mientras queden nodos por recorrer
          hijoMayor = self.hijoMayor(i)
          ### almaceno posicion del hijo es mayor
          if self.heapList[i] < self.heapList[hijoMayor]:
              ##si lo que esta en la posicion actual es mayor a lo que esta en la posicion del hijo menor
              tmp = self.heapList[i]
              ### guardo valor actual en var tmp
              self.heapList[i] = self.heapList[hijoMayor]### reemplazo valor actual por el de hijo menor
              self.heapList[hijoMayor] = tmp
              #### el valor actual ahora almacena lo que estaba en la posicion actual
          i = hijoMayor ### i toma el valor del hijo 

    def hijoMayor(self, i):
        # PREGUNTO SI ES QUE TENGO NO HIJO DERECHO
        if i * 2 + 1 > self.currentSize:
            # POR LO TANTO SOLAMENTE RETORNA LA POSICIÓN DEL IZQUIERDO
            ### cuando solo tiene un hijo lo retorna
            return i * 2
        else: ### cuando tiene dos hijos
            if self.heapList[i * 2] > self.heapList[i * 2 + 1]: ### el hijo izquierdo es mayor que el derecho?
                return i * 2 ### retorno hijo izquiero
            else:
                return i * 2 + 1 ### retorno hijo derecho

    def delMax(self):
      _max = self.heapList[1]
      ### almaceno el valor de la raiz
      self.heapList[1] = self.heapList[self.currentSize] ### la nueva raiz ahora es el ultimo elemento de la lista
      self.currentSize = self.currentSize - 1 ### se disminuye el tamaño
      self.heapList.pop()### se elimina el primer elemento de la lista
      self.hundir(1)
      ### se llama a la funcion hundir para reordenar el heap
      return _max

bh = BinHeap([3, 12, 25, 4, 8, 9, 20])

print(bh.delMax())
print(bh.delMax())
print(bh.delMax())
print(bh.delMax())
print(bh.delMax())
print(bh.delMax())