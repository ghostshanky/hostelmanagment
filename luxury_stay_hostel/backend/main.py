from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from . import models, crud

Base.metadata.create_all(bind=engine)

app = FastAPI(title="LuxuryStayHostelsAPI")

@app.get("/")
def root():
    return {"message": "Welcome to the Luxury Stay Hostels Backend!"}

@app.post("/tenants/")
def add_tenant(tenant: dict, db: Session = Depends(get_db)):
    return crud.create_tenant(db, tenant)

@app.get("/tenants/")
def get_all_tenants(db: Session = Depends(get_db)):
    return crud.get_tenants(db)

@app.post("/bookings/")
def add_booking(booking: dict, db: Session = Depends(get_db)):
    return crud.create_booking(db, booking)

@app.get("/bookings/")
def get_all_bookings(db: Session = Depends(get_db)):
    return crud.get_bookings(db)
