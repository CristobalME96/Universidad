#include <stdio.h>

int main(){

  static int myNumber = 0;
  static int myData = 0;
  long suma = 0;

  while(myNumber != 100){

    myNumber++;
    myData = 0;

    while(myData != 200){

      suma = suma + myNumber + myData;
      myData++;
    }
  }

  printf("suma %ld \n", suma);
}
