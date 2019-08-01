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
		inputs = Input(shape = img_shape)

		conv1 = Conv2D(64,(3,3),padding='same')(inputs)



