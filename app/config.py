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
    MONGO_USER: str = getenv("MONGO_USER")
    MONGO_PASSWORD: str = getenv("MONGO_PASSWORD")
    MONGO_HOST: str = getenv("MONGO_HOST", "localhost")
    MONGO_PORT: str = getenv("MONGO_PORT", "27017")
    DATABASE_NAME: str = getenv("DATABASE_NAME")
    DB_ARGS: str = getenv('DATABASE_ARGS', '?authSource=admin')
    BITA_GATEWAY_HOST: str = getenv('BITA_GATEWAY_HOST')
    SECRET_KEY_JWT: str = getenv('SECRET_KEY_JWT')
    

    @property
    def MONGO_URI(self):
        user = self.MONGO_USER
        pwd = self.MONGO_PASSWORD
        host = self.MONGO_HOST
        port = self.MONGO_PORT
        name = self.DATABASE_NAME
        args = self.DB_ARGS
        return f'mongodb://{user}:{pwd}@{host}:{port}/{name}{args}'

class Prod(Settings):
    NAME = 'prod'

class Dev(Settings):
    NAME = 'dev'
    DATABASE_NAME = getenv("DATABASE_NAME_DEV")

class Test(Settings):
    NAME = 'test'
    DATABASE_NAME = getenv("DATABASE_NAME_TEST")


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

settings: Settings = get_setting(getenv('ENV'))()
info = f'Setting selected: {settings.NAME}'
print(info)
print('=' * len(info))
