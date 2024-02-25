import numpy as np

def simpson(f, a, b, n=100):
    if n%2==1:
        raise ValueError("n must be an even integer")
    
    dx = (b-a)/n
    x = np.linspace(a, b, n+1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S

# example

g = lambda x:2*x
a = 0
b = 2
print(simpson(g, a, b, 10000))
print(simpson(lambda x:3*x**2,a,b,10000))
print(simpson(np.sin,0,np.pi/2,10000))