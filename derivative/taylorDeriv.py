import numpy as np
import matplotlib.pyplot as plt

def derivative(f, a, method='central', h=0.001):
    if method=='central':
        return (f(a+h) - f(a-h)) / (2*h)
    elif method=='forward':
        return (f(a+h) - f(a)) / h
    elif method=='backward':
        return (f(a) - f(a-h)) / h
    else:
        raise ValueError("method must be: 'central', 'forward' or 'backward' ")
    
x = np.linspace(0, 5*np.pi, 100)
dydx = derivative(np.sin, x)
Dydx = np.cos(x)
# visualization
plt.figure(figsize=(12,5))
plt.plot(x, dydx, 'r.', label='central difference')
plt.plot(x, Dydx, 'b', label='True Value')
plt.title("Central Difference Derivative of y = sin(x)")
plt.legend(loc='best')
plt.show()