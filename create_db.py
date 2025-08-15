import sqlite3
import pandas as pd
import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "db", "food.db")

# Create db folder if it doesn't exist
os.makedirs(os.path.join(BASE_DIR, "db"), exist_ok=True)

# Connect to SQLite DB
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create tables
cursor.executescript("""
CREATE TABLE IF NOT EXISTS providers (
  provider_id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  type TEXT,
  address TEXT,
  city TEXT,
  contact TEXT
);

CREATE TABLE IF NOT EXISTS receivers (
  receiver_id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  type TEXT,
  city TEXT,
  contact TEXT
);

CREATE TABLE IF NOT EXISTS food_listings (
  food_id INTEGER PRIMARY KEY,
  food_name TEXT NOT NULL,
  quantity INTEGER,
  expiry_date DATE,
  provider_id INTEGER,
  provider_type TEXT,
  location TEXT,
  food_type TEXT,
  meal_type TEXT,
  FOREIGN KEY(provider_id) REFERENCES providers(provider_id)
);

CREATE TABLE IF NOT EXISTS claims (
  claim_id INTEGER PRIMARY KEY,
  food_id INTEGER,
  receiver_id INTEGER,
  status TEXT,
  timestamp DATETIME,
  FOREIGN KEY(food_id) REFERENCES food_listings(food_id),
  FOREIGN KEY(receiver_id) REFERENCES receivers(receiver_id)
);
""")

# Load CSVs
providers_df = pd.read_csv('data/providers_data.csv')
receivers_df = pd.read_csv('data/receivers_data.csv')
food_listings_df = pd.read_csv('data/food_listings_data.csv')
claims_df = pd.read_csv('data/claims_data.csv')

# Import into SQLite
providers_df.to_sql('providers', conn, if_exists='replace', index=False)
receivers_df.to_sql('receivers', conn, if_exists='replace', index=False)
food_listings_df.to_sql('food_listings', conn, if_exists='replace', index=False)
claims_df.to_sql('claims', conn, if_exists='replace', index=False)

conn.close()

print("Database created and CSV data loaded successfully.")
