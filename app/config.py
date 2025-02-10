#!/usr/bin/env python3
from os import getenv
from abc import ABC
from typing import Any
from dotenv import load_dotenv
import sys

load_dotenv()


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
    DATABASE_NAME: str = getenv("DATABASE_NAME", "test_database")

    @classmethod
    @property
    def MONGO_URI(cls):
        return f"mongodb://{cls.MONGO_USER}:{cls.MONGO_PASSWORD}@{cls.MONGO_HOST}:{cls.MONGO_PORT}/{cls.DATABASE_NAME}?authSource=admin"

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

settings = get_setting(getenv('ENV'))
info = f'Setting selected: {settings.NAME}'
print(info)
print('=' * len(info))
