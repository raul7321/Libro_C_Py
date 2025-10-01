s1 = int(input('Dame el estado de s1 (1 cerrado, 0 abierto) '))
s2 = int(input('Dame el estado de s2 (1 cerrado, 0 abierto) '))
s3 = int(input('Dame el estado de s3 (1 cerrado, 0 abierto) '))
s4 = int(input('Dame el estado de s4 (1 cerrado, 0 abierto) '))
if (s1 and s2) and (s3 or s4):
    print('El foco esta encendido')
else:
    print('El foco esta apagado')
print('FIN')
