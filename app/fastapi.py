from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWSError, jwt
from passlib.context import CryptContext

SECRETE_KEY = "ba018d0acde64543d60a46cdfad5e0cd00306ed0b13bbb63992347815ac8ec1f"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_db = {
    "tim": {
        "username": "tim",
        "full_name": "Tim Russica",
        "email": "tim@gmail.com",
        "hashed_password": "",
        "disable": False
    }
}

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str or None = None

class User(BaseModel):
    username: str
    email: str or None = None
    fullname: str or None = None
    disable: bool or None = None

class UserInDB(User):
      hashed_password: str


app = FastAPI()

