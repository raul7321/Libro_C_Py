import matplotlib.pyplot as plt
from random import randint
n = 100
t = 0
N = [n]
T = [t]
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
fig, ax = plt.subplots()
ax.plot(T,N)
plt.show()
