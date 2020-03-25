
#include "pila.h"

int main(int argc, char *argv[])
{
  Pila *P;
  P = creaPila();

  apilar(P, 1);
  apilar(P, 2);
  apilar(P, 3);
  printf("Tope: % d\n", tope(P)->datos->dato1);
  desapilar(P);
  printf("Tope: % d\n", tope(P)->datos->dato1);
  destruirPila(P);

	P = creaPila();
  if(tope(P) == NULL)
    printf("Está vacía\n");
  apilar(P, 2);
  apilar(P, 3);
  printf("Tope: % d\n", tope(P)->datos->dato1);
  destruirPila(P);

  return 0;
}
