from random import randint
n = 10
t = 0
N = [n]
T = [t]
print('Al tiempo %d, quedan %d dados' % (t,n))
while n>0:
    c = 0
    for i in range(n):
        z = randint(1,6)
        if z == 5:
            c = c + 1
    n = n - c
    t = t + 1
    T.append(t)
    N.append(n)
    print('Al tiempo %d, quedan %d dados' % (t,n))
