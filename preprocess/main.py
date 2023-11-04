import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pyspark
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import to_timestamp
from pyspark.sql.functions import col, to_date
from pyspark.sql.functions import unix_timestamp, from_unixtime
import sqlalchemy as sa
from sqlalchemy import orm as sa_orm
from sqlalchemy import create_engine
from sqlalchemy.engine import url as sa_url
from rich.console import Console

from active_energy import AddingActiveEnergy
from datatype_conversion import DatatypeConversion
from ingest_redshift import IngesttoRedshift
from interpolate import InterpolateDF
from processing_dt import ProcessingDateTime
from renaming_columns import RenamingColumns
from inference import *



def main(url):
    url  = url
    data_types = ['datetime', 'float', 'float', 'float', 'float', 'float', 'float', 'float']
    table_name = 'energy_consump_preprocess'
    console = Console()
    with console.status("[bold green]Working on tasks...") as status:
        spark = SparkSession.builder.appName('DataPreprocessingEnergyConsumption').getOrCreate()
        df = pd.read_csv(url)
        spark_df = spark.createDataFrame(df)
        console.log("Successfully built Spark Dataframe")
        spark_df = ProcessingDateTime(spark, spark_df)
        console.log("Successfully processed datetime Column")
        spark_df = RenamingColumns(spark_df)
        console.log("Successfully renamed columns")
        spark_df = DatatypeConversion(spark_df, data_types)
        console.log("Successfully converted datatypes of the columns")
        pandas_df = spark_df.toPandas()
        console.log(print(pandas_df))
        console.log("Successfully converted spark df to pandas df")
        pandas_df = InterpolateDF(pandas_df)
        console.log("Successfully implemented interpolation")
        pandas_df = AddingActiveEnergy(pandas_df)
        console.log("Successfully added active energy column")
        pandas_df_rs = pandas_df.tail(5000)
#         IngesttoRedshift(pandas_df_rs, table_name)
        console.log("Successfully ingested data to redshift")
        # pandas_df.to_csv("energy_consump_preprocessed.csv")
        model = load_the_model(model_path)
        console.log("Successfully loaded ML Model")
        print(pandas_df)
        looper(pandas_df,model)
        console.log("Successfully Started Inferencing")
    #     print(pandas_df)

