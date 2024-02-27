import numpy as np 
import matplotlib.pyplot as plt 

# Y = a0 + a1*X
def estimate_coef(x,y):
    n = np.size(x)
    m_x, m_y = np.mean(x), np.mean(y)
    ss_xy = np.sum(y*x) - n*m_y*m_x
    ss_xx = np.sum(x*x) - n*m_x*m_x
    a1 = ss_xy / ss_xx
    a0 = m_y - a1*m_x
    return(a0, a1)

def plot_regression_line(x, y, a):
    plt.scatter(x, y, color="m", marker="o", s=30)
    y_pred = a[0] + a[1]*x
    plt.plot(x, y_pred, color="g")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def main():
    x = np.arange(0,10)
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
    a = estimate_coef(x, y)
    print("Estimated coefficients: \na0={}\ \na1={}".format(a[0], a[1]))
    plot_regression_line(x, y, a)
if __name__ == '__main__':
    main()