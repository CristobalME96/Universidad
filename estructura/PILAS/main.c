#include <stdio.h>
#include <string.h>
#include "pila.h"



int main(int argc, char *argv[])
{
  Pila *P;
  P = creaPila();
  bool estado = true;
  char a[] = "test de abbbaaabbaabaaaaabbbbb";
  for(int i = 0 ; i < strlen(a) ; i++){
    if(a[i]=='a' || a[i]=='A'){
      apilar(P, a[i]);
    }
  }
  for(int i = 0 ; i < strlen(a) ; i++){
    if(a[i]=='b' || a[i]=='B'){
      estado = desapilar(P);
    }
  }
  if(estado == false || P->tamano > 0){
    printf("La cantidad de a y b es diferente\n");
  }else {
    printf("La cantidad de a y b es igual\n");
  }
  return 0;
}
