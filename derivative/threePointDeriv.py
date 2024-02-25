# derivative of f(x) using three points

def f(x):
    return x**2 + 1

def d_f(x):
    h = 1e-4
    return (-f(x+2*h) + 4*f(x+h) - 3*f(x)) / (2*h)

x = float(input("enter x: "))
print(f"df(x)/dx at  x = {x} is {d_f(x)}")