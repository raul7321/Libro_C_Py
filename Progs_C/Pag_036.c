#include<stdio.h>
float Area(float,float);
float Volumen(float,float,float);
int main(){
float k,m,a,v,L;
printf("Dame la altura del triangulo ");
scanf("%f",&k);
printf("Dame la base del triangulo ");
scanf("%f",&m);
printf("Dame la longitud del prisma ");
scanf("%f",&L);
a = Area(m,k);
v = Volumen(m,k,L);
printf("El area del triangulo con base %f y altura %f es %f.\n",m,k,a);
printf("El volumen del prisma es %f.\n",v);
}
float Area(float b, float h){
float a;
a = b*h/2;
return(a);
}
float Volumen(float b, float h, float z){
float v;
v = Area(b,h)*z;
return(v);
}
