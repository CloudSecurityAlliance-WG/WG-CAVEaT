#!/usr/bin/env python3

import json
import os
import argparse
from collections import defaultdict

def split_json_file(input_file):
    # Read the JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    # Extract the metadata
    metadata = data['metadata']
    
    # Create a defaultdict to group objects by capability_id
    grouped_objects = defaultdict(list)
    
    # Group mapping objects by capability_id
    for obj in data['mapping_objects']:
        capability_id = obj['capability_id']
        grouped_objects[capability_id].append(obj)
    
    # Process each group of objects
    for capability_id, objects in grouped_objects.items():
        # Create a new dictionary with metadata and the current group of objects
        new_data = {
            'metadata': metadata,
            'mapping_objects': objects
        }
        
        # Create a filename based on the capability_id
        filename = f"{capability_id}.json"
        
        # Write the new JSON file
        with open(filename, 'w') as f:
            json.dump(new_data, f, indent=4)
        
        print(f"Created file: {filename} with {len(objects)} entries")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Split a JSON file into multiple files based on capability_id, grouping entries with the same capability_id.")
    parser.add_argument("input_file", help="Path to the input JSON file")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call the split_json_file function with the input file
    split_json_file(args.input_file)

if __name__ == "__main__":
    main()
    
