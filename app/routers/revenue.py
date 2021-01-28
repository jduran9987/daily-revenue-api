from sqlalchemy.orm import Session

from fastapi import Depends
from fastapi import APIRouter

from app.schemas import schemas
from app.routers.helpers import daily_revenue
from app.database.database import get_db
from app.security.security import authenticate_user

from datetime import date

router = APIRouter(
    dependencies=[Depends(authenticate_user)],
)


@router.get("/revenue/{date}", response_model=schemas.DailyRevenue)
def get_daily_revenue(date: date, db: Session = Depends(get_db)):
    return daily_revenue(date, db)
