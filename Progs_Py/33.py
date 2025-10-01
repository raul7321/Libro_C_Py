F = open('salida.csv', 'r')
resultado = list(F)
R = [[int(r) for r in T.split(',')] for T in resultado]
print(R)
F.close()
