from sqlalchemy import Table
from sqlalchemy.orm import relationship 

from app.database.database import engine, metadata, Base


class Customer(Base):
    __table__ = Table("customers", metadata, autoload=True, autoload_with=engine)


class Product(Base):
    __table__ = Table("products", metadata, autoload=True, autoload_with=engine)

    transactions = relationship("Transaction", back_populates="products")

class Store(Base):
    __table__ = Table("stores", metadata, autoload=True, autoload_with=engine)


class Transaction(Base):
    __table__ = Table("transactions", metadata, autoload=True, autoload_with=engine)

    products = relationship("Product", back_populates="transactions")


class Security(Base):
    __table__ = Table("security", metadata, autoload=True, autoload_with=engine)
    