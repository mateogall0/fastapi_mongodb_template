from enum import Enum


class TokenType(str, Enum):
    SESSION = 'session'
    REFRESH = 'refresh'
