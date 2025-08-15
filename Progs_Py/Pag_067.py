a = float(input('Dame el limite inferior a: '))
b = float(input('Dame el limite superior b: '))
M = int(input('Dame el numero de subintervalos: '))
h = (b-a)/M
s = h * ((a*a*a+2*a + b*b*b+2*b)/2 \
+ sum([(a+i*h)*(a+i*h)*(a+i*h)+2*(a+i*h) for i in range(1,M)]))
print ('El valor de la integral es: %f' % s)
