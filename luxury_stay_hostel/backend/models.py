from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base

class Tenant(Base):
    __tablename__ = "tenants"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    email = Column(String(100), unique=True, index=True)
    age = Column(Integer)
    gender = Column(String(20))
    food_preference = Column(String(50))
    occupation = Column(String(100))
    bio = Column(Text)
    bookings = relationship("Booking", back_populates="tenant")

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    hostel_name = Column(String(100), index=True)
    room_type = Column(String(50))
    check_in = Column(Date)
    check_out = Column(Date)
    guests = Column(Integer)
    total_price = Column(Float)
    tenant_id = Column(Integer, ForeignKey("tenants.id"))
    tenant = relationship("Tenant", back_populates="bookings")
    invoices = relationship("Invoice", back_populates="booking")

class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey("bookings.id"))
    amount = Column(Float)
    status = Column(String(20))  # 'Paid' or 'Unpaid'
    booking = relationship("Booking", back_populates="invoices")
