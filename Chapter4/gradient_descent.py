import numpy as np

def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x

    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad

    return x

def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)

    for idx in range(x.size):
        tmp_val = x[idx]

        # f(x+h) の計算
        x[idx] = tmp_val + h
        fxh1 = f(x)

        # f(x-h) の計算
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val

    return grad

def function_2(x):
    return x[0]**2 + x[1]**2

init_x = np.array([-3.0, 4.0])
#print(gradient_descent(function_2, init_x=init_x, lr=0.1, step_num=100))

# lr が大きすぎる例: lr = 10.0
#print(gradient_descent(function_2, init_x=init_x, lr=10.0, step_num=100))

# lr が小さすぎる例: lr = 1e-10
print(gradient_descent(function_2, init_x=init_x, lr=1e-10, step_num=100))
