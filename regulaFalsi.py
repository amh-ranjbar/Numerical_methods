import math

MAX_ITER = 10000
def f(x):
    return x**3 - x**2 + 2

e = 10**-4
def regulaFalsi(a,b):
    if f(a)*f(b) >= 0:
        print("you have not assumed right a and b")
        return -1
    
    c = a
    for i in range(MAX_ITER):
        c = (a*f(b) - b*f(a)) / (f(b) - f(a))
        if f(c) < e:
            break
        elif f(c)*f(a) < 0:
            b = c
        else:
            a = c
    
    return c
a = -10
b = 10
x_c = regulaFalsi(a, b)
print("the root is x = ", "%.4f"%x_c)