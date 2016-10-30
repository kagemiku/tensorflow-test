import tensorflow as tf

tf_string = tf.constant('Hello, TensorFlow!')
session = tf.Session()
print(session.run(tf_string))
