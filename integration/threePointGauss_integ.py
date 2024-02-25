from scipy import integrate

f = lambda x: x**8 + x**4
a = 0.0
b = 1.8
intf = integrate.quadrature(f, a, b)
#print("%.6f"%intf)
print(intf)