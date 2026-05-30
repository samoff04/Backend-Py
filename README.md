# Python Backend

A complete backend development portfolio built using **Python, Flask, and SQLite**, focused on REST APIs, authentication systems, database handling, analytics, and scalable backend architecture.

This repository demonstrates a progression from basic CRUD APIs to intermediate industry-level backend systems suitable for internship readiness.

---

# Overview

This repository contains multiple backend projects that build real-world backend engineering skills step by step.

Each project focuses on one important backend concept used in production systems such as APIs, authentication, databases, filtering, and analytics.

---

# Projects Included

## 1. Todo API
Basic CRUD API for task management.

Concepts:
- Flask basics
- REST API structure
- JSON request/response handling
- CRUD operations

---

## 2. Student Management System
Backend system with SQLite database integration.

Concepts:
- Flask + SQLite integration
- Database operations
- Persistent storage
- Structured CRUD design

---

## 3. Blog API
Structured backend for blog management system.

Concepts:
- Blueprint architecture
- Modular backend design
- RESTful API design
- Timestamp handling
- Clean project structure

---

## 4. Authentication System
User authentication system with secure login flow.

Concepts:
- Password hashing (bcrypt)
- User registration & login flow
- Authentication logic
- Service layer architecture
- Security fundamentals

---

## 5. E-Commerce Backend
A simplified backend simulating an e-commerce system.

Concepts:
- Multi-module architecture
- Business logic separation
- Product, cart, and order flow
- Scalable backend design
- System thinking basics

---

## 6. JWT Authentication System
Token-based authentication system used in real-world applications.

Concepts:
- JWT token generation & verification
- Secure authentication flow
- Protected routes
- Token expiry handling
- Industry-standard login system

---

## 7. Task Management API
Advanced task system with user-based filtering and structured APIs.

Concepts:
- User-specific data handling
- Filtering & query-based APIs
- Task status tracking
- Priority-based management
- Backend data structuring

---

# Tech Stack

- Python
- Flask
- SQLite
- REST APIs
- bcrypt
- PyJWT
- Modular backend architecture

---

# Project Structure
```
Backend-Py/
│
├── todo-api/
├── student-management/
├── blog-api/
├── auth-system/
├── ecommerce-backend/
├── jwt-auth-system/
└── task-management-api/
```
---

# How to Run

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

## Step 3: Run Any Project
```
Each project runs independently.

Example:

cd todo-api
python app.py

OR

cd jwt-auth-system
python app.py
```
---

## Step 4: Test APIs
```
Use:
- Postman
- Thunder Client (VS Code)
- Browser (for GET APIs)
```
---

# Skills Demonstrated

- REST API development
- Backend architecture design
- Authentication systems (bcrypt + JWT)
- Database integration (SQLite)
- Modular Flask applications
- Filtering & query handling
- Analytics-based backend logic
- Real-world system design thinking
- Scalable project structuring

---

# Future Scope / Upgrades

This project can be extended into production-level systems:

Backend Improvements:
- PostgreSQL integration
- Redis caching system
- API rate limiting
- Logging & monitoring system

Architecture Upgrades:
- FastAPI migration
- Microservices-based design
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