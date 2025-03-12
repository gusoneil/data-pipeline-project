import sqlite3

# Connect to SQLite database (or create one if it doesn’t exist)
conn = sqlite3.connect("data_pipeline.db")
cursor = conn.cursor()

# Create a table (if it doesn’t exist)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS processed_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        city TEXT
    )
"""
)

# Commit and close connection
conn.commit()
conn.close()

print("Database setup completed successfully!")
