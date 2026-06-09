#!/usr/bin/env python3
import json
import os
print("Scanning folder for user data files...")
combined_data = []
for file_name in os.listdir('.'):
    if file_name.endswith('_info.json'):
        print(f"Found and adding: {file_name}")
        with open(file_name, 'r') as f:
            data = json.load(f)
            combined_data.append(data)
if not combined_data:
    print("No user data files (*_info.json) found!")
    exit()
output_file = "combined_people.json"
with open(output_file, 'w') as f:
    json.dump(combined_data, f, indent=4)
print(f"\nSuccess! Total profiles combined: {len(combined_data)}")
print(f"All data saved to {output_file}")
