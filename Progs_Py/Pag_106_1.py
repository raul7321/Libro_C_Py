import matplotlib.pyplot as plt
import numpy as np
X = np.linspace(0, 2*np.pi, 100)
Y1 = np.sin(X)
Y2 = np.cos(X)
fig, ax = plt.subplots()
ax.plot(X,Y1, label='sen(x)')
ax.plot(X,Y2, label='cos(x)')
ax.set_xlabel('x')
ax.set_title('Grafica')
ax.legend(loc='upper center')
plt.show()
