import pandas as pd
def SparkDFtoPandasDF(spark_df):
    try:
        pandas_df = spark_df.toPandas()
    except Exception as e:
        print("Error occured in SparkDFtoPandasDF() with Exception as ",e)
    return pandas_df