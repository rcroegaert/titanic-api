# Containerization

This project is fully containerized using Docker, allowing to run the Titanic Prediction API in a consistent environment,
independent of any host system. 

---

## Why Docker?

Docker was chosen because it ensures that the application runs the same way on every machine, with:

- All dependencies included
- No need for manual setup
- Easy deployment to cloud platforms

---

## Dockerfile

The root of the project contains a `Dockerfile` that builds the FastAPI app with all dependencies:

=== "Dockerfile"
    ```dockerfile
    FROM python:3.10
    
    WORKDIR /app
    
    COPY . .
    
    RUN pip install --no-cache-dir -r requirements.txt
    
    CMD [   "uvicorn",              \
            "app.main:app",         \
            "--host", "0.0.0.0",    \
            "--port", "8000"        \
        ]
    ```

---

##  Build the Docker Image

From the root of the project:

=== "Bash"
    ```bash
    docker build -t titanic-api .
    ```

---

## Run the Docker Container

=== "Bash"
    ```bash
    docker run -p 8000:8000 titanic-api
    ```

Then open the browser and visit:

=== "Bash"
    ```
    http://localhost:8000/docs
    ```

---

## Run in Background (Detached Mode)

To run the container in the background:

=== "Bash"
    ```bash
    docker run -d -p 8000:8000 --name titanic-api-container titanic-api
    ```

To stop it:


=== "Bash"
    ```bash
    docker stop titanic-api-container
    ```