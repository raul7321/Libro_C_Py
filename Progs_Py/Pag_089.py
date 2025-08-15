from math import pi
def Esfera(r):
    v = pi*4.0/3.0*r**3
    a = 4*pi*r**2
    e = 2*pi*r
    return [v,a,e]
[x,y,z] = Esfera(2)
print ('El volumen de la esfera es: ', x)
print ('El area de la esfera es: ', y)
print ('El perimetro del ecuador es: ', z)
