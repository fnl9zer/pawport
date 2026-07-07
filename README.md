# PawPort

A "Pet Resume & Tenant Passport" platform connecting Malaysian cat owners with verified pet-friendly landlords and properties.

## Overview

PawPort tackles the critical issue of pet abandonment caused by restrictive housing policies in Malaysia's urban high-rise communities. Cat owners can create verified profiles for their cats and match with landlords who welcome feline tenants.

### The Problem
Many young Malaysians love cats but live in condos where pets are forbidden. Landlords often refuse tenants with cats. This leads to pets being abandoned when people are forced to move.

### The Solution
Verified cat profiles with vaccination records and character references. Pet-friendly property listings across Malaysia. Streamlined application process connecting responsible owners with welcoming landlords.

## Live Demo

[https://web-production-bba1f.up.railway.app/](https://web-production-bba1f.up.railway.app/)

## Features

- User Authentication (Register/Login/Password Recovery)
- Cat Profiles with Vaccination Records, Neutering Status & Photos
- Browse Pet-Friendly Properties
- Property Details with Rent, Deposit & Address
- Submit Applications with Custom Message
- Success Confirmation Popup
- Admin Dashboard

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Django |
| Frontend | HTML5, CSS3, PeaceSans Font |
| Database | SQLite (local), PostgreSQL (production) |
| Hosting | Railway |

## Installation

### 1. Clone the Repository
git clone https://github.com/yourusername/pawport.git
cd pawport

### 2. Create Virtual Environment
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run Migrations
python manage.py makemigrations
python manage.py migrate

### 5. Create Superuser
python manage.py createsuperuser

### 6. Run Server
python manage.py runserver

### 7. Access App
App: http://127.0.0.1:8000/
Admin: http://127.0.0.1:8000/admin/

## Environment Variables

| Variable | Description |
|----------|-------------|
| DATABASE_URL | PostgreSQL connection string (for production) |
| SECRET_KEY | Django secret key |

## Deployment on Railway

# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Deploy
railway up

# Run migrations
railway run python manage.py migrate
railway run python manage.py createsuperuser

## Project Structure

pawport/
├── core/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── forms.py
|   ├── static/core/
│   └── templates/core/
├── pawport/
│   └── settings.py
├── .gitignore
├── Procfile
├── data.json
├── db.sqlite3
├── manage.py
└── requirements.txt

## License

This project was created for the #hackthekitty 2026 hackathon.

## Author

Dania (@seven2wentys /ig)
- GitHub: [@fnl9zer](https://github.com/fnl9zer)
```
