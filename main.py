#pylint: skip-file
import time
import numpy as np
import theano
import theano.tensor as T
import utils_pg as Utils
from mlp import *
import data

lr = 0.01
batch_size = 100
train_set, valid_set, test_set  = data.mnist(batch_size)

hidden_size = [500, 100]

dim_x = train_set[0][0][0].shape[1]
dim_y = train_set[0][1][0].shape[1]
print dim_x, dim_y

model = MLP(dim_x, dim_y, hidden_size)

start = time.time()
for i in xrange(100):
    acc = 0.0
    in_start = time.time()
    for index, data_xy in train_set.items():
        X = data_xy[0]
        Y = data_xy[1]
        model.train(X, Y, lr)
    in_time = time.time() - in_start
    
    num_x = 0.0
    for index, data_xy in valid_set.items():
        X = data_xy[0]
        Y = data_xy[1]
        label = np.argmax(Y, axis=1)
        p_label = np.argmax(model.predict(X)[0], axis=1)
        for c in xrange(len(label)):
            num_x += 1
            if label[c] == p_label[c]:
                acc += 1

    print "Iter = " + str(i) + ", Accuracy = " + str(acc / num_x) + ", Time = " + str(in_time)
print time.time() - start
