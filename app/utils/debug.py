from app.infra.config import settings
import time
from inspect import currentframe, getfile

DEBUG_ENV_NAMES = ['dev', 'test']
DEBUG = settings.NAME in DEBUG_ENV_NAMES
TEST = settings.NAME == 'test'


def timer(func):
    """
    Time measurer using this wrapper. Takes the time right before executing
    the method and right after and substracts them to get the time it took to
    execute the method.

    Usage:
        ```
        @timer
        def method(self, user):
            pass
        ```
    """
    def wrapper(*ag, **kw):
        if not DEBUG:
            return func(*ag, **kw)
        start = time.time()
        result = func(*ag, **kw)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

def print_debug(key='Print debug', value=None, separator='=',
                end='\n\n') -> None:
    """
    Print big values of types like dictionaries with keys tp ease debugging
    process.
    """
    if not DEBUG:
        return
    frame = currentframe().f_back
    file_name = getfile(frame)
    line_number = frame.f_lineno
    text = f'{key} at {file_name}:{line_number}'
    print(text)
    print(separator * len(text))
    print(value, end=end)
