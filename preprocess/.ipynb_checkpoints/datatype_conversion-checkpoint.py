from pyspark.sql.functions import to_timestamp
from pyspark.sql.functions import col, to_date
from pyspark.sql.functions import unix_timestamp, from_unixtime

def DatatypeConversion(spark_df, data_types):
    try:
        columns = spark_df.columns
        for index,value in enumerate(columns):
            if data_types[index] == "float":
                spark_df = spark_df.withColumn(value, col(value).cast("float"))
            if data_types[index] == "datetime":
                spark_df = spark_df.select("*", from_unixtime(unix_timestamp(value, 'MM-dd-yyyy hh:mm:ss')).alias('date'))
                spark_df = spark_df.drop(value)
    except Exception as e:
        print("Error occured in DatatypeConversion() with Exception as ",e)
    return spark_df