from sqlalchemy.orm import Session
from . import models

def create_tenant(db: Session, tenant_data: dict):
    tenant = models.Tenant(**tenant_data)
    db.add(tenant)
    db.commit()
    db.refresh(tenant)
    return tenant

def get_tenants(db: Session):
    return db.query(models.Tenant).all()

def get_tenant(db: Session, tenant_id: int):
    return db.query(models.Tenant).filter(models.Tenant.id == tenant_id).first()

def create_booking(db: Session, booking_data: dict):
    booking = models.Booking(**booking_data)
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking

def get_bookings(db: Session):
    return db.query(models.Booking).all()

def get_booking(db: Session, booking_id: int):
    return db.query(models.Booking).filter(models.Booking.id == booking_id).first()

def create_invoice(db: Session, invoice_data: dict):
    invoice = models.Invoice(**invoice_data)
    db.add(invoice)
    db.commit()
    db.refresh(invoice)
    return invoice

def get_invoices(db: Session):
    return db.query(models.Invoice).all()
