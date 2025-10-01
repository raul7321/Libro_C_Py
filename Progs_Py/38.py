from random import randint
def Muestra(M):
    for r in M:
        for c in r:
            print (' %d' % c, end = '\t')
        print()
A = [[randint(0,20) for c in range(4)] for r in range(5)]
B = [[randint(0,20) for c in range(4)] for r in range(5)]
print('A =')
Muestra(A)
print('B =')
Muestra(B)
C = [[sum(k) for k in zip(a,b)] for a,b in zip(A,B)]
print('A + B =')
Muestra(C)
C = [[k[0]-k[1] for k in zip(a,b)] for a,b in zip(A,B)]
print('A - B =')
Muestra(C)
