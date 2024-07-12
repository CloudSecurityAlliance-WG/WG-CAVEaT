#!/usr/bin/env python3

import yaml
import json
import sys
import os
from datetime import date

def is_valid_yaml(yaml_file):
    try:
        with open(yaml_file, 'r') as y_file:
            yaml.safe_load(y_file)
        return True
    except yaml.YAMLError as e:
        print(f"Invalid YAML file: {e}")
        return False

def convert_yaml_to_json(yaml_file, json_file):
    def default_serializer(obj):
        if isinstance(obj, (date,)):
            return obj.isoformat()
        raise TypeError(f"Type {type(obj)} not serializable")

    try:
        with open(yaml_file, 'r') as y_file:
            yaml_content = yaml.safe_load(y_file)
        
        with open(json_file, 'w') as j_file:
            json.dump(yaml_content, j_file, indent=4, default=default_serializer)
        
        print(f"Successfully converted {yaml_file} to {json_file}")
    
    except Exception as e:
        print(f"Error converting file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_yaml_to_json.py <input_yaml_file> <output_json_file>")
        sys.exit(1)
    
    input_yaml_file = sys.argv[1]
    output_json_file = sys.argv[2]
    
    if not os.path.isfile(input_yaml_file):
        print(f"The file {input_yaml_file} does not exist.")
        sys.exit(1)
    
    if not is_valid_yaml(input_yaml_file):
        print(f"The file {input_yaml_file} is not a valid YAML file.")
        sys.exit(1)
    
    convert_yaml_to_json(input_yaml_file, output_json_file)
