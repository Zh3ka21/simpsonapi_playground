"""Configurational file."""

#import os
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext  # For hashing passwords

load_dotenv()  # Load environment variables from .env file

# TODO: Change to env
#DATABASE_URL = os.getenv("DATABASE_URL")
#SECRET_KEY = os.getenv("SECRET_KEY")

DATABASE_URL = "sqlite:///simpsons.sqlite3"
SECRET_KEY = "eeb88a89682e43c37c7f3fc28afd6036"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
