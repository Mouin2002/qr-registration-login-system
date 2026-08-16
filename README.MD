# QR Registration & Login System

A Django-based QR authentication system where registration and login are performed through QR codes.

## Project Overview

The system displays a QR code on a laptop browser.

The user scans the QR code using a mobile phone.

### Registration Flow

Laptop
↓
Register QR
↓
Mobile Registration Form
↓
Backend Validation
↓
MySQL Database
↓
Registration Successful
↓
Login QR

### Login Flow

Laptop
↓
Login QR
↓
Mobile Login Form
↓
Authentication
↓
Dashboard
↓
Logout

## Features

- QR-based user registration
- QR-based user login
- Automatic Register → Login QR transition
- MySQL database
- Django authentication
- Password hashing
- Registration validation
- Email uniqueness validation
- Phone number validation
- Password strength validation
- Password confirmation
- QR expiration
- Single-use QR sessions
- Session-based authentication
- Protected dashboard
- Secure logout
- Responsive UI
- Environment-based configuration

## Technology Stack

- Python
- Django
- MySQL
- HTML
- CSS
- JavaScript
- QRCode
- python-dotenv

## Project Structure

```text
qr_auth_project/
│
├── qr_auth/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── qr_system/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── users/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── static/
│   └── css/
│       └── style.css
│
├── manage.py
├── requirements.txt
├── .env.example
└── .gitignore
```
