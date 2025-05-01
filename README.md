<!-- # Part Manager

A RESTful service built with Python and FastAPI for managing and analyzing mechanical or electronic parts, backed by a PostgreSQL database and containerized with Docker.

---

## 📑 Index

- [📝 Description](#-description)  
- [🎯 Objective](#-objective)  
- [📦 Dependencies](#-dependencies)  
- [📁 Virtual Environment Setup](#-virtual-environment-setup)  
- [🐳 Running the Project with Docker](#-running-the-project-with-docker)  
- [🚨 Known Tech Debts](#-known-tech-debts)

---

## 📝 Description

**Part Manager** is a backend service designed to support parts registration and analytics workflows. It exposes HTTP APIs that allow clients to create, retrieve, and analyze data related to parts stored in a PostgreSQL database. It follows modern Python best practices, uses SQLAlchemy for ORM, Alembic for migrations, and is built with testability in mind using `pytest`.

---

## 🎯 Objective

The main goal of this project is to:

- Provide a simple yet extensible API to register and query part-related data.
- Serve as a reference implementation for a microservice architecture using FastAPI, PostgreSQL, and Docker.
- Maintain high code quality and enforce clean architecture patterns.

---

## 📦 Dependencies

All dependencies are managed via `pip` and grouped in `requirements/dev.txt`. Key packages include:

| Dependency      | Purpose                                |
|----------------|----------------------------------------|
| fastapi         | Web framework for building APIs        |
| uvicorn         | ASGI server for FastAPI                |
| psycopg2-binary | PostgreSQL adapter for Python          |
| alembic         | Database migrations                    |
| pydantic        | Data validation and serialization      |
| SQLAlchemy      | ORM for database interaction           |
| pytest          | Testing framework                      |
| httpx           | HTTP client for testing                |

To install all dev dependencies:
```bash
make install
```

---

## 📁 Virtual Environment Setup

Follow the steps below to set up the project locally with a Python virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # Linux/macOS
# .\venv\Scripts\activate  # Windows

# Install dependencies
make install
```

To run tests:
```bash
make run-test
```

---

## 🐳 Running the Project with Docker

The project uses Docker Compose for simplified development setup. Here’s how to run it step-by-step:

### 1. Run everything with one command:
```bash
make start
```

Once running, the API will be available at:  
[http://localhost:8000](http://localhost:8000)

Interactive docs are available at:  
[http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🚨 Known Tech Debts

- **Database Migration Isolation**: Alembic scripts are applied directly in the container; no current safeguards for production environments.
- **Lack of Authentication/Authorization**: All endpoints are publicly accessible; needs role-based access control.
- **No CI/CD Pipeline**: There's no integration yet for continuous testing, linting, or deployment.
- **No Healthcheck/Readiness Probe**: Missing operational endpoints or Docker healthchecks.
- **Missing Test Coverage Report**: No integration of test coverage or quality gates.
- **Scalability Readiness**: The current setup assumes a monolithic container; service partitioning and autoscaling are not in place. -->

# Part Manager

A RESTful service built with Python and FastAPI for managing and analyzing mechanical or electronic parts, backed by a PostgreSQL database and containerized with Docker.

---

## 📑 Index

- [📝 Description](#-description)  
- [🎯 Objective](#-objective)  
- [📦 Dependencies](#-dependencies)  
- [📁 Virtual Environment Setup](#-virtual-environment-setup)  
- [🐳 Running the Project with Docker](#-running-the-project-with-docker)  
- [🚨 Known Tech Debts](#-known-tech-debts)

---

## 📝 Description

**Part Manager** is a backend service designed to support parts registration and analytics workflows. It exposes HTTP APIs that allow clients to create, retrieve, and analyze data related to parts stored in a PostgreSQL database.

It is built using Python 3.13.3, the latest stable release, and follows modern Python best practices. The service uses SQLAlchemy for ORM, Alembic for migrations, and is designed with testability in mind using pytest.

---

## 🎯 Objective

The main goal of this project is to:

- Provide a simple yet extensible API to register and query part-related data.
- Serve as a reference implementation for a microservice architecture using FastAPI, PostgreSQL, and Docker.
- Maintain high code quality and enforce clean architecture patterns.

---

## 📦 Dependencies

All dependencies are managed via `pip` and grouped in `requirements/dev.txt`. Key packages include:

| Dependency      | Purpose                                |
|----------------|----------------------------------------|
| fastapi         | Web framework for building APIs        |
| uvicorn         | ASGI server for FastAPI                |
| psycopg2-binary | PostgreSQL adapter for Python          |
| alembic         | Database migrations                    |
| pydantic        | Data validation and serialization      |
| SQLAlchemy      | ORM for database interaction           |
| pytest          | Testing framework                      |
| httpx           | HTTP client for testing                |

---

## 📁 Virtual Environment Setup

Follow the steps below to set up the project locally with a Python virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # Linux/macOS
# .\venv\Scripts\activate  # Windows

# Install dependencies
make install
```

To run tests:
```bash
make run-test
```

---

## 🐳 Running the Project with Docker

The project uses Docker Compose for simplified development setup. Here’s how to run it step-by-step:

### 1. Run everything with one command:
```bash
make start
```

Once running, the API will be available at:
http://localhost:8000
🔁 This root endpoint redirects to the interactive API documentation at http://localhost:8000/docs, as implemented in main.py.

---

## 🚨 Known Tech Debts

| Category                         | Details |
|----------------------------------|---------|
| **Lack of Observability**        | No logging configuration, tracing, or metrics integration (e.g., Prometheus, OpenTelemetry). |
| **Missing Test and Type Enforcement** | No CI pipeline to enforce `pytest`, type validation (`mypy`), linting (`ruff`, `flake8`), or code formatting (`black`). |
| **Missing Authentication**       | All endpoints are publicly accessible. No RBAC, JWT, or session-based protection implemented. |
| **Settings Management**          | No clear separation of environment-based configuration (e.g., dev, staging, production); all settings come from environment variables directly. |
| **Migration Safety**             | Alembic migrations run directly inside the container without revision/version validation or locking. |
| **No Healthcheck Probes**        | Missing readiness/liveness endpoints and no container healthcheck configuration in `docker-compose`. |
| **Scalability Assumptions**      | Service assumes a single container instance. Not prepared for distributed load or horizontal scaling. |
