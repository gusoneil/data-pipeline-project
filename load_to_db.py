import pandas as pd
from sqlalchemy import create_engine

# Load and clean CSV data
df = pd.read_csv("data.csv")
df.dropna(inplace=True)
df.columns = df.columns.str.lower()
df["name"] = df["name"].str.title()

# Create a database connection
engine = create_engine("sqlite:///data_pipeline.db")

# Load data into SQL table
df.to_sql("processed_data", engine, if_exists="append", index=False)

print("Data successfully inserted into the database!")
