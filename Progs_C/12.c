#include <stdio.h>
int main(){
int z,i,n,m,t;
FILE *salva;
salva = fopen("datos.csv","w");
printf("Dame el numero de dados ");
scanf("%d",&n);
srand(time(0));
t = 0;
printf("Al tiempo %d, quedan %d dados.\n",t,n);
fprintf(salva,"%d, %d\n",t,n);
while(n>0){
m = 0;
for (i=1;i<=n;i++){
z = rand() % 6 + 1;
if (z == 5){
m = m + 1;
}
}
n = n - m;
t = t + 1;
printf("Al tiempo %d, quedan %d dados.\n",t,n);
fprintf(salva,"%d, %d\n",t,n);
}
fclose(salva);
}
