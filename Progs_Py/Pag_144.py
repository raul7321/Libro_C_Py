from math import *
def Componente(frec,fo):
    h = 1/44100
    L = len(fo)
    s = 0.0
    for i,amp in enumerate(fo):
        s = s + amp * sin(frec*i*h*2*pi) * (0.5 if (i==0 or i==(L-1)) else 1.0)
    return s*h
f = [float(a) for a in list(open('tono7.txt','r'))]
Fr = [697, 770, 852, 941]
Fc = [1209,1336,1477]
R = [Componente(fa,f) for fa in Fr]
C = [Componente(fa,f) for fa in Fc]
r = R.index(max(R))
c = C.index(max(C))
N = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
d = N[r][c]
print('El digito es', d)
