D = [500,200,100,50,20,10,5,2,1]
n = int(input('Dame una cantidad '))
for k in D:
    c = 0
    while n>=k:
        n = n - k
        c = c + 1
    if c>0:
        mensaje = ('billete de' if c==1 else 'billetes de') if k>=20 else ('moneda de' if c==1
                                                                           else 'monedas de')
        print (c,mensaje,k)
