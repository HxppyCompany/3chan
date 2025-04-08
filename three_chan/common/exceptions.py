from typing import cast
from fastapi import Request, status
from fastapi.responses import JSONResponse


class AppException(Exception):
    def __init__(self, status_code: int, details: str):
        self.__status_code = status_code
        self.__details = details

    @property
    def status_code(self):
        return self.__status_code

    @property
    def details(self):
        return self.__details


class NotFoundException(AppException):
    def __init__(self, details: str | None = None):
        super().__init__(
            status.HTTP_404_NOT_FOUND,
            "Entity was not found" if details is None else None
        )


class EntityAlreadyExistException(AppException):
    def __init__(self, details: str | None = None):
        super().__init__(
            status.HTTP_409_CONFLICT,
            "Entity already exist" if details is None else None
        )

def app_exception_handler(request: Request, exception: Exception):
    exc = cast(AppException, exception)
    return JSONResponse(
        status_code=exc.status_code,
        content={"details": exc.details},
    )
