import re
import json
import os

def read_json(file_path):
    """
    Function to read a whole JSON file
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def write_json(file_path, data):
    """
    Function to read a whole JSON file
    """
    with open(file_path, 'w') as file:
        json.dump(data, file)

def is_valid_phone_number(phone_number):
    """
    Check if input string fits phone number formats
    """

    pattern = re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
    return pattern.match(phone_number)
