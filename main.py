
from fastapi import FastAPI
from database import engine, Base

from routers import tournament, category

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tournament.router)
app.include_router(category.router)
