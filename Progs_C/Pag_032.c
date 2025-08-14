#include<stdio.h>
#include<time.h>
main(){
int z,i,n,m;
printf("Dame el numero de dados ");
scanf("%d",&n);
srand(time(0));
while(n>0) {
m=0;
for (i=1;i<=n;i++) {
z=rand() % 6 + 1;
if (z==5) {
m=m+1;
}
}
n=n-m;
printf("Quedan %d dados.\n",n);
}
}
