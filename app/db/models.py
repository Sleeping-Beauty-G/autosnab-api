from datetime import datetime

from sqlalchemy import String, Boolean, DateTime, Integer, Float, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class RequestHistory(Base):
    __tablename__ = "request_history"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    cadastral_number: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True
    )

    latitude: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    longitude: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    result: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )