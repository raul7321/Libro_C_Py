#include<stdio.h>
int main(){
int a[10],n;
for (n=0;n<10;n++){
a[n]=n*3;
}
for (n=0;n<10;n++){
printf("El valor en el cajon %d es %d\n",n,a[n]);
}
}
