# Luxury Stay Hostels

A comprehensive hostel management system built with Streamlit for the frontend and FastAPI for the backend, using SQLAlchemy for database management.

## Features

### Frontend (Streamlit)
- **Homepage**: Welcome page with navigation.
- **Properties & Booking**: View available hostels and rooms, make bookings.
- **Invoices**: View and download invoices.
- **Payments**: Make payments for invoices.
- **Tenant Profile**: Manage tenant information.
- **About Us**: Information about the hostel chain.
- **Contact Us**: Contact details and map.

### Backend (FastAPI)
- RESTful API for managing tenants, bookings, and invoices.
- Database integration with SQLite (configurable to PostgreSQL).
- CRUD operations for tenants and bookings.

## Project Structure

```
luxury_stay_hostel/
├── app.py                 # Main Streamlit application
├── README.md              # This file
└── backend/
    ├── __init__.py        # Backend package init
    ├── crud.py            # CRUD operations
    ├── database.py        # Database configuration
    ├── main.py            # FastAPI application
    ├── models.py          # SQLAlchemy models
    └── schemas.py         # Pydantic schemas (if used)
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/ghostshanky/hostelmanagment.git
   cd luxury_stay_hostel
   ```

2. Install dependencies:
   ```
   pip install streamlit fastapi uvicorn sqlalchemy
   ```

3. Run the backend:
   ```
   cd backend
   uvicorn main:app --reload
   ```

4. Run the frontend (in a separate terminal):
   ```
   streamlit run app.py
   ```

## Usage

- Access the Streamlit app at `http://localhost:8501`
- Backend API at `http://localhost:8000`

## Database

The application uses SQLite by default. To use PostgreSQL, update the `DATABASE_URL` in `backend/database.py`.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.
