#include<stdio.h>
int main(){
int d,t;
FILE *resultado;
resultado = fopen("datos.csv","r");
while(fscanf(resultado," %d, %d\n",&t,&d) != -1){
printf("Al tiempo %d, quedan %d dados\n",t,d);
}
fclose(resultado);
}
