#include <stdio.h>
#include "cola.h"

void sobreviviente(Cola *cola, int m){
  int i = 1;
  while(cola->tamano > 1){
    if(i == m){       //mata m
      i = 1;
    }else{            //salta m-1
      push(cola, pop(cola)->dato1);
      i++;
    }
  }
  printf("el sobreviviente es el de la posicion %i\n", pop(cola)->dato1);
}

int main(){
  Cola *C;
  C = creaCola();
  int p, m;
  printf("ingrese la cantidad de personas\n");
  scanf("%i", &p);
  for(int i = 0; i<p ; i++){
    push(C, i+1);
  }
  printf("ingrese la cantidad de saltos\n");
  scanf("%i", &m);
  sobreviviente(C, m);
}
