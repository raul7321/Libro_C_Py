from vpython import *
ventana = graph()
posicion = gcurve(color=color.red, graph=ventana)
velocidad = gcurve(color=color.green, graph=ventana)
k = 0.4
m = 1.0
x = 5.0
v = 0.0
h = 0.01
for t in range(5000):
    v = v + h*(-k/m * x)
    x = x + h*v
    posicion.plot(pos=(t*h,x))
    velocidad.plot(pos=(t*h,v))
