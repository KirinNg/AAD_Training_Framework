import tensorflow as tf
import nets.lenet as lenet
import nets.cifarnet as cifarnet
import nets.vgg as vgg
import nets.resnet as resnet
import nets.alexnet as alexnet
import tensorflow.contrib.slim as slim


def lenet_net(image, reuse=tf.AUTO_REUSE, keep_prop=0.5):
    image = tf.reshape(image, [-1, 28, 28, 1])
    with tf.variable_scope(name_or_scope='LeNet', reuse=reuse):
        arg_scope = lenet.lenet_arg_scope()
        with slim.arg_scope(arg_scope):
            logits, end_point = lenet.lenet(image, 10, is_training=True, dropout_keep_prob=keep_prop)
            probs = tf.nn.softmax(logits)  # probabilities
    return logits, probs, end_point


def cifar_net(image, reuse=tf.AUTO_REUSE, keep_prop=0.5):
    image = tf.reshape(image, [-1, 32, 32, 3])
    with tf.variable_scope(name_or_scope='CifarNet', reuse=reuse):
        arg_scope = cifarnet.cifarnet_arg_scope()
        with slim.arg_scope(arg_scope):
            logits, end_point = cifarnet.cifarnet(image, 10, is_training=True, dropout_keep_prob=keep_prop)
            probs = tf.nn.softmax(logits)  # probabilities
    return logits, probs, end_point


def Alex_net(image, reuse=tf.AUTO_REUSE, keep_prop=0.5):
    image = tf.reshape(image, [-1, 224, 224, 3])
    with tf.variable_scope(name_or_scope='Alex', reuse=reuse):
        arg_scope = alexnet.alexnet_v2_arg_scope()
        with slim.arg_scope(arg_scope):
            logits, end_point = alexnet.alexnet_v2(image, 1000, is_training=True, dropout_keep_prob=keep_prop)
            probs = tf.nn.softmax(logits)  # probabilities
    return logits, probs, end_point


def vgg_net(image, reuse=tf.AUTO_REUSE, keep_prop=0.5):
    image = tf.reshape(image, [-1, 224, 224, 3])
    with tf.variable_scope(name_or_scope='VGG16', reuse=reuse):
        arg_scope = vgg.vgg_arg_scope()
        with slim.arg_scope(arg_scope):
            logits, end_point = vgg.vgg_16(image, 1000, is_training=True, dropout_keep_prob=keep_prop)
            probs = tf.nn.softmax(logits)  # probabilities
    return logits, probs, end_point


def resnet2_net(image, reuse=tf.AUTO_REUSE):
    image = tf.reshape(image, [-1, 224, 224, 3])
    with tf.variable_scope(name_or_scope='ResNet', reuse=reuse):
        arg_scope = resnet.resnet_utils.resnet_arg_scope()
        with slim.arg_scope(arg_scope):
            logits, end_point = resnet.resnet_v2_50(image, 1000, is_training=True)
            probs = tf.nn.softmax(logits)  # probabilities
    return logits, probs, end_point
