import pytest


def test_utils():
    from app.infra.utils import timer, DEBUG

@pytest.mark.asyncio
async def test_core():
    from app.core.exceptions import Conflict
