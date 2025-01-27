import hmac
import hashlib
import time
import os
from fastapi import FastAPI, Request, HTTPException
from backend.db import engine
from backend.models.user import Base
from backend.routers import user
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("API_TOKEN")

if not TELEGRAM_BOT_TOKEN:
	raise RunTimeError("API_TOKEN is not set in the env variables")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/ping")
async def ping():
    return {"status": "Backend is running!"}

@app.get("/auth/telegram")
async def auth_telegram(request: Request):
    # Extract query parameters from the Telegram widget
    query = dict(request.query_params)
    hash_check = query.pop("hash", None)
    if not hash_check:
        raise HTTPException(status_code=400, detail="Missing hash parameter")

    # Construct data-check-string
    data_check_string = "\n".join(
        [f"{key}={value}" for key, value in sorted(query.items())]
    )

    # Verify hash
    secret_key = hashlib.sha256(TELEGRAM_BOT_TOKEN.encode()).digest()
    calculated_hash = hmac.new(
        secret_key, data_check_string.encode(), hashlib.sha256
    ).hexdigest()
    if calculated_hash != hash_check:
        raise HTTPException(status_code=400, detail="Invalid hash")

    # Verify timestamp to prevent outdated data
    auth_date = int(query.get("auth_date", 0))
    if auth_date < time.time() - 86400:  # 1 day expiration
        raise HTTPException(status_code=400, detail="Outdated authentication")

    # Process user data
    user_data = {
        "id": query["id"],
        "first_name": query.get("first_name"),
        "last_name": query.get("last_name"),
        "username": query.get("username"),
        "photo_url": query.get("photo_url"),
    }

    return {"status": "success", "user": user_data}

app.include_router(user.router)
