import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(y, t):
    f = -y + 1
    return f

y0 = 0
x0 = 0
xn = 5
t = np.linspace(x0, xn)
y = odeint(model, y0, t)

print(np.column_stack((t, y)))

plt.plot(t, y)
plt.xlabel('time')
plt.ylabel("y(t)")
plt.show()