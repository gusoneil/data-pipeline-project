import pandas as pd
import schedule
import time
from sqlalchemy import create_engine


def run_pipeline():
    print("Running data pipeline...")

    # Load and clean data
    df = pd.read_csv("data.csv")
    df.dropna(inplace=True)
    df.columns = df.columns.str.lower()
    df["name"] = df["name"].str.title()

    # Insert into database
    engine = create_engine("sqlite:///data_pipeline.db")
    df.to_sql("processed_data", engine, if_exists="append", index=False)

    print("Pipeline execution completed!")


# Schedule the pipeline to run every 1 minute
schedule.every(1).minutes.do(run_pipeline)

print("Pipeline is scheduled. Running every minute...")
while True:
    schedule.run_pending()
    time.sleep(1)
