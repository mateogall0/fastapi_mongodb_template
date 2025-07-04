#!/usr/bin/env python3
from .core import SDK


prefix = '/forward/emails'
class EmailSDK(SDK):
    async def send_email(self, recipients: list[str], html: str, subject: str):
        body = {
            'recipients': recipients,
            'html': html,
            'subject': subject,
        }
        res = await self._request('post', prefix, body)
        return res
    
    async def get_all_sent_emails(self):
        res = await self._request('get', prefix)
        return res