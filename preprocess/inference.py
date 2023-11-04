import pandas as pd
import time
import pickle
import pandas as pd
import numpy as np
import time
import pickle
import boto3
from sqlalchemy import create_engine
from sqlalchemy.engine import url as sa_url
import datetime

s3_client = boto3.client('s3')
# path1="s3://dev-data228-bigdatafinalproject/energy_consump_preprocessed.csv"
model_path="model_final.pkl"
s3_client.download_file('dev-data228-bigdatafinalproject', 'model_final.pkl', 'model_final.pkl')
# meta_data=pd.read_csv(path1)
def test_convertor(meta_data):
    meta_data=meta_data[["date","active_energy"]]
    meta_data=meta_data.set_index(["date"])
    tester=meta_data[-2880:]
    meta_train=[]
    meta_target=[]
    for i in range(120,meta_data.shape[0]):
        meta_train.append(meta_data.values[i-120:i])
        meta_target.append(meta_data.values[i])
    return meta_train,meta_target
def load_the_model(model_path):
    loaded_model= pickle.load(open(model_path, 'rb'))
    return loaded_model
def looper(meta_data,model):
    
    url = sa_url.URL(
    drivername='postgresql+psycopg2', # indicate redshift_connector driver and dialect will be used
    host='dev-datarangers-final.cwmgpuwjy8xr.us-east-1.redshift.amazonaws.com', # Amazon Redshift host
    port='5439', # Amazon Redshift port
    database='dev', # Amazon Redshift database
    username='root', # Amazon Redshift username
    password='Datarangers4' # Amazon Redshift password
    )
    conn = create_engine(url)
    
    #model1=load_the_model(model_path)
    test,target =test_convertor(meta_data)
    l1=[]
    l1.append(model.predict(test[0])[-1])
    #print(model.predict(test[0])[-1],"---",target[0])
    l1.append(model.predict(test[1])[-1])
    #print(model.predict(test[1])[-1],"----",target[1])
    df1=pd.DataFrame({"main":l1})
    print(df1)
    
    date = datetime.datetime(2008,9,1,0,0,0)
    for i in range(2,len(test)):
        pred=model.predict(test[i])[-1]
        #print(pred[-1],"---",target[i])
        df2=pd.DataFrame({"date": date,"active_energy":pred, "energy_cost":(pred*0.126)/1000 })
#         df1=pd.concat([df1,df2],ignore_index=True,axis=0)
        print(df2)
        print("uploading data to redshift")
        df2.to_sql('energy_consump_pred', conn, index=False, if_exists='append')
        print("finished uploading")
        date += datetime.timedelta(minutes=1)
        time.sleep(59)
        


