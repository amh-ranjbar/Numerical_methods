import math

def f(x):
    return pow(x,3) + x - 1

def secant(x1,x2,E):
    n = 0; xm = 0; x0 = 0; c = 0
    if f(x1) * f(x2) < 0:
        while True:
            x0 = ( (x1*f(x2) - x2*f(x1)) ) / (f(x2) - f(x1))
            c = f(x1)*f(x0)
            x1 = x2
            x2 = x0
            n +=1
            if(c==0):
                break
            xm = ( (x1*f(x2) - x2*f(x1)) ) / (f(x2) - f(x1))
            if(abs(xm - x0) < E):
                break
            
    else:
        print("there is no real root in the given interval")
    print("the answer is x = : ", round(x0, 6))
    print("number of itteration is = ", n)
    return x0

x1 = 0
x2 = 1
E = 10**-4
secant(x1, x2, E)