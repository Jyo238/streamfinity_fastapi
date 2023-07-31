from datetime import timedelta
from typing import Annotated

from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session,select
from fastapi import APIRouter, HTTPException,status
from fastapi import Depends

from streamfinity_fastapi.db import get_session
from streamfinity_fastapi.schemas.user_schema import User
from streamfinity_fastapi.schemas.token_schema import Token
from streamfinity_fastapi.security.hashing import create_access_token, verify_password

ACCESS_TOKEN_EXPIRE_MINUTES = 3000000
router = APIRouter(prefix="/token")
@router.post("/", response_model=Token)
def login_login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_session)):
    query = select(User).where(User.email == form_data.username)
    user : User | None = db.exec(query).first()
    if user is None:
        raise HTTPException(status_code=401, detail="Incorrect username or password",headers={"WWW-Authenticate": "Bearer"})
    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect username or password",headers={"WWW-Authenticate": "Bearer"})
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email},
                                       expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

def raise_401_exception():
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )