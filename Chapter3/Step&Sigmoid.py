import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype=np.int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)

y = sigmoid(x)
z = step_function(x)

plt.plot(x, y, label='sigmoid')
plt.plot(x, z, linestyle='--', label='step')
plt.ylim(-0.1, 1.1) # y軸の範囲を指定
plt.legend()
plt.show()
