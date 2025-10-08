#Load and prepare datalog correctednames.csv
#file is temporarily stored within browser environment
csv_dataLog = '/content/original.csv'

# Load the CSV file
df_dataLog = pd.read_csv(csv_dataLog)

# Create a new column named datetime by combining 'Date' and 'UTC Time'
# Handle potential errors by coercing invalid parsing to NaT
df_dataLog['datetime'] = pd.to_datetime(df_dataLog['Date'].astype(str) + ' ' + df_dataLog['UTC Time'].astype(str), errors='coerce')

# Drop any rows where the datetime column is NaT
df_dataLog.dropna(subset=['datetime'], inplace=True)

# Drop the original 'Date' and 'UTC Time' columns
df_dataLog = df_dataLog.drop(columns=['Date', 'UTC Time'])

# Reorder the columns so that the datetime column is the first column
cols = df_dataLog.columns.tolist()
# Find the index of 'datetime'
datetime_index = cols.index('datetime')
# Move 'datetime' to the first position
cols.insert(0, cols.pop(datetime_index))
df_dataLog = df_dataLog[cols]

# Display the head of the resulting DataFrame to verify
display(df_dataLog.head())
