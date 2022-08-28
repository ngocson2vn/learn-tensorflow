import tensorflow.compat.v1 as tf

a = 2
b = 3
c = tf.add(a, b, name='Add')
print(c)

with tf.Session() as session:
  result = session.run(c)
  print(result)
