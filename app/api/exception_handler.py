from fastapi import FastAPI, HTTPException, Request
from app.core.exceptions import (Conflict, CoreException, BadRequest,
                                 Unauthorized, Forbidden, NotFound,
                                 NotAcceptable, PreconditionFailed,
                                 NotImplemented, PaymentRequired, Timeout,
                                 Teapot, Unprocessable,)


exc_to_status= {
    BadRequest: 400,
    Unauthorized: 401,
    PaymentRequired: 402,
    Forbidden: 403,
    NotFound: 404,
    NotAcceptable: 406,
    Timeout: 408,
    Conflict: 409,
    PreconditionFailed: 412,
    Teapot: 418,
    Unprocessable: 422,
    NotImplemented: 501,
}

def register_exceptions(app: FastAPI):
    @app.exception_handler(CoreException)
    async def generic_exception_handler(request: Request, exc: CoreException):
        status = exc_to_status.get(type(exc), None)
        if status is None:
            raise exc
        raise HTTPException(status, detail=str(exc))
