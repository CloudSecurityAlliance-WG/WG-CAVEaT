#!/usr/bin/env python3

import json
import sys
from jsondiff import diff

if len(sys.argv) != 3:
    print("Usage: python compare_json.py file1.json file2.json")
    sys.exit(1)

file1_path = sys.argv[1]
file2_path = sys.argv[2]

try:
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        json1 = json.load(file1)
        json2 = json.load(file2)
        
    differences = diff(json1, json2)
    
    if differences:
        print("Differences found:")
        print(json.dumps(differences, indent=4))
    else:
        print("No differences found.")
except Exception as e:
    print(f"Error: {e}")
    
