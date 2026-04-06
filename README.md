# Zorvyn API

A robust "Finance Data Processing and Access Control Backend" built with FastAPI and Tortoise ORM. This system is designed to manage users, roles, and financial entries, while serving aggregated summary-level analytics to a frontend dashboard.

## Features

Based on the core system requirements, the API provides:

- **User & Role Management**: Create and manage users, assign access levels (e.g., Viewer, Analyst, Admin), and toggle active/inactive status.
- **Financial Records Management**: Perform full CRUD operations on financial entries, storing details like amount, type (income/expense), category, date, and notes.
- **Dashboard Analytics**: Retrieve summary-level data including total income, total expenses, net balance, and category-wise totals.
- **Role-Based Access Control (RBAC)**: Secure endpoints by enforcing strict access control logic to ensure users can only perform actions permitted by their assigned roles.

## Tech Stack

- **Framework**: FastAPI
- **ORM**: Tortoise ORM
- **Dependency Management**: Poetry
- **Environment Management**: Python `python-dotenv` integration

## Project Structure

The project is structured to enforce separation of concerns:

- `main.py`: The entry point for the FastAPI application.
- `core/`: Contains core configuration logic.
  - `environ.py`: Automatically loads and manages environment variables from a `.env` file.
  - `lifespan.py`: Handles the async lifespan context of the API, taking care of database connections and teardowns.
  - `settings.py`: Centralized configuration settings.
- `models/`: Defines the Tortoise ORM database models, such as the `User` model.
- `utils/`: Contains helper functions (e.g., security and password hashing).

## Local Setup

### 1. Prerequisites
Ensure you have Python installed, along with **Poetry** for dependency management.

### 2. Install Dependencies
Navigate to the project root and install the dependencies defined in your `pyproject.toml` and `poetry.lock`:
```bash
poetry install
```

### 3. Environment Variables
Create a `.env` file in the root directory. The application's environment manager will automatically load it.
```env
# Example .env configuration
DATABASE_URL=sqlite://db.sqlite3
```

### 4. Run the Server
Start the FastAPI development server:
```bash
poetry run fastapi dev
```
The application will automatically connect to the database and generate the required schemas on startup.

## API Documentation

Once the server is running, FastAPI automatically generates interactive API documentation. You can access it by visiting:
- **Swagger UI**: `http://localhost:8000/docs`
