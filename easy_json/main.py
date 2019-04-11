import json

def read(file_path):
    f = open(file_path, 'r')
    return json.load(f)

def write(file_path, list, indent = 2):
    f = open(file_path,'w')
    json.dump(list, f, indent = indent)
    f.close
