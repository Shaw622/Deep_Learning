import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def identity_function(x):
    return x

X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

print(W1.shape)
print(X.shape)
print(B1.shape)
print('------------------')
A1 = np.dot(X, W1) + B1
Z1 = sigmoid(A1)
print(Z1)
print('------------------')

W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])

print(W2.shape)
print(Z1.shape)
print(B2.shape)
print('------------------')
A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)
print(Z2)
print('------------------')

W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])

print(W3.shape)
print(Z2.shape)
print(B3.shape)
print('------------------')
A3 = np.dot(Z2, W3) + B3
Y = identity_function(A3)  #もしくは Y = A3
print(Y)
