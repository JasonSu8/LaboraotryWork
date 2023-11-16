# step 1
import os
import tensorflow as tf
import timeRecognitionNetwork
import imageio
import numpy as np

# step 2
video_path = 'D:/AAA/video.mp4'
ckpt_path = 'D:/BBB/weight.ckpt'

x_min = 111
x_max = 281
y_min = 333
y_max = 358

number_left_boundary = [8, 35, 62, 89, 116, 143]
number_right_boundary = [27, 54, 81, 108, 135, 162]

os.environ['CUDA_VISIBLE_DEVICES'] = '2'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# step 3
tf.reset_default_graph()
with tf.Graph().as_default() as graph:
    x = tf.placeholder(tf.float32, [None, 25, 19, 3]) 
    with tf.variable_scope('Network'):
        y_pred, y_reg = timeRecognitionNetwork.network(x)
    y_pred_max = tf.argmax(y_pred, 1)
    y_pred_percent = tf.reduce_max(y_pred, 1)
    
    # step 4 
    config = tf.ConfigProto()
    config.gpu_options.per_process_gpu_memory_fraction = 0.25
    
    init = tf.global_variables_initializer()                                                                                                                                                                               
    network_variables = tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES, scope = 'Network')
    saver_network = tf.train.Saver(network_variables)
    
    # step 5
    with tf.Session(config = config, graph = graph) as sess:
        sess.run(init)
        saver_network.restore(sess, ckpt_path)
        
        # step 6
        video = imageio.get_reader(video_path, 'ffmpeg')    
        for i in range(video.count_frames()):
            image = vid.get_data(i)
            time_image = image[y_min: y_max, x_min: x_max, :]
            
            # step 7
            y_prediction = 0
            hms = ''
            y_percentage_array = np.array([])                      
            
            for j in range(6):
                number_image = np.expand_dims(time_image[:, number_left_boundary[j]: number_right_boundary[j], :], 0)
                y_prediction, y_percentage = sess.run([y_pred_max, y_pred_percent], feed_dict = {x: number_image})
                y_prediction = y_prediction[0]
                hms = hms + str(y_prediction)
                y_percentage_array = np.append(y_percentage_array, y_percentage)                     
            
            print('Prediction:', hms)
            print('Accuracy:', y_percentage_array)
