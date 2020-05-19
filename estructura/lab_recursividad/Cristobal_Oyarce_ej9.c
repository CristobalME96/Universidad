#include <stdio.h>

int calcularMaximo(int arr[], int max, int pos){
  if(pos == 0){
    if(max < arr[pos]){
      return arr[pos];
    }
    else{
      return max;
    }
  }else {
    if(max < arr[pos]){
      return calcularMaximo(arr, arr[pos], pos - 1);
    }
    else{
      return calcularMaximo(arr, max, pos - 1);
    }
  }
}

int main(){
  int arr[] = {18,2,3,17,5,12,6,7,8,9,15};
  printf("%i\n", calcularMaximo(arr, 0, sizeof(arr)/sizeof(arr[0]) - 1));
  return 0;
}
