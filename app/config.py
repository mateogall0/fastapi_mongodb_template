#!/usr/bin/env python3
from abc import ABC
from typing import Any
from dotenv import load_dotenv
import sys

load_dotenv(override=True)
from os import getenv

class Settings(ABC):
    def __setattr__(self, name: str, value: Any) -> None:
        """
        Block setting attributes after initialization.
        """
        if name == "_attributes":
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"'{name}' is read-only!")
    NAME = 'abstract'
    MONGO_URI: str = getenv('MONGO_URI')
    BITA_GATEWAY_HOST: str = getenv('BITA_GATEWAY_HOST')

class Prod(Settings):
    NAME = 'prod'

class Dev(Settings):
    NAME = 'dev'
    MONGO_URI: str = getenv('MONGO_URI_DEV')

class Test(Settings):
    NAME = 'test'
    MONGO_URI: str = getenv('MONGO_URI_TEST')


def get_setting(name: str) -> Settings:
    if 'pytest' in sys.modules:
        return Test
    if not isinstance(name, str):
        raise TypeError('ENV must be a string')
    subclasses = Settings.__subclasses__()
    for subclass in subclasses:
        if subclass.NAME == name:
            return subclass
    raise ValueError(f"'{name}' config not found")

settings = get_setting(getenv('ENV'))
info = f'Setting selected: {settings.NAME}'
print(info)
print('=' * len(info))
