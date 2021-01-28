from fastapi import FastAPI

from app.routers import revenue

app = FastAPI()

app.include_router(revenue.router)