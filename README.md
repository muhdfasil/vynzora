record : https://drive.google.com/file/d/1PS-F3I8jlnX2R8O3RCcQQBN6w3Kke2Oi/view?usp=sharing

# 🚗 Vehicle Booking System API

A Django REST Framework based API for managing Vehicles and Bookings.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
git clone https://github.com/muhdfasil/vynzora/  
cd vehicle_system  

### 2️⃣ Create Virtual Environment
python -m venv env  
env\Scripts\activate  

### 3️⃣ Install Dependencies
pip install django djangorestframework  

### 4️⃣ Apply Migrations
python manage.py makemigrations  
python manage.py migrate  

### 5️⃣ Run Server
python manage.py runserver  

Server will run at:  
http://127.0.0.1:8000/

---

## 🧪 How to Test APIs

You can test the APIs using Postman or any API testing tool.

---

# 🚗 Vehicle APIs

## ➤ Create Vehicle (POST)
POST http://127.0.0.1:8000/api/vehicles/

Sample JSON:
{
  "name": "X5",
  "brand": "BMW",
  "year": 2024,
  "price_per_day": "8000.00",
  "fuel_type": "Diesel",
  "is_available": true
}

---

## ➤ Get All Vehicles (GET)
GET http://127.0.0.1:8000/api/vehicles/

---

## ➤ Get Single Vehicle (GET)
GET http://127.0.0.1:8000/api/vehicles/1/

---

## ➤ Update Vehicle (PUT)
PUT http://127.0.0.1:8000/api/vehicles/1/

---

## ➤ Delete Vehicle (DELETE)
DELETE http://127.0.0.1:8000/api/vehicles/1/

---

## 🔎 Vehicle Filter Examples

/api/vehicles/?brand=BMW  
/api/vehicles/?fuel_type=Diesel  
/api/vehicles/?is_available=true  

---

# 📅 Booking APIs

## ➤ Create Booking (POST)
POST http://127.0.0.1:8000/api/bookings/

Sample JSON:
{
  "vehicle": 1,
  "customer_name": "Rahul",
  "customer_phone": "1010101010",
  "start_date": "2026-02-25",
  "end_date": "2026-02-28"
}

---

## ➤ Get All Bookings (GET)
GET http://127.0.0.1:8000/api/bookings/

---

## ➤ Get Single Booking (GET)
GET http://127.0.0.1:8000/api/bookings/1/

---

# 📌 API Endpoint List

## 🚗 Vehicle Endpoints

GET     /api/vehicles/  
POST    /api/vehicles/  
GET     /api/vehicles/{id}/  
PUT     /api/vehicles/{id}/  
DELETE  /api/vehicles/{id}/  

---

## 📅 Booking Endpoints

GET     /api/bookings/  
POST    /api/bookings/  
GET     /api/bookings/{id}/  

---
