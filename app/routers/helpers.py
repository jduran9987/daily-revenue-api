from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database.models import Transaction, Product

from datetime import date 


def daily_revenue(date: date, db: Session):
    revenue = db.query(
        Transaction.transaction_date, func.sum(Product.price).label("revenue")
    ).join(
        Transaction.products
    ).filter(
        Transaction.transaction_date == date
    ).group_by(
        Transaction.transaction_date
    ).first()
    if not revenue:
        return False
    return revenue 
