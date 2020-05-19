import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon, LineString
import rapiditotiti as dj

def load():
	comuna_path		= "DATOS/Comunas/comunas.shp"
	trenes_path		= "DATOS/lineas_metro/LineasdeMetroSantiago-line.shp"
	estacion_path	= "DATOS/estaciones_metro/Estaciones_Metro_2019-point.shp"
	# https://es.wikipedia.org/wiki/Metro_de_Santiago

	stgo_sf			= gpd.read_file(  comuna_path, encoding='utf-8')
	#stgo_sf			= stgo_sf[stgo_sf.Provincia == 'Santiago']
	stgo_sf			= stgo_sf[stgo_sf.Comuna.isin([
			'Lo Prado', 'Estación Central', 'Santiago', 'Providencia', 'Las Condes', # L1
			'Huechuraba', 'Recoleta', 'Santiago', 'San Miguel', 'La Cisterna', # L2
			'Quilicura', 'Conchalí', 'Independencia', 'Santiago', 'Ñuñoa', 'La Reina', # L3
			'Providencia', 'Las Condes', 'La Reina', 'Ñuñoa', 'Peñalolén', 'Macul', 'La Florida', 'Puente Alto', # L4
			'La Florida', 'La Granja', 'San Ramón', 'La Cisterna', # L4A
			'Maipú', 'Pudahuel', 'Lo Prado', 'Quinta Normal', 'Santiago', 'Providencia', 'Ñuñoa', 'Macul', 'San Joaquín', 'La Florida', # L5
			'Cerrillos', 'Pedro Aguirre Cerda', 'San Miguel', 'San Joaquín', 'Santiago', 'Ñuñoa', 'Providencia', # L6
		]
	)]

	estacion_sf		= gpd.read_file(  estacion_path)
	estacion_sf		= gpd.read_file(  estacion_path)
	trenes_sf		= gpd.read_file(  trenes_path)
	trenes_sf		= gpd.read_file(  trenes_path)

	return stgo_sf, estacion_sf, trenes_sf

def glow(p, ax, color='red', diff_linewidth = 1.05, alpha_value = 0.03, n_lines = 20, marker=None):
	p.plot(ax=ax, color=color)
	for n in range(1, n_lines+1):
		p.plot(ax=ax,	linewidth=2+diff_linewidth*n, alpha=alpha_value, color=color)


def plot(region, estacion, trenes, res=None, show=True, **kwarg):
	L1 = trenes[trenes.Name == "Línea 1 Metro de Santiago"]
	L2 = trenes[trenes.Name == "Línea 2 Metro de Santiago"]
	L3 = trenes[trenes.Name == "Futura Línea 3 Metro de Santiago"]
	L4 = trenes[trenes.Name == "Línea 4 Metro de Santiago"]
	L4A = trenes[trenes.Name == "Línea 4-A Metro de Santiago"]
	L5 = trenes[trenes.Name == "Línea 5 Metro de Santiago"]
	L6 = trenes[trenes.Name == "Futura Línea 6 Metro de Santiago"]

	eL1 = estacion[estacion.linea == "Linea 1"]
	eL2 = estacion[estacion.linea == "Linea 2"]
	eL3 = estacion[estacion.linea == "Linea 3"]
	eL4 = estacion[estacion.linea == "Linea 4"]
	eL4A = estacion[estacion.linea == "Linea 4A"]
	eL5 = estacion[estacion.linea == "Linea 5"]
	eL6 = estacion[estacion.linea == "Linea 6"]

	r = 22/255
	g = 43/255
	b = 58/255
	fig, ax = plt.subplots(figsize=(10, 10), dpi=60, facecolor=(r, g, b))
	ax.set_axis_off()
	glow(region.boundary, ax, 'purple', diff_linewidth = .75, alpha_value = 0.03, n_lines = 20, marker=None)

	diff_linewidth = 0
	alpha_value = 1
	n_lines = 1
	marker=None
	glow(L1, ax, 'red')
	glow(L2, ax, 'yellow')
	glow(L3, ax, 'firebrick')
	glow(L4, ax, 'b')
	glow(L4A, ax, 'c')
	glow(L5, ax, 'lime')
	glow(L6, ax, 'deeppink')

	eL1.plot(ax=ax, color="red", markersize=20)
	eL2.plot(ax=ax, color="yellow", markersize=20)
	eL3.plot(ax=ax, color="firebrick", markersize=20)
	eL4.plot(ax=ax, color="b", markersize=20)
	eL4A.plot(ax=ax, color="c", markersize=20)
	eL5.plot(ax=ax, color="lime", markersize=20)
	eL6.plot(ax=ax, color="deeppink", markersize=20)

	return fig, ax

def  convert(path, estacion):
	estacion = estacion[["nombre", "geometry"]].sort_values(by=['nombre'])
	print(path, len(path))
	num = 0
	aux = []
	for i in path:
		for e in set(estacion.nombre):
			if e.find(i.strip()) != -1 and aux.count(i.strip()) == 0:
				x =estacion[estacion.nombre.isin([e])].geometry.item().y
				y = estacion[estacion.nombre.isin([e])].geometry.item().x
				a = [1, i.strip(), x, y]
				aux.append(a)

	df = pd.DataFrame(aux, columns = ['path' , 'nombre', 'latitude', 'longitude'])
	gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude))

	gdf2 = gdf.groupby(['path'])['geometry'].apply(lambda x: LineString(x.tolist()))
	gdf2 = gpd.GeoDataFrame(gdf2, geometry='geometry')
	return gdf2

region, estacion, trenes = load()
res = dj.rapiditotiti()
aux = convert(res[0], estacion)
fig, ax = plot(region, estacion, trenes)
glow(aux, ax, 'white')
plt.show()