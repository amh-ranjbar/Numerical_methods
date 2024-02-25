import numpy as np

def trapezoid(f, a, b, n=50):
    x = np.linspace(a, b, n+1)
    y = f(x)
    y_right = y[1:]
    y_left = y[:-1]
    dx = (b-a)/n
    T = (dx/2) * np.sum(y_right + y_left)
    return T

# example

g = lambda x:2*x
a = 0
b = 2
print(trapezoid(g, a, b, 10000))
print(trapezoid(lambda x:3*x**2,a,b,10000))
print(trapezoid(np.sin,0,np.pi/2,10000))