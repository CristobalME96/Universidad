#include "orden.h"

void burbuja(int *a, int n) {
	int i, j;
	int temp;
	int interruptor = 1;

	/* pasadas */
	for(i = 0; i < n && interruptor; i++) {
		interruptor = 0;
		for(j = 0; j < n - i; j++) {
			if(a[j] > a[j+1]) {
				interruptor = 1;
				/* Intercambiamos */
		 		temp = a[j];
				a[j] = a[j+1];
				a[j+1] = temp;
			}
		}
	}
}

void seleccion(int *a, int n) {
	int indiceMenor, i, j;
	int aux;
	/* ordenar a[0]... a[n-2] y a[n-1]
	en cada pasada */
	for (i = 0; i < n-1; i++) {
		/* comienzo de la exploración en índice i */
		indiceMenor = i;
		/* j explora la sublista a[i+1]..a[n-1] */
		for (j = i+1; j < n; j++)
			if (a[j] < a[indiceMenor])
				indiceMenor = j;
			/* sitúa el elemento más pequeño en a[i] */
		if (i != indiceMenor) {
			aux = a[i];
			a[i] = a[indiceMenor];
			a[indiceMenor] = aux ;
		}
	}
}

void quicksort(int *a, int primero, int ultimo) {
	int i, j, central;
	double pivote;
	central = (primero + ultimo)/2;
	pivote = a[central];
	i = primero;
	j = ultimo;
	do {
		while (a[i] < pivote) i++;
		while (a[j] > pivote) j--;
		if (i<=j) {
			double tmp;
			tmp = a[i];
			a[i] = a[j];
			a[j] = tmp; /* intercambia a[i] con a[j] */
			i++;
			j--;
		}
	} while (i <= j);
	if (primero < j)
		quicksort(a, primero, j);/* mismo proceso con sublista izqda */
	if (i < ultimo)
		quicksort(a, i, ultimo); /* mismo proceso con sublista drcha */
}
