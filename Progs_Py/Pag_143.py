from math import *
def Componente(frec,fo):
    h = 1/44100
    L = len(fo)
    s = 0.0
    for i,amp in enumerate(fo):
        s = s + amp * sin(frec*i*h*2*pi) * (0.5 if (i==0 or i==(L-1)) else 1.0)
    return s*h
f = [float(a) for a in list(open('tono7.txt','r'))]
F = [697, 770, 852, 941, 1209,1336,1477]
for i,fi in enumerate(F):
    print('A%d (phi = %d) = %.2f' % (i,fi, round(Componente(fi,f),2)))
