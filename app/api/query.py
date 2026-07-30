from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_session
from app.db.models import RequestHistory

from app.schemas.request import QueryRequest
from app.schemas.response import QueryResponse

from app.services.external import send_external_request


router = APIRouter(prefix="/query", tags=["Query"])


@router.post("", response_model=QueryResponse)
async def create_query(
    data: QueryRequest,
    session: AsyncSession = Depends(get_session),
):

    result = await send_external_request(
        cadastral_number=data.cadastral_number,
        latitude=data.latitude,
        longitude=data.longitude,
    )

    history = RequestHistory(
        cadastral_number=data.cadastral_number,
        latitude=data.latitude,
        longitude=data.longitude,
        result=result,
    )

    session.add(history)
    await session.commit()
    await session.refresh(history)

    return {
        "cadastral_number": data.cadastral_number,
        "result": result,
    }
