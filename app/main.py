from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import ping
from app.api import query
from app.api import history
from app.api import result

from app.db.database import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await engine.dispose()


app = FastAPI(
    title="AutoSnab API",
    version="1.0.0",
    lifespan=lifespan,
)


app.include_router(ping.router)
app.include_router(query.router)
app.include_router(history.router)
app.include_router(result.router)
