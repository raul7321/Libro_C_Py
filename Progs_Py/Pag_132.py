import sys
import os
M = input('Escribe el nombre del paquete que quieres instalar: ')
P = os.path.dirname(sys.executable)+'\Scripts\\'
f = open('TempPy.bat','w')
f.write('chdir /D ' + P + '\n')
f.write('pip3 install ' + M + '\npause\n')
f.write('exit\n')
f.close()
os.system('TempPy.bat')
