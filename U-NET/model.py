'''
 * @author [Ritwik Singh]
 * @create date 2019-07-25 00:14:15
 * @modified date 2019-07-26 14:11:28
 * @desc [description]

'''
from __future__ import print_function,division

import os
import numpy as np 

import keras
from keras.models import *
from keras.layers import *
from keras.optimizers import *
from keras import backend as K
from keras.callbacks import ModelCheckpoint, LearningRateScheduler

class UNet():
	def __init__(self):
		pass

	def craete_model(self,img_shape,num_class):
		input = Input(shape = img_shape)

		conv1 = Conv2D(64,(3,3),activation='relu',padding='same')(inputs)
		conv1 = Conv2D(64,(3,3),activation='relu',padding='same')(inputs)(conv1)
		pool1 = MaxPooling2D(pool_size=(2,2))(conv1)


		conv2 = Conv2D(128,(3,3),activation='relu',padding='same')(pool1)
		conv2 = Conv2D(128,(3,3),activation='relu',padding='same')(conv2)
		pool2 = MaxPooling2D(pool_size=(2,2))(conv2)


		conv3 = Conv2D(256,(3,3),activation='relu',padding='same')(pool2)
		conv3 = Conv2D(256,(3,3),activation='relu',padding='same')(conv3)
		pool3 = MaxPooling2D(pool_size=(2,2))(conv3)

		conv4 = Conv2D(512,(3,3),activation='relu',padding='same')(pool3)
		conv4 = Conv2D(512,(3,3),activation='relu',padding='same')(conv3)
		pool4 = MaxPooling2D(pool_size=(2,2))(conv4)

		conv5 = Conv2D(1024,(3,3),activation='relu',padding='same')(pool4)
		conv5 = Conv2D(1024,(3,3),activation='relu',padding='same')(conv5)

		up_conv6 = UpSampling2D(size=(2,2))(conv5)
		conv6 = Conv2D(512,(3,3),activation='relu',padding='same')(up_conv6)
		conv6 = Conv2D(512,(3,3),activation='relu',padding='same')(conv6)

		up_conv7 = UpSampling2D(size=(2,2))(conv6)
		conv6 = Conv2D(256,(3,3),activation='relu',padding='same')(up_conv7)
		conv6 = Conv2D(256,(3,3),activation='relu',padding='same')(conv7)

		up_conv8 = UpSampling2D(size=(2,2))(conv7)
		conv8 = Conv2D(128,(3,3),activation='relu',padding='same')(up_conv8)
		conv8 = Conv2D(128,(3,3),activation='relu',padding='same')(conv8)	


		up_conv9 = UpSampling2D(size=(2,2))(conv8)
		conv9 = Conv2D(64,(3,3),activation='relu',padding='same')(up_conv9)
		conv9 = Conv2D(64,(3,3),activation='relu',padding='same')(conv9)






