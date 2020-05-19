#include <stdio.h>

int sumarArreglo(int arr[], int pos){
  if(pos == 0){
    return arr[pos];
  }else {
    return arr[pos] + sumarArreglo(arr, pos - 1);
  }
}

int main(){
  int arr[] = {1,2,3,4,5,6,7,8,9,10};
  printf("%i\n", sumarArreglo(arr, sizeof(arr)/sizeof(arr[0]) - 1));
  return 0;
}
