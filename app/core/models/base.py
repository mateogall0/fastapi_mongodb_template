#!/usr/bin/env python3
from mongoengine import Document, DateTimeField, EmbeddedDocument
from datetime import datetime

class Base(Document):
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    meta = {
        'abstract': True,
    }

class BaseEmbedded(EmbeddedDocument):
    meta = {
        'abstract': True,
    }
