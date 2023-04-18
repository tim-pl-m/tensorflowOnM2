#source: https://www.geeksforgeeks.org/install-tensorflow-on-macos/


# importing tensorflow
import tensorflow as tf
	
# creating nodes in computation graph
node1 = tf.constant(3, dtype = tf.int32)
print("Size of Tensor 1 is:", node1.numpy())
node2 = tf.constant(5, dtype = tf.int32)
print("Size of Tensor 2 is:", node2.numpy())
node3 = tf.add(node1, node2)
	
# create tensorflow session object
#sess = tf.Session()
#sess = tf.compat.v1.Session()
	
# evaluating node3 and printing the result
#print("Sum of node1 and node2 is:", sess.run(node3))
#print("Sum of node1 and node2 is:", node3)
print("Sum of node1 and node2 is:", node3.numpy())
#print("Sum of node1 and node2 is:", node3.toString)
	
# closing the session
#sess.close()

