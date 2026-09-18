# 🚀 Learning FastAPI

Welcome to my repository dedicated to mastering **FastAPI**! This project serves as a central hub for my hands-on practice, code samples, and building modern, high-performance web APIs using Python.

## 📌 Project Overview
The goal of this repository is to learn the core concepts of FastAPI, from setting up basic routing to handling advanced features like database integration, background tasks, and authentication.

## 🛠️ Tech Stack & Tools
* **Language:** Python 3.10+
* **Framework:** FastAPI
* **Server:** Uvicorn (ASGI server)
* **Data Validation:** Pydantic v2
* **Documentation:** Swagger UI & ReDoc (built-in)

## 📁 Repository Structure
* `/basics` - Initial setup, path parameters, and query parameters.
* `/models` - Request body handling and data validation with Pydantic.
* `/crud_app` - A mini-project implementing Create, Read, Update, Delete functionality.

## 🚀 Getting Started

Follow these steps to run the code locally:

### 1. Clone the repository
```bash
git clone https://github.com/TasisAlwaz/FastAPI_Learn.git
cd FastAPI_Learn
```

### 2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install fastapi uvicorn
```

### 4. Run the development server
```bash
uvicorn main:app --reload
```
The application will be available at `http://127.0.0.1:8000`.

## 📖 What I Have Learned So Far
* [x] Setting up a FastAPI instance and creating a root route (`@app.get("/")`).
* [ ] Handling Path and Query parameters.
* [ ] Request body validation using Pydantic models.
* [ ] Exploring automatic interactive API documentation at `/docs`.

## 🗺️ Roadmap / Next Steps
* [ ] Connect the application to a database (SQLAlchemy / PostgreSQL).
* [ ] Implement User Authentication (JWT tokens).
* [ ] Deploy the API to a cloud platform (e.g., Render or AWS).

---
*Feel free to star ⭐ this repository if you find my learning journey helpful!*
