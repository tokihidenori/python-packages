import json

def read(file_path):
    f = open(file_path, 'r')
    return json.load(f)
