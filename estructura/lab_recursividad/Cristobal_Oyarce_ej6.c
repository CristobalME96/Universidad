#include <stdio.h>

int calcularOcurrencia(int arr[], int num, int pos){
  if(pos == 0){
    if(num == arr[pos]){
      return 1;
    }
    else{
      return 0;
    }
  }else {
    if(num == arr[pos]){
      return calcularOcurrencia(arr, num, pos - 1) + 1;
    }
    else{
      return calcularOcurrencia(arr, num, pos - 1);
    }
  }
}

int main(){
  int arr[] = {1,1,2,2,3,1,3,1,3,4,1,2,2,3,5,3,5,2,1,2}; // 1 = 6, 2 = 6, 3 = 5, 4 = 1, 5 = 2
  int num = 5;
  printf("%i\n", calcularOcurrencia(arr, num, sizeof(arr)/sizeof(arr[0]) - 1));
  return 0;
}
