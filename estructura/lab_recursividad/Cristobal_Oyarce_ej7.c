#include <stdio.h>
#include <stdbool.h>

int sonIguales(int arr1[], int arr2[], int pos1, int pos2){
  if((pos1 == 0 || pos2 == 0) && pos1 != pos2){
    return 0;
  }
  if(arr1[pos1] != arr2[pos2]){
    return 0;
  }else {
    if(pos1 == pos2 && pos1 == 0){
      return 1;
    }
    return sonIguales(arr1, arr2, pos1 - 1, pos2 - 1);
  }
}

int main(){
  int arr1[] = {1,2,3,4,5,6,7,8,9,10};
  int arr2[] = {1,2,3,4,5,6,7,8,9,10};
  printf("%i\n", sonIguales(arr1, arr2, sizeof(arr1)/sizeof(arr1[0]) - 1, sizeof(arr2)/sizeof(arr2[0]) - 1));
  return 0;
}
