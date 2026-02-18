import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("data/raw/flights.csv")

# Memory Optimization

# Downcast integers
int_cols = df.select_dtypes(include=['int64']).columns
for col in int_cols:
    df[col] = pd.to_numeric(df[col], downcast='integer')

# Downcast floats
float_cols = df.select_dtypes(include=['float64']).columns
for col in float_cols:
    df[col] = pd.to_numeric(df[col], downcast='float')


# Feature Engineering

# Create flight_date
df['flight_date'] = pd.to_datetime(df[['year', 'month', 'day']])

# Create day_of_week
df['day_of_week'] = df['flight_date'].dt.day_name()

# Create route
df['route'] = df['origin'] + "-" + df['dest']

# Create cancelled column
df['cancelled'] = df['dep_time'].isna().astype(int)

# Create on_time column
df['on_time'] = (df['arr_delay'] <= 0).astype(int)


# Cleaning

# Remove rows with missing arrival delay
df = df.dropna(subset=['arr_delay'])


# Save cleaned data

df.to_csv("data/processed/flights_clean.csv", index=False)

print("Preprocessing completed successfully.")
print("Final dataset shape:", df.shape)