import tensorflow as tf
from tensorflow.keras.layers import Input, Conv1D, BatchNormalization, Dense, Dropout
from tensorflow.keras.layers import AvgPool1D, GlobalAveragePooling1D, MaxPool1D, Conv1DTranspose
from tensorflow.keras.models import Model
from tensorflow.keras.layers import ReLU, concatenate
import tensorflow.keras.backend as K
from sklearn.model_selection import GridSearchCV
class Hyper_parameter_tuning:
    def __init__self(self,model,training_data,training_target_data):
        #So lets make decide the specifications of the model by finding the best out of best specifications that are there
        self.model=model
        #lets get the model first
        self.training_data=training_data
        #now get the training data
        self.training_target_data=training_target_data
        #now let us get the target data
    def hyper_parameter_tuning(self):
        """
        Units:
        The selection of the number of hidden layers and the number of memory cells in LSTM probably depends
        on the application domain and context where you want to apply this LSTM.
        The optimal number of hidden units could be smaller than the number of inputs.
        AFAIK, there is no rule like multiply the number of inputs with N.
        """
        self.units=[i for i in range(60,240,60)]
        """
        Traditionally, LSTMs use the tanh activation function for the activation of the cell state and
        the sigmoid activation function for the node output.
        """
        self.activation=["tanh"]

        """
        recurrent_activation is for activate input/forget/output gate.
        activation if for cell state and hidden state. Follow this answer to receive notifications.
        """
        self.recurrent_activation=["sigmoid"]

        """
        Dropout decides, which neurons need to be drooped on each iteration form the layer, kindoff works like if the
        value of the neuron is less than the dropout then the neuron gets dropped.
        """
        self.dropout=[i/10 for i in range(1,11,1)]

        """
        Initializers define the way to set the initial random weights of Keras layers.
        The keyword arguments used for passing initializers to layers depends on the layer.
        Usually, it is simply kernel_initializer and bias_initializer.
        golorot_uniform : t draws samples from a uniform distribution within -limit, limit where limit is sqrt(6 / (fan_in + fan_out))
        where fan_in is the number of input units in the weight tensor and fan_out is the number of output units in the weight tensor.
        """

        self.kernel_initializer=['glorot_uniform']

        """
        While training the deep learning model, we need to modify each epoch's weights and minimize the loss function.
        An optimizer is a function or an algorithm that modifies the attributes of the neural network, such as weights and learning rate.
        Thus, it helps in reducing the overall loss and improve the accuracy.
        Adam is the best optimizer for the time series data
        """
        self.optimizer = ['Adam', 'Adamax']
        "epoch easily known to train the network n times with different batches with differnt values in the each batch,"
        self.epochs=[i for i in range(5,26,5)]
        #let us create a dictionary for this all params
        self.parameter_grid=dict(units=self.units,activation=self.activation,recurrent_activation=self.recurrent_activation,self.dropout=dropout,self.kernel_initializer=kernel_initializer)
        #deploy the grid search cv inot he model
        self.Final_Grid=GridSearchCV(estimator=self.model,parameter_grid=self.parameter_grid,n_jobs=-1,cv=3)
        #make the model fit inot the trian and target data
        self.final_model=self.Final_Grid.fit(self.training_data,self.training_target_data)
        #to get the best parameter pair use this line
        self.best_params=self.final_model.best_params_
        #return the model and the best parameter
        return self.final_model,self.best_params