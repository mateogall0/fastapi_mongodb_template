#!/usr/bin/env python3
import pytest


def test_utils():
    from app.utils import timer, DEBUG, compare_hash

@pytest.mark.asyncio
async def test_core():
    from app.core import bita