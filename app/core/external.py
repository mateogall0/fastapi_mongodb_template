#!/usr/bin/env python3
from app.core.bita.sdk import BitaSDK
from app.config import settings
from os import getenv

if getenv('BITA_SDK_INITAL_REFRESH_TOKEN') is None:
    bita = None
else:
    bita = BitaSDK(host=settings.BITA_GATEWAY_HOST)
