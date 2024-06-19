from sqlalchemy import Column, Integer, Date, Double, String, ForeignKey, Float, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Address(Base):
    __tablename__ = 'addresses'

    postalCode = Column(Integer, primary_key=True)
    city = Column(String(100), nullable=False)
    street = Column(String(100), nullable=False)
    houseNumber = Column(String(100), nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(200), unique=False, nullable=False)
    phoneNumber = Column(String(15), unique=False, nullable=False)
    region = Column(String(50), nullable=False)

    postalCode = Column(Integer, ForeignKey('addresses.postalCode'))
    address = relationship("Address")


class Farmer(Base):
    __tablename__ = 'farmers'

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")


class Deliveryman(Base):
    __tablename__ = 'deliverymen'

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")


class ProductDetail(Base):
    __tablename__ = 'productDetails'

    sku = Column(String(5), primary_key=True)
    name = Column(String(150), unique=True)
    imageName = Column(String(150), nullable=False)
    price = Column(Double)
    category = Column(String(50))


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    quantity = Column(Integer)
    validity = Column(Date)

    farmer_id = Column(Integer, ForeignKey('farmers.id'))
    farmer = relationship("Farmer")

    sku = Column(String(5), ForeignKey('productDetails.sku'))
    productDetail = relationship("ProductDetail")


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    total_price = Column(Double, nullable=False)
    order_date = Column(DateTime, default=func.now())

    items = relationship("OrderItem", back_populates="order")

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User")


class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True)
    product_name = Column(String(150), nullable=False)
    product_price = Column(Double, nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Double, nullable=False)

    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    order = relationship("Order", back_populates="items")

    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    product = relationship("Product")
