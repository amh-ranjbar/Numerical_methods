from math import exp

def midpoint(f, a, b, n):
    h = (b-a)/n
    result = 0
    for i in range(n):
        result += f((a+h)/2 + i*h)
    result *= h
    return result

g = lambda y: exp(-y**2)
a = 0
b = 2

print('n                            midpoint')
print("\n")
for i in range(1,21):
    n = 2**i
    m = midpoint(g, a, b, n)
    print(n,"\t\t\t", m)