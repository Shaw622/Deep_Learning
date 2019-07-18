import numpy as np

A = np.array([[1, 2], [3, 4]])
print(A.shape)
print('------------------')

B = np.array([[5, 6], [7, 8]])
print(B.shape)
print('------------------')

print(np.dot(A, B))
print(np.dot(B, A))
