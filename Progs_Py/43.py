import matplotlib.pyplot as plt
import numpy as np
X = np.linspace(0, 2*np.pi, 100)
fig, ax = plt.subplots()
ax.plot(X,np.sin(X), label='sen(x)')
ax.plot(X,np.cos(X), label='cos(x)')
ax.set_xlabel('x')
ax.set_title('Grafica')
ax.legend(loc='upper center')
plt.show()
