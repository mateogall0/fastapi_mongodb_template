#!/usr/bin/env python3
from app.core.bita.sdk import BitaSDK
from app.config import settings

# Bit-A SDK declaration
bita = BitaSDK(host=settings.BITA_GATEWAY_HOST)