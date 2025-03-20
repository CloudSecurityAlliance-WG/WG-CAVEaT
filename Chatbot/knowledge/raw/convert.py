#!/usr/bin/env python3

import csv
import sys

def csv_to_markdown(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        with open(output_file, 'w', encoding='utf-8') as mdfile:
            for row in csv_reader:
                # Use Control Title as the main heading
                mdfile.write(f"# {row['Control Title']}\n\n")
                
                # Add other fields as subheadings with their values
                mdfile.write(f"**Control Domain:** {row['Control Domain']}\n\n")
                mdfile.write(f"**Control ID:** {row['Control ID']}\n\n")
                mdfile.write(f"**Control Specification:**\n\n{row['Control Specification']}\n\n")
                
                # Add a horizontal rule to separate sections
                mdfile.write("---\n\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.csv output.md")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    csv_to_markdown(input_file, output_file)
    print(f"Conversion complete. Output saved to {output_file}")
    
