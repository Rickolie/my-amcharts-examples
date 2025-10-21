# 📁 Load and correct column names in original datalog
import pandas as pd

# Define file paths
csv_dataLog = '/content/original.csv'
output_filename = '/content/dataLog_CorrectedNames.csv'

# Define the corrected column names
corrected_columns = [
    'SeqNo', 'Date', 'UTC Time',
    '[°C*10] LCC_CABINET_TEMP', '[°C*10] LCC_CABINET_HUM', '[%] LCC_UPS_BATT_LVL',
    '[bar] HPU_SYSTEM_PRESSURE', '[°C*10] HPU_OIL_TEMPERATURE', '[rpm] HPU_MOTOR_SPEED',
    '[W] HPU_MOTOR_POWER', '[V] BATTERIES_VOLTAGE', '[A*10] BATTERIES_CURRENT',
    '[kWh] BATTERIES_CAPACITY', '[%] BATTERIES_SOC', '[A*10] CHARGER_CURRENT',
    'FRONT_LINKS_UL_POS', 'FRONT_LINKS_UL_SPEED', 'FRONT_LINKS_UL_VALVE',
    'FRONT_LINKS_UR_POS', 'FRONT_LINKS_UR_SPEED', 'FRONT_LINKS_UR_VALVE',
    'FRONT_LINKS_LL_POS', 'FRONT_LINKS_LL_SPEED', 'FRONT_LINKS_LL_VALVE',
    'FRONT_LINKS_LR_POS', 'FRONT_LINKS_LR_SPEED', 'FRONT_LINKS_LR_VALVE',
    '[°*10] TUGGER ROTATION', '[°/s*100] TUGGER ROTATION SPEED',
    '[bar] TUGGER PRESSURE A', '[bar] TUGGER PRESSURE B', '[bar] TUGGER PRESSURE BRAKE',
    '[%] TUGGER VALVE', '[mm] COG LEFT POSITION', '[mm*100] COG LEFT SPEED',
    '[bar] COG LEFT BOTTOMSIDE PRESSURE', '[bar] COG LEFT RODSIDE PRESSURE',
    '[mm] COG RIGHT POSITION', '[mm*100] COG RIGHT SPEED',
    '[bar] COG RIGHT BOTTOMSIDE PRESSURE', '[bar] COG RIGHT RODSIDE PRESSURE',
    '[%] COG VALVE FEEDBACK'
]

# Optional: Print expected column count
print(f"📊 Expecting {len(corrected_columns)} columns in each row.")

# Read and manually parse the CSV
parsed_data = []
with open(csv_dataLog, 'r') as file:
    next(file)  # Skip header
    for line_num, line in enumerate(file, start=2):
        values = line.strip().split(',')
        if len(values) == len(corrected_columns):
            parsed_data.append(values)
        else:
            print(f"⚠️ Line {line_num} skipped (found {len(values)} values): {line.strip()}")

# Create DataFrame with corrected column names
df_corrected = pd.DataFrame(parsed_data, columns=corrected_columns)

# Save to new CSV
df_corrected.to_csv(output_filename, index=False)

# Display preview
print(f"✅ Corrected data saved to {output_filename}")
print(df_corrected.head())
