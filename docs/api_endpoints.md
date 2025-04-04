# API Endpoints

This page explains the different Endpoints offered by the API for predicting the survival probability of Titanic 
passengers using a trained LightGBM model.

The two prediction modes are:

- **Synchronous** — Returns the result immediately after request
- **Asynchronous** — Runs in the background and allows result retrieving via a unique job ID

Both endpoints accept the same input data format.

------

## Input Format

All prediction requests have to send a JSON object with the following structure:

=== "JSON"
```json
{
  "Pclass": 3,
  "Sex": 0,
  "Age": 22,
  "Fare": 15
}
```

| Field  | Type | Description | Constraints |
|--------|------|-------------|-------------|
| `Pclass` | int | Passenger class (1, 2, or 3) | ≥ 1, ≤ 3    |
| `Sex`    | int | Gender (0 = male, 1 = female) | ∈ {0, 1}       |
| `Age`    | float | Passenger's age | ≥ 0         |
| `Fare`   | float | Ticket fare | ≥ 0         |

------

## Synchronous Endpoint

### Endpoint
**POST** `/titanic_sync`

This endpoint returns the survival probability immediately after processing the input.

### Example Response:

=== "JSON"
    ```json
    {
      "survival_probability": 0.8676121599174949
    }
    ```

!!! note
    - The model is loaded once when the API starts and reused for all incoming requests

------

## Asynchronous Endpoint

The asynchronous workflow consists of two steps:

### <ins>Step 1</ins>: Submit a Job

**POST** `/titanic_async`

#### Example Response:

=== "JSON"
    ```json
    {
      "job_id": "job-1743685729"
    }
    ```

You will receive a `job_id` which can be used to retrieve the result later.


### <ins>Step 2</ins>: Retrieve the Result

**GET** `/titanic_async/{job_id}`

#### Possible Responses:

If still processing:
=== "JSON"
    ```json
    {
      "status": "Processing"
    }
    ```

If completed:
=== "JSON"
    ```json
    {
      "status": "Done",
      "survival_probability": 0.8676121599174949
    }
    ```

!!! note
    - All jobs are tracked in memory using a dictionary. Memory is deleted when API is shut down.
    - Job IDs are timestamp-based (e.g., `job-1743685729`)
