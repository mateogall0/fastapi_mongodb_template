#!/usr/bin/env python3
"""
External core functionallities.
"""
from app.core.bita.sdk import BitaSDK
from .config import settings
from os import getenv
from app.utils import TEST

if getenv('BITA_SDK_INITAL_ACCESS_TOKEN') is None or TEST:
    bita = None
else:
    bita = BitaSDK(host=settings.BITA_GATEWAY_HOST)
