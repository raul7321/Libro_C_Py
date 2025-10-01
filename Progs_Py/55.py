import matplotlib.pyplot as plt
from math import *

def MiEval(F,x):
    return eval(F)

def Aj(f,j):
    M = 1000
    h = 2*pi/M
    s = (MiEval(f,-pi)*cos(-j*pi)+MiEval(f,pi)*cos(j*pi))/2
    s = s + sum([MiEval(f,-pi+i*h)*cos(j*(-pi+i*h)) for i in range(1,M)])
    return h*s/pi

def Bj(f,j):
    M = 1000
    h = 2*pi/M
    s = (MiEval(f,-pi)*sin(-j*pi)+MiEval(f,pi)*sin(j*pi))/2
    s = s + sum([MiEval(f,-pi+i*h)*sin(j*(-pi+i*h)) for i in range(1,M)])
    return h*s/pi

def Four(n,x,A,B):
    return A[0]/2+sum([A[j]*cos(j*x)+B[j]*sin(j*x) for j in range(1,n)])

F = input('Dame la funcion f(x) = ')
N = int(input('Dame el numero de terminos de la serie de Fourier '))
Fig, ax = plt.subplots()
X = [i*2*pi/200-pi for i in range(201)]
A = [Aj(F,j) for j in range(N)]
B = [Bj(F,j) for j in range(N)]
Y1 = [Four(N,x,A,B) for x in X] # Aproximacion en Serie de Fourier
Y2 = [MiEval(F,x) for x in X] # Funcion original
ax.plot(X,Y1,color = 'blue')
ax.plot(X,Y2,color = 'red')
plt.show()
