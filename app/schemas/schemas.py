from pydantic import BaseModel

from datetime import date 


class DailyRevenue(BaseModel):
    transaction_date: date 
    revenue: float

    class Config:
        orm_mode = True
