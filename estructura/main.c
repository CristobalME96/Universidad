// gcc -o exe main.c orden.c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "orden.h"

int* arreglo(int n) {
	int i;
	int *A = (int*) malloc(sizeof(int)*n);
	return A;
}

void llenar(int *A, int n) {
	int i;

	for(i = 0; i < n; i++) {
		A[i] = rand();
	}
}

void mostrar(int *A, int n) {
	int i;

	for(i = 0; i < n; i++) {
		printf("%i ", A[i]);
	}
}

int main(int argc, char *argv[]) {
	clock_t t_inicio, t_final;
	double Aseg, Bseg, Cseg;
	int *A, *B, *C, n, max;
	int i;
	FILE *file = fopen("datos.csv", "w");
	max = 10000;
	A = arreglo(max);
	B = arreglo(max);
	C = arreglo(max);

	srand(time(NULL));
	fprintf(file,"n, b, s, q\n");
	for(n = 100; n < max; n = n + 100){
		llenar(A, n); // Llenamos el arreglo A
		llenar(B, n); // Llenamos el arreglo B
		llenar(C, n); // Llenamos el arreglo C

		t_inicio = clock();
		burbuja(A, n);
		t_final = clock();
		Aseg = (double)(t_final - t_inicio) / CLOCKS_PER_SEC;

		t_inicio = clock();
		seleccion(B, n);
		t_final = clock();
		Bseg = (double)(t_final - t_inicio) / CLOCKS_PER_SEC;

		t_inicio = clock();
		quicksort(C, 0, n);
		t_final = clock();
		Cseg = (double)(t_final - t_inicio) / CLOCKS_PER_SEC;

		fprintf(file,"%i, %.16g, %.16g, %.16g\n", n, Aseg*1000, Bseg*1000, Cseg*1000);

	}
	free(A);
	free(B);
	free(C);
	fclose(file);
	return 0;
}
