#include<stdio.h>
main(){
float h,m,a,b,sum;
int i;
printf("a = ");
scanf("%f",&a);
printf("b = ");
scanf("%f",&b);
printf("m = ");
scanf("%f",&m);
h=(b-a)/m;
sum = h*(a*a*a+2*a+b*b*b+2*b)/2;
for (i=1;i<=m-1;i++) {
sum=sum+h*((a+i*h)*(a+i*h)*(a+i*h)+2*(a+i*h));
}
printf("El resultado de la integral es %f",sum);
}
