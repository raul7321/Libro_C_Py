import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from mpl_toolkits.mplot3d.axes3d import get_test_data
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
X = np.arange(-np.pi, np.pi, 0.25)
Y = np.arange(-np.pi, np.pi, 0.25)
X,Y = np.meshgrid(X, Y)
Z = np.sin(X)*np.cos(Y)
surf=ax.plot_surface(X,Y,Z, cmap=cm.coolwarm)
plt.show()
