#!/usr/bin/env python3
from pydantic import BaseModel, HttpUrl

class Item(BaseModel):
    title: str
    unit_price: float
    quantity: int
    currency_id: str
    description: str = ""


class BackUrls(BaseModel):
    success: str
    failure: str
    pending: str


class PaymentPreference(BaseModel):
    items: list[Item]
    back_urls: BackUrls
    auto_return: str = 'approved'