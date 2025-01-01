from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from .config import Settings

settings = Settings()
DATABASE_URL = settings.DATABASE_URL

# Create async engine
engine = create_async_engine(DATABASE_URL, future=True, echo=True)

# Create session factory
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# Dependency for creating a session
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
