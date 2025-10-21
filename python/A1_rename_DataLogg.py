# Load and prepare datalog correctednames.csv
import pandas as pd

# Path to the uploaded CSV file
csv_dataLog = '/content/original.csv'

# Load the CSV file with better memory handling
df_dataLog = pd.read_csv(csv_dataLog, low_memory=False)

# Optional: Print column names for debugging
print("📋 Columns in CSV:", df_dataLog.columns.tolist())

# Try to create a new 'datetime' column by combining 'Date' and 'UTC Time'
try:
    df_dataLog['datetime'] = pd.to_datetime(
        df_dataLog['Date'].astype(str) + ' ' + df_dataLog['UTC Time'].astype(str),
        errors='coerce'
    )
except Exception as e:
    raise ValueError(f"❌ Failed to parse datetime: {e}")

# Drop rows where datetime parsing failed
df_dataLog.dropna(subset=['datetime'], inplace=True)

# Drop the original 'Date' and 'UTC Time' columns if they exist
for col in ['Date', 'UTC Time']:
    if col in df_dataLog.columns:
        df_dataLog.drop(columns=[col], inplace=True)

# Reorder columns to place 'datetime' first
if 'datetime' in df_dataLog.columns:
    cols = df_dataLog.columns.tolist()
    cols.insert(0, cols.pop(cols.index('datetime')))
    df_dataLog = df_dataLog[cols]
else:
    raise ValueError("❌ 'datetime' column missing after parsing. Check 'Date' and 'UTC Time' formatting.")

# Save the corrected CSV
df_dataLog.to_csv('/content/corrected.csv', index=False)

# Display the head of the resulting DataFrame
print("✅ Preview of corrected data:")
print(df_dataLog.head())
