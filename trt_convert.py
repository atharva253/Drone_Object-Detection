# To convert the trained model into tensorrt graph.
# Uncomment the required portion and replace the paths.

# Option 1:
# Convert frozen graph to tensorrt graph

import tensorflow.compat.v1 as tf
from tensorflow.python.compiler.tensorrt import trt_convert as trt
with tf.Session() as sess:
    # First deserialize your frozen graph:
    with tf.gfile.GFile("/home/atharva/tensorflow/models/research/object_detection/models/model/iot/frozen_inference_graph.pb", 'rb') as f:
        frozen_graph = tf.GraphDef()
        frozen_graph.ParseFromString(f.read())
    # Now you can create a TensorRT inference graph from your
    # frozen graph:
    converter = trt.TrtGraphConverter(
	    input_graph_def=frozen_graph,
	    nodes_blacklist=['logits', 'classes']) #output nodes
    trt_graph = converter.convert()
    # Import the TensorRT graph into a new graph and run:
    output_node = tf.import_graph_def(
        trt_graph,
        return_elements=['logits', 'classes'])
    sess.run(output_node)


# Option 2:
# Convert saved model to tensorrt graph
'''
import tensorflow.compat.v1 as tf
from tensorflow.python.compiler.tensorrt import trt_convert as trt

converter = trt.TrtGraphConverter(
    input_saved_model_dir="/home/atharva/tensorflow/models/research/object_detection/models/model/iot/saved_model",
    max_workspace_size_bytes=(11<32),
    precision_mode="FP16",
    maximum_cached_engines=100)
output_saved_model_dir = "/home/atharva/tensorflow/models/research/object_detection/models/model/iot/trt_model"    
converter.convert()
converter.save(output_saved_model_dir)
'''


