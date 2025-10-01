import matplotlib.pyplot as plt
from math import *
X = [t/100.0 * 2*pi for t in range(100)]
Y1 = [sin(x) for x in X]
Y2 = [cos(x) for x in X]
fig, ax = plt.subplots()
ax.plot(X,Y1, label='sen(x)')
ax.plot(X,Y2, label='cos(x)')
ax.set_xlabel('x')
ax.set_title('Grafica')
ax.legend(loc='upper center')
plt.show()
