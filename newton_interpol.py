import numpy as np

x = np.array([0, 1, 2, 5.5, 11, 13, 16, 18], float)
y = np.array([0.5, 3.134, 5.9, 9.9, 10.2, 9.35, 7.2, 6.2], float)
n = len(x)
p = np.zeros([n, n+1])
value = float(input("Enter the point at which you wwant to calculate: "))

for i in range(n):

    p[i,0] = x[i]
    p[i,1] = y[i]

for i in range(2, n+1):
    for j in range(n+1-i):

        p[j,i] = (p[j+1,i-1] - p[j,i-1]) / (x[j+i-1] - x[j])

np.set_printoptions(suppress=True)

b = p[0][1:]
print("b = ", b)
print("x = ", x)
lst = []

t = 1
for i in range(len(x)):
    t = t * (value-x[i])
    lst.append(t)
print("The list of product elements is: ", lst, "\n")
f = b[0]
for k in range(1, len(b)):
    f = f + b[k]*lst[k-1]
print("The value of polynomial :", "%.3f"%f)
