from vpython import *
ventana = graph()
conejos = gcurve(color=color.red, graph=ventana)
zorros = gcurve(color=color.green, graph=ventana)
a = 0.5
b = 0.4
c = 0.35
d = 0.06
C = 3
Z = 2
h = 0.01
for t in range(5000):
    C = C + h*(a*C-c*C*Z)
    Z = Z + h*(-b*Z+d*C*Z)
    conejos.plot(pos=(t*h,C))
    zorros.plot(pos=(t*h,Z))
