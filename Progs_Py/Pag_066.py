from random import randint
A = [0 for i in range(12)]
for n in range(1000):
    d1 = randint(1,6)
    d2 = randint(1,6)
    s = d1+d2
    A[s-1] = A[s-1]+1
s1 = sum(A)
print(A)
print ('la suma es',s1)
B = [k/1000.0 for k in A]
s2 = sum(B)
print (B)
print ('la suma es',s2)
