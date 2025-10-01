#include<stdio.h>
#include<time.h>
int main(){
int A[4][4],B[4][4],S[4][4],R[4][4];
int r,c;
for (r=0;r<4;r++){
for (c=0;c<4;c++){
A[r][c] = rand() %21;
B[r][c] = rand() %21;
}}
printf("A = \n");
for (r=0;r<4;r++){
for (c=0;c<4;c++){
printf("%d\t",A[r][c]);
}
printf("\n");
}
printf("B = \n");
for (r=0;r<4;r++){
for (c=0;c<4;c++){
printf("%d\t",B[r][c]);
}
printf("\n");
}
for (r=0;r<4;r++){
for (c=0;c<4;c++){
S[r][c] = A[r][c]+B[r][c];
R[r][c] = A[r][c]-B[r][c];
}}
printf("A + B = \n");
for (r=0;r<4;r++){
for (c=0;c<4;c++){
printf("%d\t",S[r][c]);
}
printf("\n");
}
printf("A - B = \n");
for (r=0;r<4;r++){
for (c=0;c<4;c++){
printf("%d\t",R[r][c]);
}
printf("\n");
}
}
