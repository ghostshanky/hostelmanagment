from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from .database import engine, Base, get_db
from . import models, crud, schemas, auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="LuxuryStayHostelsAPI")

@app.get("/")
def root():
    return {"message": "Welcome to the Luxury Stay Hostels Backend!"}

@app.post("/auth/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = auth.get_password_hash(user.password)
    user_data = user.dict()
    user_data["hashed_password"] = hashed_password
    return crud.create_user(db, user_data)

@app.post("/auth/login", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/tenants/", response_model=schemas.Tenant)
def add_tenant(tenant: schemas.TenantCreate, db: Session = Depends(get_db)):
    return crud.create_tenant(db, tenant.dict())

@app.get("/tenants/", response_model=list[schemas.Tenant])
def get_all_tenants(db: Session = Depends(get_db)):
    return crud.get_tenants(db)

@app.get("/tenants/{tenant_id}", response_model=schemas.Tenant)
def get_tenant(tenant_id: int, db: Session = Depends(get_db)):
    tenant = crud.get_tenant(db, tenant_id)
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return tenant

@app.post("/bookings/", response_model=schemas.Booking)
def add_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    return crud.create_booking(db, booking.dict())

@app.get("/bookings/", response_model=list[schemas.Booking])
def get_all_bookings(db: Session = Depends(get_db)):
    return crud.get_bookings(db)

@app.get("/bookings/{booking_id}", response_model=schemas.Booking)
def get_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = crud.get_booking(db, booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@app.post("/invoices/", response_model=schemas.Invoice)
def add_invoice(invoice: schemas.InvoiceCreate, db: Session = Depends(get_db)):
    return crud.create_invoice(db, invoice.dict())

@app.get("/invoices/", response_model=list[schemas.Invoice])
def get_all_invoices(db: Session = Depends(get_db)):
    return crud.get_invoices(db)
