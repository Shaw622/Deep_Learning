import numpy as np

x = np.array([1.0, 2.0, 3.0])
y = np.array([4.0, 5.0, 6.0])

print(x+y)
print(x-y)
print(x*y)
print(x/y)

print(x / 2.0) #ブロードキャスト


z = np.array([[4, 5], [1, 2]])
print(z)
print(z.shape)
print(z.dtype)
