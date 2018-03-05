#include <stdio.h>

int main(void){
	int a = 10;
	int b = 20;
	int c = 30;
	printf("a=%i,b=%i,c=%i\n",a,b,*((&b)-1));
    return 0;
}

