from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Tenant(Base):
    __tablename__ = "tenants"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    age = Column(Integer)
    gender = Column(String)
    food_preference = Column(String)
    occupation = Column(String)
    bio = Column(String)
    bookings = relationship("Booking", back_populates="tenant")

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    hostel_name = Column(String)
    room_type = Column(String)
    check_in = Column(Date)
    check_out = Column(Date)
    guests = Column(Integer)
    total_price = Column(Float)
    tenant_id = Column(Integer, ForeignKey("tenants.id"))
    tenant = relationship("Tenant", back_populates="bookings")

class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey("bookings.id"))
    amount = Column(Float)
    status = Column(String)  # 'Paid' or 'Unpaid'
    booking = relationship("Booking")
