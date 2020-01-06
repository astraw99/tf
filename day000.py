import tensorflow as tf
tf.compat.v1.enable_eager_execution()

# tf.executing_eagerly()

tf.add(1, 2).numpy()
hello = tf.constant('Hello, TensorFlow!')
hello.numpy()
