# Titanic Prediction Service

This project is a lightweight and containerized machine learning API for predicting Titanic passenger survival 
probabilities using FastAPI and a LightGBM model.

- Synchronous and asynchronous endpoints
It includes:
- A trained model
- Synchronous and asynchronous endpoints
- Full documentation
- Containerization with Docker
- Extra: Streamlit App for interactive testing

## Documentation

Full usage instructions and technical documentation [here](https://rcroegaert.github.io/titanic-api])

## Streamlit App

Link to the [Streamlit App](https://titanic-prediction-app.streamlit.app/)

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