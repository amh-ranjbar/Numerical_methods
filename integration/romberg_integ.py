import numpy as np
from scipy import integrate
from scipy.special import erf

g = lambda x: 1/np.sqrt(np.pi) * np.exp(-x**2)

result = integrate.romberg(g, 0, 1, show=True)