from math import *
mps = 44100
h = 1/mps
duracion = 0.5
Muestras = int(duracion * mps)
freq1 = 1209
freq2 = 852
f = [str(sin(2*pi*t*h*freq1)+sin(2*pi*t*h*freq2))+'\n' for t in range(Muestras)]
Ar = open('Tono7.txt','w')
Ar.writelines(f)
Ar.close()
