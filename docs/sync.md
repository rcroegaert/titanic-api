# Synchronous Prediction Endpoint

This endpoint returns the survival probability **immediately** after submitting the input data.

---

## 🔗 Endpoint

**POST** `/titanic_sync`

---

## 🧾 Request Body

```json
{
  "Pclass": 3,
  "Sex": 1,
  "Age": 24,
  "Fare": 15.0
}
```

- `Pclass` — Passenger class (1, 2, or 3)
- `Sex` — Gender (0 = male, 1 = female)
- `Age` — Passenger age
- `Fare` — Ticket fare price

---

## ✅ Example Response

```json
{
  "survival_probability": 0.8251
}
```

---

## 💡 Notes

- The prediction is computed instantly.
- The model is loaded once when the API starts and reused for all incoming requests.

# Asynchronous Prediction Endpoint

This version handles predictions in the background and lets the user **poll the result** later using a job ID.

---

## 🔗 Step 1: Submit a Job

**POST** `/titanic_async`

### 📤 Request Body

```json
{
  "Pclass": 1,
  "Sex": 0,
  "Age": 40,
  "Fare": 60.0
}
```

---

### 📥 Example Response

```json
{
  "job_id": "job-1712066113000"
}
```

The returned `job_id` is used to check the result.

---

## 🔗 Step 2: Retrieve the Result

**GET** `/titanic_async/{job_id}`

### 🔄 Possible Responses:

#### 🔸 If still processing:
```json
{
  "status": "processing"
}
```

#### ✅ If completed:
```json
{
  "status": "done",
  "survival_probability": 0.8123
}
```

---

## 💡 Notes

- Use this endpoint for heavy loads or async pipelines.
- All jobs are stored in memory using a dictionary.
- Each job ID is based on a timestamp (e.g., `job-1712066113000`).
