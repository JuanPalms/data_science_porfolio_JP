"""
This python module implements some functions to be used in the main.py file.
"""
import os
import yaml
import sys
import base64

CURRENT = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(CURRENT)

# Function to load yaml configuration file
def load_config(config_name):
    """
    Sets the configuration file path
    Args:
    config_name: Name of the configuration file in the directory
    Returns:
    Configuration file
    """
    with open(os.path.join(ROOT, config_name), encoding="utf-8") as conf:
        config = yaml.safe_load(conf)
    return config


# Function to encode the file to base64
def get_binary_file_downloader_html(bin_file, file_label='File'):
    """
    Generates a link allowing the data in a given file to be downloaded
    Args:  bin_file (str) -> Path to the file to be downloaded
            file_label (str) -> Label to be displayed on the download link (default: 'File')
    Returns: href (str) -> HTML link to download the file
    """
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{bin_file}">{file_label}</a>'
    return href
