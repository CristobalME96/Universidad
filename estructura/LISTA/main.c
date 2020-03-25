#include "lista.h"
/**
 * Función Principal
 *
 */

int main(int argc, char *argv[])
{
	Lista *L;
	L = creaLista();
	insertar(L, 1);
	insertar(L, 2);
	insertar(L, 3);
	recorrer(L);
	int eliminado = eliminar(L);
	printf("Se elimina%d\n", eliminado);
	recorrer(L);
	destruirLista(L);
	/* se vuelve a crear una nueva lista */
	L = creaLista();
	insertar(L, 2);
	insertar(L, 3);
	recorrer(L);
	destruirLista(L);
	return 0;
}
