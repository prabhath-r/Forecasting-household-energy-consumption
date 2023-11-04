def AddingActiveEnergy(pandas_df):
    try:
        pandas_df['active_energy'] = (pandas_df['global_active_power']*1000/60 - pandas_df['sub_metering_1'] - pandas_df['sub_metering_2'] - pandas_df['sub_metering_3'])
    except Exception as e:
        print("Error occured in AddingActiveEnergy() with Exception as ",e)
    return pandas_df