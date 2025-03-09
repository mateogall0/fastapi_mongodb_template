#!/usr/bin/env python3
from fastapi.middleware.cors import CORSMiddleware
import json
def _read_origins(path='origins.json'):
    with open(path, 'r') as f:
        j = json.loads(f.read())
        return j['allowed_origins']

args = {
    'middleware_class': CORSMiddleware,
    'allow_origins': _read_origins(),
    'allow_credentials': True,
    'allow_methods': ['*'],
    'allow_headers': ['*']
}