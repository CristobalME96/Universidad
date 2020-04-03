#include <stdio.h>

/*ASUMIENDO QUE LAS LISTAS ESTAN CREADAS EN BASE A LA SIGUIENTE ESTRUCTURA
typedef struct info {
	int valor;
	int rut;
	char empleado[20];
}Info;

typedef struct nodo {
	Info *datos;
	struct nodo *siguiente;
}Nodo;

typedef struct lista {
	Nodo *inicio;
	Nodo *fin;
	int tamano;
}Lista;
*/

int sumartotal(Lista *plista){
	Nodo *aux;
	aux = plista->inicio;
	int total = 0;
	for(int i = 0 ; i < plista->tamano ; i++){
		total += aux->datos->valor;
		aux = aux->siguiente;
	}
	return total;
}

void ventasRUT(Lista *plista, int rut){
	Nodo *aux;
	aux = plista->inicio;
	printf("ventas con rut %i:", rut);
	for(int i = 0 ; i < plista->tamano ; i++){
		if(aux->datos->rut == rut){
			printf("%i", aux->datos->valor);
		}
		aux = aux->siguiente;
	}
}

int promedio(Lista *plista, char empleado[]){
	Nodo *aux;
	aux = plista->inicio;
	int suma = 0;
	int n = 0;
	for(int i = 0 ; i < plista->tamano ; i++){
		if(aux->datos->empleado == empleado){
			suma += aux->datos->valor;
			n++;
		}
		aux = aux->siguiente;
	}
	return suma/n;
}

int main(int argc, char *argv[]){
	return 0;
}
