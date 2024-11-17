from http import HTTPStatus

from fastapi import HTTPException


class NotFoundException(HTTPException):
    '''
    Обработчик ошибки со статус-кодом "404"
    '''
    def __init__(self, detail: str) -> None:
        super().__init__(
            status_code=HTTPStatus.NOT_FOUND,
            detail=detail
        )


class BadRequestException(HTTPException):
    '''
    Обработчик ошибки со статус-кодом "400"
    '''
    def __init__(self, detail: str) -> None:
        super().__init__(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=detail
        )


class InternalServerException(HTTPException):
    '''
    Обработчик ошибки со статус-кодом "500"
    '''
    def __init__(self, detail: str) -> None:
        super().__init__(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=detail
        )


class NoContentException(HTTPException):
    '''
    Обработчик ошибки со статус-кодом "204"
    '''
    def __init__(self, detail: str) -> None:
        super().__init__(
            status_code=HTTPStatus.NO_CONTENT,
            detail=detail
        )


class UnprocessableEntityException(HTTPException):
    '''
    Обработчик ошибки со статус-кодом "422"
    '''
    def __init__(self, detail: str) -> None:
        super().__init__(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            detail=detail
        )


class ConflictException(HTTPException):
    '''
    Обработчик ошибки со статус-кодом "409"
    '''
    def __init__(self, detail: str) -> None:
        super().__init__(
            status_code=HTTPStatus.CONFLICT,
            detail=detail
        )
