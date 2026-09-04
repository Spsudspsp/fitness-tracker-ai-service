import secrets
from fastapi import Header, HTTPException
from starlette import status

from settings.config import settings


async def verify_service_key(x_service_key: str = Header(...),):
    if not secrets.compare_digest(x_service_key, settings.service_key):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid service key")
