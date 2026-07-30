from fastapi import APIRouter

from sqlalchemy import text

from app.db.database import engine


router = APIRouter(prefix="/ping", tags=["Ping"])


@router.get("")
async def ping():
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))

        value = result.scalar()

    return {"database": value}
