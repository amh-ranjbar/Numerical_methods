import math

def f(x):
    return x**3 - x*2 -1

def derivF(x):
    return 3*x**2 - 2*x

e = 10**-4
def newtonRaphson(x):
    h = f(x)/derivF(x)
    while abs(h) > e:
        h = f(x)/derivF(x)
        # x(i+1) = x(i) - f(x)/f'(x)
        x = x - h
    return x

x0 = -20
x = newtonRaphson(x0)
print("the root is x =",'%.4f'% x)