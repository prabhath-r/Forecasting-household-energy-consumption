# Household Electric Power Consumption Forecast Application

## 1. Introduction :
- The real energy demand made on the present electrical supply is referred to as electric energy consumption. However, poor management of its use can result in a reduction in electrical supply. As a result, it is critical that everyone be concerned about energy efficiency in order to reduce consumption. The goals of this study are to develop a model for forecasting household electricity usage and to determine the best forecasting period, which could be daily, weekly, monthly, or quarterly. Individual household electric power usage is the time-series data in our investigation.
- Any household requires electricity to function. In this period of global instability, the globe requires rising amounts of energy to maintain economic and social progress and improve living standards. Mishandling of electric energy could result in future excessive costs. Over 60% of residential energy in the United States is wasted.  Many people who use power on a regular basis are unaware of how much energy is wasted. The monthly electricity usage is predicted using a forecasting tool. We employ a Neural network model based on LSTM (Long short-term memory), which is quite efficient for time series samples like ours.

## 2. Data Collection :
** https://www.kaggle.com/datasets/uciml/electric-power-consumption-data-set **

Dataset is taken from an open-source Kaggle, which consists of 20,75,259 rows and 9 columns. The data is collected between 2006 to 2008.

## 2.1 Dataset Description:
  The format for Date is taken as: dd/mm/yyyy                                                                 
  The format for Time is taken as: hh/mm/ss
  Global_active_power: It is the power that is actually consumed by an     appliance averaged per minute
 Global_reactive_power: It is the Imaginary power that is not consumed by an appliance averaged per minute.
 Voltage: Minute averaged voltage
 Global_intensity: Household minute averaged current intensity
Sub_metering_1: It corresponds to the kitchen, containing mainly a dishwasher, an oven, and a microwave.
Sub_metering_2: It corresponds to the laundry room, containing a washing machine, a tumble-drier, a refrigerator, and a light.
Sub_metering_3: It corresponds to an electric water heater and an air-conditioner.
 Active energy consumed every minute = (global active power) *1000/60 - submetering1 - submetering2 - submetering3

## 3. Project Architecture :
The basic idea of the project is that every user has different kinds of electricity usage in their own homes. Users will be able to interact with the application with a Web UI where they can upload their past data CSV files in the application. An LSTM based Machine Learning model will be trained according to the User data. Then, the user can connect his live electricity stream data to the application and he can show the monthly forecast of the bill and the application in a Power BI Dashboard.

The project architecture has all the significant steps required for the production environment. The data flow is divided into two significant steps which are Training Pipeline and Inference Pipeline. The whole project is built on Amazon Web Services and the whole project, for now, is deployed on an EC2 Instance with a t3 large machine. The development work is done using the Amazon SageMaker Notebooks. Github is used for the version control of the project. Asana is used as the project management tool for assigning tasks and roles accordingly. The project logs are monitored using Cloud Watch. The architecture design has been implemented following four categories.

## 4. Project Flow:
The flow has been designed in two steps. The user can register in our application through a Sign-In page displayed in the application. Before that, users should have the project-execution IAM role access to interact with the underlying AWS resources. The user should contact the owners (Developers) before accessing the application. Single Sign-ON has been implemented using AWS SSO. 

## 4.1. Training Pipeline:

Users with correct IAM permissions to access the Energy Forecast Application will land on the sign-up page upon starting the Flask Application. The user first needs to sign up using details like FirstName, LastName, email and password. Then User can log in to the application using login credentials. It will land the user on the Homepage where there will be project information. Then there will be a forecast button which will direct to the Training Pipeline button. 

## 4.1.1 Data Preprocessing:

Preprocessing is implemented using PySpark in order to handle huge amounts of data. Firstly, a spark season has been created using the app name DataPreprocessing Energy Consumption. The uploaded CSV is read using pandas data frame and converted into spark Dataframe. Various preprocessing steps have been performed during the process. Date and time columns are handled using spark and developed as a single timestamp column and converted to the desired timestamp. The column names are processed according to the redshift column naming convention. The data types are being converted according to the redshift data type formats. Sampling and Interpolation have been implemented using the panda's library. The Active Energy column has been added according to a measure. The data will be then staged in an Amazon Redshift table.

## 4.1.2 Machine Learning Model Development:

The LSTM model has been trained using the Tensorflow library. Model takes the number of layers and the input shape of the data (the data with which we want to build the model) as an input for the model preparation. Various nodes have also been implemented in the middle such as Dropout and Dense. The model undergoes a hyper parameter tuning where the model is iterated using various parameters to find the best accurate model. The model will be then packaged and stored as a .pkl file in the AWS S3 bucket.

## 4.2. Inference Pipeline:

After the model has been successfully built, the model will be stored as a .pkl file in the s3 bucket location, then the user will have a Inference Pipeline tab in which he has a lot of input data sources. Then the Real-time data gets inferenced to the model and the results get stored in to a Redshift table.