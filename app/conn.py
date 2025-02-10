#!/usr/bin/env python3
from mongoengine import connect
from app.config import settings

connect(
    host=settings.MONGO_URI,
    uuidRepresentation='standard',
)

from mongoengine.connection import get_db

db = get_db()
