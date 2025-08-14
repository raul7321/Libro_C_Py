#include<stdio.h>
#include<math.h>
float MiFuncion(float,float,float);
float Derivada(float,float);
int main(){
float n,a,x,e;
printf("Dame el valor de a ");
scanf("%f",&a);
printf("Dame el valor de n ");
scanf("%f",&n);
printf("Dame el valor de x0 ");
scanf("%f",&x);
printf("Dame el valor de e ");
scanf("%f",&e);
while(fabs(MiFuncion(x,n,a))>e){
x = x - MiFuncion(x,n,a) / Derivada(x,n);
}
printf("La solucion es x = %f\n",x);
}
float MiFuncion(float x, float n, float a){
return(pow(x,n)-a);
}
float Derivada(float x, float n){
return(n*pow(x,n-1));
}
