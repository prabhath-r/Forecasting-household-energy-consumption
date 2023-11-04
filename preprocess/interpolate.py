import pandas as pd
def InterpolateDF(pandas_df):
    try:
        pandas_df_copy = pandas_df.copy()
        pandas_df['date'] = pd.to_datetime(pandas_df['date'])
        pandas_df.index = pandas_df['date']
        del pandas_df['date']
        pandas_df_interpolate = pandas_df.resample('1T').sum()
        columns = pandas_df_interpolate.columns.tolist()
        for i in columns:
            if i != "datetime":
                pandas_df_interpolate[i] = pandas_df_interpolate[i].interpolate()
        pandas_df = pandas_df_interpolate
        pandas_df = pandas_df.reset_index()
    except Exception as e:
        print("Error occured in InterpolateDF() with Exception as ",e)
    return pandas_df