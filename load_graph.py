import tensorflow as tf

with tf.Session() as sess:
	new_saver = tf.train.import_meta_graph('./saved_variables/3.meta')
	new_saver.restore(sess, './saved_variables/3')
	z = tf.get_collection('z')[0]
	a = sess.run(z)
	print(a)

