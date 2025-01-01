from fastapi import FastAPI
from .db import engine
from .models.user import Base
from .routers import user

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/ping")
async def ping():
    return {"status": "Backend is running!"}

# Include the user router
app.include_router(user.router)
