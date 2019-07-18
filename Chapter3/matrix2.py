import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
print(A.shape)
print('------------------')

B = np.array([[1, 2], [3, 4], [5, 6]])
print(B.shape)
print('------------------')

print(np.dot(A, B))
print(np.dot(B, A))
