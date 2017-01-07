import tensorflow as tf

x = tf.Variable(tf.truncated_normal([10],stddev=0.1), name='x')
y = tf.Variable(tf.truncated_normal([10],stddev=0.1), name='y')
z = x + y
saver = tf.train.Saver()
tf.add_to_collection('z', z)
sess = tf.Session()
sess.run(tf.initialize_all_variables())
saver.save(sess, './saved_variables/3')

