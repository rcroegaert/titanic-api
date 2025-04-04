# Welcome to the Titanic Prediction Service!

This project fulfills a typical ML deployment pipeline, covering:

- Data processing and model training
- Building RESTful API endpoints (synchronous & asynchronous)
- Containerization using Docker
- Clear Documentation

---

## What does the API do?

The API predicts the **probability of survival** for Titanic passengers based on:

- Passenger class (`Pclass`)
- Sex (`Sex`)
- Age (`Age`)
- Ticket fare (`Fare`)

It offers both:

- **Synchronous prediction** (instant response)
- **Asynchronous prediction** (background processing using job IDs to retrieve results)

## Project layout

    ├── app/                 # FastAPI app and model logic
        ├── main.py          # FastAPI app with sync/async endpoints
        ├── model.pkl        # Trained LightGBM model
        └── lgbm_model.py    # Model
    ├── docs/             # MkDocs documentation
    ├── data/             # Training data
    ├── Dockerfile        # Container build instructions
    ├── requirements.txt  # Dependencies
    └── mkdocs.yml        # MkDocs configuration 