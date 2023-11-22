# Import required modules
import os
import pandas as pd
import pymysql
from sqlalchemy import create_engine
import dotenv
dotenv.load_dotenv()


# Load the dataset into a pandas DataFrame
dataset_path = "earthquake_data.csv"
df = pd.read_csv(dataset_path)

# Connect to MySQL database and push data into the table
username = os.environ['db_username']
password = os.environ['db_password']
database_name = os.environ['database_name']
table_name = "neic_earthquakes"

url  = f"mysql+pymysql://{username}:{password}@localhost/{database_name}"
engine = create_engine(url)
df.to_sql(table_name, con=engine, if_exists='replace', index=False)
