import matplotlib.pyplot as plt
X = [0,1,2,3,4,5]
Y = [0,1,4,9,16,25]
Fig, ax = plt.subplots()
ax.plot(X, Y, color = 'red', marker = 'o', label = 'Ejemplo 1')
ax.set_xlabel('Nombre del eje X')
ax.set_ylabel('Nombre del eje Y')
ax.set_title('Titulo de la Grafica')
ax.legend(loc = 'upper left')
plt.show()
