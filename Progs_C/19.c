#include<stdio.h>
#include<time.h>
int main(){
int a[20],n,t,k;
srand(time(0));
printf("La lista original:\n");
for (n=0;n<20;n++){
a[n]=rand() %100+1;
printf("El valor en el cajon %d es %d\n",n,a[n]);
}
for (k=0;k<20;k++){
for (n=k;n<20;n++){
if (a[n] < a[k]){
t = a[k];
a[k] = a[n];
a[n] = t;
}
}}
printf("La lista ordenada:\n");
for (n=0;n<20;n++){
printf("El valor en el cajon %d es %d\n",n,a[n]);
}
}
