'''

 * @author [Ritwik Singh]
 * @created date 2019-08-01 12:45:15
 * @desc [description]

'''


from __future__ import print_function,division

import os
import numpy as np 

import keras
from keras.models import *
from keras.layers import *
from keras.optimizers import *
from keras.activations import *
from keras import backend as k
from keras.callbacks import ModelCheckpoint, LearningRateScheduler

class SegNet():
	
	def __init__(self):
		pass

	def build_model(self):

		# Encoder

		inputs = Input(shape = img_shape)

		conv1 = Conv2D(64,(3,3),padding='same')(inputs)
		conv1 = BatchNormalization()(conv1)
		conv1 = Activation("relu")(conv1)
		conv2 = COnv2D(64,(3,3),padding='same')(conv1)
		conv2 = BatchNormalization()(conv2)
		conv2 = Activation("relu")(conv2)
		pool1,mask1 = MaxPoolingWithArgmax2D((2,2))(conv2)


		conv3 = Conv02D(128,(3,3),padding='same')(pool1)
		conv3 = BatchNormalization()(conv3)
		conv3 = Activation("relu")(conv3)
		conv4 = COnv2D(128,(3,3),padding='same')(conv3)
		conv4 = BatchNormalization()(conv4)
		conv4 = Activation("relu")(conv4)
		pool2,mask2 = MaxPoolingWithArgmax2D((2,2))(conv4)


		conv5 = Conv2D(256,(3,3),padding='same')(pool2)
		conv5 = BatchNormalization()(conv5)
		conv5 = Activation("relu")(conv5)
		conv6 = COnv2D(256,(3,3),padding='same')(conv5)
		conv6 = BatchNormalization()(conv6)
		conv6 = Activation("relu")(conv6)
		conv7 = COnv2D(256,(3,3),padding='same')(conv6)
		conv7 = BatchNormalization()(conv7)
		conv7 = Activation("relu")(conv7)
		pool3,mask3 = MaxPoolingWithArgmax2D((2,2))(conv7)



		conv8 = Conv2D(512,(3,3),padding='same')(pool3)
		conv8 = BatchNormalization()(conv8)
		conv8 = Activation("relu")(conv8)
		conv9 = COnv2D(512,(3,3),padding='same')(conv8)
		conv9 = BatchNormalization()(conv9)
		conv9 = Activation("relu")(conv9)
		conv10 = COnv2D(512,(3,3),padding='same')(conv9)
		conv10= BatchNormalization()(conv10)
		conv10 = Activation("relu")(conv10)
		pool4,mask4 = MaxPoolingWithArgmax2D((2,2))(conv10)


		conv11 = Conv2D(512,(3,3),padding='same')(pool4)
		conv11 = BatchNormalization()(conv11)
		conv11 = Activation("relu")(conv11)
		conv12 = COnv2D(512,(3,3),padding='same')(conv11)
		conv12 = BatchNormalization()(conv12)
		conv12 = Activation("relu")(conv12)
		conv13 = COnv2D(512,(3,3),padding='same')(conv12)
		conv13= BatchNormalization()(conv13)
		conv13 = Activation("relu")(conv13)
		pool5,mask5 = MaxPoolingWithArgmax2D((2,2))(conv13)

		# Decoder

