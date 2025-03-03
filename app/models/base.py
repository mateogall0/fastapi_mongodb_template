#!/usr/bin/env python3
from mongoengine import Document, DateTimeField, EmbeddedDocument
from datetime import datetime

class Base(Document):
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
    meta = {
        'abstract': True,
    }

class BaseEmbedded(EmbeddedDocument):
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
    meta = {
        'abstract': True,
    }