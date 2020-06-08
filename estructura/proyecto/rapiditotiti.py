import functools

def leerArchivo(archivo):
	with open(archivo,'r') as f:
		for line in f.readlines():
			yield line.split("\n")[0].split(",")

def generarGrafo(origen):
	grafo = []
	pos = 0
	estaciones = leerArchivo('metro_neo_santiago.csv')

	for est in estaciones:

		existe = False
		for i in range(len(grafo)):
			if(grafo[i][0] == est[0]):
				grafo[i].append(("".join(est[1]),est[2]))
				existe = True

		if(existe == False):
			grafo.append([est[0]])
			grafo[len(grafo)-1].append(("".join(est[1]),est[2]))
			if (est[0] == origen):
				pos = len(grafo)-1

		existe = False
		for i in range(len(grafo)):
			if(grafo[i][0] == est[1]):
				grafo[i].append(("".join(est[0]),est[2]))
				existe = True

		if(existe == False):
			grafo.append([est[1]])
			grafo[len(grafo)-1].append(("".join(est[0]),est[2]))
			if (est[1] == origen):
				pos = len(grafo)-1
	return grafo, pos

def posEstacion(estaciones, actual):
	return

def dijkstra(grafo, origen, final, pos_origen):
	destino = 0
	visitar = {}
	estaciones = {}
	dist = []
	path = []
	for i in range(len(grafo)):
		estaciones[grafo[i][0]] = i
		path.append(-1)
		if(i == pos_origen):
			dist.append(0)
			visitar[grafo[i][0]] = 0
		else:
			dist.append(999999)
			visitar[grafo[i][0]] = 999999
	while len(visitar) > 0:
		minimo = min(visitar.keys(), key=(lambda k: visitar[k]))
		pos = estaciones[minimo]
		visitar.pop(minimo)
		for i in range(1, len(grafo[pos])):
			destino = estaciones[grafo[pos][i][0]]
			if(dist[pos] + int(grafo[pos][i][1]) < dist[destino]):
				dist[destino] = dist[pos] + int(grafo[pos][i][1])
				visitar[grafo[pos][i][0]] = dist[destino]
				path[destino] = pos
	camino = []
	pos = estaciones[final]
	while path[pos] !=-1:
		camino.insert(0, grafo[pos][0])
		pos = path[pos]
	camino.insert(0, grafo[pos][0])
	return camino, dist[estaciones[final]]

def rapiditotiti():
	origen, destino = leerArchivo('confidencial.txt')
	origen = "".join(origen)
	destino = "".join(destino)
	grafo, pos_origen = generarGrafo(origen)
	camino = []
	camino, t_est = dijkstra(grafo, origen, destino, pos_origen)
	return(camino, t_est)

rapiditotiti()
