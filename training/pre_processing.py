import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
class preprocessing:
    def __init__self(self,path,main_column,n_train_days,n_test_days,n_sample_minutes):
        #path of the csv file
        self.path=path
        #Target Column in the csv file
        self.main_column=main_column
        #Number of days you were planning ot give as the training data
        self.n_train_days=n_train_days
        #Number of the days you were planning to consider as a test data
        self.n_test_days=n_test_days
        #Number of sample minutes you are planning to consider since these number of minutes are converted to your input_shape-
        #-shape of the neural network you are going to build
        self.n_sample_minutes=n_sample_minutes

    def data_frame_reader(self):
        self.meta_data=pd.read_csv(self.path)
        #return the data frame
        return self.meta_data
    def data_frame_convertor(self):
        self.meta_data=meta_data[["date","active_energy"]]
        #Direct plan -- just take the essential columns for the data frame
        return self.meta_data
    def index_setter(self):
        #Set the date as index, since it is not useful while building the model other than just tracking the information flow.
        self.meta_data=self.meta_data.set_index(["date"])
        return self.meta_data
    def train_shaper(self):
        #Number of points in a formulation way deducing from the number of number of train days you selected
        num_points=self.n_train_days*24*60
        #Number of points in a formulation way deducing from the number of number of test days you selected
        test_points=self.n_test_days*24*60
        #This trainer class holds the subsetted data frame values we have taken by using the number of train days parameter
        self.trainer=self.meta_data.values[-num_points:-test_points]
        return self.trainer
    def test_shaper(self):
        #Number of points in a formulation way deducing from the number of number of test days you selected
        test_points=self.n_test_days*24*60
        #This tester class holds the subsetted data frame values we have taken by using the number of train days parameter
        self.tester=self.meta_data.values[-test_points:]
        return self.tester
    def train_main_convertor(self):
        #meta_train list holds the training values -- which means it holds all the column data of that particular row
        self.meta_train=[]
        #meta_target list holds the training values of the target -- which means it holds the target
        self.meta_target
        #So this is the parameter that decides how many columns you are going to use as the input shape for the network.
        start=self.n_sample_minutes*60
        for i in range(start,self.trainer.shape[0]):
            self.meta_train.append(slef.trainer.values[i-start:i])
            self.meta_target.append(self.trainer.values[i])
        #Now the value's shape that are there in the meta_train was(60,)
        #For the target the shape is 1
        return self.meta_train,self.meta_target
    def test_main_convertor(self):
        #meta_test list holds the training values -- which means it holds all the column data of that particular row
        self.meta_test=[]
        #meta_test_target list holds the testing target values -- which means it holds the target
        self.meta_test_target=[]
        #So this is the parameter that decides how many columns you are going to use as the input shape for the network.
        start=self.n_sample_minutes*60
        for i in range(start,self.tester.shape[0]):
            self.meta_test.append(slef.tester.values[i-start:i])
            self.meta_test_target.append(self.tester.values[i])
        #Now the value's shape that are there in the meta_train was(60,)
        #For the target the shape is 1
        return self.meta_test,self.meta_test_target
    def array_convertor(self):
        #Array convertor function is mainly used to convert the sahpe of the lists to array, so that-
        #- they are compatiable while we are fitting it into the network
        self.meta_train=np.array(self.meta_train)
        self.meta_target=np.array(self.meta_target)
        self.meta_test=np.array(self.meta_test)
        self.meta_test_target=np.array(self.meta_test_target)
        #This method is similar to the train test split method we use using the sklearn.model_selection train_test_split supreme_method
        #Anyway moving on :) :) :)
        return self.meta_train,slef.meta_target,self.meta_test,self.meta_test_target
    def supreme_method(self):
        #call the first method --- now the data frame is ready
        self.meta_data=self.data_frame_reader()
        #call the second method to convert the frame to our needed type
        self.meta_data=self.data_frame_convertor()
        #3rd method for setting index as date
        self.meta_data=self.index_setter()
        #creating training - (train,target) lists
        self.trainer=self.train_shaper()
        #creating testing - (test,target) lists
        self.tester=self.test_shaper()
        #this is for train
        #Converting to fetch the details or the values form the data frmae adn creating the row_columnary_data
        self.meta_train,self.meta_target=self.train_main_convertor()
        #this is for test
        #Converting to fetch the details or the values form the data frmae adn creating the row_columnary_data
        self.meta_test,self.meta_test_target=self.test_main_convertor()
        #As the final step convert this to arrays, so we get the nicely shape values
        self.meta_train,slef.meta_target,self.meta_test,self.meta_test_target=self.array_convertor
        #Basically,
        #the supreme function holds the control of all over the code
        #step by step calling and throwing out the perfect shape arrays
        return self.meta_train,slef.meta_target,self.meta_test,self.meta_test_target