def RenamingColumns(spark_df):
    try:
        columns = spark_df.columns
        for value in columns:
            spark_df = spark_df.withColumnRenamed(value, value.replace(" ","_").lower()) 
    except Exception as e:
        print("Error occured in RenamingColumns() with Exception as ",e)
    return spark_df