import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
t = np.linspace(-5 * np.pi, 5 * np.pi, 500)
X = 5 * np.sin(t)
Y = 5 * np.cos(t)
Z = t
ax.plot(X, Y, Z, label='Curva Parametrica')
ax.legend()
plt.show()
