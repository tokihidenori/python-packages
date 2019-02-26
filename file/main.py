import json

def load_json(file_path):
    f = open(file_path, 'r')
    return json.load(f)
