# Titanic Prediction Service

This project is a lightweight and containerized machine learning API for predicting Titanic passenger survival 
probabilities using FastAPI and a LightGBM model.

It includes:
- A trained model
- Synchronous and asynchronous endpoints
- Full documentation
- Containerization with Docker

## Documentation

Full usage instructions and technical documentation are available at:
👉 [https://rcroegaert.github.io/titanic-api](https://rcroegaert.github.io/titanic-api)  


# Project Structure

    ├── app/                 # FastAPI app and model logic
        ├── main.py          # FastAPI app with sync/async endpoints
        ├── model.pkl        # Trained LightGBM model
        └── lgbm_model.py    # Model
    ├── docs/             # MkDocs documentation
    ├── data/             # Training data
    ├── Dockerfile        # Container build instructions
    ├── requirements.txt  # Dependencies
    └── mkdocs.yml        # MkDocs configuration    