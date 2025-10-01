import sys
import os
M = input('Escribe el nombre del paquete que quieres instalar: ')
P = os.path.dirname(sys.executable)
f = open('TempPy.sh', 'w')
f.write('#!/bin/bash\n')
f.write('cd ' + P + '\n')
f.write('pip3 install ' + M + '\n')
f.write('read -p "Presiona Enter para continuar..."\n')
f.write('exit\n')
f.close()
subprocess.run(['chmod', '+x', '/TempPy.sh'], check=True)
os.system('./TempPy.sh')
