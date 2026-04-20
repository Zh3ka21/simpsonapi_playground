"""Configurational file."""

import os
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

load_dotenv()

DATABASE_URL: str = os.getenv("DATABASE_URL") or ""
SECRET_KEY: str = os.getenv("SECRET_KEY") or ""

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY environment variable is not set")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
