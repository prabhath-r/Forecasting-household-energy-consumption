import pyspark
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import to_timestamp
from pyspark.sql.functions import col, to_date
from pyspark.sql.functions import unix_timestamp, from_unixtime


def ProcessingDateTime(spark, spark_df):
    spark_df = spark_df
    spark_df.createOrReplaceTempView("energy")
    spark_df = spark.sql("SELECT CONCAT(Date,' ', Time) Datetime,* from energy")
    try:
        spark_df = spark_df.drop('Date','time')
    except Exception as e:
        print("Error occured in ProcessingDateTime() with Exception as ",e)
    return spark_df 
