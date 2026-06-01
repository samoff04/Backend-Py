# Python Backend Portfolio

A complete backend development portfolio built using **Python, Flask, and SQLite**, focused on REST APIs, authentication systems, URL shortening systems, database handling, and scalable backend architecture.

This repository demonstrates a structured progression from beginner-level CRUD APIs to intermediate backend systems suitable for internship and entry-level backend developer roles.

---

## Overview

This repository contains multiple backend projects built to develop real-world backend engineering skills step by step. Each project focuses on a core backend concept used in production systems such as APIs, authentication, databases, system design, and scalable backend workflows.

The goal of this repository is to show a clear learning path from basic API creation to advanced backend systems with authentication, modular design, and real-world logic implementation.

---

## Projects Included

### 1. Todo API
A basic CRUD API for task management.

Concepts: Flask basics, REST APIs, JSON request/response handling, CRUD operations.

---

### 2. Student Management System
Backend system with SQLite database integration.

Concepts: Flask + SQLite integration, database operations, persistent storage, structured CRUD design.

---

### 3. Blog API
Structured backend system for blog management.

Concepts: Blueprint architecture, modular backend design, RESTful APIs, timestamp handling.

---

### 4. Authentication System
Secure user authentication system.

Concepts: Password hashing using bcrypt, user registration/login flow, service layer architecture, security fundamentals.

---

### 5. E-Commerce Backend
Mini backend simulating an e-commerce system.

Concepts: Multi-module architecture, business logic separation, product/cart/order flow, system design basics.

---

### 6. JWT Authentication System
Token-based authentication system used in real-world applications.

Concepts: JWT token generation and verification, protected routes, token expiry handling, secure API design.

---

### 7. Task Management API
Advanced task system with filtering and structured APIs.

Concepts: User-based data handling, query filtering, status tracking, priority management, backend structuring.

---

### 8. URL Shortener System (Advanced Project)
Real-world backend system similar to Bitly.

Concepts: URL shortening logic, unique code generation, redirect handling, click tracking analytics, JWT-protected APIs for authentication.

---

## Tech Stack

Python, Flask, SQLite, REST APIs, bcrypt, PyJWT

---

## Project Structure

InternProjects/  
├── todo-api/  
├── student-system/  
├── blog-api/  
├── auth-system/  
├── ecommerce/  
├── jwt-auth-system/  
├── task-management-api/  
└── url-shortener/  

---

## How to Run
Clone the repository:
```
git clone https://github.com/samoff04/Backend-Py.git  
cd Backend-Py  
```
Install dependencies:
```
pip install -r requirements.txt  
```
If required, initialize database:
```
python init_db.py  
```
Run any project independently:
```
cd todo-api  
python app.py  
```
OR
```
cd url-shortener  
python app.py  
```
---

## Testing APIs

Use Postman, Thunder Client (VS Code), or browser (for GET routes and redirects).

---

## Skills Demonstrated

REST API development, backend architecture design, authentication systems using bcrypt and JWT, URL shortening system design, SQLite database integration, modular Flask applications, filtering and query handling, real-world backend logic, and system design fundamentals.

---

## Future Scope / Improvements

This project can be extended into production-level systems with the following upgrades:

Backend Improvements: PostgreSQL integration, Redis caching system, API rate limiting, logging and monitoring system.

Architecture Upgrades: FastAPI migration, microservices-based architecture, Docker containerization, CI/CD pipeline integration.

Deployment: Hosting on Render, Railway, or AWS with live API endpoints and domain mapping.

Security Enhancements: OAuth2 authentication, refresh tokens, and role-based access control (RBAC).