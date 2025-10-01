from random import randint
salva = open('salida.csv','w')
A = [0 for i in range(12)]
for n in range(1000):
    d1 = randint(1,6)
    d2 = randint(1,6)
    s = d1 + d2
    A[s-1] = A[s-1] + 1
print(A)
for i,f in enumerate(A):
    salva.write(f'{i+1},{f}\n')
salva.close()
