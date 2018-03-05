#_*_ coding:utf8 _*_
from __future__ import print_function

import tensorflow as tf

node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0, dtype=tf.float32)
print(node1, node2)

node3 = tf.add(node1, node2,name='add')

sess = tf.Session()
print(sess.run(node3))
