EeasyCRM

A simple Customer Relationship Management (CRM) web application built with Django.

This project allows authenticated users to manage customer records and categories through a clean dashboard interface with search, authentication, and full CRUD functionality.

Features
User Registration & Authentication
Secure Login / Logout System
Dashboard for managing client records
Create, Update, View, and Delete client records
Create, Update, and Delete categories
Search records by:
First Name
Last Name
Phone Number
Address
Category
Height
Weight
Django Admin Panel
Form Validation
Custom 404 Error Page
Bootstrap UI with Crispy Forms
Tech Stack
Python
Django 5
SQLite
Bootstrap 5
Crispy Forms
HTML / CSS / JavaScript


Project Structure
main_crm/
│
├── crm/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│
├── templates/
├── static/
├── main_crm/
│   ├── settings.py
│   ├── urls.py
│
└── manage.py

Installation
Clone repository
git clone https://github.com/MoazAbdelGhany/EeasyCRM.git
cd EeasyCRM

Create virtual environment
python -m venv env

Activate it:

Windows

env\Scripts\activate

Linux / Mac

source env/bin/activate
Install dependencies
pip install -r requirements.txt
Run migrations
python manage.py migrate
Create superuser
python manage.py createsuperuser
Run server
python manage.py runserver

Visit:

http://127.0.0.1:8000/
Environment Variables

Create .env

SECRET_KEY=your_secret_key
DEBUG=True
Models
Category

Stores record categories.

Fields:

name
created_at
updated_at
Record

Stores client information.

Fields:

first_name
last_name
phone
tall
weight
address
category
created_at
updated_at
Authentication

Uses Django built-in authentication system:

Register
Login
Logout
Protected dashboard routes
Search Functionality

Supports searching client records using Django ORM queries with:

Partial text matching
Category search
Numeric field search
Admin Panel

Access admin panel:

http://127.0.0.1:8000/admin/

Manage:

Categories
Records
Users
Future Improvements
REST API support
Pagination
Export records to CSV/PDF
User profile management
Role-based permissions
Author

Moaz AbdelGhany

GitHub:
MoazAbdelGhany
