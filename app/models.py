from sqlalchemy import Column, Integer, Date, Double, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)


class Farmer(Base):
    __tablename__ = 'farmers'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    farm_name = Column(String(100), nullable=False)
    address = Column(String(255))
    user = relationship("User", back_populates="farmer")


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Double)
    quantity = Column(Integer)
    validity = Column(Date)
    farmer_id = Column(Integer, ForeignKey('farmers.id'))
    farmer = relationship("Farmer", back_populates="products")


User.farmer = relationship("Farmer", uselist=False, back_populates="user")
Farmer.products = relationship("Product", back_populates="farmer")
