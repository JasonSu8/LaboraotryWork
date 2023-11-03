# step 1
import tensorflow as tf
import numpy as np
import math


# step 2
def general_variable_counter_reset():
    
    global g_w_counter, g_b_counter
    g_w_counter = 0
    g_b_counter = 0


# step 3
def general_weight_variable(shape, regRate = 0.01):

    global g_w_counter
    g_w_counter = g_w_counter + 1

    initializer = tf.random_normal_initializer(mean = 0.0, stddev = 0.01)
    weight = tf.get_variable(name = 'g_w_' + str(g_w_counter), shape = shape, 
                             initializer = initializer)
    reg = tf.contrib.layers.l2_regularizer(regRate)(weight)
    
    return weight, reg


# step 4
def general_bias_variable(shape, regRate = 0.01):
    
    global g_b_counter
    g_b_counter = g_b_counter + 1    

    initializer = tf.random_normal_initializer(mean = 0.0, stddev = 0.01)
    bias = tf.get_variable(name = 'g_b_' + str(g_b_counter), shape = shape, 
                           initializer = initializer)

    return bias


# step 5
def general_conv2d(input_tensor, input_channel, filter_size, n_filters, stride, 
                   activation = tf.nn.relu, padding = 'SAME'):
    
    w_conv, r_conv = general_weight_variable([filter_size, filter_size, input_channel, n_filters])
    b_conv = general_bias_variable([n_filters])
    h_conv = activation(tf.nn.conv2d(input = input_tensor, filter = w_conv, 
                                     strides = [1, stride, stride, 1], padding = padding) 
                        + b_conv)
    
    return h_conv, r_conv


# step 6
def general_fc(input_tensor, n_input, n_output, activation = tf.nn.relu):
    
    w_fc, r_fc = general_weight_variable([n_input, n_output])
    b_fc = general_bias_variable([n_output])
    h_fc = activation(tf.matmul(input_tensor, w_fc) + b_fc)
    
    return h_fc, r_fc


# step 7
def network(x):
    
    general_variable_counter_reset() 
    
    x_shape = x.get_shape().as_list()
    
    filter_size_1 = 5   # 19 x 25 -> 9 x 13
    n_filters_1 = 32
    h_conv1, r_conv1 = general_conv2d(x, x_shape[3], filter_size_1, n_filters_1, 2)

    filter_size_2 = 3   # 9 x 13 -> 5 x 7
    n_filters_2 = 64
    h_conv2, r_conv2 = general_conv2d(h_conv1, n_filters_1, filter_size_2, n_filters_2, 2)
    
    flat_size_1 = math.ceil(math.ceil(x_shape[1] / 2) / 2)
    flat_size_2 = math.ceil(math.ceil(x_shape[2] / 2) / 2)
    
    h_conv2_flat = tf.reshape(h_conv2, [-1, flat_size_1 * flat_size_2 * n_filters_2])
    
    n_fc1 = 1024
    h_fc1, r_fc1 = general_fc(h_conv2_flat, flat_size_1 * flat_size_2 * n_filters_2, n_fc1)
    
    n_fc2 = 64
    h_fc2, r_fc2 = general_fc(h_fc1, n_fc1, n_fc2)
    
    n_output = 10
    h_fc3, r_fc3 = general_fc(h_fc2, n_fc2, n_output, activation = tf.nn.softmax)
    
    r_total = r_conv1 + r_conv2 + r_fc1 + r_fc2 + r_fc3
    
    return h_fc3, r_total 
