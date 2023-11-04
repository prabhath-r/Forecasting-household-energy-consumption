import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow.keras.layers import Input, Conv1D, BatchNormalization, Dense, Dropout
from tensorflow.keras.layers import AvgPool1D, GlobalAveragePooling1D, MaxPool1D, Conv1DTranspose
from tensorflow.keras.models import Model
from tensorflow.keras.layers import ReLU, concatenate
import tensorflow.keras.backend as K
# Creating LSTM
class model_building:
    def __init__self(self,input_shape,number_of_layers_you_want):
        #the shape of the input data you ar going to feed the network
        self.input_shape=input_shape
        #the number of layers you want into the network --- to make it super advanced
        self.number_of_layers_you_want=number_of_layers_you_want
    def create_model():
        #create a first layer as input layer to concatenate with the original lstm network
        #Inpuit shape extract from the passed parameter
        input=Input(self.input_shape)
        #The first layer of the lstm ---> why we need to create this ... if we have a loop ? think harshith mawa
        self.model=LSTM(units=120,input_shape=input_shape,return_sequences=True)(input)
        self.model=Dropout(0.25)(model)
        #The answer is what if the number_of layers you gave is 0. Then as a super coder, we need to run the network
        #-even with the one layer.
        for i in range(number_of_layers_you_want):
            #This adds the LSTM layers to the existing model
            self.model=LSTM(units=120,return_sequences=True)(model)
            #This adds the dropout layers to the existing model
            self.model=Dropout(0.25)(model)
        #Now since teh shape of the layers will be(shape,units) but since we are approching the end layers -
        #- return_sequences are false to not copy the shape of the above layers
        #- From now the units is the shape
        self.model=LSTM(units=120,return_sequences=False)(model)
        #The final touch with the dropout
        self.model=Dropout(0.2)(model)
        #Lastly the output node luckily we have one target class so go with that
        self.output = Dense(units=1, activation = 'tanh')(model)
        #The keras model fucntion to concatenate the two ends (even though the output is carrying the properties of the every layer on top of it)
        self.model = Model(input, output)
        #The finally, finally, return the kong out to the Hyper_parameter_tuning
    return self.model