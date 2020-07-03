"""Script to post csv into database"""
import pandas as pd
from sqlalchemy import create_engine

#File to read
FILE_TO_PUT_IN_DB = pd.read_csv('/location/of/file.csv')

#Converting column names to lower case 
FILE_TO_PUT_IN_DB.columns = [c.lower() for c in FILE_TO_PUT_IN_DB.columns]

#Postgres connection (make sure the port is exposed)
engine = create_engine('postgresql://postgres:postgres@ip_address:5432/db_name') # db_name should exist in postgres 


FILE_TO_PUT_IN_DB.to_sql("table_name", engine)
