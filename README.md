# ⚡ FastAPI & React Full-Stack Learning Hub

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python_3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![React](https://img.shields.io/badge/React_18-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://react.dev/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white)](https://www.uvicorn.org/)

A hands-on, progressive repository documenting the journey of building modern, production-grade REST APIs with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**, complete with an interactive **React** frontend dashboard.

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Repository Structure](#-repository-structure)
- [API Endpoints Reference](#-api-endpoints-reference)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [1. Clone Repository](#1-clone-repository)
  - [2. Database Setup](#2-database-setup-postgresql)
  - [3. Backend Setup (FastAPI)](#3-backend-setup-fastapi)
  - [4. Frontend Setup (React)](#4-frontend-setup-react)
- [Interactive API Documentation](#-interactive-api-documentation)
- [Learning Progression & Milestones](#-learning-progression--milestones)
- [Roadmap & Upcoming Enhancements](#-roadmap--upcoming-enhancements)
- [Author & Acknowledgments](#-author--acknowledgments)

---

## 🌟 Overview

This repository captures a step-by-step evolution from introductory FastAPI routing to a full-stack CRUD application. It demonstrates:
- Building performant REST endpoints using standard HTTP methods.
- Strict request validation and serialization with **Pydantic v2**.
- Object-Relational Mapping (ORM) and relational persistence using **SQLAlchemy** and **PostgreSQL**.
- Decoupled session handling via FastAPI's **Dependency Injection** system (`Depends`).
- A responsive client dashboard created with **React** to interact with the backend in real time.

---

## ✨ Key Features

- **Full CRUD Persistence**: Create, Read, Update, and Delete inventory items backed by a relational PostgreSQL database.
- **Dependency Injection (`Depends`)**: Clean lifecycle management for database sessions, ensuring sessions auto-close per request.
- **Automatic Schema Migration & Seeding**: Auto-creates the required tables on server boot and seeds default product data if the table is empty.
- **Strict Data Validation**: Pydantic models validate payloads with descriptive errors for invalid types or missing fields.
- **Interactive API Documentation**: Live testing and exploration through auto-generated Swagger UI and ReDoc endpoints.
- **Full-Stack React Dashboard**: Includes search filtering, dynamic sorting, inline editing, and auto-dismissing notifications.

---

## 🛠️ Tech Stack

### Backend
| Tool | Purpose |
| :--- | :--- |
| **[FastAPI](https://fastapi.tiangolo.com/)** | High-performance Python web framework |
| **[Uvicorn](https://www.uvicorn.org/)** | Lightning-fast ASGI server |
| **[SQLAlchemy 2.0](https://www.sqlalchemy.org/)** | Database ORM and SQL toolkit |
| **[PostgreSQL](https://www.postgresql.org/)** | Relational Database Management System |
| **[Psycopg2-binary](https://pypi.org/project/psycopg2-binary/)** | PostgreSQL database adapter for Python |
| **[Pydantic v2](https://docs.pydantic.dev/)** | Data validation and serialization |

### Frontend
| Tool | Purpose |
| :--- | :--- |
| **[React 18](https://react.dev/)** | Frontend user interface library |
| **[Axios](https://axios-http.com/)** | Promise-based HTTP client for API calls |
| **Custom CSS** | Modern responsive grid layout and dashboard styling |

---

## 📁 Repository Structure

```text
FastAPI_Learn/
├── database.py           # Database connection, engine, and sessionmaker config
├── database_models.py    # SQLAlchemy ORM models (table schemas)
├── models.py             # Pydantic schemas for data validation and serialization
├── main.py               # FastAPI application, route handlers, and DB lifecycle
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── frontend/             # React single-page client
    ├── package.json      # Node.js dependencies and run scripts
    ├── public/           # Static assets and index.html
    └── src/
        ├── App.js        # Main inventory management dashboard
        ├── App.css       # Dashboard UI styles
        ├── TaglineSection.js # Header banner & tagline component
        ├── TaglineSection.css# Tagline component styling
        ├── index.js      # React application entry point
        └── index.css     # Global styles
```

---

## 🔌 API Endpoints Reference

All API endpoints are hosted by default at `http://localhost:8000`.

| Method | Endpoint | Query / Path Params | Description |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | None | Welcome greeting and health check |
| `GET` | `/products` | None | Retrieve all products from the database |
| `GET` | `/product/{id}` | `id` (path, `int`) | Retrieve a single product by its unique ID |
| `POST` | `/product` | None | Add a new product to the database |
| `PUT` | `/product` | `id` (query, `int`) | Update an existing product by ID |
| `DELETE` | `/product` | `id` (query, `int`) | Delete a product from the database |

### Sample Product Payload

```json
{
  "id": 1,
  "name": "Mechanical Keyboard",
  "description": "RGB mechanical keyboard with brown switches",
  "price": 89.99,
  "quantity": 15
}
```

---

## 🚀 Getting Started

Follow these instructions to run the entire stack locally.

### Prerequisites

Ensure you have the following installed on your machine:
- **Python**: `3.10` or higher ([Download Python](https://www.python.org/downloads/))
- **PostgreSQL**: `14` or higher with **pgAdmin 4** (or command-line `psql`) ([Download PostgreSQL](https://www.postgresql.org/download/))
- **Node.js & npm**: Node `v16+` & npm `v8+` ([Download Node.js](https://nodejs.org/))
- **Git**: Installed and configured

---

### 1. Clone Repository

```bash
git clone https://github.com/TasisAlwaz/FastAPI_Learn.git
cd FastAPI_Learn
```

---

### 2. Database Setup (PostgreSQL)

1. Open your PostgreSQL terminal (`psql`) or launch **pgAdmin 4**.
2. Create a new database named `Telusko`:
   ```sql
   CREATE DATABASE "Telusko";
   ```
3. Open `database.py` and verify or update the connection string with your PostgreSQL credentials:
   ```python
   # database.py
   db_url = "postgresql://<username>:<password>@localhost:5432/Telusko"
   ```
   > **Note:** The default configuration expects username `postgres` and password `postgres`.

---

### 3. Backend Setup (FastAPI)

1. **Create and activate a virtual environment:**
   - **Linux / macOS:**
     ```bash
     python3 -m venv myenv
     source myenv/bin/activate
     ```
   - **Windows:**
     ```cmd
     python -m venv myenv
     myenv\Scripts\activate
     ```

2. **Install backend dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the FastAPI server:**
   ```bash
   uvicorn main:app --reload
   ```

4. The API will now be running at:
   - **Base URL:** `http://localhost:8000`
   - The database tables will be auto-generated and seeded on first run!

---

### 4. Frontend Setup (React)

Open a **new terminal tab or window**:

1. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install frontend dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm start
   ```

4. The React dashboard will automatically open at `http://localhost:3000`.

---

## 📖 Interactive API Documentation

FastAPI provides out-of-the-box interactive documentation. Once your backend server is running, explore:

- **Swagger UI (Interactive API Explorer):**
  [http://localhost:8000/docs](http://localhost:8000/docs)
  > Test all endpoints directly in the browser with live request bodies and response previews.

- **ReDoc (Alternative Clean Reference):**
  [http://localhost:8000/redoc](http://localhost:8000/redoc)
  > Well-structured, readable API technical reference.

---

## 🏆 Learning Progression & Milestones

This repository is organized around core engineering milestones:

- [x] **Chapter 3: Foundations** &mdash; Initialized FastAPI app instance and basic root routes.
- [x] **Chapter 4: Schema Validation** &mdash; Integrated Pydantic models for type safety and serialization.
- [x] **Chapter 5: Path Parameters & POST** &mdash; Handled URL path variables (`/product/{id}`) and JSON request bodies.
- [x] **Chapter 6: In-Memory CRUD** &mdash; Implemented in-memory item updates and deletions.
- [x] **Chapter 8: Database Architecture** &mdash; Configured PostgreSQL engine and connection pools with SQLAlchemy.
- [x] **Chapter 9: Declarative ORM Models** &mdash; Created `database_models.py` mapping Python classes to PostgreSQL tables.
- [x] **Chapter 10: Automatic Seeding** &mdash; Implemented startup routine `init_db()` to seed initial product records.
- [x] **Chapter 11: Dependency Injection** &mdash; Decoupled database sessions using FastAPI's `Depends(get_db)` pattern.
- [x] **Chapter 12: Persistent CRUD** &mdash; Completed full relational database operations with transaction commit and rollback handling.
- [x] **Frontend Integration** &mdash; Built and linked a modern React single-page UI for end-to-end user interaction.

---

## 🗺️ Roadmap & Upcoming Enhancements

- [ ] **Cross-Origin Resource Sharing (CORS)**: Explicitly configure `CORSMiddleware` in FastAPI.
- [ ] **Environment Configuration**: Secure database credentials using `.env` and `pydantic-settings`.
- [ ] **Authentication & Security**: Add OAuth2 with JWT (JSON Web Tokens) and password hashing (bcrypt).
- [ ] **Database Migrations**: Integrate **Alembic** for tracked database schema migrations.
- [ ] **Automated Testing**: Write unit and integration test suites using `pytest` and `httpx`.
- [ ] **Containerization**: Add `Dockerfile` and `docker-compose.yml` to orchestrate FastAPI, PostgreSQL, and React with a single command.

---

## 👨‍💻 Author & Acknowledgments

- **Author:** [Tasis Alwaz](https://github.com/TasisAlwaz)
- **Repository:** [FastAPI_Learn](https://github.com/TasisAlwaz/FastAPI_Learn)
- **Inspiration:** Inspired by Telusko's FastAPI & modern web development tutorials.

---

