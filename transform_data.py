import pandas as pd

# Load CSV data
df = pd.read_csv("data.csv")

# Drop rows with missing values
df.dropna(inplace=True)

# Convert column names to lowercase for consistency
df.columns = df.columns.str.lower()

# Convert names to title case
df["name"] = df["name"].str.title()

# Print cleaned data
print(df)
