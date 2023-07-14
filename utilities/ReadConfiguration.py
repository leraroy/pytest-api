import json
from configparser import ConfigParser

def read_configurations(category, key):
    config = ConfigParser()
    config.read("configurations/config.ini")
    return config.get(category, key)

def get_base_url():
    return read_configurations("basic", "base_url")

def get_headers():
    return json.loads(read_configurations("basic", "headers"))