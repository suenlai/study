#include <stdio.h>

void declareAndInitArray(){
	int array[100];
	for(int i=0;i<100;i++){
		array[i]=i;
	}
}
void printArray(){
	int array[100];
	for(int i=0;i<100;i++){
		printf("%i,",array[i]);
	}

}

int main(void){
	declareAndInitArray();
	printf("balabala");
	printArray();
    return 0;
}

