import sqlalchemy as sa
from sqlalchemy import orm as sa_orm
from sqlalchemy import create_engine
from sqlalchemy.engine import url as sa_url

def IngesttoRedshift(pandas_df, table_name):
    try:
        # build the sqlalchemy URL
        url = sa_url.URL(
        drivername='postgresql+psycopg2', # indicate redshift_connector driver and dialect will be used
        host='dev-datarangers-final.cwmgpuwjy8xr.us-east-1.redshift.amazonaws.com', # Amazon Redshift host
        port='5439', # Amazon Redshift port
        database='dev', # Amazon Redshift database
        username='root', # Amazon Redshift username
        password='Datarangers4' # Amazon Redshift password
        )
        conn = create_engine(url)
        pandas_df['energy_cost'] = (pandas_df['active_energy']*0.126)/1000
        pandas_df.to_sql(table_name, conn, index=False, if_exists='replace')
    except Exception as e:
        print("Error occured in IngesttoRedshift() with Exception as ",e)
    return pandas_df