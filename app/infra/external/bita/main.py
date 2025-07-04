#!/usr/bin/env python3
from sdk import BitaSDK
import asyncio

async def main():
    #url = 'https://gateway-939307440735.us-central1.run.app/'
    url = 'http://localhost:8000'
    sdk = BitaSDK(url)
    await asyncio.sleep(1)
    a = await sdk.send_email(['mateogesede@gmail.com'], 'holi', 'jeje')
    print(a.content)
    print(a)


asyncio.run(main())
