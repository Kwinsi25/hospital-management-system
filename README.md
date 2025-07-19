
# 🏥 Hospital Management System

This is a mini hospital management system built with **Django**, **Django REST Framework**, and **SQLite**.  
It includes user authentication (doctor/patient), slot management by doctors, and appointment booking by patients.

---

## 🚀 Setup Instructions (Local)

Follow these steps to run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/Kwinsi25/hospital-management-system.git
cd hospital-management-system
```

### 2. Create a Virtual Environment

```bash
python -m venv env
# Activate:
# Linux/macOS
source env/bin/activate
# Windows
env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

---

## 📘 Sample API Request (Login)

### Endpoint: `POST /api/login/`

**Request Body:**

```json
{
  "email": "doctor1@gmail.com",
  "password": "tempDoctor1"
}
```

**Success Response:**

```json
{
  "status": 200,
  "message": "Login successful",
  "token": "e4a241d239as9df3...1c302"
}
```

**Error Response:**

```json
{
  "non_field_errors": ["Unable to log in with provided credentials."]
}
```

---

## 🔐 Roles

### Doctor

- Can create slots  
- Can view their appointments

### Patient

- Can view available slots  
- Can book appointments

---

## 🧪 Postman Collection

You can test all endpoints using the Postman collection provided.

📥 **Download**: `Hospital.postman_collection.json`

### To Import:

1. Open **Postman**
2. Click **Import** → Choose the `.json` file
3. Set the base URL as: `http://127.0.0.1:8000`

---

## ✅ Tech Stack

- **Backend**: Django, Django REST Framework  
- **Database**: SQLite  
- **API Testing**: Postman

---
