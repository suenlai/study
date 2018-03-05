#include <stdio.h>
void swap1(int *vp1,int *vp2){
     int tmp = *vp1;
	 *vp1=*vp2;
	 *vp2=tmp;
}

void swap2(void *vp1,void *vp2){
	long *lp1 = (long*)vp1;
	long *lp2 = (long*)vp2;
	long tmp = *lp1;
	*lp1 = *lp2;
	*lp2 = tmp;

}
int main(void){
	int i = 10;
	int j = 20;
	int *a=&i;
	int *b=&j;
	printf("a=%i,b=%i\n",*a,*b);
	//swap1(&a,&b);
	swap2(&a,&b);
	printf("a=%i,b=%i\n",*a,*b);
    return 0;
}

