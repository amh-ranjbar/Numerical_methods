import math
import numpy as np
import matplotlib.pyplot as plt

# y' = -y + 1 = f(x,y)
N = 50
x0 = 0
xn = 5
y0 = 0
x = np.linspace(x0, xn, N+1)
y = np.zeros(len(x))
y[0] = y0
h = x[1] - x[0]

def f(x,y):
    return -y + 1

for i in range(N):

    K1 = f(x[i], y[i])
    K2 = f(x[i]+0.5*h, y[i]+0.5*h*K1)
    K3 = f(x[i]+0.5*h, y[i]+0.5*h*K2)
    K4 = f(x[i]+h, y[i]+h*K3)

    y[i+1] = y[i] + h/6*(K1 + 2*K2 + 2*K3 + K4)

plt.plot(x,y)
plt.show()