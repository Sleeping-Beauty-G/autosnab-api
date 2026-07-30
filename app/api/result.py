from fastapi import APIRouter
from pydantic import BaseModel
import random


router = APIRouter(prefix="/result", tags=["Result"])


class ExternalRequest(BaseModel):
    cadastral_number: str
    latitude: float
    longitude: float


class ExternalResponse(BaseModel):
    result: bool


@router.post("", response_model=ExternalResponse)
async def get_external_result(request: ExternalRequest):
    """
    Эмуляция внешнего сервера.
    Сервер обрабатывает запрос и возвращает true/false.
    """

    return ExternalResponse(result=random.choice([True, False]))
