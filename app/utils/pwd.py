#!/usr/bin/env python3
import bcrypt

def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def compare_hash(password: str, hashed: bytes):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)