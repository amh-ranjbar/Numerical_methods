import numpy as np
import matplotlib.pyplot as plt

def Euler(f, y0, x):

    y = np.zeros(len(x))
    y[0] = y0
    h = x[1] - x[0]
    for n in range(len(x)-1):
        y[n+1] = y[n] + h*f(y[n], x[n])
    
    return y

# example
x = np.linspace(0, 2, 20)
y0 = 1

f = lambda y, x: y
y = Euler(f, y0, x)
y_True = np.exp(x)

plt.plot(x, y, 'b.-', x, y_True, 'r-')
plt.legend(['Euler', 'y_True'])
plt.axis([0,2, 0,9])
plt.grid(True)
plt.title("Solution of $y'=y , y(o)=1$")
plt.show()