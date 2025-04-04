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

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
