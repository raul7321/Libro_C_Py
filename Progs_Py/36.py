from math import *
def MiEval(F,x):
    return eval(F)
f = input('Dame la funcion f(x) = ' )
a = float(input('Dame el limite inferior a: '))
b = float(input('Dame el limite superior b: '))
M = int(input('Dame el numero de subintervalos: '))
h = (b-a)/M
s = h*((MiEval(f,a)+MiEval(f,b))/2+sum([MiEval(f,a+i*h) for i in range(1,M)]))
print ('El valor de la integral es: %f' % s)
