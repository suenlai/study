#include <stdio.h>

int main(void){
	short s = 123;
	printf("s:%i\n",s);
	int i = *(int *)&s;
	
	printf("i:%i\n",i);
	return 0;
}
