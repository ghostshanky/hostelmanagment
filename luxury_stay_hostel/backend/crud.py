from . import models

def create_tenant(db, tenant_data):
    tenant = models.Tenant(**tenant_data)
    db.add(tenant)
    db.commit()
    db.refresh(tenant)
    return tenant

def get_tenants(db):
    return db.query(models.Tenant).all()

def create_booking(db, booking_data):
    booking = models.Booking(**booking_data)
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking

def get_bookings(db):
    return db.query(models.Booking).all()

def create_invoice(db, invoice_data):
    invoice = models.Invoice(**invoice_data)
    db.add(invoice)
    db.commit()
    db.refresh(invoice)
    return invoice
