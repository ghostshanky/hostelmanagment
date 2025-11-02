from pydantic import BaseModel
from typing import Optional
from datetime import date

class TenantBase(BaseModel):
    name: str
    email: str
    age: int
    gender: str
    food_preference: str
    occupation: str
    bio: str

class TenantCreate(TenantBase):
    pass

class Tenant(TenantBase):
    id: int

    class Config:
        from_attributes = True

class BookingBase(BaseModel):
    hostel_name: str
    room_type: str
    check_in: date
    check_out: date
    guests: int
    total_price: float
    tenant_id: int

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id: int

    class Config:
        from_attributes = True

class InvoiceBase(BaseModel):
    booking_id: int
    amount: float
    status: str

class InvoiceCreate(InvoiceBase):
    pass

class Invoice(InvoiceBase):
    id: int

    class Config:
        from_attributes = True
