import os

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from api.v0 import parts
from dependencies.database import init_engine


if os.getenv("PYTEST_RUNNING") != "1":
    init_engine(os.getenv("DATABASE_URL"))

app = FastAPI(title="Part Manager")
app.include_router(parts.router)

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")