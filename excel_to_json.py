import os
import pandas as pd
import subprocess
import sys

# === CONFIGURE YOUR FILE PATH HERE ===
file_path = r'C:\Users\Lemuel\Documents\Search\data.xlsx'  # or .csv

# === Auto-detect file type ===
file_ext = os.path.splitext(file_path)[1].lower()

# === Check if the file exists ===
if not os.path.exists(file_path):
    print(f"❌ File not found at: {file_path}")
    sys.exit()

try:
    # === Read based on extension ===
    if file_ext == '.xlsx':
        df = pd.read_excel(file_path, engine='openpyxl')  # Excel file
    elif file_ext == '.csv':
        df = pd.read_csv(file_path)  # CSV file
    else:
        print("❌ Unsupported file format. Please use .xlsx or .csv")
        sys.exit()

    # === Convert to JSON ===
    json_data = df.to_json(orient='records', indent=2)
    output_path = os.path.join(os.path.dirname(file_path), 'names.json')

    # === Save to JSON file ===
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(json_data)

    print("✅ File converted to JSON successfully!")
    print(f"📄 JSON saved as: {output_path}")

    # === Open in Notepad (Windows only) ===
    subprocess.Popen(['notepad.exe', output_path])

except Exception as e:
    print(f"❌ An error occurred:\n{e}")
