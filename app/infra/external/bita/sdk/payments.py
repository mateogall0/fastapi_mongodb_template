#!/usr/bin/env python3 
from .core import SDK
try:
    from ..schemas.payments import PaymentPreference
except ImportError:
    from schemas.payments import PaymentPreference



prefix='/forward/payments/preference'
class PaymentsSDK(SDK):
    async def create_service_payment_preference(self, data: dict):
        json = PaymentPreference(**data).model_dump(mode='json')
        print(self.prefix)
        res = await self._request('post', prefix, json=json)
        return res
