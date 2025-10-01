#include<stdio.h>
#include<time.h>
int main(){
int r,c,k,s;
int m,n,h;
m = 6; n = 4; h = 5;
int A[m][n],B[n][h],P[m][h];
printf("A = \n");
for (r=0;r<m;r++){
for (c=0;c<n;c++){
A[r][c] = rand() %11;
printf("%d\t",A[r][c]);
}
printf("\n");
}
printf("B = \n");
for (r=0;r<n;r++){
for (c=0;c<h;c++){
B[r][c] = rand() %11;
printf("%d\t",B[r][c]);
}
printf("\n");
}
for (r=0;r<m;r++){
for (c=0;c<h;c++){
s = 0;
for (k=0;k<n;k++){
s = s + A[r][k]*B[k][c];
}
P[r][c] = s;
}
}
printf("A B = \n");
for (r=0;r<m;r++){
for (c=0;c<h;c++){
printf("%d\t",P[r][c]);
}
printf("\n");
}
}
