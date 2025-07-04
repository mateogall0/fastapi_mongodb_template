#!/usr/bin/env python3
import httpx, asyncio
from dotenv import load_dotenv
from os import getenv


class SDK:
    """
    This SDK class takes care of the refresh and access tokens connecting to
    the Bit-A gateway.
    """
    prefix='/'
    def __init__(self, host: str) -> None:
        self.host = host
        load_dotenv(override=True)
        self.access_token: str = getenv('BITA_SDK_INITAL_ACCESS_TOKEN')

    def _get_headers(self, include_access_token: bool):
        headers = {
            'Content-Type': 'application/json',
            'bita-agent': 'BitaSDK/1.0',
            'Accept': 'application/json',
        }
        if include_access_token:
            headers['Authorization'] = f'Bearer {self.access_token}'
        return headers

    async def _request(self, method: str, endpoint: str, json: dict = None,
                       include_access_token=True):
        url = f'{self.host}{endpoint}'

        async with httpx.AsyncClient() as client:
            headers = self._get_headers(include_access_token,)
            res = await client.request(
                method.upper(),
                url,
                json=json,
                headers=headers,
            )
            return res
