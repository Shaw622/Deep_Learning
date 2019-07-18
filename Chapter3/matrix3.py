import numpy as np

A = np.array([[1, 2]])
print(A.shape)
print('------------------')

B = np.array([[1, 3, 5], [2, 4, 6]])
print(B.shape)
print('------------------')

C = np.dot(A, B)
print(C)
print('------------------')

