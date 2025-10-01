from random import randint
def Muestra(M):
    for r in M:
        for c in r:
            print (' %d' % c, end = '\t')
        print()
A = [[randint(0,20) for i in range(4)] for j in range(3)]
B = [[randint(0,20) for i in range(4)] for j in range(3)]
C = [[randint(0,20) for i in range(4)] for j in range(3)]
print ('A = ')
Muestra(A)
print ('B = ')
Muestra(B)
print ('C = ')
Muestra(C)
