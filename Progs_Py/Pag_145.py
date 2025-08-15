from math import *
mps = 44100
h = 1/mps
duracion = 0.5
Muestras = int(duracion * mps)
Fr = [697, 770, 852, 941]
Fc = [1209,1336,1477]
k = 0
for freq2 in Fr:
    for freq1 in Fc:
        k=k+1
        f = [str(sin(2*pi*t*h*freq1)+sin(2*pi*t*h*freq2))+'\n'
            for t in range(Muestras)]
        Ar = open('Tono'+str(k)+'.txt','w')
        Ar.writelines(f)
        Ar.close()
