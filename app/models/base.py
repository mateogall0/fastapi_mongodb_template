#!/usr/bin/env python3
from mongoengine import Document

class Base(Document):
    meta = {
        'abstract': True,
        'timestamps': True,
    }
