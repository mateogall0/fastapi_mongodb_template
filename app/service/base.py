from app.core.repositories import Repository
from app.core.usecases import Service


class CRUDService(Service):
    def __init__(self, repo: Repository):
        self.repo: Repository = repo

    async def create(self, data: dict):
        return await self.repo.create(data)

    async def get(self, id: str):
        return await self.repo.get_by_id(id)

    async def update(self, obj, data: dict):
        return await self.repo.update(obj, data)

    async def delete(self, obj):
        return await self.repo.delete(obj)

class SocketRequestService(Service):
    async def handshake(self, *ag, **kw) -> dict:
        return {'status': 'connected'}

    async def ping(self, *ag, **kw) -> dict:
        return {'status': 'pong'}

    async def handle(self, action: str, payload: dict, *ag, **kw) -> dict:
        action_s = str(action)
        if action is None or action_s == 'handle':
            return {'error': 'wrong action type'}
        method = getattr(self, action_s, None)
        if not method or not callable(method):
            return {'error': f'unknown action `{action}`'}
        return await method(payload)


class SocketSingleRoomService(Service):
    def __init__(self, room_handler) -> None:
        self.room = room_handler

    def connect(self, ws, doc):
        self.room.connect(ws, doc)

    def disconnect(self, ws):
        self.room.disconnect(ws)

    async def broadcast(self, payload: dict):
        self.room.broadcast(payload)

    async def message(self, doc, payload: dict):
        self.room.send_to_doc(doc, payload)
