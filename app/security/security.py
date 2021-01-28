from app.database.database import get_db
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from sqlalchemy.orm import Session

from passlib.context import CryptContext

from app.database.models import Security

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

security = HTTPBasic()


def verify_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password)


def authenticate_user(db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(security)):
    user = db.query(Security).filter(Security.username == credentials.username).first()
    if not user or not verify_password(credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"}
        )
