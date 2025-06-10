from sqlalchemy import Integer, String, Date, Float, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    age: Mapped[int] = mapped_column(Integer)
    gender: Mapped[str] = mapped_column(String)
    signup_date: Mapped[Date] = mapped_column(Date)
    preferences: Mapped[str] = mapped_column(String)

class Product(Base):
    __tablename__ = "products"
    item_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    category: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    subcategory: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Float)
    avg_rating: Mapped[float] = mapped_column(Float)
    num_ratings: Mapped[int] = mapped_column(Integer)
    popular: Mapped[float] = mapped_column(Float)
    new_arrival: Mapped[float] = mapped_column(Float)
    on_sale: Mapped[float] = mapped_column(Float)
    arrival_date: Mapped[Date] = mapped_column(Date)

class Feedback(Base):
    __tablename__ = "feedback"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.item_id"))
    rating: Mapped[float] = mapped_column(Float)
    comment: Mapped[str] = mapped_column(String, nullable=True)

class CartItem(Base):
    __tablename__ = "cart_items"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.item_id"))
    quantity: Mapped[int] = mapped_column(Integer)

class Order(Base):
    __tablename__ = "orders"
    order_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    total_amount: Mapped[float] = mapped_column(Float)
    order_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    status: Mapped[str] = mapped_column(String)

class WishlistItem(Base):
    __tablename__ = "wishlist"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.item_id"))

class Login(Base):
    __tablename__ = "logins"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), unique=True)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)

class Interactions(Base):
    __tablename__ = "interactions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.item_id"))
    rating: Mapped[float] = mapped_column(Float)    
    quantity: Mapped[int] = mapped_column(Integer)

class NegInteractions(Base):
    __tablename__ = "neg_interactions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.item_id"))
    rating: Mapped[float] = mapped_column(Float)    