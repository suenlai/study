#include <stdio.h>
#include <stdlib.h>

int main(void){
	float f = 17.0;
	printf("f:%f\n",f);
	short s = *(short *)&f;
	
	printf("s:%i\n",s);
	int* c = malloc(4);
	*c= 32311;
	printf("c:%i\n",*c);
	free(c);
	int *d = malloc(4);
	free(d);
	printf("c:%i\n",*c);
	return 0;
}
