# How to Run the Titanic Prediction API

This guide explains how to run the Titanic Prediction API using either a local Python environment or Docker.
You can then test both the synchronous (`/titanic_sync`) and asynchronous (`/titanic_async`) endpoints using the Swagger UI.

---

## Option 1: Run with Docker

### 1. Clone the repository

```bash
git clone https://github.com/rcroegaert/titanic-api.git
cd titanic-api
```

### 2. Build the Docker image

```bash
docker build -t titanic-api .
```

### 3. Run the container

```bash
docker run -p 8000:8000 titanic-api
```

### 4. Open your browser

Navigate to:
```
http://localhost:8000/docs
```

This opens the interactive Swagger UI.

---

## Option 2: Run Locally with Python

### 1. Clone the repository

```bash
git clone https://github.com/your-username/titanic-api.git
cd titanic-api
```

### 2. Create a virtual environment

```bash
python3 -m venv /path/to/new/virtual/environment

source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the FastAPI app

```bash
uvicorn app.main:app --reload
```

### 5. Open your browser

Navigate to:
```
http://localhost:8000/docs
```