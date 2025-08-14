#include<stdio.h>
#include<math.h>
int main(){
int i;
float t,x,y;
printf("Las coordenadas son:\n");
for (i=0;i<12;i++){
t = i*3.1416/6.0;
x = 7*cos(t);
y = 7*sin(t);
printf("( %f, %f) \n",x,y);
}
printf("Fin del programa\n");
}
