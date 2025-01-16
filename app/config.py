#!/usr/bin/env python3
from os import getenv
from dotenv import load_dotenv
from abc import ABC
from typing import Any


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

    MONGO_URI: str = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{DATABASE_NAME}"

class Prod(Settings):
    NAME = 'prod'

class Dev(Settings):
    NAME = 'dev'
    DATABASE_NAME = getenv("DATABASE_NAME_DEV")

class Test(Settings):
    NAME = 'test'
    DATABASE_NAME = getenv("DATABASE_NAME_TEST")


def get_setting(name: str) -> Settings:
    if not isinstance(name, str):
        raise TypeError('ENV must be a string')
    subclasses = Settings.__subclasses__()
    for subclass in subclasses:
        if subclass.NAME == name:
            return subclass
    raise ValueError(f"'{name}' config not found")

settings = get_setting(getenv('ENV'))