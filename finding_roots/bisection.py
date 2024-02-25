import math

def f(x):
    return pow(x,3) - pow(x,2) + 2

e = 10**-4

def bisection(a,b):
    if f(a)*f(b)>=0:
        print("you have not assumed right a and b")
        return
    

    while abs(b-a) > e:
        c = (a+b)/2
        if abs(f(c)) < e:
            break
        if f(a)*f(c)<0:
            b = c
        elif f(c)*f(b)<0:
            a = c
        c = (a+b)/2
    print(f'the answer is x =','%.4f'%c)
    return c
a = -2
b = 5
bisection(a, b)