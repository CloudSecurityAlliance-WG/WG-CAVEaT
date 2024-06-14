#!/usr/bin/env python3

import sys
import os
from bs4 import BeautifulSoup, Comment

def read_html_file(file_path):
    encodings = ['utf-8', 'windows-1252', 'iso-8859-1']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            continue
    raise ValueError(f"Failed to decode {file_path} with any of the specified encodings")

def clean_html(input_file, output_dir):
    # Read the input HTML file using the function with encoding fallback
    html_content = read_html_file(input_file)
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove unwanted attributes
    for tag in soup.find_all():
        for attribute in ["class", "style", "lang"]:
            if attribute in tag.attrs:
                del tag[attribute]

    # Remove all comments
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    for comment in comments:
        comment.extract()

    # Remove all style tags
    for style_tag in soup.find_all('style'):
        style_tag.decompose()

    # Normalize whitespace in text nodes
    for element in soup.find_all(text=True):
        normalized_text = ' '.join(element.split())
        element.replace_with(normalized_text)

    # Unwrap all span tags
    for span in soup.find_all('span'):
        span.unwrap()

    # Add a newline after specific tags to maintain readability
    tags_to_break = ['p', 'td', 'tr']  # Specify more tags as needed
    for tag_name in tags_to_break:
        for tag in soup.find_all(tag_name):
            next_sibling = tag.next_sibling
            # Only append newline if there's not already one
            if not (next_sibling and isinstance(next_sibling, str) and next_sibling.startswith('\n')):
                tag.insert_after('\n')

    # Remove empty paragraphs and other empty tags
    empty_tags = ['p', 'b', 'span']  # Add other tags as needed
    for tag_name in empty_tags:
        for tag in soup.find_all(tag_name):
            if not tag.text.strip():  # Checks if there is no text inside
                tag.decompose()

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Determine output file path
    output_file = os.path.join(output_dir, os.path.basename(input_file))

    # Write the cleaned HTML to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(str(soup))

    print(f"Cleaned HTML has been saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py --input input_file.html --output output_directory")
        sys.exit(1)

    # Map command line arguments to variables
    input_index = sys.argv.index('--input') + 1
    output_index = sys.argv.index('--output') + 1
    input_file = sys.argv[input_index]
    output_dir = sys.argv[output_index]

    # Run the clean up process
    clean_html(input_file, output_dir)

    
