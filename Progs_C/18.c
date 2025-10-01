#include<stdio.h>
int main(){
int k,n;
float s,p,x;
printf("Cuantos datos tienes? ");
scanf("%d",&k);
float a[k];
for(n = 0; n<k; n++){
printf("Dame el dato %d ",n+1);
scanf("%f",&x);
a[n] = x;
}
printf("Los datos son:\n");
s = 0.0;
for(n = 0; n<k; n++){
printf("Dato %d = %f\n",n+1,a[n]);
s = s + a[n];
}
p = s/n;
printf("El promedio es %f\n",p);
}
