# Luxury Stay Hostels

A modern, full-stack hostel management system designed for seamless tenant experiences and efficient administration. Built with Streamlit for the frontend and FastAPI for the backend, this application provides a comprehensive solution for hostel operations.

## Features

### Frontend (Streamlit)
- **Home Page**: Welcome dashboard with hostel overview
- **Properties & Booking**: Browse available rooms and make reservations
- **Invoices**: View and manage billing statements
- **Payments**: Secure payment processing
- **Tenant Profile**: Personal account management
- **About Us**: Information about the hostel
- **Contact Us**: Get in touch with management

### Backend (FastAPI)
- **Tenant Management**: CRUD operations for tenant profiles
- **Booking System**: Handle reservations with date validation
- **Invoice Generation**: Automated billing and status tracking
- **Payment Integration**: Secure payment processing
- **Database**: SQLite with SQLAlchemy ORM

## Architecture

- **Frontend**: Streamlit application for user interface
- **Backend**: FastAPI REST API with Pydantic schemas
- **Database**: SQLite with SQLAlchemy ORM
- **Models**: Tenant, Booking, Invoice entities with relationships

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/ghostshanky/hostelmanagment.git
   cd luxury_stay_hostel
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

1. **Start the Backend API**:
   ```bash
   uvicorn backend.main:app --reload
   ```
   The API will be available at `http://localhost:8000`

2. **Start the Frontend**:
   ```bash
   streamlit run app.py
   ```
   The app will be available at `http://localhost:8501`

### API Endpoints

- `GET /` - API root
- `POST /tenants/` - Create tenant
- `GET /tenants/` - List all tenants
- `GET /tenants/{id}` - Get tenant by ID
- `POST /bookings/` - Create booking
- `GET /bookings/` - List all bookings
- `GET /bookings/{id}` - Get booking by ID
- `POST /invoices/` - Create invoice
- `GET /invoices/` - List all invoices

## Database Schema

### Tenant
- id: Primary key
- name: Full name
- email: Unique email address
- age: Age
- gender: Gender
- food_preference: Dietary preferences
- occupation: Job/profession
- bio: Personal description

### Booking
- id: Primary key
- hostel_name: Name of the hostel
- room_type: Type of room
- check_in: Check-in date
- check_out: Check-out date
- guests: Number of guests
- total_price: Total booking cost
- tenant_id: Foreign key to Tenant

### Invoice
- id: Primary key
- booking_id: Foreign key to Booking
- amount: Invoice amount
- status: Payment status ('Paid' or 'Unpaid')

## Development

### Project Structure
```
luxury_stay_hostel/
├── app.py                 # Streamlit frontend
├── backend/
│   ├── __init__.py
│   ├── main.py           # FastAPI application
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas
│   ├── crud.py           # Database operations
│   └── database.py       # Database configuration
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── TODO.md               # Development tasks
```

### Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support or questions, please contact us through the Contact Us page in the application.
