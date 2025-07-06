"""
Core exceptions that are raised from this layer.
These are intended to be catched on the controller layer to then raise an HTTP
exception.
"""

class CoreException(Exception):
    pass

class BadRequest(CoreException):
    pass

class Unauthorized(CoreException):
    pass

class Forbidden(CoreException):
    pass

class NotFound(CoreException):
    pass

class NotAcceptable(CoreException):
    pass

class Conflict(CoreException):
    pass

class PreconditionFailed(CoreException):
    pass

class Unprocessable(CoreException):
    pass

class FeatureNotImplemented(CoreException):
    pass

class PaymentRequired(CoreException):
    pass

class Timeout(CoreException):
    pass

class Teapot(CoreException):
    pass
