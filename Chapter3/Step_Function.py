import numpy as np

x = np.array([-1.0, 1.9, 2.0])

# 整数のみに対応
def step_function(x):
    if x > 0:
        return 1
    else:
        return 0

# NumPy の配列にも対応
def step_function2(x):
    y = x > 0
    return y.astype(np.int)

print(step_function2(x))
