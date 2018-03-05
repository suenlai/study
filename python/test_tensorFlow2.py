#_*_ coding:utf8 _*_
from __future__ import print_function

import tensorflow as tf

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

add_node = tf.add(a, b, name='addnode')
mul_node = tf.multiply(add_node, 3, name="mulnode")
sess = tf.Session()
file_writer = tf.summary.FileWriter('/Users/suenlai/Downloads/tensor_logdir',
                                    sess.graph)
result2 = sess.run(mul_node, {a: 23, b: 4})
print(result2)
