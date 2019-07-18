import numpy as np

def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

a = np.array([1010, 1000, 990])
print(np.exp(a) / np.sum(np.exp(a))) # nan(not a number) になる

c = np.max(a) # 1010
print(a-c) # オーバーフロー対策

print(np.exp(a-c) / np.sum(np.exp(a-c)))
