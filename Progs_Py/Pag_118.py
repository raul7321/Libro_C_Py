from vpython import *
ventana = graph(ytitle='velocidad, momento', xtitle = 'posicion')
fase = gcurve(color=color.green, graph=ventana)
k = 0.4
m = 1.0
x = 5.0
v = 0.0
h = 0.01
for t in range(5000):
    v = v + h*(-k/m * x)
    x = x + h*v
    fase.plot(pos=(x,m*v))
