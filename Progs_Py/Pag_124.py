from vpython import *
k = 0.4
m = 1.0
x = 5.0
v = 0.0
h = 0.02
ventana1 = canvas(range = 6.0, align = 'left')
ventana2 = graph(align = 'right')
masa = sphere(radius = 1.0, color = color.red, pos = vec(x, 0.0, 0.0))
resorte = helix(pos = vec(-8,0,0),radius = 0.5, coils = 10, axis=vec(x+8,0,0),
thickness = 0.1)
fase = gcurve(color=color.red)
for t in range(5000):
    rate(100)
    v = v + h*(-k/m * x)
    x = x + h*v
    masa.pos.x = x
    fase.plot(pos=(x,v))
    resorte.axis=vec(x+8,0,0)

