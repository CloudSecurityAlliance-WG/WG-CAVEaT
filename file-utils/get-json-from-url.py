#!/usr/bin/env python3

#!/usr/bin/env python3

import argparse
import subprocess
import tempfile
import os
from urllib.parse import urlparse
from csa_ai_foundation_model_api_clients import FoundationModelAPIClient

def get_dom_from_url(url):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_name = temp_file.name
    chrome_command = f"google-chrome --no-sandbox --crash-dumps-dir=/tmp/www --disable-crash-reporter --headless --disable-gpu --enable-javascript --disable-3d-apis --dump-dom {url} > {temp_file_name}"
    subprocess.run(chrome_command, shell=True, check=True)
    with open(temp_file_name, 'r', encoding='utf-8') as file:
        dom_data = file.read()
    return dom_data

def get_output_filename_from_url(url, root_url):
    parsed_url = urlparse(url)
    parsed_root_url = urlparse(root_url)
    path = parsed_url.path.replace(parsed_root_url.path, '').strip('/')
    filename = path.replace('/', '-')
    if not filename:
        filename = 'index'
    return f"{filename}.json"

def main():
    parser = argparse.ArgumentParser(description="Extract data from a HTML page which is a DOM dump using Google Chrome headless and FoundationModelAPIClient.")
    parser.add_argument('url', type=str, help='The URL of the web page to process.')
    parser.add_argument('root_url', type=str, help='The root URL to be removed from the URL to create the output filename.')
    args = parser.parse_args()

    url = args.url
    root_url = args.root_url
    dom_data = get_dom_from_url(url)
    output_file = get_output_filename_from_url(url, root_url)

    model = 'chatgpt'
    system_prompt = "You are a helpful AI that takes HTML content (a dump of the Document Object Model or DOM from google chrome headless) and extracts data from it into a JSON format and then gives that back to the user. Do not include anything like ```json at the start, I just want raw JSON"
    user_prompt = "I want you to extract the data from the main section of the following HTML DOM document that I will include at the end of this prompt, put the information from the main part of the HTML DOM page into a JSON format and show me just the JSON and no other data. Make sure to include as much information as possible for each item in the JSON output, especially any URLs. The HTML DOM data is: "
    user_data = dom_data

    FoundationModelAPIClient(
        model=model,
        system_prompt=system_prompt,
        system_prompt_type="text",
        user_prompt=user_prompt,
        user_prompt_type="text",
        user_data=user_data,
        user_data_type="text",
        output_file=output_file
    )

if __name__ == "__main__":
    main()
