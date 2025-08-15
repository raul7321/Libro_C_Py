from vpython import *
ventana1 = canvas(align = 'left')
ventana2 = graph(xtitle='Angulo (rad)', ytitle='Velocidad (rad/s)',
background=color.white,foreground=color.black,align='right')
curva = gcurve(color=color.red)
h = 0.01
g = 9.81
L = 0.5
x = pi/5
v = 0.0
B = 0.3
cuerda = cylinder(pos=vec(0,0,0),axis=vec(0,-20,0), radius=0.2)
masa = sphere(pos=vec(0,-20,0), radius=1, color=color.red)
pendulo = compound([cuerda,masa])
pendulo.rotate(axis=vec(0,0,1),angle=x, origin = vec(0,0,0))
for t in range(4000):
    rate(100)
    v = v+h*(-g/L*sin(x)-B*v);
    x = x+h*v;
    pendulo.rotate(axis=vec(0,0,1),angle=h*v, origin = vec(0,0,0))
    curva.plot(pos=(x,v))
