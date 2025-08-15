P = 'python'
L = list(P)
A = ['_' for i in L]
print (' '.join(A))
while A!=L:
    letra = input('Dame una letra ')
    for k,p in enumerate(L):
        if p == letra:
            A[k]=letra
    print (' '.join(A))
print ('Ganaste!')
