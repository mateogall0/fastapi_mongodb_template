import json

def read_origins(path='origins.json'):
    with open(path, 'r') as f:
        j = json.loads(f.read())
        return j['allowed_origins']

