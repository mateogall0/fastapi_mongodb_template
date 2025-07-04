#!/usr/bin/env python3
from .core import SDK

prefix='/forward/files'
class FilesSDK(SDK):
    def _connect_files_container(self, res):
        if res.status_code not in [200, 201]:
            raise ValueError(f'container not found or created correctly: {res.status_code}')
        self.files_container_id = res.json()['_id']

    async def connect_files_container(self, container_id: str):
        res = await self._request('get', f'{prefix}/{container_id}')
        self._connect_files_container(res)
        return res
    
    async def create_files_container(self):
        res = await self._request('post', prefix)
        self._connect_files_container(res)
        return res