from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_session
from app.db.models import RequestHistory


router = APIRouter(
    prefix="/history",
    tags=["History"]
)


@router.get("")
async def get_history(
    cadastral_number: Optional[str] = None,
    session: AsyncSession = Depends(get_session),
):
    query = select(RequestHistory)

    if cadastral_number:
        query = query.where(
            RequestHistory.cadastral_number == cadastral_number
        )

    result = await session.execute(query)

    history = result.scalars().all()

    return history