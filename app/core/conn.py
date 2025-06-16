#!/usr/bin/env python3
"""
When imported, this module will initialize the mongoengine connectino to
MongoDB using the desired URI
"""
from mongoengine import connect
from .config import settings

connect(
    host=settings.MONGO_URI,
    uuidRepresentation='standard',
)

from mongoengine.connection import get_db

db = get_db()
