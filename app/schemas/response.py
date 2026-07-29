from pydantic import BaseModel


class QueryResponse(BaseModel):
    cadastral_number: str
    result: bool


class PingResponse(BaseModel):
    database: int