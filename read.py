#!/usr/bin/env python3
import json
import os
input_file = "combined_people.json"
if not os.path.exists(input_file):
    print(f"Error: {input_file} not found! Run merge.py first.")
    exit()
with open(input_file, 'r') as file:
    people = json.load(file)
print(f"--- Total Profiles Found: {len(people)} ---\n")
for index, user in enumerate(people, start=1):
    print(f" Profile #{index}")
    print(f"  Name:   {user.get('name')}")
    print(f"  Age:    {user.get('age')}")
    print(f"  Gender: {user.get('gender')}")
    print(f"  Place:  {user.get('place')}")
    print(f"  Likes it: {user.get('likes it')}")
    print("-" * 30)
