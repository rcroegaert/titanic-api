from time import sleep

import pandas as pd
import pydantic
from fastapi import FastAPI, BackgroundTasks, HTTPException
import os
import joblib
import time
app = FastAPI()

# Load model
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(model_path)

# Input Schema
class Passenger(pydantic.BaseModel):
    Pclass: int = pydantic.Field(..., gt=0, le=3, description="Passenger class (1st, 2nd, or 3rd)")
    Sex: int = pydantic.Field(...,ge=0, le=1, description="0 = Male, 1 = Female")
    Age: float = pydantic.Field(..., ge=0, description="Passenger age (0 or older)")
    Fare: float = pydantic.Field(..., ge=0, description="Ticket fare (0 or more)")

# Synchronous endpoint
@app.post("/titanic_sync")
def predict_sync(data: Passenger):
    input_df = pd.DataFrame([{
        "Pclass": data.Pclass,
        "Sex": data.Sex,
        "Age": data.Age,
        "Fare": data.Fare
    }])
    result = model.predict_proba(input_df)[0][1]
    return {"survival_probability": result}

# Asynchronous endpoint
jobs = {}
@app.post("/titanic_async")
def predict_async(data: Passenger, background_tasks: BackgroundTasks):
    job_id = f"job-{int(time.time())}"
    jobs[job_id] = None

    def run_prediction():
        sleep(5)
        input_df = pd.DataFrame([{
            "Pclass": data.Pclass,
            "Sex": data.Sex,
            "Age": data.Age,
            "Fare": data.Fare
        }])
        result = model.predict_proba(input_df)[0][1]
        jobs[job_id] = result

    background_tasks.add_task(run_prediction)
    return {"job_id": job_id}

@app.get("/titanic_async/{job_id}")
def get_async_result(job_id: str):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    result = jobs[job_id]
    if result is None:
        return {"status": "Processing"}
    else:
        return {"status": "Done", "survival_probability": result}