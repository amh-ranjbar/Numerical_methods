import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(z, t):
    dxdt = 3*np.exp(-t)
    dydt = -z[1] + 3
    dzdt = [dxdt, dydt]
    return dzdt

z0 = [0,0]
t = np.linspace(0,5)
z = odeint(model, z0, t)
print(np.column_stack((t,z)))
plt.plot(t, z[:,0], 'b-', label=r'$\frac{dx}{dt}=3\:\exp(-t)$')
plt.plot(t, z[:,1], 'r--', label=r'$\frac{dy}{dt}=-y+3$')
plt.ylabel('response')
plt.xlabel('time')
plt.legend(loc='best')
plt.show()