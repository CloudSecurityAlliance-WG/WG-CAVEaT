#!/usr/bin/env python3

import csv
import json
import sys

def csv_to_json(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]

    with open(output_file, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python csv_to_json.py <input_csv_file> <output_json_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    csv_to_json(input_file, output_file)
    print(f"Successfully converted {input_file} to {output_file}")

    
