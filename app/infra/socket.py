from fastapi import WebSocket
from .db.models import BaseDoc

class SingleRoom:
    def __init__(self,):
        self.conns: dict[WebSocket, BaseDoc] = {}

    def connect(self, ws: WebSocket, doc: BaseDoc) -> None:
        self.conns[ws] = doc

    def disconnect(self, ws):
        self.conns.pop(ws, None)

    async def broadcast(self, payload: dict):
        for ws in self.conns:
            await ws.send_json(payload)

    async def send_to_doc(self, doc: BaseDoc, payload: dict) -> int:
        count = 0
        for ws, stored_doc in self.conns.items():
            if doc == stored_doc:
                count += 1
                await ws.send_json(payload)
        return count
