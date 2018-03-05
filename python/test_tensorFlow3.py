#_*_ coding:utf8 _*_
from __future__ import print_function

import tensorflow as tf

W = tf.Variable([-.1], dtype=tf.float32)
b = tf.Variable([.1], dtype=tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W * x + b
y = tf.placeholder(tf.float32)

squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
file_writer = tf.summary.FileWriter('/Users/suenlai/Downloads/tensor_logdir',
                                    sess.graph)


for i in range(1000):
    sess.run(train, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]})

current_W, current_b, current_loss = sess.run([W, b, loss], {
    x: [1, 2, 3, 4],
    y: [0, -1, -2, -3]
})
print("current_W:%s current_b %s loss %s" % (current_W, current_b,
                                             current_loss))
