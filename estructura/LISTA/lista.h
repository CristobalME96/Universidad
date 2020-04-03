#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#ifndef __LISTA__H__
#define __LISTA__H__
/**
 * Estructura que guarda la información.
 */
typedef struct info {
	int valor;
	int rut;
	int n;

	/* int dato2; */
	/* ... */
}Info;
/**
 * Estructura que guarda el nodo, un puntero que apunta a la Info,
 * y otro que apunta al nodo siguiente
 */
typedef struct nodo {
	Info *datos;
	struct nodo *siguiente;
}Nodo;
/**
 * Estructura que guarda la Lista, con un puntero que apunta al inicio
 *	y al fin de ésta. Además, almacena el tamaño de la lista.
 */
typedef struct lista {
	Nodo *inicio;
	Nodo *fin;
	int tamano;
}Lista;

Lista *creaLista();
void destruirLista(Lista *plista);
Nodo *crearNodo(Info *dato, Nodo *ptro);
Info * agregar(int dato1, int dato2, int dato3);
bool insertar(Lista *plista, int info);
int eliminar(Lista *plista);
void recorrer(Lista *plista);

#endif
