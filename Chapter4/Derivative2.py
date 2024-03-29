import numpy as np
import matplotlib.pylab as plt

def numerical_diff(f, x): #中心差分
    h = 1e-4
    return ( f(x+h) - f(x-h) / (2*h))

def function_1(x):
    return 0.01*x**2 + 0.1*x

x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
plt.show()

numerical_diff(function_1, 10)



