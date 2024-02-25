import numpy as numpy
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial

x = [float(input()) for i in range(int(input("enter the number of elements in the list: ")))]
y = [float(input()) for i in range(int(input("enter the number of elements in the list: ")))]

print("x = ", x)
print("y = ", y)

poly = lagrange(x, y)
print("coefficients of the polynomyal is : ", Polynomial(poly).coef)
z = float(input("z = "))
print(poly(z))