#include<stdio.h>
#include<stdio.h>
float MiFuncion(float);
int main(){
float h,m,a,b,integral;
int i;
printf("a = ");
scanf("%f",&a);
printf("b = ");
scanf("%f",&b);
printf("m = ");
scanf("%f",&m);
h=(b-a)/m;
integral=(MiFuncion(a)+MiFuncion(b))*h/2;
for (i=1;i<=m-1;i++) {
integral=integral+h*MiFuncion(a+i*h);
}
printf("El resultado de la integral es %f\n",integral);
}
float MiFuncion(float x){
return(x*x*x+2*x);
}
