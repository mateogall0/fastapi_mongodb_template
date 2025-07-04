"""
Core exceptions that are raised from this layer.
These are intended to be catched on the controller layer to then raise an HTTP
exception.
"""

class CoreExceptions(Exception): 
    pass

class Conflict(CoreExceptions): 
    pass

class NotFound(CoreExceptions): 
    pass

class PreconditionFail(CoreExceptions): 
    pass

class Unexpected(CoreExceptions): 
    pass

class UserError(CoreExceptions): 
    pass

class Unauthorized(CoreExceptions): 
    pass

class NotEnoughAmount(CoreExceptions): 
    pass

class Timeout(CoreExceptions): 
    pass

class RateLimited(CoreExceptions): 
    pass

class Forbidden(CoreExceptions): 
    pass
