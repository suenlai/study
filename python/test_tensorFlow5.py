#_*_coding=utf8_*_
import tensorflow as tf
import numpy as np

one_fill_tensor = tf.Variable(tf.fill([4,4],3.0))
square_tensor = tf.square(one_fill_tensor)
reduce_sum_tensor = tf.reduce_sum(square_tensor,1,keep_dims=True)
sqrt_tensor = tf.sqrt(reduce_sum_tensor)

embeddings = tf.Variable(
            tf.random_uniform([10, 4], -1.0, 1.0))

norm = tf.sqrt(tf.reduce_sum(tf.square(embeddings), 1, keep_dims=True))
normalized_embeddings = embeddings / norm
init = tf.global_variables_initializer()

with tf.Session() as sess:
  sess.run(init) # reset values to wrong
  #print (normalized_embeddings.eval(session=sess))
  #print (embeddings.eval(sess))
  print (one_fill_tensor.eval(sess))
  print(sess.run(square_tensor))
  print(sess.run(reduce_sum_tensor))
  print(sess.run(sqrt_tensor))
  #print (square_tensor.eval(sess))
