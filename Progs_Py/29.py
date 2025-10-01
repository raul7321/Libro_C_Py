from random import randint
z = randint(1,20)
c = 0
while True:
    c = c + 1
    n = int(input('Intento %d. Que numero crees que es? ' % c))
    if n>z: print ('El numero que diste es mayor')
    if n<z: print ('El numero que diste es menor')
    if n==z or c>4: break
if n==z: print ('Adivinaste!')
else: print ('Perdiste. El numero es',z)
