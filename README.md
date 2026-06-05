# Python Backend Portfolio

A complete backend development portfolio built using **Python, Flask, and SQLite**, focused on REST APIs, authentication systems, URL shortening systems, file handling, database integration, and scalable backend architecture.

This repository demonstrates a structured learning progression from beginner-level CRUD APIs to intermediate backend systems suitable for internship and entry-level backend developer roles.

---

# Overview

This repository contains multiple backend projects designed to build real-world backend engineering skills step by step. Each project focuses on core backend concepts used in production systems such as API design, authentication, database handling, modular architecture, and system design fundamentals.

The goal is to demonstrate practical backend development skills with clean structure, reusable code, and scalable design patterns.

---

# Projects Included

## 🔹 Todo API
Basic task management backend system with CRUD operations.

Concepts:
Flask basics, REST API design, JSON request/response handling, CRUD operations.

---

## 🔹 Student Management System
Database-driven system for managing student records.

Concepts:
SQLite integration, persistent storage, CRUD with database operations.

---

## 🔹 Blog API
Structured backend system for blog posts.

Concepts:
Blueprint architecture, modular backend design, RESTful APIs, timestamp handling.

---

## 🔹 Authentication System
User authentication system with secure password handling.

Concepts:
bcrypt password hashing, user registration/login flow, security fundamentals.

---

## 🔹 E-Commerce Backend
Simplified backend simulating product-based system.

Concepts:
Product/cart/order flow, multi-module architecture, backend business logic.

---

## 🔹 JWT Authentication System
Token-based authentication system used in real-world applications.

Concepts:
JWT token generation and verification, protected routes, secure API design, session-less authentication.

---

## 🔹 Task Management API
Advanced task system with filtering and structured APIs.

Concepts:
User-based data handling, filtering, priority/status tracking, query-based APIs.

---

## 🔹 URL Shortener System
Bitly-like backend system for URL shortening.

Concepts:
URL shortening logic, unique code generation, redirect handling, click tracking analytics.

---

## 🔹 File Storage Backend System
Cloud-style file storage backend system.

Concepts:
File upload/download/delete APIs, file system handling, SQLite metadata storage, service-layer architecture.

---

# Tech Stack

Python, Flask, SQLite, REST APIs, bcrypt, PyJWT, Werkzeug

---

# Project Structure
```
InternProjects/
│
├── todo-api/
├── student-system/
├── blog-api/
├── auth-system/
├── ecommerce/
├── jwt-auth-system/
├── task-management-api/
├── url-shortener/
└── file-storage-app/
```
---

# How to Run Projects

## Step 1: Clone Repository
```
git clone https://github.com/samoff04/Backend-Py.git  
cd Backend-Py  
```
---

## Step 2: Install Dependencies
```
pip install -r requirements.txt  
```
---

## Step 3: Initialize Database (if required)
```
python init_db.py  
```
---

## Step 4: Run Any Project
```
Each project runs independently.

Example:
cd file-storage-backend
python app.py  

OR  
cd jwt-auth-system  
python app.py  
```
---

# Testing APIs

Use:
Postman / Thunder Client / Browser (for GET endpoints)

---

# Skills Demonstrated

REST API development  
Backend architecture design  
Authentication systems (bcrypt + JWT)  
URL shortening system design  
File handling systems  
SQLite database integration  
Modular Flask applications  
Filtering and query handling  
Real-world backend logic  
System design fundamentals  

---

# Learning Outcome

This repository demonstrates a clear progression in backend development:

Beginner → CRUD APIs  
Intermediate → Authentication + File Systems  
Advanced understanding → JWT + System Design Basics  

---

# Future Improvements

This project can be extended into production-level backend systems with:

Backend Enhancements:
- PostgreSQL integration  
- Redis caching system  
- API rate limiting  
- Logging and monitoring system  

Architecture Upgrades:
- FastAPI migration  
- Microservices-based architecture  
- Docker containerization  
- CI/CD pipeline integration  

Deployment:
- Render / Railway / AWS hosting  
- Domain mapping  
- Live API endpoints  

Security Enhancements:
- OAuth2 authentication  
- Refresh tokens  
- Role-based access control (RBAC)  

---

# Author

Samarth Varshney