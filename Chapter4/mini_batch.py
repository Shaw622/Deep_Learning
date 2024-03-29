# ミニBatch 処理を行う
import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=True)

#print(x_train.shape)
#print(t_train.shape)

train_size = x_train.shape[0]
print(train_size)
batch_size = 10
print(batch_size)
batch_mask = np.random.choice(train_size, batch_size)
print(batch_mask)
x_batch = x_train[batch_mask]
print(x_batch)
t_batch = t_train[batch_mask]
print(t_batch)


