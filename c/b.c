#include <stdio.h>

int main(void){
	double d = 3.1416;
	printf("d:%f\n",d);
	char c = *(char *)&d;
	
	printf("c:%c\n",c);
	return 0;
}
