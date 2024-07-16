from passlib.context import CryptContext
from pydantic import EmailStr


def pwd_contex_hasher():
    pwd_context_hash = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context_hash

def hash_password(password: EmailStr):
    pwd_context = pwd_contex_hasher()
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    pwd_context = pwd_contex_hasher()
    return pwd_context.verify(plain_password, hashed_password)