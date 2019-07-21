import sys, os
sys.path.append(os.pardir) # 親ディレクトリを参照
from dataset.mnist import load_mnist

#(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False, one_hot_label=True)

print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)
