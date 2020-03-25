#include "busqueda.h"

int Secuencial(int *a, int n, int num){
  for(int i = 0 ; i < n ; i++){
    if(a[i] == num){
      return i;
    }
  }
  return -1;
}
