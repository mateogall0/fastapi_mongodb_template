#!/usr/bin/env python3
import pytest

def test_attrs_get():
    from app.config import settings
    assert settings.NAME == 'test'

def test_attrs_set():
    from app.config import settings
    with pytest.raises(AttributeError):
        settings.NAME = 'invalid'